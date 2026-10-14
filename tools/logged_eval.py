"""
Run GPT-1900 checkpoints on the physics eval and log every generation in full.

Upstream's physics_eval.py saves prompt, mode, completions and nothing else, so
when its runs disagree there is no way to tell why. This writes one JSON line
per generation with the settings, model revision, hardware and output. Schema
in notes/logging-schema.md. Imports upstream, never edits it (D003).

No judging here. Judge fields are left null for a separate pass.

    python tools/logged_eval.py --only discovery-rl-v11-s560 \
        --temperature 0.0 --num-samples 1 --out evidence/run-a.jsonl
"""

import argparse
import gc
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
import traceback
import uuid
from datetime import datetime, timezone

# Upstream is a pinned clone that we import from and never modify.
UPSTREAM = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "upstream", "gpt1900")
sys.path.insert(0, UPSTREAM)

import torch
from huggingface_hub import HfApi, snapshot_download
from nanochat.engine import Engine
from scripts.physics_eval import (
    CHECKPOINTS,
    build_model_only,
    download_tokenizer,
    make_prompt_text,
)

SCHEMA_VERSION = "1.2"
RUBRIC_VERSION = "v1"


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def sha256_text(text):
    """Hash a string. Lets two runs be compared for identity without diffing text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path, chunk_size=1 << 20):
    """Hash a file in chunks so a 6.6GB checkpoint does not have to fit in memory."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def git_state(repo_dir):
    """(commit, dirty) for a git tree. A hash alone hides uncommitted edits."""
    def run(args):
        return subprocess.run(args, cwd=repo_dir, capture_output=True,
                              text=True, check=True).stdout.strip()
    try:
        commit = run(["git", "rev-parse", "HEAD"])
        dirty = run(["git", "status", "--porcelain"]) != ""
        return commit, dirty
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None, None


def resolve_revision(repo_id):
    """HF repo name -> commit hash it points at now. Names can move, hashes can't."""
    if repo_id == "local":
        return None
    try:
        return HfApi().repo_info(repo_id).sha
    except Exception:
        return None


def pick_device(requested):
    if requested != "auto":
        return torch.device(requested)
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def environment_fields(device):
    """
    Hardware and software facts for the record.

    dtype is not here on purpose. 1.0 guessed it from the device (cuda -> bf16),
    which is wrong on V100. 1.1 reads it off the loaded model instead, see
    model_dtype_of. bf16_supported is recorded so the two can be checked.
    """
    fields = {
        "device": str(device),
        "num_gpus": torch.cuda.device_count() if torch.cuda.is_available() else 0,
        "gpu_name": None,
        "compute_capability": None,
        "bf16_supported": None,
        "torch_version": torch.__version__,
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "slurm_job_id": os.environ.get("SLURM_JOB_ID"),
        "deterministic_algorithms": False,
        "dtype_override": "auto",
    }
    if torch.cuda.is_available():
        index = device.index or 0
        fields["gpu_name"] = torch.cuda.get_device_name(index)
        fields["compute_capability"] = ".".join(
            str(x) for x in torch.cuda.get_device_capability(index))
        fields["bf16_supported"] = torch.cuda.is_bf16_supported(including_emulation=False)
    return fields


def model_dtype_of(model):
    """dtype the weights are actually held in. None if the model has no params."""
    try:
        return str(next(model.parameters()).dtype).replace("torch.", "")
    except StopIteration:
        return None


def apply_dtype_override(which):
    """
    Force the KV cache dtype without editing upstream.

    Upstream's Engine.generate() picks bf16 on cuda for the KV cache regardless
    of the weights, so casting only the model would give a mixed run. This
    patches KVCache.__init__ to match. "auto" leaves upstream alone.
    """
    if which == "auto":
        return
    import nanochat.engine as _eng
    want = {"float32": torch.float32, "bfloat16": torch.bfloat16}[which]
    orig = _eng.KVCache.__init__
    def patched(self, *a, **kw):
        kw["dtype"] = want
        orig(self, *a, **kw)
    _eng.KVCache.__init__ = patched


def apply_determinism(enabled):
    """
    Force deterministic kernels. Off by default: phase 2 measures the pipeline
    as it stands. On is the follow-up if runs still differ at temperature 0.
    """
    if not enabled:
        return False
    # cuBLAS needs this set before the first CUDA context is created.
    os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
    torch.use_deterministic_algorithms(True)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    return True


# ---------------------------------------------------------------------------
# Checkpoint download, with the revision pinned
# ---------------------------------------------------------------------------

def download_checkpoint_pinned(ckpt, cache_dir, revision):
    """
    Upstream's download_checkpoint with the revision pinned and the weights path
    returned. Keeps their allow_patterns filter: one step's files, not the repo.
    """
    step_str = f"{ckpt.step:06d}"
    local_dir = os.path.join(cache_dir, ckpt.name)
    weights_path = os.path.join(local_dir, f"model_{step_str}.pt")

    if os.path.exists(weights_path):
        print(f"  [cached] {ckpt.name}")
        return local_dir, weights_path

    if ckpt.repo == "local":
        raise FileNotFoundError(
            f"Checkpoint {ckpt.name} is registry-local and was never published. "
            f"Expected weights at {weights_path}."
        )

    print(f"  downloading {ckpt.repo} step={ckpt.step} revision={revision} ...")
    snapshot_download(
        repo_id=ckpt.repo,
        revision=revision,
        allow_patterns=[f"model_{step_str}.pt", f"meta_{step_str}.json", "tokenizer/*"],
        local_dir=local_dir,
    )
    return local_dir, weights_path


# ---------------------------------------------------------------------------
# One generation, one record
# ---------------------------------------------------------------------------

def build_prompt_tokens(tokenizer, task, mode):
    """Task -> token list, copied from upstream so prompts stay byte-identical."""
    prompt_text = make_prompt_text(task)
    if mode == "completion":
        tokens = tokenizer.encode(prompt_text, prepend=tokenizer.get_bos_token_id())
    else:
        conversation = {
            "messages": [
                {"role": "user", "content": prompt_text},
                {"role": "assistant", "content": ""},
            ]
        }
        tokens = tokenizer.render_for_completion(conversation)
    return prompt_text, tokens


def generate_one(engine, tokenizer, tokens, seed, temperature, top_k, max_tokens):
    """
    One completion, one seed, one call. Never a batch.

    Upstream shares one RNG across a batch, so sample 0 of a 3-sample run and
    sample 0 of a 1-sample run get different draws from the same seed (E026).
    Their paired runs used different --num-samples, so they could never match.

    Returns (text, n_tokens, finish_reason, seconds).
    """
    torch.manual_seed(seed)
    prompt_len = len(tokens)

    started = time.time()
    all_tokens, _ = engine.generate_batch(
        tokens,
        num_samples=1,
        max_tokens=max_tokens,
        temperature=temperature,
        top_k=top_k,
        seed=seed,
    )
    seconds = time.time() - started

    gen_tokens = all_tokens[0][prompt_len:]
    # stop = model chose to end, length = hit max_tokens. Judge should know which.
    finish_reason = "length" if len(gen_tokens) >= max_tokens else "stop"
    return tokenizer.decode(gen_tokens), len(gen_tokens), finish_reason, seconds


def make_record(*, run_meta, ckpt, revision, weights_hash, task, prompt_text,
                mode, prompt_condition, seed, sample_index, temperature, top_k,
                num_samples, max_tokens, env, model_dtype, completion,
                completion_tokens, finish_reason, seconds, error=None):
    """
    One archive line, per notes/logging-schema.md (schema 1.1, 50 fields).
    model_dtype is None when the checkpoint never loaded. Judge fields are None
    until the judging pass.
    """
    return {
        # identity of the run
        "run_id": run_meta["run_id"],
        "timestamp_utc": utc_now(),
        "code_commit": run_meta["code_commit"],
        "code_dirty": run_meta["code_dirty"],
        "eval_config_path": run_meta["eval_config_path"],
        "eval_config_sha256": run_meta["eval_config_sha256"],

        # identity of the model
        "model_repo": ckpt.repo,
        "model_revision": revision,
        "checkpoint_name": ckpt.name,
        "checkpoint_step": ckpt.step,
        "weights_sha256": weights_hash,

        # the prompt
        "task_id": task["id"],
        "prompt": prompt_text,
        "prompt_sha256": sha256_text(prompt_text),
        "prompt_condition": prompt_condition,
        "mode": mode,

        # sampling
        "seed": seed,
        "sample_index": sample_index,
        "temperature": temperature,
        "top_k": top_k,
        "top_p": None,              # not implemented upstream
        "num_samples": num_samples,
        "max_tokens": max_tokens,
        "repetition_penalty": None,  # not implemented upstream

        # hardware and software
        **env,
        "dtype": model_dtype,

        # the output
        "completion": completion,
        "completion_sha256": sha256_text(completion) if completion is not None else None,
        "completion_tokens": completion_tokens,
        "finish_reason": finish_reason,
        "generation_seconds": seconds,

        # the judge, filled in by the judging pass
        "judge_model": None,
        "judge_model_version": None,
        "judge_prompt_sha256": None,
        "judge_temperature": None,
        "judge_raw_response": None,
        "score": None,
        "rubric_version": RUBRIC_VERSION,
        "judged_at_utc": None,

        # a failure is a record too, because the denominator matters
        "error": error,
        "schema_version": SCHEMA_VERSION,
    }


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

def smoke_test(device):
    """Print hardware, versions, upstream commit, run one matmul. No download."""
    import socket

    env = environment_fields(device)
    commit, dirty = git_state(UPSTREAM)

    line = "=" * 62
    print(line)
    print("SMOKE TEST")
    print(line)
    print(f"hostname          {socket.gethostname()}")
    print(f"slurm job id      {os.environ.get('SLURM_JOB_ID', 'not running under slurm')}")
    print(f"slurm partition   {os.environ.get('SLURM_JOB_PARTITION', 'n/a')}")
    print(f"slurm nodelist    {os.environ.get('SLURM_JOB_NODELIST', 'n/a')}")
    print(f"working dir       {os.getcwd()}")
    print()
    print(f"python            {env['python_version']}")
    print(f"platform          {env['platform']}")
    print(f"torch             {env['torch_version']}")
    print()
    print(f"device selected   {device}")
    print(f"cuda available    {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        for i in range(torch.cuda.device_count()):
            cap = ".".join(str(x) for x in torch.cuda.get_device_capability(i))
            print(f"  gpu {i}           {torch.cuda.get_device_name(i)}, compute capability {cap}")
    print(f"gpu_name          {env['gpu_name']}")
    print(f"compute capab.    {env['compute_capability']}")
    print(f"bf16 supported    {env['bf16_supported']}")
    print()
    print("dtype is not guessed from the device. Schema 1.1 reads it off the")
    print("loaded model, so it is only known once a checkpoint is loaded and does")
    print("not appear here. bf16_supported above is what the hardware can do.")
    print()
    print(f"upstream path     {UPSTREAM}")
    print(f"upstream commit   {commit} {'(dirty)' if dirty else '(clean)'}")
    print(f"checkpoints       {len(CHECKPOINTS)} in registry")
    print()

    # real compute, not just imports
    x = torch.randn(512, 512, device=device)
    checksum = (x @ x).sum().item()
    print(f"matmul on {device}     ok, checksum {checksum:.4f}")
    print(line)
    print("TEST RUN COMPLETE")
    print(line)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="GPT-1900 generation pass with a full per-generation record")
    parser.add_argument("--out", default=None,
                        help="Output JSONL path. Appended to, never overwritten. "
                             "Required unless --smoke-test.")
    parser.add_argument("--smoke-test", action="store_true",
                        help="Print hardware, versions and upstream commit, run one "
                             "matmul, then exit. Downloads nothing. Use this as the "
                             "first Slurm job to prove the job ran at all.")
    parser.add_argument("--only", default=None,
                        help="Comma-separated checkpoint names. Default is every v11 checkpoint.")
    parser.add_argument("--eval-config", default=None,
                        help="Path to eval config JSON. Default is EVAL.json in the upstream root.")
    parser.add_argument("--prompt-condition", default=None,
                        help="scaffolded, minimal or leading. Guessed from the config filename if unset.")
    parser.add_argument("--num-samples", type=int, default=1)
    parser.add_argument("--max-tokens", type=int, default=1024)
    parser.add_argument("--temperature", type=float, default=0.0,
                        help="Default 0.0, which is greedy. Upstream defaults to 0.7.")
    parser.add_argument("--top-k", type=int, default=50)
    parser.add_argument("--seed", type=int, default=1337,
                        help="Base seed. Sample i of a task uses seed + i.")
    parser.add_argument("--cache-dir", default=None)
    parser.add_argument("--device", default="auto", help="auto, cpu, mps or cuda")
    parser.add_argument("--hash-weights", action="store_true",
                        help="Hash the weight file. Proves identity if the revision is later "
                             "deleted, but reads 6.6GB per checkpoint.")
    parser.add_argument("--keep-cache", action="store_true",
                        help="Keep downloaded weights. Off by default because 24 checkpoints "
                             "do not fit on this machine.")
    parser.add_argument("--limit-tasks", type=int, default=None,
                        help="Use only the first N tasks. For a cheap first run on new "
                             "hardware: prove one generation works before paying for eight.")
    parser.add_argument("--dtype", default="auto", choices=["auto", "float32", "bfloat16"],
                        help="Force weights and KV cache to this dtype. auto = upstream's rule, "
                             "bf16 on cuda and fp32 elsewhere. float32 on a V100 is the control "
                             "for bf16 emulation.")
    parser.add_argument("--deterministic", action="store_true",
                        help="Force PyTorch deterministic kernels. Off by default, because "
                             "the phase 2 experiment measures whether this pipeline "
                             "reproduces as it stands. Recorded per generation either way.")
    args = parser.parse_args()

    if args.smoke_test:
        smoke_test(pick_device(args.device))
        return

    if not args.out:
        parser.error("--out is required unless --smoke-test is given")

    # hash the config: the file can change without its name changing
    eval_path = args.eval_config or os.path.join(UPSTREAM, "EVAL.json")
    with open(eval_path) as f:
        eval_config_raw = f.read()
    eval_config = json.loads(eval_config_raw)
    tasks = eval_config["tasks"]

    prompt_condition = args.prompt_condition
    if prompt_condition is None:
        base = os.path.basename(eval_path)
        if "no_assumptions" in base:
            prompt_condition = "minimal"
        elif "leading" in base:
            prompt_condition = "leading"
        elif "probe" in base:
            prompt_condition = "probe"
        else:
            prompt_condition = "scaffolded"

    # default to v11: published weights, 24 x 8 = 192 = the published score count
    if args.only:
        wanted = set(args.only.split(","))
        checkpoints = [c for c in CHECKPOINTS if c.name in wanted]
        missing = wanted - {c.name for c in checkpoints}
        if missing:
            parser.error(f"unknown checkpoint names: {sorted(missing)}")
    else:
        checkpoints = [c for c in CHECKPOINTS if c.name.startswith("discovery-rl-v11-")]

    if args.limit_tasks is not None:
        tasks = tasks[:args.limit_tasks]

    device = pick_device(args.device)
    env = environment_fields(device)
    env["deterministic_algorithms"] = apply_determinism(args.deterministic)
    env["dtype_override"] = args.dtype
    apply_dtype_override(args.dtype)
    cache_dir = args.cache_dir or os.path.join(os.path.dirname(args.out) or ".", "hf_cache")
    os.makedirs(cache_dir, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)

    code_commit, code_dirty = git_state(UPSTREAM)
    run_meta = {
        "run_id": f"{utc_now()}-{uuid.uuid4().hex[:6]}",
        "code_commit": code_commit,
        "code_dirty": code_dirty,
        "eval_config_path": os.path.relpath(eval_path, UPSTREAM),
        "eval_config_sha256": sha256_text(eval_config_raw),
    }

    total = len(checkpoints) * len(tasks) * args.num_samples
    print(f"run_id      {run_meta['run_id']}")
    print(f"upstream    {code_commit} {'(dirty)' if code_dirty else '(clean)'}")
    print(f"device      {device}"
          + (f"  {env['gpu_name']} cc {env['compute_capability']}"
             f"  bf16_supported {env['bf16_supported']}" if env["gpu_name"] else ""))
    print(f"determinism {env['deterministic_algorithms']}"
          + (f"  slurm job {env['slurm_job_id']}" if env["slurm_job_id"] else ""))
    print(f"config      {run_meta['eval_config_path']}  condition {prompt_condition}")
    print(f"sampling    temperature {args.temperature}  top_k {args.top_k}  base seed {args.seed}")
    print(f"work        {len(checkpoints)} checkpoints x {len(tasks)} tasks "
          f"x {args.num_samples} samples = {total} generations")
    print(f"writing     {args.out}\n")

    print("loading tokenizer ...")
    tokenizer = download_tokenizer(cache_dir)

    written = 0
    failed = 0
    started_at = time.time()
    # append + flush per line, so a crash loses one line not the run
    with open(args.out, "a") as out:

        def emit(record):
            nonlocal written
            out.write(json.dumps(record) + "\n")
            out.flush()
            os.fsync(out.fileno())
            written += 1

        for ckpt in checkpoints:
            print(f"\n[{ckpt.name}] {ckpt.repo} step={ckpt.step} mode={ckpt.mode}")
            revision = resolve_revision(ckpt.repo)

            try:
                local_dir, weights_path = download_checkpoint_pinned(ckpt, cache_dir, revision)
                weights_hash = sha256_file(weights_path) if args.hash_weights else None
                model = build_model_only(local_dir, ckpt.step, device)
                if args.dtype == "float32":
                    model = model.float()
                elif args.dtype == "bfloat16":
                    model = model.bfloat16()
                engine = Engine(model, tokenizer)
            except Exception as exc:
                # failed load still gets a row per task, or the denominator lies
                print(f"  FAILED to load: {type(exc).__name__}: {exc}")
                failed += 1
                for task in tasks:
                    for i in range(args.num_samples):
                        emit(make_record(
                            run_meta=run_meta, ckpt=ckpt, revision=revision,
                            weights_hash=None, task=task,
                            prompt_text=make_prompt_text(task), mode=ckpt.mode,
                            prompt_condition=prompt_condition, seed=args.seed + i,
                            sample_index=i, temperature=args.temperature,
                            top_k=args.top_k, num_samples=args.num_samples,
                            max_tokens=args.max_tokens, env=env, model_dtype=None,
                            completion=None, completion_tokens=None,
                            finish_reason=None, seconds=None,
                            error=f"{type(exc).__name__}: {exc}",
                        ))
                continue

            model_dtype = model_dtype_of(model)
            print(f"  loaded, weights held as {model_dtype}")
            if env["bf16_supported"] is False and model_dtype == "bfloat16":
                print("  WARNING: weights are bfloat16 on hardware without bf16 support. "
                      "Results here are not comparable to a bf16-capable GPU.")

            for task in tasks:
                prompt_text, tokens = build_prompt_tokens(tokenizer, task, ckpt.mode)

                for i in range(args.num_samples):
                    seed = args.seed + i
                    try:
                        completion, n_tokens, finish_reason, seconds = generate_one(
                            engine, tokenizer, tokens, seed,
                            args.temperature, args.top_k, args.max_tokens,
                        )
                        error = None
                    except Exception:
                        completion, n_tokens, finish_reason, seconds = None, None, None, None
                        error = traceback.format_exc(limit=3)
                        print(f"    {task['id']} sample {i}: FAILED")

                    emit(make_record(
                        run_meta=run_meta, ckpt=ckpt, revision=revision,
                        weights_hash=weights_hash, task=task, prompt_text=prompt_text,
                        mode=ckpt.mode, prompt_condition=prompt_condition, seed=seed,
                        sample_index=i, temperature=args.temperature, top_k=args.top_k,
                        num_samples=args.num_samples, max_tokens=args.max_tokens,
                        env=env, model_dtype=model_dtype, completion=completion,
                        completion_tokens=n_tokens, finish_reason=finish_reason,
                        seconds=seconds, error=error,
                    ))
                    if error is not None:
                        failed += 1

                    if error is None:
                        print(f"    {task['id']} sample {i}: {n_tokens} tokens, "
                              f"{finish_reason}, {seconds:.1f}s")

            del model, engine
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            gc.collect()

            # pull, use, delete. 24 x 6.6GB does not fit anywhere we run
            if not args.keep_cache and ckpt.repo != "local":
                ckpt_cache = os.path.join(cache_dir, ckpt.name)
                if os.path.isdir(ckpt_cache) and not os.path.islink(ckpt_cache):
                    import shutil
                    shutil.rmtree(ckpt_cache)
                    print(f"  removed cache {ckpt_cache}")

    elapsed = time.time() - started_at
    print()
    print("=" * 62)
    print(f"run_id      {run_meta['run_id']}")
    print(f"records     {written} written, {failed} carrying an error")
    print(f"expected    {total}")
    print(f"elapsed     {elapsed / 60:.1f} min")
    print(f"output      {args.out}")
    if written != total:
        print(f"WARNING: wrote {written} records but expected {total}. "
              f"The denominator is wrong, do not report a rate from this file.")
    print("=" * 62)
    print("RUN COMPLETE")
    print("=" * 62)


if __name__ == "__main__":
    main()

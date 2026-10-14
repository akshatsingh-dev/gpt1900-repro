"""
Score logged_eval generations with the Claude judge, and record how.

Why this exists
---------------
Upstream's judge (scripts/physics_eval.py, judge_all) calls the Claude API and
keeps only score and rationale. It does not record which model version
answered, what temperature it sampled at (none was set, so the API default
applied), or the exact prompt it saw. And when the call failed it silently
wrote a score of 0. This pass uses upstream's own build_judge_messages, so the
prompt is byte-identical to theirs, and fills the eight judge fields of the
generation record instead of throwing that information away.

Rules
-----
- Never modifies the input file. Writes <name>.judged.jsonl beside it.
- Resumable. If the output exists, records already scored are skipped.
- A judge failure is recorded as score null with the error text, never as 0.
- Records that carry a generation error pass through unchanged, so the
  denominator in the output matches the input.

Usage (on the Mac, needs `pip install anthropic` and ANTHROPIC_API_KEY)
-----
    python tools/judge.py evidence/sweep/v11-scaffolded.jsonl --dry-run   # no API call
    python tools/judge.py evidence/sweep/v11-scaffolded.jsonl --limit 3   # cheap first test
    python tools/judge.py evidence/sweep/v11-scaffolded.jsonl             # the real pass
"""

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone

UPSTREAM = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "upstream", "gpt1900")
sys.path.insert(0, UPSTREAM)
from scripts.physics_eval import build_judge_messages  # noqa: E402  (their prompt, unchanged)

# Upstream's judge. Deprecated at Anthropic but still served, and the point of
# a reproduction is to use what they used. Override with --model if it is gone.
UPSTREAM_JUDGE = "claude-sonnet-4-20250514"

# Newer models reject the temperature parameter outright. For those the field
# is recorded as null, meaning "the API decided", which is itself a fact worth
# having in the record.
NO_TEMPERATURE_PREFIXES = ("claude-opus-5", "claude-sonnet-5", "claude-fable",
                           "claude-mythos", "claude-opus-4-8", "claude-opus-4-7")

# $ per million tokens, input / output. Only for the estimate printed up front.
PRICE = {
    "claude-sonnet-4-20250514": (3.0, 15.0),
    "claude-sonnet-4-0": (3.0, 15.0),
    "claude-sonnet-5": (2.0, 10.0),
    "claude-opus-5": (5.0, 25.0),
    "claude-haiku-4-5": (1.0, 5.0),
}


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_jsonl(path):
    out = []
    with open(path) as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    print(f"{path}:{n}: skipped unparseable line, {exc}", file=sys.stderr)
    return out


def record_key(r):
    return (r.get("checkpoint_name"), r.get("task_id"), r.get("prompt_condition"),
            r.get("seed"), r.get("sample_index"))


def load_eval_config(record):
    """
    Find the exact config the generation used, and prove it is the same bytes.
    eval_config_path is stored relative to the upstream root.
    """
    rel = record["eval_config_path"]
    path = os.path.normpath(os.path.join(UPSTREAM, rel))
    if not os.path.exists(path):
        raise SystemExit(f"eval config {rel} (looked at {path}) not found")
    raw = open(path).read()
    if sha256_text(raw) != record["eval_config_sha256"]:
        raise SystemExit(f"{path} has changed since the generations were made "
                         f"(sha256 differs). Refusing to judge against a different rubric.")
    return json.loads(raw), path


def parse_judge_json(raw):
    """Same extraction as upstream: strip a ``` fence if present, then json.loads."""
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(raw)


def call_judge(client, model, system_text, messages, temperature, max_tokens):
    """One API call with the retries a batch job needs. Returns the Message."""
    import anthropic
    kwargs = dict(model=model, max_tokens=max_tokens, system=system_text, messages=messages)
    if temperature is not None:
        kwargs["temperature"] = temperature
    for attempt in range(5):
        try:
            return client.messages.create(**kwargs)
        except anthropic.RateLimitError as exc:
            wait = int(exc.response.headers.get("retry-after", "20"))
            print(f"    rate limited, waiting {wait}s", flush=True)
            time.sleep(wait)
        except anthropic.APIStatusError as exc:
            if exc.status_code >= 500 and attempt < 4:
                time.sleep(5 * (attempt + 1))
                continue
            raise
        except anthropic.APIConnectionError:
            if attempt < 4:
                time.sleep(5 * (attempt + 1))
                continue
            raise
    raise RuntimeError("gave up after 5 attempts")


def main():
    ap = argparse.ArgumentParser(description="Judge logged_eval generations with Claude")
    ap.add_argument("inputs", nargs="+", help="one or more JSONL files from logged_eval.py")
    ap.add_argument("--out", default=None,
                    help="output path. Only with a single input. Default <input>.judged.jsonl")
    ap.add_argument("--model", default=UPSTREAM_JUDGE,
                    help=f"judge model id. Default is upstream's: {UPSTREAM_JUDGE}")
    ap.add_argument("--temperature", type=float, default=0.0,
                    help="judge temperature. 0 by default: a grader that samples adds noise "
                         "to the measurement. Ignored on models that reject the parameter.")
    ap.add_argument("--max-tokens", type=int, default=1024,
                    help="upstream used 512. 1024 leaves room for a long rationale.")
    ap.add_argument("--limit", type=int, default=None,
                    help="judge only the first N unscored records. For a cheap first test.")
    ap.add_argument("--delay", type=float, default=0.3, help="seconds between calls, as upstream")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the first judge prompt and the cost estimate. No API call.")
    args = ap.parse_args()

    if args.out and len(args.inputs) != 1:
        ap.error("--out only makes sense with a single input")

    temperature = None if args.model.startswith(NO_TEMPERATURE_PREFIXES) else args.temperature

    grand_scored = grand_failed = 0
    grand_in_tok = grand_out_tok = 0

    for in_path in args.inputs:
        out_path = args.out or (os.path.splitext(in_path)[0] + ".judged.jsonl")
        records = load_jsonl(in_path)
        if not records:
            print(f"{in_path}: empty, skipped")
            continue

        # what is already done, so a crash mid-way costs nothing on rerun.
        # The output may hold two lines for one key after a crash (see the
        # journal below); the scored one wins.
        done = {}
        if os.path.exists(out_path):
            for r in load_jsonl(out_path):
                k = record_key(r)
                if k not in done or r.get("score") is not None:
                    done[k] = r

        eval_config, config_path = load_eval_config(records[0])
        tasks_by_id = {t["id"]: t for t in eval_config["tasks"]}

        todo = []
        for r in records:
            k = record_key(r)
            if k in done and done[k].get("score") is not None:
                continue            # already scored
            if r.get("error") or r.get("completion") is None:
                continue            # nothing to score, passes through below
            task = tasks_by_id.get(r["task_id"])
            if task is None or "scoring_rubric" not in task:
                raise SystemExit(f"task {r['task_id']} has no scoring_rubric in {config_path}. "
                                 f"This file is not something the judge can score.")
            todo.append(r)
        if args.limit is not None:
            todo = todo[:args.limit]
        todo_keys = {record_key(r) for r in todo}

        line = "=" * 62
        print(line)
        print(f"JUDGE  {in_path}")
        print(line)
        print(f"records       {len(records)}   already scored {sum(1 for r in done.values() if r.get('score') is not None)}"
              f"   with errors {sum(1 for r in records if r.get('error') or r.get('completion') is None)}")
        print(f"to judge now  {len(todo)}")
        print(f"judge model   {args.model}   temperature {temperature}   max_tokens {args.max_tokens}")
        print(f"eval config   {os.path.relpath(config_path)}   sha256 {records[0]['eval_config_sha256'][:12]}...")
        print(f"output        {out_path}")

        # cost estimate from the actual prompts, roughly 4 chars per token
        est_in = 0
        for r in todo:
            msgs, sys_text = build_judge_messages(eval_config, tasks_by_id[r["task_id"]], r["completion"])
            est_in += (len(sys_text) + len(msgs[0]["content"])) // 4
        est_out = 300 * len(todo)
        p_in, p_out = PRICE.get(args.model, (None, None))
        if p_in is not None:
            print(f"estimate      ~{est_in:,} input + ~{est_out:,} output tokens "
                  f"= about ${est_in / 1e6 * p_in + est_out / 1e6 * p_out:.2f}")
        else:
            print(f"estimate      ~{est_in:,} input + ~{est_out:,} output tokens (price unknown for this model)")
        print()

        if args.dry_run:
            if todo:
                msgs, sys_text = build_judge_messages(eval_config, tasks_by_id[todo[0]["task_id"]], todo[0]["completion"])
                print("---- SYSTEM PROMPT (first record) ----")
                print(sys_text)
                print("\n---- USER MESSAGE (first record) ----")
                print(msgs[0]["content"])
            print("\nDRY RUN, no API call made.")
            continue

        try:
            import anthropic
        except ImportError:
            raise SystemExit("anthropic package missing. Run:  .venv/bin/pip install anthropic")
        client = anthropic.Anthropic()

        scored = failed = 0
        in_tok = out_tok = 0
        seen_scores = []
        started = time.time()
        # Every finished judgement is appended to the output at once (a
        # journal), so a crash keeps what was paid for. At the end the file is
        # rewritten once, one line per record, in input order.
        final = dict(done)
        with open(out_path, "a") as journal:
            for r in records:
                k = record_key(r)
                if k not in todo_keys:
                    continue
                task = tasks_by_id[r["task_id"]]
                messages, system_text = build_judge_messages(eval_config, task, r["completion"])
                new = dict(r)
                new.update({
                    "judge_model": args.model,
                    "judge_prompt_sha256": sha256_text(system_text + "\n\n" + messages[0]["content"]),
                    "judge_temperature": temperature,
                    "judged_at_utc": utc_now(),
                })
                try:
                    resp = call_judge(client, args.model, system_text, messages,
                                      temperature, args.max_tokens)
                    raw = "".join(b.text for b in resp.content if b.type == "text")
                    new["judge_model_version"] = resp.model
                    new["judge_raw_response"] = raw
                    in_tok += resp.usage.input_tokens
                    out_tok += resp.usage.output_tokens
                    try:
                        parsed = parse_judge_json(raw)
                        new["score"] = int(parsed["score"])
                        scored += 1
                        seen_scores.append(new["score"])
                    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
                        new["score"] = None
                        new["judge_raw_response"] = f"UNPARSEABLE ({type(exc).__name__}: {exc}): {raw}"
                        failed += 1
                        print(f"    {r['checkpoint_name']}/{r['task_id']}/s{r['sample_index']}: unparseable judge output")
                except Exception as exc:  # network, auth, 4xx: record it, keep going
                    new["score"] = None
                    new["judge_raw_response"] = f"JUDGE CALL FAILED: {type(exc).__name__}: {exc}"
                    failed += 1
                    print(f"    {r['checkpoint_name']}/{r['task_id']}/s{r['sample_index']}: FAILED {type(exc).__name__}")
                    if isinstance(exc, getattr(anthropic, "AuthenticationError", ())):
                        print("    ANTHROPIC_API_KEY is missing or wrong. Stopping.")
                        journal.write(json.dumps(new) + "\n")
                        journal.flush()
                        final[k] = new
                        break
                final[k] = new
                journal.write(json.dumps(new) + "\n")
                journal.flush()
                time.sleep(args.delay)
                n = scored + failed
                if n % 10 == 0 or n == len(todo):
                    mean = sum(seen_scores) / len(seen_scores) if seen_scores else float("nan")
                    print(f"    judged {n}/{len(todo)}   mean so far {mean:.3f}", flush=True)

        # one clean line per input record, in input order
        with open(out_path, "w") as out:
            for r in records:
                out.write(json.dumps(final.get(record_key(r), r)) + "\n")

        elapsed = time.time() - started
        p_in, p_out = PRICE.get(args.model, (0, 0))
        print()
        print(f"scored {scored}   failed {failed}   {elapsed / 60:.1f} min")
        print(f"tokens {in_tok:,} in / {out_tok:,} out   cost about ${in_tok / 1e6 * p_in + out_tok / 1e6 * p_out:.2f}")
        print(f"wrote  {out_path}")
        grand_scored += scored
        grand_failed += failed
        grand_in_tok += in_tok
        grand_out_tok += out_tok

    if not args.dry_run and len(args.inputs) > 1:
        print("=" * 62)
        print(f"TOTAL scored {grand_scored}   failed {grand_failed}   "
              f"tokens {grand_in_tok:,} in / {grand_out_tok:,} out")


if __name__ == "__main__":
    main()

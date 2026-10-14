# Logging schema

What must be written down for every generation so that someone else can
regenerate it.

Drafted 25 Aug 2026 against GPT-1900 at commit `5b489c8c`. Every field below is
marked with its current status in that codebase: **present**, **in scope and
discarded**, or **absent entirely**.

---

## The point of this, in one paragraph

A generation record is only evidence if a reader can take it and produce the same
output. Today's record cannot do that. It holds the question, a mode label and
the answer, and nothing else. So when two runs disagree, and 118 of 120 paired
generations do, nothing in the archive can say why. The fix is not a new
pipeline. It is a longer record written at the same place the short one is
written now.

## Format

One JSON object per line, JSON Lines, written append-only. One line per
generation, not per task and not per checkpoint.

Reasons for JSONL over a single JSON document: it survives a crash mid-run
because every completed line is already valid; it can be appended to without
rewriting; and it can be read with standard tools without loading the whole file.
The current pipeline rewrites one large JSON file after every checkpoint, which
is why a crash costs the current checkpoint rather than the whole run. JSONL
reduces that to the current line.

---

## Fields

### Identity of the run

| Field | Type | Example | Status today |
|---|---|---|---|
| `run_id` | string | `"2026-08-26T09:14:03Z-a1b2c3"` | absent |
| `timestamp_utc` | ISO 8601 string | `"2026-08-26T09:14:07Z"` | **absent** |
| `code_commit` | string, 40 hex | `"5b489c8c5378f6..."` | **absent** |
| `code_dirty` | bool | `false` | absent |
| `eval_config_path` | string | `"EVAL.json"` | absent |
| `eval_config_sha256` | string | `"e3b0c442..."` | absent |

`code_dirty` records whether the working tree had uncommitted changes. A commit
hash alone is misleading if the tree was modified.

`eval_config_sha256` matters because the prompt file can be edited without
changing its name.

### Identity of the model

| Field | Type | Example | Status today |
|---|---|---|---|
| `model_repo` | string | `"mhla/gpt1900-d34-contradiction-rl-v11"` | present, as a directory key |
| `model_revision` | string | `"9f2c1ab..."` | **absent entirely** |
| `checkpoint_name` | string | `"discovery-rl-v11-s560"` | present |
| `checkpoint_step` | int | `560` | in registry, not in output |
| `weights_sha256` | string | `"4a7f..."` | absent |

`model_revision` is the single most important addition after the seed. Hugging
Face names are mutable, so a name without a revision does not identify which
weights produced an answer. `snapshot_download` currently resolves the name with
no revision argument.

`weights_sha256` is belt and braces: a hash of the downloaded weight file proves
identity even if the revision is later deleted or the repository is moved.

### The prompt

| Field | Type | Example | Status today |
|---|---|---|---|
| `task_id` | string | `"uv_catastrophe_main"` | present, as a key |
| `prompt` | string | full text | **present** |
| `prompt_sha256` | string | `"7d2b..."` | absent |
| `prompt_condition` | enum | `"scaffolded"` / `"minimal"` / `"leading"` | partially, via `mode` |
| `mode` | enum | `"completion"` / `"chat"` | **present** |

`prompt_sha256` allows two runs to be compared for prompt identity without
storing or diffing the full text twice. The comparison that produced this
project's headline finding had to do exactly that by hand.

`prompt_condition` and `mode` are different things and should not share a field.
`mode` is how the model is addressed. `prompt_condition` is how much of the
answer the prompt gives away, which is the variable in the prompt-sensitivity
work.

### Sampling

| Field | Type | Example | Status today |
|---|---|---|---|
| `seed` | int | `1337` | **absent entirely** |
| `sample_index` | int | `0` | implied by list position |
| `temperature` | float | `0.7` | **in scope at write, discarded** |
| `top_k` | int | `50` | **in scope at write, discarded** |
| `top_p` | float or null | `null` | not implemented upstream |
| `num_samples` | int | `3` | **in scope at write, discarded** |
| `max_tokens` | int | `1024` | **in scope at write, discarded** |
| `repetition_penalty` | float or null | `null` | not implemented upstream |

`seed` is the field whose absence caused the finding. It must be set explicitly
rather than left to the library default, and it must be recorded per generation
rather than per run, because with multiple samples the effective state differs
between them.

`sample_index` currently exists only as a position in the `completions` list.
Making it explicit is what allows sample 2 of one run to be compared against
sample 2 of another.

### Hardware and software

| Field | Type | Example | Status today |
|---|---|---|---|
| `device` | string | `"mps"` / `"cuda:0"` / `"cpu"` | **in scope at write, discarded** |
| `num_gpus` | int | `1` | **in scope at write, discarded** |
| `dtype` | string | `"bfloat16"` | absent |
| `torch_version` | string | `"2.4.1"` | absent |
| `platform` | string | `"Darwin-24.5.0-arm64"` | absent |
| `python_version` | string | `"3.12.2"` | absent |

These are the fields that make a portability claim possible. Without them, a
result that differs between two machines cannot be attributed to the machines.

`dtype` deserves particular attention: fp32 against bf16 changes output with
identical code, seed and weights.

### The output

| Field | Type | Example | Status today |
|---|---|---|---|
| `completion` | string | full text | **present** |
| `completion_sha256` | string | `"1f0a..."` | absent |
| `completion_tokens` | int | `842` | absent |
| `finish_reason` | string | `"stop"` / `"length"` | absent |
| `generation_seconds` | float | `31.4` | absent |

`finish_reason` distinguishes an answer that ended because the model finished
from one truncated at `max_tokens`. Those are different objects and should not be
scored the same way.

### The judge

| Field | Type | Example | Status today |
|---|---|---|---|
| `judge_model` | string | `"claude-opus-5"` | **absent** |
| `judge_model_version` | string | as returned by the API | **absent** |
| `judge_prompt_sha256` | string | `"c9e1..."` | absent |
| `judge_temperature` | float | `0.0` | absent |
| `judge_raw_response` | string | full text | partially, in judged runs |
| `score` | float or int | `1` | present, in judged runs |
| `rubric_version` | string | `"v1"` | absent |
| `judged_at_utc` | ISO 8601 string | `"2026-08-26T10:02:11Z"` | absent |

The judge is a hosted model that changes over time. Recording its identity and
version is the difference between a score that can be re-derived and one that
cannot. Treat it as instrumentation and record it the way a lab records which
instrument took a reading.

`judge_temperature` should be 0 for a grader. A grader that samples introduces
variance into the measurement itself.

`judged_at_utc` is separate from `timestamp_utc` because generation and judging
are separate stages and can happen days apart.

---

## Example record

One line of the file, formatted here for readability. In the file it is a single
line.

```json
{
  "run_id": "2026-08-26T09:14:03Z-a1b2c3",
  "timestamp_utc": "2026-08-26T09:14:07Z",
  "code_commit": "5b489c8c5378f6b1bf3e1ba782f56876f65cde7a",
  "code_dirty": false,
  "eval_config_path": "EVAL.json",
  "eval_config_sha256": "e3b0c44298fc1c149afbf4c8996fb924...",

  "model_repo": "mhla/gpt1900-d34-contradiction-rl-v11",
  "model_revision": "9f2c1ab7e4d3c8b1a5f60923de47bb01c2d8e4f6",
  "checkpoint_name": "discovery-rl-v11-s560",
  "checkpoint_step": 560,
  "weights_sha256": "4a7f2c9e18b03d5a...",

  "task_id": "uv_catastrophe_main",
  "prompt": "A heated cavity in thermal equilibrium emits radiation...",
  "prompt_sha256": "7d2b8e01c4f9a6...",
  "prompt_condition": "scaffolded",
  "mode": "chat",

  "seed": 1337,
  "sample_index": 0,
  "temperature": 0.7,
  "top_k": 50,
  "top_p": null,
  "num_samples": 3,
  "max_tokens": 1024,
  "repetition_penalty": null,

  "device": "mps",
  "num_gpus": 0,
  "dtype": "bfloat16",
  "torch_version": "2.4.1",
  "platform": "Darwin-24.5.0-arm64",
  "python_version": "3.12.2",

  "completion": "You have touched a matter of considerable importance...",
  "completion_sha256": "1f0adc73b2e5...",
  "completion_tokens": 842,
  "finish_reason": "stop",
  "generation_seconds": 31.4,

  "judge_model": "claude-opus-5",
  "judge_model_version": "claude-opus-5-20260401",
  "judge_prompt_sha256": "c9e1f4a70b28...",
  "judge_temperature": 0.0,
  "judge_raw_response": "{\"score\": 1, \"reasoning\": \"...\"}",
  "score": 1,
  "rubric_version": "v1",
  "judged_at_utc": "2026-08-26T10:02:11Z"
}
```

---

## Field count and current status

Counted from the tables above rather than by hand.

| Status | Count |
|---|---|
| Present today | 7 |
| Partially present | 4 |
| In scope at the write and discarded | 6 |
| Not implemented upstream at all (`top_p`, `repetition_penalty`) | 2 |
| Absent from the codebase entirely | 24 |
| **Total** | **43** |

"Partially present" covers fields that exist in some form but not usably:
`checkpoint_step` is in the registry but not written to the output,
`prompt_condition` is conflated with `mode`, `sample_index` exists only as a
position in a list, and `judge_raw_response` appears only in judged runs.

The two that matter most, and that are absent rather than merely discarded, are
`seed` and `model_revision`. Between them they determine whether a generation can
be regenerated at all. Everything else describes the conditions under which it
was.

---

## Failures are records too

A failed generation gets a record. Same schema, with `completion` null and an
added `error` field holding the exception type and message.

The reason is the denominator. A reproducibility rate computed only over
successful generations is not a reproducibility rate. If 20 of 120 attempts
crashed and were never written down, every percentage in this project is wrong.
Upstream currently has no error records at all, so it is not possible to say
whether any run had failures.

---

## What this does not solve

Recording these fields makes a run re-derivable. It does not make it correct.

It does not address whether the judge agrees with a physicist, whether the corpus
is genuinely free of post-cutoff material, or whether the questions test
reasoning rather than retrieval. Those are separate pieces of work and are
covered elsewhere in `notes/plan.md`.

What it does is turn every future run into evidence rather than an anecdote,
which is the precondition for all three of those questions being answerable.

---

## Implementation note

The intervention point is line 609 of `scripts/physics_eval.py`, where
`json.dump(all_generations, f, indent=2)` writes the current record. The sampling
parameters are already in scope three lines above, at lines 595 to 604.

The plan is to write a wrapper in `tools/` that calls into the upstream script
rather than editing it, so that upstream stays at its pinned commit and any
difference in results remains attributable to environment rather than to local
changes. That decision is recorded as D003 in `notes/decisions.md`.

Two fields require adding something upstream does not have rather than recording
something it does: `seed` must be set with `torch.manual_seed` before generation,
and `model_revision` must be passed to `snapshot_download` and read back.

---

## Schema 1.1, 3 Sep 2026

43 fields became 48. One field changed meaning. The reason for every change is
below, because a schema that changes without a recorded reason has the same
problem as the archive this sprint is criticising.

### Changed

| Field | 1.0 | 1.1 |
|---|---|---|
| `dtype` | `"bfloat16" if device.type == "cuda"`, inferred from the device | read off the loaded model with `next(model.parameters()).dtype` |

The 1.0 rule was inherited from upstream and assumes every GPU is Ampere or
later. Expanse GPU nodes are V100, compute capability 7.0, which has no hardware
bfloat16. Under 1.0 this archive would have recorded a dtype the hardware cannot
produce. A parameter knows what it is; a device name does not. Null when the
checkpoint failed to load, which means "no weights existed", not "not recorded".

### Added

| Field | Why |
|---|---|
| `gpu_name` | `Tesla V100-SXM2-32GB` and an A100 are not interchangeable and the archive should say which ran |
| `compute_capability` | The number that determines what the hardware can actually do, `7.0` for Volta |
| `bf16_supported` | `torch.cuda.is_bf16_supported()`. Recorded next to `dtype` so the two can be checked against each other rather than assumed consistent |
| `slurm_job_id` | Ties a record to the scheduler log that produced it. Without it a cluster run cannot be traced back |
| `deterministic_algorithms` | Whether `torch.use_deterministic_algorithms(True)` was in force. Off by default, because phase 2 measures reproduction as the pipeline stands. Recorded either way, so no reader has to guess which run they are reading |

### Consequence for comparisons

`tools/compare_runs.py` treats `temperature`, `top_k`, `num_samples`,
`max_tokens`, `model_repo`, `model_revision`, `eval_config_sha256`,
`code_commit` and `schema_version` as blocking: if any differ between two runs it
refuses to report a reproduction rate. `device`, `dtype`, `gpu_name`,
`compute_capability`, `bf16_supported`, `torch_version`, `platform`,
`python_version`, `deterministic_algorithms` and `code_dirty` are reported as
differences but do not block, because a comparison across them is a portability
test rather than a determinism test and should be labelled as one.

---

## Schema 1.2, 22 Sep 2026

One field added.

| Field | Why |
|---|---|
| `dtype_override` | `auto`, `float32` or `bfloat16`. What `--dtype` was passed. `auto` means upstream's rule was left alone. Needed because the float32 control on a V100 patches upstream's KV cache dtype at runtime, and a reader has to be able to see that a run was forced rather than default |

`dtype` still records what the weights were actually held in, read off the model. The two together say what was asked for and what happened.

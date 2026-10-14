# Working in this repo

For scripts, automation and anyone picking the project up cold. The README says what was found; this page says how the repo is organised and the rules it runs on.

## Layout

```
notes/        lab-notebook.md (E001...), decisions.md (D001...), where-we-are.md, runbook.md, provenance.md, logging-schema.md
evidence/     one directory per experiment: raw .jsonl, graded .jsonl, html page, readings
tools/        every script; run from the repo root
logs/         terminal output of every command, one file per command; logs/expanse/ holds Slurm .o and .e files
reports/      memo, overview page, paper drafts, talking points
upstream/     the authors' clone, pinned, never edited, not tracked (see .gitignore)
docs/         this page
```

## Rules

1. `upstream/gpt1900` is pinned at `5b489c8c` and never edited. Patches, if any, are applied at runtime from `tools/` and recorded in `notes/decisions.md`.
2. Never push to the upstream repository.
3. Every command that produced a result has its output under `logs/`. A command whose output was not captured did not happen.
4. Every experiment gets one entry in `notes/lab-notebook.md`: phase, goal, command, exit status, upstream commit, result with denominators, interpretation, next. Entries are append-only and numbered. Cite by number.
5. A choice that could bend a result is written in `notes/decisions.md` before the result is seen: what was decided, why, what was rejected, what would change it.
6. Report every count with its denominator. Report negative results. Nothing is dropped from `evidence/`.
7. Grades carry the grader's name, version and temperature in the record. A grading failure is `null`, never `0`.
8. The comparison tool refuses to report a match rate when two runs differ in any generation setting. Do not work around it.
9. `notes/paper-mapping.md`, `notes/meeting-1-notes.md` and anything quoting the draft paper stay out of the repo.
10. Prose: plain English, no em dashes, numbers over adjectives.

## The generation record

`tools/logged_eval.py` writes one JSON line per answer with 50 fields (schema 1.2, listed in `notes/logging-schema.md`): model repo and revision, weights SHA-256, prompt and its hash, eval config and its hash, seed, temperature, top_k, top_p, num_samples, max_tokens, dtype, device, GPU name, `bf16_supported`, deterministic-kernel flag, torch and Python versions, Slurm job id, timing, finish reason, completion and its hash, the eight judge fields, and the code commit. Downstream tools key records by `checkpoint_name|task_id|seed|sample_index`.

## Commands

```
python tools/logged_eval.py --help                      generate; see notes/runbook.md for each experiment
python tools/compare_runs.py a.jsonl b.jsonl            byte identity, refuses on mismatched settings
python tools/render_html.py run.jsonl --html run.html   readable page
python tools/blind_packet.py run.jsonl --batches 24     shuffled grading batches, sealed key
python tools/judge_import.py ...                         grades back through the key
python tools/judge.py run.jsonl --dry-run               the authors' judge model and rubric; needs ANTHROPIC_API_KEY
python tools/report.py ...                               means, bootstrap intervals, per task and checkpoint
python tools/abduction_report.py ...                     verdict pages for the blind-read runs
python tools/decide.py run.jsonl --config ... --mode verdict --dry-run   second machine reader; needs OPENAI_API_KEY
```

Slurm jobs for Expanse: `tools/run_*.sh`, `tools/debug/*.sh` for the 30-minute debug partition. Each writes to `logs/expanse/`.

## Conventions

- Checkpoint names are the authors' (`discovery-rl-v11-s035` ... `s839`, base `d34-22btok`).
- Prompt conditions: `scaffolded` (authors' prompt), `minimal` (no classical assumptions), `leading` (scaffolded plus one generated hint paragraph, D007).
- Blind reading verdicts come from the ladder in the eval config (`verdicts`, `verdict_help`), highest rung reached, D009.
- Readings and grades are merged back through `key.json` in each evidence directory; the key is kept so the mapping can be audited.
- Dates in notes are absolute. Intervals are 95% bootstrap, 2000 resamples.

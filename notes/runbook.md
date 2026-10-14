# Runbook: what is left, in order

Written 15 Sep 2026. Status 23 Sep: steps 0 to 8 done (E035 to E044); scores came from the blinded session grader (D008) rather than the API judge; step 9 memo written, slides drafted, benchmark table written. Kept as the record of how the runs were sequenced. Every step is one command, ends in an HTML page, and says
what to expect before it runs. GPU steps run on Expanse from the project root.
Mac steps run from `~/Desktop/Akshat/Projects/gpt1900-repro/` with `.venv`.

## Where things stand

Done: pipeline (`logged_eval.py`, 50-field record), comparison tool, HTML
renderer, Expanse working on V100, determinism test at temperature 0 (8 of 8
identical, E032), three weekly reports.

Not done: everything below. Only one checkpoint (s560) has ever been run, at
temperature 0, once, unjudged.

## The six workstreams and what covers each

| Workstream | What covers it | Status |
|---|---|---|
| 1. Reproduce a published evaluation on released checkpoints | Step 3, all 24 v11 checkpoints at upstream's exact settings, then judged in step 6 | scripted, not run |
| 2. Pipeline recording prompt, output, model version, seed, temperature, scoring decision | `logged_eval.py` + `judge.py`, 50 fields per record | built, generation half proven, judge half dry-run only |
| 3. Prompt sensitivity (scaffolded, minimal, leading) and contamination | Step 2 for the three prompts, steps 4 and 5 for contamination | scripted, not run |
| 4. Archive all generations, no cherry-picking | every JSONL under `evidence/`, failures included, denominators in every report | standing |
| 5. Source-backed evidence table of AI-discovery benchmarks | nothing. Desk research with citations, no script possible | not started |
| 6. Blinded review packet, memo, presentation | Step 8 for the packet; memo and slides are writing | packet scripted, memo and slides not started |

## Order

Steps 1 to 5 are Expanse jobs and can all be submitted the same afternoon; the
scheduler runs them as GPUs free up. Steps 6 to 9 happen on the Mac once the
evidence is pulled back.

### Step 0. Pull the new tools up to Expanse

    rsync -av tools/ $EXPGPT/tools/
    rsync -av upstream/gpt1900/EVAL_no_assumptions.json $EXPGPT/upstream/gpt1900/

Expect: file list, no errors. `EVAL_no_assumptions.json` is already in the
upstream clone on Expanse if the clone is complete; the second line is a
belt-and-braces copy.

### Step 1. Seeded sampling, `sbatch tools/run_sampling.sh`

What it does: s560, all 8 tasks, temperature 0.7, top_k 50, seed 42, one
sample, four times. Runs a and b with normal kernels, c and d with
`--deterministic`. Three comparisons and one report.

Expect: about 8 minutes. Read `evidence/sampling/compare-ab.html`.

Why: temperature 0 never touches the random generator, so E032 said nothing
about sampled runs. These are upstream's actual settings. Three outcomes:

- a = b, 8 of 8. Seeded sampling reproduces on one machine. Their divergence
  was bookkeeping: unrecorded seed, unmatched sample counts. The fix is a
  seed field and a matched `--num-samples`, which the record now carries.
- a differs from b but c = d. Normal GPU kernels are non-deterministic at the
  bit level and a tiny logit shift flips a near-tie token under sampling. The
  fix is `--deterministic`, and the memo says so.
- c differs from d. Something below the sampler is unstable even with
  deterministic kernels forced. Bigger finding. Stop and look before step 3.

The upstream column: whether our seed-42 bytes equal their published v11 bytes
for the same cell. A match means their run reproduces exactly on a V100 with
emulated bf16, which would be remarkable. Zero matches is the expected outcome
and is a portability statement, not a failure: different GPU, different
torch, bf16 emulated here.

### Step 2. Prompt sensitivity, `sbatch tools/run_sensitivity.sh`

What it does: checkpoints s560, s630, s735 (the three upstream used for their
minimal-prompt run), 8 tasks, 3 samples (seeds 42, 43, 44), temperature 0.7,
under three prompts: scaffolded (`EVAL.json`), minimal
(`EVAL_no_assumptions.json`), leading (`tools/EVAL_leading.json`, upstream's
prompt plus one hint paragraph that hands over the core idea). 216 generations.

Expect: about 50 minutes, two checkpoint downloads. Three JSONL files and
`evidence/prompt-sensitivity/report.html` with text-level facts. Scores come
in step 6.

Why: upstream's own comparison used different sample counts per condition
(E025). This holds everything equal except the prompt. If leading scores rise
well above scaffolded, the benchmark is partly measuring how much of the
answer the prompt already contains. The 3-sample spread per cell is also the
error bar the published mean lacks.

### Step 3. The full sweep, `sbatch tools/run_sweep.sh`

What it does: all 24 v11 checkpoints, 8 tasks, 1 sample, seed 42, temperature
0.7, scaffolded prompt. 192 generations, the exact cell count behind the
published 0.932. Keeps every checkpoint in `hf_cache/` (~158 GB, inside the
500 GB allocation).

Expect: 60 to 90 minutes. `evidence/sweep/v11-scaffolded.jsonl`, 192 lines,
and `report.html` showing byte matches against upstream per cell (expect
near zero, see step 1) and the stock-opening rate.

Why: this is workstream 1. Once judged (step 6) it gives a mean with a
denominator and a bootstrap interval, computed by someone outside the project,
against their 0.932. The interval on their number, computed from their own
file, is 0.84 to 1.03; ours will be about as wide. Agreement or not, both
numbers will finally have error bars.

If the job dies part way, move the partial file aside before resubmitting.
The file is append-only and a rerun into it would double-count.

### Step 4. Knowledge probe, `sbatch tools/run_knowledge_probe.sh`

What it does: 16 sentence stems from `tools/probe_knowledge.json`, continued
greedily (temperature 0, 200 tokens) by the base model `d34-22btok` in
completion mode and by s560 in chat mode. 11 stems are post-1900 physics
(Planck's constant, photon, Einstein, relativity, E = mc^2, spacetime, Bohr,
the year 1905, the 1901 Nobel, the Wright brothers), 5 are pre-1900 controls
(Thomson's electron, Michelson-Morley, Maxwell, the aether, Rontgen's rays).

Expect: about 8 minutes, one download. `evidence/contamination/probe.html`:
rows in red use a post-1900 term or cite a year of 1900 or later.

Why: contamination from the model's side. Expect the controls to be
continued sensibly and the post-1900 stems to be continued with period
confusion or invention ("Einstein" as an unknown name, "photon" as nonsense).
Any confident, correct continuation of a post-1900 stem is a lead worth
reading closely. Keyword flags are a sort, not a verdict.

### Step 5. Corpus search, `sbatch tools/run_corpus_search.sh`

Before the first submit, once, on Expanse:

    conda activate GPT1900 && pip install pyarrow

What it does: downloads the 56 GB training corpus and scans every document
for 15 terms (Planck, Michelson, Morley, aether wind, Rayleigh, quantum,
quanta, photoelectric, Einstein, relativity, Lorentz, FitzGerald, photon,
spacetime, Nobel Prize), with a year histogram and snippets per term, and
counts any document dated 1900 or later. CPU only.

Expect: 30 to 70 minutes. `evidence/contamination/corpus-search.html`.

Why: contamination from the corpus side, plan item 3.2. Planck and
Rayleigh hits dated 1899 or earlier are fine and expected (both published
before 1900). Michelson and Morley hits are expected and are the point: the
task's experiment is in the training data. "photon" and "spacetime" should be
zero; any hit is a mislabeled document and goes in the memo. "Documents with
year >= 1900" should be zero per the corpus README; if it is not, that is a
finding on its own. A clean result is still a result: "checked, found
nothing" is a real contribution to the contamination section.

### Step 6. Pull evidence down, judge on the Mac

    rsync -av $EXPGPT/evidence/ evidence/
    rsync -av $EXPGPT/script_logs/ logs/expanse/
    .venv/bin/pip install anthropic
    export ANTHROPIC_API_KEY=...        # from Keating, or your own

Then, cheap first:

    .venv/bin/python tools/judge.py evidence/sweep/v11-scaffolded.jsonl --dry-run
    .venv/bin/python tools/judge.py evidence/sweep/v11-scaffolded.jsonl --limit 3

Expect: dry run prints the exact prompt and a cost estimate (about $1 for
192). `--limit 3` spends a few cents and proves the key works. Then the real
passes:

    .venv/bin/python tools/judge.py evidence/sweep/v11-scaffolded.jsonl
    .venv/bin/python tools/judge.py evidence/prompt-sensitivity/scaffolded.jsonl \
        evidence/prompt-sensitivity/minimal.jsonl evidence/prompt-sensitivity/leading.jsonl
    .venv/bin/python tools/judge.py evidence/sampling/run-a.jsonl

Each writes `<name>.judged.jsonl` beside its input, never touching the input.
Resumable: rerun the same command after a crash and it skips what is scored.
Failures are recorded as null, not 0. Whole budget for everything above:
under $5 with upstream's judge model.

Judge reliability, the grade graded twice:

    .venv/bin/python tools/judge.py evidence/sweep/v11-scaffolded.jsonl \
        --out evidence/sweep/v11-scaffolded.judged-again.jsonl

Why: upstream never judged a repeat run, so no reproducibility figure for the
score exists. Two answers can differ in text and both score 1; the score may
be stable when the text is not. This is the number the memo is about.

### Step 7. Reports

    .venv/bin/python tools/report.py evidence/sweep/v11-scaffolded.judged.jsonl \
        evidence/sweep/v11-scaffolded.judged-again.jsonl \
        --upstream-dir upstream/gpt1900/results/physics_eval_v11 \
        --out evidence/sweep/report.json --html evidence/sweep/report.html

    .venv/bin/python tools/report.py evidence/prompt-sensitivity/scaffolded.judged.jsonl \
        evidence/prompt-sensitivity/minimal.judged.jsonl evidence/prompt-sensitivity/leading.judged.jsonl \
        --upstream-dir upstream/gpt1900/results/physics_eval_v11_no_assumptions \
        --out evidence/prompt-sensitivity/report.json --html evidence/prompt-sensitivity/report.html

Expect: the headline table, mean with 95% CI and n per series, per task, per
checkpoint, per condition, and pairwise byte and score agreement. The sweep
page sets our mean beside 0.932 and shows judge-vs-judge exact agreement. The
sensitivity page shows leading minus scaffolded per task.

Numbers already known from upstream's own files, for calibration: scaffolded
0.93 (n=192, CI 0.84 to 1.03); their minimal run 1.38 (n=72, CI 1.21 to
1.54); 150 of 192 scaffolded and 72 of 72 minimal outputs open with the stock
phrase.

### Step 8. Blinded packet

    .venv/bin/python tools/blind_packet.py evidence/sweep/v11-scaffolded.judged.jsonl \
        evidence/prompt-sensitivity/leading.judged.jsonl \
        --upstream-dir upstream/gpt1900/results/physics_eval_v11 \
        --per-task 6 --outdir evidence/review-packet

Expect: 48 answers, shuffled with a recorded seed, provenance stripped.
`packet.html` for reviewers, `score-sheet.csv` to fill in, `key.json` sealed.
Mixing ours, theirs and the leading-prompt answers means a reviewer cannot
tell which is which, and the key later tells whether humans rank the leading
answers higher the way the LLM judge does.

### Step 9. Writing

- `reports/reproducibility-memo.md`. From `report.html` pages. Sections: what
  was reproduced and how (settings, revisions, hardware, denominators); the
  numbers with intervals; what could not be checked and why (unpublished
  checkpoints, V100 bf16 emulation, judge model deprecated); the record-keeping
  standard.
- Evidence table of AI-discovery benchmarks (workstream 5). Desk research,
  every row cited. Not scripted, not started.
- Presentation. From the memo.

## If something is blocked

- No API key: steps 1 to 5 still run and every text-level fact still lands.
  The memo reports generations reproduced or not, and states that scoring was
  not possible. Say so on the day, not at the end.
- Sweep too slow: it checkpoints per record. A partial file with its
  denominator stated is still evidence.
- Corpus download too slow: `--max-shards 4` scans 10 percent and says so.

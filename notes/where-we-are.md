# Where we are

**The one file to open when picking this back up.** Updated at the end of every
block of work. Newest work log entry is at the bottom.

---

# START HERE: the next thing to do

**14 Oct, done.** The repo is on GitHub, private: https://github.com/akshatsingh-dev/gpt1900-repro. README for readers, `docs/agents.md` for anyone running the tools. Results pack and one-page summary sent to a new collaborator.

**7 Oct, done.** The professor's elevator question in his words to every checkpoint (E049): 0 of 75 say you feel no weight, 23 say weight is still felt, rising with training. The abduction suite (E050): 0 of 140 reach the jump under any phrasing or help, and the in-corpus deduction and induction controls fail as well. Pages `evidence/elevator-final/report.html` and `evidence/abduction/report.html`. Design note `notes/abduction-suite.md`, D009.

**1 Oct, done.** Free fall at n=72 graded and read (E047): hint effect +0.00 against +0.89 on the elevator (E045); given the 1907 observation alone, 0 of 144 answers supply the equivalence. Pages `evidence/freefall/summary.html` and `jump.html`. Paper draft has no placeholders left; memo 5.1, brief and talking points carry both GR tasks.

**22 Sep, done.** Sweep generated and graded (E042), cross-graded against the authors' own answers (E044): the model reproduces to within 0.01 under one grader; the published 0.93 moves by 0.33 with a change of grader. Memo, talking points, slides 6, and `reports/presentation-brief.md` carry the numbers. The dtype control is E043, files in `evidence/dtype-control/`.


**Read the notebook from E041 onward.**

Three things ran overnight on 22 Sep:

1. **Grading the 24-checkpoint sweep.** 192 generations at upstream's exact
   settings, job 54390360 [E038], scored through the blinded packet, the
   provisional grader of D008. Lands in `evidence/sweep/`.
2. **A float32 dtype control** on s560. The GPU attempt hit upstream's own
   bf16 assert (gpt.py:396); the CPU path ran instead, job 54390459. Result:
   **0 of 8** identical to the V100 run, identical prefixes of 35 to 142 words
   then one token flips and the rest cascades [E043]. The CPU path run twice
   is 8 of 8 identical (job 54390635). Each machine repeats itself; the two
   machines disagree. Everything in `evidence/dtype-control/`.
3. **Finishing the corpus search** over the 56 GB training set, job 54390362
   [E038]. Lands in `evidence/contamination/corpus-search.html`.

Each result has its own notebook entry from E041 onward, failures included.

Then, in this order:

- **Put the sweep mean beside 0.932.** `evidence/sweep/report.html`. Their
  interval, from their own file, is 0.84 to 1.03 [E033].
- **Fill the PENDING marks** in `reports/reproducibility-memo.md` and
  `reports/presentation-talking-points.md` from the sweep and corpus pages.
- **Repeat batch 01** of the review packet for a second grader reliability
  figure. Batch 02 came back 24 of 24 [E039].
- **Ask Keating for the API key.** The one thing on the list only he can
  unblock. Every score so far is from a provisional grader, not the judge the
  paper used (D006, D008). `tools/judge.py` is written and dry-tested [E033].
  The whole pass costs under $5.

## Closed since 1 Sep

- `notes/meeting-1-notes.md` is gitignored.
- The vintage-model survey is rows in `reports/evidence-table.md`.

---

# The one question

If someone else re-ran GPT-1900's physics test, would they get the same score?
Nobody had ever checked. That is the gap this sprint closes.

Where it stands: the text reproduces. Same checkpoint, same settings, run
twice on one machine: 8 of 8 answers byte-identical at temperature 0 [E032]
and 8 of 8 at upstream's own sampled settings [E035]. The published divergence
was bookkeeping, not the model [E026]. The score has never been checked with
the judge the paper used, because there is no API key. That is the open half.

# The map

```
0. Set up and pin their code             DONE
1. Read their files, find what's there   DONE
2. Install it, get one model running     DONE, on Expanse, V100          [E028 to E032]
3. Run one question, compare to theirs   DONE, 0 of 8 bytes match, expected [E032]
4. Run it twice with randomness off      DONE, 8 of 8, then seeded 8 of 8  [E032, E035]
5. Build proper logging                  DONE, schema 1.2                 [E031]
6. Test if wording changes the score     DONE, provisional grader         [E037, E039]
7. Check the training data for leaks     DONE, probe and corpus search [E036, E040, E041]
8. Write the benchmark comparison table  DONE, reports/evidence-table.md
9. Judge packet, memo, talk              DONE, packets built, memo, slides, talk given 23 Sep
```

Phase 9 detail: `tools/blind_packet.py` and a first packet in
`evidence/review-packet-a` [E039]; `reports/reproducibility-memo.md` drafted
22 Sep, numbers filled in from the sweep and corpus pages;
`reports/presentation-talking-points.md` written; `reports/slides.html`
drafted the same night.

---

# What has been found, all measured here

## From their archive, 25 Aug

| Finding | Number |
|---|---|
| Occurrences of `seed` in their eval code | **0** |
| Occurrences of `revision` in their eval code | **0** |
| Fields saved per generation | 3: `prompt`, `mode`, `completions` |
| `v8` vs `v8_det`, prompts identical | 96 of 96 |
| `v8` vs `v8_det`, answers identical | **0 of 96** |
| `v11` vs `v11_replication`, answers identical | **2 of 24** |
| **Combined reproduction rate** | **2 of 120, 1.7%** |
| Checkpoints in registry | 89 |
| Checkpoints never published (`"local"`) | **54, 61%** |
| Published v11 outputs opening "You have touched" | **150 of 192, 78%** |
| Runs with generations that were never graded | **5 of 12** |
| Tests covering `physics_eval.py` | **0** |

## From runs on Expanse, 8 to 22 Sep

| Finding | Number |
|---|---|
| Same checkpoint, temperature 0, run twice, byte-identical | **8 of 8** [E032] |
| Our temperature-0 answers matching their published sampled ones | 0 of 8, expected [E032] |
| Seeded sampling at their settings (0.7, top_k 50, seed 42), a vs b | **8 of 8** [E035] |
| Same, deterministic kernels forced, c vs d | 8 of 8 [E035] |
| Same, normal vs deterministic, a vs c | 8 of 8 [E035] |
| Sensitivity generations, 3 checkpoints x 3 prompts x 3 seeds | 216 of 216, 0 errors [E037] |
| Stock opening under all three prompt conditions | **216 of 216** [E037] |
| Scaffolded mean, provisional grader, 95% bootstrap CI | 1.36 (1.22 to 1.50), n=72 [E039] |
| Minimal mean | 1.22 (1.12 to 1.32), n=72 [E039] |
| Leading mean | **1.64 (1.46 to 1.83)**, n=72 [E039] |
| Answers scored through the blinded packet | 224 of 224, 0 unparseable [E039] |
| Grader re-grading one batch, exact agreement | 24 of 24 [E039] |
| Sampling run a, s560, graded | 1.00, n=8 (0.62 to 1.38); their s560 row 1.25; same score in 6 of 8 cells [E039] |
| Greedy knowledge probe, generations | 32 of 32; every flag an echo of the stem's own word [E036] |
| Sampled knowledge probe, post-1900 stems clean | **66 of 66** [E040] |
| Sampled probe, pre-1900 controls the base model knew | 2 of 15, both the aether [E040] |
| Sampled probe, controls the RL model knew | 0 of 15 [E040] |

## From their files, recomputed with `report.py`

| Finding | Number |
|---|---|
| Their scaffolded sweep, mean with 95% CI | 0.93 (0.84 to 1.03), n=192 [E033] |
| Their minimal run, mean with 95% CI | 1.38 (1.21 to 1.54), n=72 [E033] |
| Their minimal outputs with the stock opening | 72 of 72 [E033] |
| Their judge failures written as 0 in the v11 file | 0 of 192 rationales say "Judge error" [E033] |

## Why it happens, traced to the line, then confirmed by running it

1. `scripts/physics_eval.py` never passes a seed, so the engine default of 42
   applied to every published run. The seed was fixed, not absent. It was
   never written down. [E026]
2. One random generator serves every row of a batch, so sample 0 of a
   three-sample run and sample 0 of a one-sample run consume different draws
   from the same seed. Both upstream run pairs used mismatched
   `--num-samples`. [E022, E026]
3. Line 609 writes the results. Temperature and top_k sit three lines above,
   left out. [E017, E018]
4. No `revision` on the download, so weights behind a name can change. [E020]
5. Prediction from 1 and 2: record the seed, match the sample count, get byte
   identity. Measured: 8 of 8 at temperature 0, 8 of 8 sampled, on normal and
   on deterministic kernels. No hardware nondeterminism was needed and none
   was seen. [E032, E035]

## What the score is sensitive to

With checkpoints, seeds and sample counts matched, one hint paragraph moves
the mean by +0.28, on a benchmark whose whole published signal is 0.93. The
biggest gains land on the two tasks whose hint most nearly states the rubric's
top answer: elevator +0.89, frozen light +0.56. UV catastrophe goes the other
way, -0.33. Leading above scaffolded above minimal holds on all three
checkpoints. Removing the assumptions costs about 0.14, the reverse of
upstream's own unmatched comparison. [E025, E039]

## What the model knows

Nothing datable, in either direction. 66 of 66 post-1900 stems came back clean
under sampling, but the base model could state one of five pre-1900 facts (the
aether, twice) and the RL model none. The probe measures absence of recall in
general, so the clean post-1900 result bounds contamination by recall, and
recall is near zero at the level of named facts. The corpus search is the
instrument that separates "never saw it" from "did not retain it". [E036,
E040] The RL checkpoint answers every stem in the same letter voice, boiler
design for Michelson and Morley, wages for E = mc^2. That is the line to show
Keating. [E036]

## What they did well

Results saved after every checkpoint for crash resilience. Each checkpoint
deleted after use, download filtered to one step's weights. Peak disk is one
checkpoint. [E018, E020] Their judge prompt builder imports unchanged into
`tools/judge.py`, so the rubric is theirs byte for byte. [E033]

## Corrections made, kept on the record

- **Mode mismatch.** Suspected the v8 run used the wrong prompt format. Checked.
  It did not. Withdrawn. [E020]
- **Sample counts.** Said every run stored one answer per question. Two of four
  store three. Redid the headline comparison allowing any of three to match.
  Result held at 0 of 96. [E022]
- **Prefix agreement.** Read a 904-character shared opening as near-determinism.
  It is a stock phrase. [E023]
- **"Abandoned" runs.** Implied an accident. They used a documented
  `--skip-judge` flag. [E016]
- **Field count.** Wrote "seventeen" then "37" from hand counts. Recomputed from
  the tables: 43.
- **"No seed."** Carried from E011 to E026. Literally true of
  `physics_eval.py`, wrong as an inference: the engine seeds at 42 by default.
  The logging gap stands. The mechanism changed. [E026]
- **"Nothing installed."** This file said so on 1 Sep. The venv existed and
  imported clean on 3 Sep. The real blocker was 3.3 GB of free disk. [E028]
- **"No GPU allocation."** Read off `expanse-client` without `-a`.
  `accessusage` shows 1000 GPU hours, unused. One tool is one source. [E029,
  E030]
- **dtype recorded by guess.** My own tool wrote `bfloat16` for any CUDA
  device. V100 has no bfloat16. Now read off the loaded model, with
  `bf16_supported` beside it. [E028, E031]
- **E032 entered a week late.** Run 8 Sep, reported in week 3, entered in the
  notebook 15 Sep. [E032]

---

# Promise status

Against the six items in Keating's email, `notes/goal.md`.

| Assigned | Status |
|---|---|
| 1. Reproduce a published evaluation on released checkpoints | **Partly.** Generation reproduces, 8 of 8 twice [E032, E035]. The full 24 x 8 sweep at their settings ran as job 54390360 [E038] and was graded with the provisional grader: 1.27 against the published 0.93, and the gap is the grader [E042, E044]. **Not graded with their judge model**, `claude-sonnet-4-20250514` (D006). No API key. |
| 2. Pipeline recording prompt, output, model version, seed, temperature, scoring decision | **Generation half done and proven** [E031, E032]. Scoring half: `judge.py` dry-run only [E033]; the scores that exist were written by `judge_import.py` with the grader named and temperature null [E039], per D008. |
| 3. Prompt sensitivity and contamination: scaffolded, minimal, leading | **Done under the provisional grader** [E037, E039]. The leading condition was **generated, not hand-written**: one hint paragraph appended per task by script, every other field byte-identical (D007). Model-side probe done [E036, E040]. **Corpus search is tonight** [E038]. |
| 4. Archive every generation, no cherry-picking | **Standing.** Every JSONL under `evidence/` with its denominator: 16 determinism, 32 sampling, 216 sensitivity, 32 greedy probe, 96 sampled probe, 0 errors in any [E032, E035, E036, E037, E040]. |
| 5. Source-backed evidence table of AI-discovery benchmarks | **Done**, `reports/evidence-table.md`, every row read at the source 22 Sep. |
| 6. Blinded review packet, reproducibility memo, presentation | **Packet built**, `evidence/review-packet-a`, 224 answers in 10 batches, key sealed [E039]. **Memo written**, numbers filled in from the sweep. **Talking points written.** Slides built, talk given 23 Sep. |

The 15 Sep date passed with the sweep unsubmitted and nothing judged [E033].
The definition of done in `notes/goal.md` is being met a week late, with a
provisional grader standing in for the real one.

The 23 Aug inventory promises are all closed. "Whether it runs" closed on
Expanse [E028, E032]. "Related vintage-model projects" closed in the evidence
table.

---

# Files

## Notes

| File | What it holds |
|---|---|
| `notes/where-we-are.md` | This. The resume point |
| `notes/goal.md` | The six assigned items and the one experiment that matters |
| `notes/runbook.md` | The remaining steps in order, one command each, what to expect |
| `notes/lab-notebook.md` | Every step, E001 onward, and what it meant |
| `notes/decisions.md` | D001 to D008, why a choice was made |
| `notes/provenance.md` | Pinned upstream commit, HF revisions, corpus shards |
| `notes/logging-schema.md` | The record fields, schema 1.2 |
| `notes/expanse-environment.md` | The 3 Sep cluster survey |
| `notes/serving-plan.md` | Hosting the model for public queries. Not started |
| `notes/tool-inventory.md` | Five-column audit table |
| `notes/paper-mapping.md` | Which draft sections this lands in. Gitignored |
| `notes/plan.md` | The 10 phases, and the four holes |

## Reports

| File | What it holds |
|---|---|
| `reports/reproducibility-memo.md` | The memo, drafted 22 Sep, numbers filled in after the sweep |
| `reports/evidence-table.md` | Workstream 5, benchmarks and their limits, every row cited |
| `reports/presentation-talking-points.md` | One heading per slide |
| `reports/plain-summary.md` | The whole thing in plain words |
| `reports/results-overview.html` | Every result on one page, for someone new to the project. 8 Oct |
| `reports/slides.html` | Slides for the 23 Sep talk |
| `reports/progress-week-1.md`, `-2.md`, `-3.md` | Monday updates to Keating |
| `reports/meeting-1notes.md`, `explanations.md`, `meeting-2026-08-26.md` | The 25 Aug meeting set |

## Evidence

| Directory | What it holds |
|---|---|
| `evidence/determinism/` | E032. Runs a and b, `compare.html` |
| `evidence/sampling/` | E035. Runs a to d, three compares, `run-a.graded.jsonl` |
| `evidence/prompt-sensitivity/` | E037, E039. Three conditions, `.graded.jsonl`, `report.html` |
| `evidence/contamination/` | E036, E040 probes, E041 corpus search |
| `evidence/review-packet-a/` | The blinded packet: `batches/`, `grades/`, `grades-repeat/`, `key.json`, `score-sheet.csv` |
| `evidence/sweep/` | E042, E044. The 24-checkpoint sweep and the cross-grade |
| `evidence/dtype-control/` | E043. V100 against CPU |

## Tools

| File | What it does |
|---|---|
| `tools/logged_eval.py` | The generation pass. Schema 1.2, `--dtype`, `--deterministic`, `--smoke-test` |
| `tools/compare_runs.py` | Two JSONL files to matched over total. Refuses when settings differ |
| `tools/render_html.py` | JSONL to a readable page |
| `tools/judge.py` | Their rubric, their judge model, temperature 0, failures null. Dry-run only |
| `tools/blind_packet.py` | Strips provenance, shuffles with a recorded seed, seals the key |
| `tools/judge_import.py` | Grades back through the key into the judge fields |
| `tools/report.py` | Means, bootstrap CIs, per task, checkpoint, condition, pairwise agreement |
| `tools/probe_report.py` | Keyword flags and blind readings for the knowledge probe |
| `tools/corpus_search.py` | 15 terms over the training corpus, year histogram, snippets |
| `tools/make_leading_config.py`, `tools/EVAL_leading.json` | The leading condition, generated (D007) |
| `tools/probe_knowledge.json` | 16 stems, 11 post-1900, 5 controls |
| `tools/run_sampling.sh`, `run_sensitivity.sh`, `run_sweep.sh`, `run_knowledge_probe.sh`, `run_knowledge_probe_sampled.sh`, `run_corpus_search.sh` | Slurm jobs, one per experiment |
| `tools/runsmoke.sh`, `runeval.sh`, `runprobe.sh`, `runfp32.sh` | The early one-off jobs, and the dtype control |
| `logs/` | Raw output. `logs/expanse/` holds every Slurm `.o` and `.e` file |

---

# Work log

## 25 Aug 2026

Phases 0 and 1 complete. Nothing run against a model.

Cloned upstream and pinned to `5b489c8c`. Read `scripts/physics_eval.py` end to
end. Compared both available pairs of runs and measured 2 of 120 paired
generations reproducing. Traced the cause to zero occurrences of a seed, sampling
on at 0.7, and the settings being dropped at the write on line 609. Found no
revision pinning, 54 of 89 checkpoints unpublished, 78 percent of published
outputs sharing one opening phrase, 5 of 12 runs never graded, and no test
coverage of the eval script.

Wrote the tool inventory, the logging schema, the paper mapping, the meeting
brief, its plain-language companion, and a pasteable summary for the meeting.

Made four corrections to my own earlier claims and kept them on the record.

Also wrote the week 1 progress email to Keating in two lengths, and a meeting
prep pass covering how to explain temperature and seed to a physics audience:
temperature as the Boltzmann factor on token logits, the seed as a Monte Carlo
initial state that was never recorded, and the observation that the published
mean of 0.93 carries no error bar because each of the 192 scores is a single
draw.

**Ended at:** ready to install the environment. Nothing blocking it.

## 26 Aug to 1 Sep 2026

No code run. Work was on communication and the compute application.

Wrote the week 1 progress update to Keating in two lengths plus a PDF. Built the
meeting brief with 12 findings, each with a plain-language companion entry, and a
prep pass on explaining temperature and seed to a physics audience: temperature
as the Boltzmann factor on token logits, the seed as an unrecorded Monte Carlo
initial state, and the fact that the published mean carries no error bar because
each of the 192 scores is a single draw.

Two new findings came out of reading the judged results, logged as E024 and E025.
86 percent of the 192 scores are 0 or 1 and the top of the rubric is never used,
though the mean does rise from 0.62 to 1.11 across training. And prompt wording
moves individual task scores by up to 1.3 points on a benchmark averaging 1.3,
though that comparison is confounded by differing sample counts and covers only
3 of 24 checkpoints.

Replaced `notes/plan.md` with a full week-by-week roadmap to 15 Sep, sized to 8
hours a week, with risks and an explicit out-of-scope list.

Drafted the ACCESS allocation request CIS261668 and filled it: 1000 GPU-hours,
4000 CPU core-hours, 500 GB storage on SDSC Expanse, 58,346 of 200,000 credits.
Both resource questions answered Yes.

Corrected a scope error along the way: an early draft of the allocation text
claimed training work that has not been assigned. The current sprint is inference
and analysis only. Whether the pre-1911 model is mine to build is an open
question for Keating.

**Ended at:** still nothing installed. Phase 2 unchanged and unblocked.

## 3 Sep 2026, environment and Expanse survey

E028 to E031. Nothing run against a model.

Found the local venv already worked, 33 packages, torch 2.14.0, imports clean,
and that free disk had fallen to 3.3 GB against a 6.6 GB checkpoint, so the
laptop was out [E028]. Surveyed Expanse over SSH: account `sdp197`, V100 GPUs
with no hardware bfloat16, PyTorch 2.2.1 in the SDSC container, and no GPU
allocation visible [E029]. Withdrew that last reading the same day:
`accessusage` shows 1000 GPU hours under CIS261668, unused, to Aug 2027
[E030]. Fixed the dtype recording bug in my own tool so dtype is read off the
loaded model, added `--deterministic`, `--limit-tasks` and `--smoke-test`,
bumped the schema to 1.1 at 48 fields, and wrote `compare_runs.py` with the
refuse-on-mismatch rule tested on fixtures [E031]. Wrote `notes/goal.md`,
`notes/expanse-environment.md` and `notes/serving-plan.md`.

**Ended at:** ready to clone upstream on Expanse and run the smoke test under
Slurm.

## 7 to 8 Sep 2026, first generation and determinism

E032. The first tokens generated, and the first measurement.

Four smoke jobs on Expanse to get a GPU node to load the model, then job
54222400: s560 at revision `71bf395f`, bf16 weights emulated on a V100,
temperature 0, all 8 tasks, run twice back to back. 8 of 8 byte-identical,
token counts identical per task, 8 of 8 opening with the stock phrase. 0 of 8
matched upstream's published sampled answers, as expected [E032]. Wrote
`render_html.py` and `reports/progress-week-3.md`. The notebook entry was not
written until 15 Sep.

**Ended at:** determinism settled at temperature 0. Seeded sampling at their
real settings next.

## 15 Sep 2026, scripted everything, then ran three of it

E033 to E037. The date the sprint was meant to end.

Turned every open experiment into a Slurm job ending in an HTML page, built
`judge.py`, `report.py`, `blind_packet.py`, `probe_report.py`,
`corpus_search.py` and the generated `EVAL_leading.json`, and wrote the runbook
[E033]. Running `report.py` over upstream's own files put an interval on their
number for the first time: 0.93 (0.84 to 1.03) scaffolded, 1.38 (1.21 to 1.54)
minimal, and 72 of 72 minimal outputs with the stock opening [E033]. Submitted
sampling, sensitivity and the greedy probe [E034]. Seeded sampling at their
settings came back 8 of 8 three ways [E035]. The greedy probe found no
post-1900 recall and no pre-1900 recall either, with loops on 13 of 16 stems
[E036]. Sensitivity generations landed 216 of 216, stock opening 216 of 216
[E037].

**Ended at:** sweep never submitted, nothing judged, no API key. Sprint
deadline missed on the reproduction number.

## 22 Sep 2026, sweep and corpus submitted, sensitivity graded

E038 to E040, D005 to D008.

Submitted the sweep, the sampled probe and the corpus search, jobs 54390360 to
54390362 [E038]. With no API key, graded the 216 sensitivity answers and
sampling run a through the blinded packet in fresh sessions, 224 of 224 scored:
leading 1.64, scaffolded 1.36, minimal 1.22, n=72 each, and 24 of 24 exact
agreement on a re-graded batch [E039]. The sampled probe came back 66 of 66
post-1900 stems clean, and the controls still failed [E040]. Wrote D005 to
D008, `reports/evidence-table.md`, the reproducibility memo draft, the
presentation talking points and the plain summary.

**Ended at:** sweep and corpus search still running on Expanse. Picked up
again at 03:01 the same night, below.

## 22 Sep 2026, from 03:01: dtype control, sweep graded, cross-grade

E041 to E044.

Started 03:01. Went back over what 15 and 22 Sep had already covered, found
three of the four job scripts I had drafted for the night redundant with E035
and E037, deleted them, kept the float32 control. Patched the KV cache dtype
at runtime from `logged_eval.py` so `--dtype float32` gives a pure float32
computation, upstream untouched (D003), schema 1.2. Submitted it at 03:05
with the sweep at 104 of 192 and the corpus search at 32 of 42 shards. From
there: graded the sweep through the blinded packet, rendered every page,
logged E041 onward, built `reports/slides.html`.

The corpus search came back 0 of 2,074,160 documents dated 1900 or later,
with one misdated 1909 report in the set anyway [E041]. The sweep graded at
1.27 (1.18 to 1.36) against the published 0.93 [E042]. The GPU float32 run
hit upstream's own bf16 assert, so the control ran on the CPU path: 0 of 8
identical to the V100 run, and the CPU path repeated against itself 8 of 8,
job 54390635 [E043]. Cross-grading the authors' 192 published answers put
their text at 1.26 under our grader, so the 0.34 gap is the grader, not the
model [E044].

**Ended at:** memo, talking points, slides and `reports/presentation-brief.md`
carrying the sweep and cross-grade numbers. The API key still open.

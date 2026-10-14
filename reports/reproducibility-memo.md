# GPT-1900 physics evaluation: reproducibility memo

Akshat Singh, for Prof. Brian Keating. Draft of 22 Sep 2026, covering work
from 25 Aug to 22 Sep. Every number below has a lab notebook entry (E001 to
E038 in `notes/lab-notebook.md`), a raw log under `logs/`, and an evidence
file under `evidence/`. Upstream is github.com/michaelhla/gpt1900 at commit
`5b489c8c`, never edited.

All jobs finished on 22 Sep; every number below is on disk.

## 1. The question and the short answer

GPT-1900 is a 3.29B-parameter model trained on about 22B tokens of pre-1900
English. Its authors evaluated 24 training checkpoints on 8 conceptual
physics prompts and had Claude grade each answer 0 to 5. The published
figure is a mean of 0.932 over 192 graded answers.

The question for this memo: can that figure be reproduced, and does the
record behind it allow anyone to check?

Short answer. The generation step reproduces exactly once two missing
settings are recorded. The published archive did not record them, which is
why the authors' own repeat runs disagreed with themselves 118 times out of
120. The score step had never been repeated by anyone. This memo reports a
repeat, with denominators and intervals: the model's answers reproduce the
published score level to within 0.01 under one grader, and the published
0.93 moves by a third of a point when the grader changes. The tooling makes
the next repeat a one-line job.

## 2. What the published record contains, and what it lacks

Read from the upstream repository before any model was run (E001 to E025).

| Fact | Where |
|---|---|
| Per-answer record holds three fields: prompt, mode, completions | `scripts/physics_eval.py`, write path at line 609 |
| Temperature, top_k, num_samples, max_tokens are in scope three lines above the write and not written | same |
| No `revision` pin on weight downloads; the Hugging Face name can move | `download_checkpoint` |
| No `seed` in the eval script; the engine's default of 42 applied silently | `nanochat/engine.py` line 171 |
| Run and repeat used different `--num-samples` (1 vs 3); one generator is shared across a batch, so the draws differ | E022, E026 |
| 54 of 89 registry checkpoints marked `local`, never published; every v8 checkpoint among them | E020 |
| 5 of 12 runs with generations were never graded; both repeat runs used `--skip-judge` | E012 |
| Judge call sets no temperature; a judge failure is written as score 0 | `judge_all`; 0 such cases in v11 |
| No test covers the eval script | E013 |

Consequence: 2 of 120 paired generations between published runs are
byte-identical (E014, E021). That number says nothing about the model. It
says the archive cannot distinguish a change in the model from a change in
the dice.

## 3. Does generation reproduce

All runs on SDSC Expanse, one Tesla V100-SXM2-32GB, torch 2.14.0+cu126,
weights held as bfloat16 with bf16 emulated (the card has no bf16 hardware;
recorded per generation as `bf16_supported: false`).

| Test | Settings | Result | Entry |
|---|---|---|---|
| Determinism | s560, temperature 0, twice | 8 of 8 byte-identical | E032 |
| Seeded sampling | s560, temperature 0.7, top_k 50, seed 42, one sample, twice | 8 of 8 | E035 |
| Same with deterministic kernels forced | as above plus `torch.use_deterministic_algorithms(True)` | 8 of 8 | E035 |
| Normal vs deterministic | run a vs run c | 8 of 8 | E035 |
| Against upstream's published bytes for the same cells | seed 42, their settings | 0 of 8 | E035 |

Reading. On one machine, with the seed and the sample count recorded,
generation at the authors' own settings is exactly repeatable, and the
deterministic-kernel switch changes nothing. The published divergence is
fully explained by the two unrecorded settings. The 0 of 8 against their
bytes is a portability statement: different GPU, different torch build,
emulated bf16. It is expected and it is not a failure of their pipeline.
Measured directly: the same checkpoint, prompt and argmax path on a CPU at
float32 gives 0 of 8 answers identical to the V100 run, with the two texts
agreeing for 35 to 142 words before one token flips and the rest diverges
[E043]. The CPU path run twice is itself 8 of 8 identical. Same-machine
repeatability holds on both machines; cross-machine text does not, even with
every setting recorded.

## 4. The full sweep

All 24 v11 checkpoints, 8 prompts, one sample, seed 42, temperature 0.7,
top_k 50, the scaffolded prompt. 192 generations, the cell count behind the
published mean. Each record carries the Hugging Face revision
(`71bf395f...`), the sha256 of the weight file, and 48 other fields.

Generation: 192 of 192, 0 errors, 4 answers cut at max_tokens, 64 minutes on
one V100 (E042). Stock opening 151 of 192 (published 150 of 192). Byte-identical
to the published answers: 0 of 192, as expected across hardware.

Scores: section 6. The short version: under one grader, our 192 answers and
their 192 published answers score within 0.01 of each other. The model
reproduces.

## 5. Prompt sensitivity

Three wordings of each prompt on three checkpoints (s560, s630, s735, the
ones the authors used for their own minimal-prompt run), three seeds each
(42, 43, 44), temperature 0.7. 216 generations, 0 errors, 0 truncated (E037).

- scaffolded: `EVAL.json`, classical assumptions listed
- minimal: `EVAL_no_assumptions.json`, assumptions removed
- leading: `tools/EVAL_leading.json`, the scaffolded prompt plus one hint
  paragraph that states the core idea. Generated from `EVAL.json` with every
  judge field byte-identical (D007).

Text-level result before any grading: 216 of 216 answers open with "You have
touched a matter of considerable importance", under every wording. The
published sweep: 150 of 192.

Scores (provisional grader, section 6), n=72 per condition, 95% bootstrap
intervals:

| Condition | Mean | Interval | Histogram 0/1/2/3/4 |
|---|---|---|---|
| minimal | 1.22 | 1.12 to 1.32 | 0 / 56 / 16 / 0 / 0 |
| scaffolded | 1.36 | 1.22 to 1.50 | 1 / 49 / 17 / 5 / 0 |
| leading | 1.64 | 1.46 to 1.83 | 0 / 40 / 20 / 10 / 2 |

The ordering leading > scaffolded > minimal holds on every checkpoint
separately (s560 1.54 / 1.29 / 1.17; s630 1.54 / 1.38 / 1.12; s735 1.83 /
1.42 / 1.38). Leading minus scaffolded per task: elevator +0.89, frozen light
+0.56, photoelectric +0.44, Michelson-Morley +0.44, free fall +0.11,
approaching c +0.11, train 0.00, UV catastrophe -0.33.

Reading. A hint that states the answer moves the mean by +0.28, on a scale
where the published signal is 0.93 and the whole spread across 24 checkpoints
is 0.25 to 1.25. The leading and minimal intervals do not overlap. The two
largest gains are on the tasks whose hint most nearly restates the rubric's
top answer. Removing the assumptions costs 0.14. The benchmark measures the
prompt as well as the model, by an amount comparable to the differences the
paper reports between checkpoints.

The authors' own comparison (scaffolded 0.93, n=192, against their minimal
run 1.38, n=72) used different sample counts per condition and different
checkpoint sets, so it cannot be read as a sensitivity result. Bootstrap
95% intervals computed from their files: 0.84 to 1.03 and 1.21 to 1.54.

### 5.1 The two general-relativity tasks at n=72

Upstream's two GR tasks are Einstein's two steps. `gr_free_fall_equivalence`
is the 1907 seed: a person falling from a roof feels no weight, so gravity
and acceleration are locally the same. `gr_main_elevator_light` is the 1911
consequence: if so, light must bend in gravity. Both were run on all 24
checkpoints, three seeds, three wordings, 72 answers per condition, graded
blind (E045, E047).

| Task | minimal | scaffolded | leading | hint effect, paired | highest score |
|---|---|---|---|---|---|
| 1911 elevator | 1.31 (1.18 to 1.43) | 1.57 (1.44 to 1.69) | 2.46 (2.26 to 2.65) | +0.89 (+0.69 to +1.08) | 4 |
| 1907 free fall | 0.92 (0.81 to 1.03) | 0.99 (0.89 to 1.07) | 0.99 (0.90 to 1.07) | +0.00 (-0.12 to +0.12) | 2 |

On the elevator the hint lifts 39 of 72 answers to 3 or 4; without it none
reaches 3. On free fall no answer in 216 reaches 3 under any wording, and a
hint of the same kind, stating that free fall is the natural state and
gravity is structure, moves nothing. Published means for the two columns are
1.46 and 0.92; ours under the published wording 1.57 and 0.99.

Then the test the benchmark lacks. The 1907 observation alone, with or
without the question "What does this tell us about gravity?", 24 checkpoints
x 3 seeds x 2 forms = 144 answers, read blind by two independent readers:
**0 of 144** bring in acceleration, equivalence, not-a-force or geometry on
their own. Every automatic keyword hit (7 of 144) is a false positive on
reading. The answers are period prose about air, muscles, inertia and
Newton's attraction, 117 of 144 in the stock voice.

Reading. The model can be led to the consequence and cannot be led to the
seed, even when the seed is handed to it. The elevator prompt states the
equivalence and asks for its consequence; the model carries a stated idea
forward. The free-fall prompt asks for the equivalence itself; the model
restates the observation. Given the observation and nothing else, it never
makes the step. That is the first stage of the Artificial Einstein Test
failing, measured on 360 answers rather than argued.

Caveats. Provisional grader (D008); regrades 35 of 48 exact on the elevator
packet and 38 of 48 on free fall, 96 of 96 within one point. One reading
pass on the jump count, two readers in agreement, no regrade. Pages:
`evidence/elevator/summary.html`, `evidence/freefall/summary.html`,
`evidence/freefall/jump.html`.

## 6. Scores

Every score below is on a page under `evidence/*/report.html`, with the
record behind it in the matching `.graded.jsonl`.

Grader. No API access was available during the sprint. Scores were produced
by a blinded reader: answers shuffled with seed 20260922, every provenance
field stripped, graded in fresh sessions of 24 by a Claude model
(claude-fable-5-1) that saw only the prompt, the authors' rubric and the
answer, then mapped back through the sealed key (D008). Two batches were
graded twice by independent sessions for a reliability figure. These scores
are provisional. The upstream judge, `claude-sonnet-4-20250514` at
temperature 0, should replace them when a key exists; `tools/judge.py` does
that in one command and the report then shows both graders side by side.

- Sweep, three series, n=192 each (E042, E044):

  | Text | Grader | Mean | 95% interval | 0 / 1 / 2 / 3 / 4 |
  |---|---|---|---|---|
  | our sweep | ours | 1.27 | 1.18 to 1.36 | 13 / 126 / 41 / 12 / 0 |
  | their published answers | ours | 1.26 | 1.17 to 1.35 | 13 / 125 / 45 / 9 / 0 |
  | their published answers | theirs, as published | 0.93 | 0.84 to 1.03 | 44 / 122 / 22 / 3 / 1 |

  Our text against their text under our grader: 126 of 192 cells exact, mean
  difference +0.01. Their text under our grader against their published
  grades, same bytes: 119 of 192 exact, 188 of 192 within one point, +0.33.
  Training trend, first eight to last eight checkpoints: 0.97 to 1.52 (ours),
  0.92 to 1.45 (their text, our grader), 0.62 to 1.11 (published). Rank
  correlation of the 24 per-checkpoint means, ours against published: 0.71.

  Reading. The generation step reproduces the published result at the level
  of the score: a fresh sweep on different hardware, graded beside the
  authors' own answers by one grader, lands within 0.01 with two thirds of
  cells agreeing exactly. The whole 0.34 gap between 1.27 and 0.93 is the
  grader. Same rubric, same answers, a different Claude, plus a third of a
  point, mostly from the zero row (44 zeros against 13). That shift is larger
  than the leading-prompt effect (+0.28, section 5) and comparable to the
  training gain across the sweep (+0.49). The published number is a property
  of the grader as much as of the model.
- Per-condition means and intervals: section 5
- Seeded sampling run a (s560, their settings), graded: 1.00, n=8, interval
  0.62 to 1.38; the published s560 row is 1.25; exact score agreement with
  the published grades on 6 of 8 cells despite different text and a
  different grader
- Grader reliability: 48 answers graded twice in independent sessions, 44 of
  48 exact (92%), 48 of 48 within one point, batch means identical
- Cross-grader check: the authors' minimal run on the same three checkpoints
  under their judge, 1.38 (1.21 to 1.54); ours on the same wording under this
  grader, different samples, 1.22 (1.12 to 1.32). The intervals overlap;
  their point estimate lies outside ours.

## 7. Contamination

### 7.1 Model side, greedy (E036)

16 sentence stems, continued at temperature 0 by the base model
`d34-22btok` and by `discovery-rl-v11-s560`. 11 stems about post-1900
physics, 5 controls about pre-1900 physics inside the corpus.

| Model | Post-1900 stems | Controls |
|---|---|---|
| base | 11 of 11 drew a blank | 4 fail, 1 partial, 0 correct |
| RL s560 | 11 of 11 drew a blank | 2 fail, 3 partial, 0 correct |

No post-1900 knowledge surfaced. Every keyword hit was the stem's own word
echoed. But the controls failed too: neither model could describe Thomson's
electron or the Michelson-Morley experiment. The negative result therefore
shows weak factual recall in general, not a clean pre/post-1900 split. Two
confounds: the base model loops at temperature 0 on 13 of 16 stems, and the
RL model answers every stem in the same period voice regardless of content
("Michelson and Morley showed that" a double-tube boiler is efficient).

### 7.2 Model side, sampled

The same 16 stems at temperature 0.7, three samples each, 96 continuations,
every one read blind against the expected outcome (E040).

| Model | Post-1900 stems (33) | Controls (15) |
|---|---|---|
| base | 33 clean, 0 leak | 2 knows (aether), 13 fail |
| RL s560 | 33 clean, 0 leak | 6 partial, 9 fail, 0 knows |

The repetition loops are gone and the verdict does not move. The base model
writes fluent 1890s prose in which "the electron" is a steel bar in copper
sulphate and "Michelson and Morley in 1887 showed that" is followed by
membership statistics of a National Association. It cannot state a single one
of the five pre-1900 facts except, twice, that the aether is the medium of
light.

Reading. The clean post-1900 result stands, and so does its limit: a
3.29B model on 22B tokens of OCR'd books does not carry named facts as
retrievable items, so a stem-completion probe cannot separate "never saw
Planck" from "saw it and did not retain it". The corpus search is the
instrument that can. The useful bound for the paper: contamination risk is
capped by recall, and recall at the level of named facts is near zero.

### 7.3 Corpus side

The training corpus itself, `mhla/pre1900-corpus` at revision `ff332ef6`, 42
shards, 56.4 GB, 2,074,160 documents, was scanned for 15 terms with a year
histogram per term and a count of documents dated 1900 or later [E041].

By metadata, 0 documents are dated 1900 or later; the range is 1547 to 1899.
Every term that could only exist after 1900 returns zero: Einstein, photon,
photoelectric, spacetime, aether wind. The terms that do appear are pre-1900
usages: Planck (705 documents, latest 1899), Lorentz (330), Michelson (277)
and Rayleigh (702) were all publishing before 1900; quantum (14,407) and
quanta (2,614) are ordinary Latin; relativity (1,391) is the philosophical
word; Morley (14,235) and FitzGerald (19,216) are surnames.

One hit is real contamination. A single document matches "Nobel Prize". Its
metadata year is 1829. Its text reads "The Nobel Prize was awarded in December
last to two distinguished Scandinavian peace workers, one-half to Mr. Fredrik
Bajer of Denmark". Bajer received the Peace Prize in 1908. The document is a
1909 annual report of the American Peace Society carrying a wrong date, and it
passed a date filter because of it.

Two conclusions follow. There is no evidence that the eight physics tasks are
answerable from leaked text: nothing in two million documents names the
physics that came after 1900, and the model-side probe (7.2) found no recall
of it. And the count of zero post-1900 documents is a lower bound, not a
proof: the corpus was assembled by date, at least one misdated source is in
it, and a term search cannot see paraphrase or post-1900 ideas written in
period vocabulary. The clean physics result stands with that caveat attached.

## 8. The record-keeping standard

`tools/logged_eval.py` writes one JSON line per generation with 50 fields
(`notes/logging-schema.md`), grouped as: run identity (run id, code commit,
dirty flag, config path and hash); model identity (repo, revision,
checkpoint, step, weight sha256); prompt (text, hash, condition, mode);
sampling (seed, sample index, temperature, top_k, num_samples, max_tokens);
environment (device, GPU, compute capability, bf16 support, dtype as loaded,
torch, platform, Python, Slurm job, deterministic flag); output (text, hash,
tokens, finish reason, seconds); judge (model, model version, prompt hash,
temperature, raw response, score, rubric version, time); and error.

Three design rules that matter more than the field count:

1. One sample per engine call (D004), so a record is comparable to any other
   record with the same seed regardless of batch size.
2. `compare_runs.py` refuses to report a rate when settings differ, which is
   the exact mistake in the published comparison.
3. A judge failure is null, never 0.

## 9. What could not be checked, and why

- The v5 to v8 results. Their weights were never published. 54 of 89
  checkpoints are unreachable to anyone outside the project.
- Bit-level agreement with the authors' own outputs. Expanse V100s emulate
  bfloat16; their hardware is unknown. Same-machine repeatability is
  established; cross-machine is now measured, not assumed: V100 emulated
  bf16 against CPU float32, 0 of 8 identical [E043]. Their text cannot be
  reproduced elsewhere with the seed and settings alone; the device, dtype
  and library build are part of the record, and theirs has none of them.
- Scores from the authors' judge. `claude-sonnet-4-20250514` is deprecated,
  still served, and was not reachable without a key during the sprint.
- The judge's own reliability on the authors' data. No repeat of their
  judging was ever run by them, and could not be run here.
- A full corpus audit. The search covers 15 terms and the year field, not
  semantic leakage.

## 10. What is next

1. API judge pass, 20 minutes, under $3. Replaces the provisional scores
   and adds a judge-vs-judge comparison.
2. Blinded physicist review from `evidence/review-packet-a/packet.html`.
3. Adopt a leakage benchmark of the TypewriterLM kind for the corpus.
4. Serve the model where researchers can query it (Jetstream2, not Expanse).
5. Decide whether a pre-1911 model is in scope.

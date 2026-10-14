# Paper draft: skeleton with numbers

Started 28 Sep 2026. Target: PRX Intelligence, Regular Article. See
`reports/journal-recon.md` for the journal's shape and required statements.

How to use this file. Every section has three parts: the numbers it must
carry (with the lab notebook entry in a comment so each can be checked), a
pointer to the memo paragraph that already holds the argument, and a slot
marked `WRITE:` for the prose. The prose is Akshat's to write in his own
words first. The memo is the source; nothing in it needs to be re-derived.

Two corrections to hold to throughout. The meeting notes describe the
cross-machine result as "V100 byte-identical, CPU did not match", which
reads as if the CPU was unstable. It was not: the CPU also repeats itself
8 of 8. Both machines are self-consistent and they disagree with each other.
And the elevator task carries two different numbers in older files: -0.90
from the authors' unmatched scaffolded-to-minimal comparison (E025) and
+0.89 from the matched leading-minus-scaffolded gain (E039). Only the second
is a sensitivity result.

No placeholders left. E045, E046 and E047 are in; the free-fall numbers come
from `evidence/freefall/summary.html` and `jump.html`.

---

## Title

Working: "Reproducing an LLM-judged physics benchmark: what a record must
contain before a score can be checked"

Alternatives to weigh: something naming GPT-1900; something naming the
grader finding. The grader finding is the headline, so the title should
point at it.

## Abstract

Numbers the abstract must carry, in this order:

- 3.29B parameters, pre-1900 text, 8 physics prompts, 24 checkpoints, 192
  graded answers, published mean 0.93 of 5 <!-- upstream summary.txt; E033 for the interval 0.84 to 1.03 -->
- Authors' own repeat runs: 2 of 120 paired answers byte-identical <!-- E014, E021 -->
- Three fields per published answer; the two settings that explain the
  divergence were never recorded <!-- E016, E022, E026 -->
- Same machine, settings recorded: 8 of 8 identical at temperature 0 and
  8 of 8 at the authors' sampled settings <!-- E032, E035 -->
- Different machine, same settings: 0 of 8 identical, each machine
  self-consistent <!-- E043 -->
- Fresh sweep, 192 answers, one grader on both sets: 1.27 ours, 1.26 theirs;
  their published grades 0.93. The grader alone is +0.33 <!-- E042, E044 -->
- One hint paragraph: +0.28 overall; on the 1911 elevator task +0.89 at
  n=72, CI +0.69 to +1.08; on the 1907 free-fall seed +0.00 at n=72, CI
  -0.12 to +0.12. Given only the 1907 observation, 0 of 144 answers supply
  the equivalence <!-- E039; E045; E047 -->
- Corpus: 2,074,160 documents, 0 dated after 1899, one misdated leak <!-- E041 -->

WRITE: four to six sentences. Lead with the grader finding, not the tooling.

## 1. Introduction

Pointer: memo section 1.

The claim under test and why it is a physics question: an LLM-judged
benchmark asserting that a model restricted to pre-1900 text reasons toward
post-1900 physics. Nobody had checked whether the number could be checked.

Relation to existing benchmarks: `reports/evidence-table.md`. Eight
benchmarks, four vintage models. None tests reconstruction from restricted
knowledge; LLM-as-judge is the weak point in every one; PaperBench is the
only one with a rubric validated against human grading.
<!-- evidence-table.md, families 1 to 3 -->

WRITE: the question, the artefact, what this paper adds (a repeat with
denominators, a record schema, a grader comparison, a blinded packet), and
the one-sentence answer.

## 2. The published artefact and its record

Pointer: memo section 2, the table.

| Fact | Source |
|---|---|
| Per-answer record: prompt, mode, completions. Three fields | `scripts/physics_eval.py:609` <!-- E016 --> |
| Temperature, top_k, num_samples, max_tokens in scope three lines above the write, not written | same <!-- E017, E018 --> |
| No revision pin on weight downloads | `download_checkpoint` <!-- E020 --> |
| Seed: none in the eval script; engine default 42 applied silently | `nanochat/engine.py:171` <!-- E026 --> |
| Run and repeat used 1 vs 3 samples; one generator shared across a batch | <!-- E022, E026 --> |
| 54 of 89 registry checkpoints never published | <!-- E020 --> |
| 5 of 12 runs never graded | <!-- E012 --> |
| Judge: no temperature set; a judge failure written as score 0 | `judge_all` <!-- E016 --> |
| Consequence: 2 of 120 paired answers identical between published runs | <!-- E014, E021 --> |

Authors' own account of the model, for the description paragraph: nanochat
framework; d34, 34 layers; 22B tokens of pre-1900 English from HathiTrust,
British Library, American Stories; trained on 8 nodes of 8 H100s; RL
checkpoints trained with physics reasoning rewards on the base.
<!-- upstream/gpt1900/PROJECT_LOG.md:28-75 -->

WRITE: describe the artefact neutrally, then the table, then the
consequence sentence: the archive cannot distinguish a change in the model
from a change in the dice.

## 3. Methods

Pointer: memo section 8 for the record; `notes/decisions.md` D003 to D008
for each choice and what was rejected.

- Upstream imported at commit `5b489c8c`, never edited. Every difference is
  attributable to environment or settings. <!-- D003 -->
- One sample per engine call. Removes the batch coupling that broke the
  authors' own repeats. <!-- D004, E026 -->
- Their settings for anything set beside a published number: seed 42,
  temperature 0.7, top_k 50, one sample. <!-- D005 -->
- Model pinned by Hugging Face revision hash (`71bf395f...`), weight file
  sha256 recorded. <!-- E032 -->
- 50 fields per generation, grouped: run identity, model identity, prompt,
  sampling, environment, output, judge, error. Schema 1.2.
  <!-- notes/logging-schema.md -->
- Comparison tool refuses to report a rate when settings differ. <!-- compare_runs.py -->
- Judge failure recorded as null, never 0. <!-- D006 -->
- Leading prompt generated from `EVAL.json` with one appended hint paragraph
  per task; every judge field byte-identical. <!-- D007 -->
- Grader: no API access; blinded reader in fresh sessions of 24 with
  provenance stripped and a sealed key; labelled provisional. <!-- D008 -->
- Hardware: SDSC Expanse, one Tesla V100-SXM2-32GB, torch 2.14.0+cu126,
  bf16 emulated (recorded per generation as `bf16_supported: false`).
  CPU control on a `shared` node, float32. <!-- E029, E043 -->

WRITE: one paragraph per bullet group. The methods section is where the
record schema earns its place; keep the field list in a table, not prose.

## 4. Results

### 4.1 Missing metadata

This is section 2's table restated as a result: what a reader of the
published archive cannot recover. Short.

### 4.2 Generation is deterministic on one machine and diverges across machines

Pointer: memo section 3.

| Test | Result | |
|---|---|---|
| s560, temperature 0, twice, V100 | 8 of 8 identical | <!-- E032 --> |
| s560, temperature 0.7, seed 42, one sample, twice, V100 | 8 of 8 | <!-- E035 --> |
| Same with deterministic kernels forced | 8 of 8 | <!-- E035 --> |
| V100 emulated bf16 vs CPU float32, temperature 0 | 0 of 8 | <!-- E043 --> |
| CPU float32, twice | 8 of 8 | <!-- E043 --> |
| Shared prefix before first divergence, V100 vs CPU | 35 to 142 words, mean 450 chars | <!-- E043 --> |
| GPU float32 | cannot run; `gpt.py:396` asserts bf16 rotary tables | <!-- E043 --> |

WRITE: the published divergence is explained by two unrecorded settings.
Then the cross-machine paragraph, stated correctly: each machine
self-consistent, the two disagree, the mechanism is floating-point summation
order flipping one near-tied token. Their hardware is unrecorded, so their
text cannot be reproduced elsewhere even with every setting matched.

### 4.3 The full sweep: the model reproduces, the number does not

Pointer: memo sections 4 and 6.

| Text | Grader | Mean | 95% interval | 0 / 1 / 2 / 3 / 4 | |
|---|---|---|---|---|---|
| our sweep, 192 | ours | 1.27 | 1.18 to 1.36 | 13 / 126 / 41 / 12 / 0 | <!-- E042 --> |
| their published answers | ours | 1.26 | 1.17 to 1.35 | 13 / 125 / 45 / 9 / 0 | <!-- E044 --> |
| their published answers | theirs, as published | 0.93 | 0.84 to 1.03 | 44 / 122 / 22 / 3 / 1 | <!-- E033 --> |

- Ours vs theirs under one grader: 126 of 192 cells exact, +0.01 <!-- E044 -->
- Their text, two graders: 119 of 192 exact, 188 within one, +0.33 <!-- E044 -->
- Training trend, first 8 to last 8 checkpoints: 0.97 to 1.52 ours; 0.62 to
  1.11 published; rank correlation of per-checkpoint means 0.71 <!-- E042 -->
- 192 of 192 generated, 0 errors, 4 hit max_tokens, 64 min <!-- E042 -->
- Stock opening "You have touched": 151 of 192 ours, 150 of 192 theirs <!-- E042, E023 -->
- Grader reliability: 96 answers graded twice, 89 exact, 96 within one <!-- E039, E042 -->

WRITE: the generation step reproduces at the level of the score. The whole
gap between 1.27 and 0.93 is the grader, mostly the zero row. That shift is
larger than the hint effect and comparable to the training gain. The
published number is a property of the grader as much as of the model.

### 4.4 Prompt sensitivity, with the two general-relativity tasks as the worked example

Pointer: memo section 5.

Three wordings, three checkpoints (s560, s630, s735), three seeds, n=72 per
condition. 216 of 216 generated. <!-- E037 -->

| Condition | Mean | Interval | 0 / 1 / 2 / 3 / 4 | |
|---|---|---|---|---|
| minimal | 1.22 | 1.12 to 1.32 | 0 / 56 / 16 / 0 / 0 | <!-- E039 --> |
| scaffolded | 1.36 | 1.22 to 1.50 | 1 / 49 / 17 / 5 / 0 | |
| leading | 1.64 | 1.46 to 1.83 | 0 / 40 / 20 / 10 / 2 | |

Ordering holds on every checkpoint. Leading minus scaffolded per task:
elevator +0.89, frozen light +0.56, photoelectric +0.44, Michelson-Morley
+0.44, free fall +0.11, approaching c +0.11, train 0.00, UV catastrophe
-0.33. <!-- E039 --> Stock opening under every wording: 216 of 216. <!-- E037 -->

Upstream has two general-relativity tasks and they are Einstein's two steps.
`gr_free_fall_equivalence` is the 1907 seed: a person falling from a roof
feels no weight, so gravity and acceleration are locally the same.
`gr_main_elevator_light` is the 1911 consequence: if that is so, light must
bend in gravity. Keating's elevator test is the first. Both are reported.

**The 1911 task at n=72, all 24 checkpoints** <!-- E045 -->

| Condition | Mean | Interval | 0 / 1 / 2 / 3 / 4 |
|---|---|---|---|
| minimal | 1.31 | 1.18 to 1.43 | 0 / 53 / 16 / 3 / 0 |
| scaffolded | 1.57 | 1.44 to 1.69 | 2 / 27 / 43 / 0 / 0 |
| leading | 2.46 | 2.26 to 2.65 | 0 / 11 / 22 / 34 / 5 |

- Leading minus scaffolded, paired: +0.89 (+0.69 to +1.08). Without the hint
  no answer in 72 scores above 2; with it 39 of 72 score 3 or 4. <!-- E045 -->
- The hint: "consider that gravity might not be a force pulling on mass at
  all, but a change in the shape of space and time itself, which light
  follows like everything else." It states rubric levels 4 and 5.
  <!-- tools/make_leading_config.py:62 -->
- Published Elev column mean 1.46; ours 1.57. Training trend first 8 to
  last 8 checkpoints: scaffolded 1.21 to 1.83, leading 1.71 to 2.79. <!-- E045 -->
- Regrade: 35 of 48 exact, 48 of 48 within one. <!-- E045 -->

**The 1907 task at n=72, all 24 checkpoints** <!-- E047 -->

| Condition | Mean | Interval | 0 / 1 / 2 / 3 / 4 |
|---|---|---|---|
| minimal | 0.92 | 0.81 to 1.03 | 12 / 54 / 6 / 0 / 0 |
| scaffolded | 0.99 | 0.89 to 1.07 | 6 / 61 / 5 / 0 / 0 |
| leading | 0.99 | 0.90 to 1.07 | 5 / 63 / 4 / 0 / 0 |

- Leading minus scaffolded, paired: +0.00 (-0.12 to +0.12). Scaffolded
  minus minimal +0.07 (-0.07 to +0.21). Highest score in 216 answers: 2.
  <!-- E047 -->
- The hint: "consider that free fall might be the natural, unforced state of
  motion, and that what we call gravity is an effect of the structure of
  space and time, which is why it can be removed locally by falling." It
  states rubric levels 4 and 5, as the elevator hint did, and moves nothing.
  <!-- tools/make_leading_config.py -->
- Published Fall column mean 0.92; ours 0.99; exact agreement on the 24
  shared cells 17 of 24. Training trend first 8 to last 8 checkpoints:
  scaffolded 0.83 to 1.00, leading 0.92 to 1.08. <!-- E047 -->
- Regrade: 38 of 48 exact, 48 of 48 within one. <!-- E047 -->
- Earlier, smaller numbers for the record: sweep n=24 mean 1.04; sensitivity
  n=9 scaffolded 1.11, minimal 1.22, leading 1.22, hint +0.11. <!-- E042, E039 -->

**The 1907 observation alone** <!-- E047 -->

- Two new prompts, 24 checkpoints x 3 seeds each: seed (the falling person
  and the floating objects, then "What does this tell us about gravity?")
  and bare (the two observations, nothing appended). Neither mentions an
  accelerating cabin, equivalence, or gravity disappearing.
- Read blind by two independent readers, 72 each, highest rung reached:
  **0 of 144** bring in acceleration, equivalence, not-a-force or geometry.
  144 none, 0 loops. Automatic keyword flags fired on 7; all false positives
  on reading. Stock opener 117 of 144. <!-- E047, evidence/freefall/jump.html -->

WRITE: a hint that states the answer moves the mean by +0.28 on a benchmark
whose published signal is 0.93. Then the two GR tasks as one argument: on
the 1911 consequence the hint is worth +0.89; on the 1907 seed it is worth
+0.00 at n=72, and no answer in 216 reaches 3 under any wording. Given the
seed alone, 0 of 144 answers supply the equivalence. The model can be led to
the consequence and not to the seed, even when the seed is handed to it. Then the authors' own unmatched comparison
(0.93 vs 1.38, different sample counts and checkpoint sets) and why it
cannot be read as a sensitivity result.

### 4.5 The elevator thought experiment without a question

Pointer: `evidence/elevator-open/open_report.html`, `evidence/elevator/summary.html`, E046.

Design: the seven numbered observations only, no puzzle, no question, no
hint. Two forms: continue (no question) and ask ("What follows from this?").
Base model `d34-22btok` in completion mode and s035, s560, s839 in chat
mode. 8 samples each, seeds 42 to 49, temperature 0.7. 64 continuations,
read blind, one verdict each from {equivalence, bends-in-gravity,
not-a-force, geometry, none, incoherent, loops}.

Mode confound to state: the base model runs in completion mode and the RL
checkpoints in chat mode, because that is how the registry defines them.

Result <!-- E046 -->: base model 16 of 16 loop. s839 16 of 16 equivalence,
which is line 4 of the prompt, and nothing further. s560 14 of 16. Geometry
0 of 64; rung 3 1 of 64; three continuations state light does not bend. The
only verdicts above rung 1 come from s035, the least-trained checkpoint,
two of three marked marginal by the reader.

WRITE: what the model does when nobody asks it a rubric-shaped question. It
restates the given as a conclusion and stops. Set beside 4.4: with the hint,
39 of 72 reach rung 3 or 4; without a question, 0 of 64 reach rung 4. The
hint supplies the thought. Then the stage-gated framing: both upstream tasks
hand the model stage 1 (the problem) and stage 2 (the explanatory idea) in
the prompt, and the rubric rewards restating them. The seed and bare
conditions in 4.4 are the first attempt to withhold stage 2.

### 4.6 Contamination

Pointer: memo section 7.

Model side, sampled: 66 of 66 post-1900 stems clean; base model fails 13 of
15 pre-1900 controls, RL model fails 9 and partial on 6. Recall of named
facts is near zero on both sides of 1900. <!-- E040 -->

Corpus side: 2,074,160 documents, 56.4 GB, revision `ff332ef6`, 15 terms.
0 dated 1900 or later. Einstein, photon, photoelectric, spacetime, aether
wind: 0 each. Planck 705, Lorentz 330, Michelson 277, Rayleigh 702, all
latest year 1899. One "Nobel Prize" hit dated 1829 describes Fredrik Bajer's
1908 award: a misdated 1909 document that passed the date filter. <!-- E041 -->

WRITE: no evidence the tasks are answerable from leaked text; the zero is a
lower bound because the corpus was assembled by date and one misdated
source is in it; a term search cannot see paraphrase.

## 5. Discussion

WRITE: three points. What a record must contain before a score can be
checked (the 50-field list, condensed to the categories). Why the grader is
the largest single source of variance in this benchmark and what that means
for every LLM-judged benchmark in the evidence table. What the elevator
results say about the difference between passing a rubric and reasoning
toward general relativity.

## 6. Limitations

Each one a sentence or two, no softening:

- The v5 to v8 checkpoints were never published; 54 of 89 are unreachable. <!-- E020 -->
- Hardware changes exact outputs: floating-point summation order diverges
  and flips a later token. Measured, 0 of 8 across V100 and CPU. <!-- E043 -->
- The original evaluation did not record hardware, dtype or library build. <!-- E016 -->
- The authors' judge model, `claude-sonnet-4-20250514`, was not reachable
  without a key; every score here is from a provisional blinded grader, and
  the cross-grade bounds the effect at about 0.33. <!-- D008, E044 -->
- Which grader is closer to a physicist is untested until the blinded packet
  is graded by physicists. <!-- evidence/review-packet-* -->
- The contamination scan is lexical: 15 terms and a date field over
  2,074,160 documents. Paraphrase and period-vocabulary leakage are outside
  it. <!-- E041 -->
- Base-vs-RL comparisons in 4.5 carry a mode confound. <!-- E046 -->

## 7. Data and code availability

- Code: `github.com/michaelhla/gpt1900` at `5b489c8c` (upstream, MIT); this
  repository's `tools/` (to be published with the paper).
- Every generation, grade and rationale: `evidence/` as JSONL, schema in
  `notes/logging-schema.md`.
- Blinded packets: `evidence/review-packet-a`, `-b`, `-c`, and the elevator
  packet.
- Weights: Hugging Face `mhla/gpt1900-d34-contradiction-rl-v11` at revision
  `71bf395f06dff39ad5ee9f8981b941b3c37daae9`; base `mhla/gpt1900-d34-22btok`.
- Corpus: `mhla/pre1900-corpus` at `ff332ef64f896c8d44672b4d1d0c752029e32f29`.

Data Availability statement and AI-use disclosure are both required by APS;
see `reports/journal-recon.md`. The AI-use disclosure must cover the
provisional grader (D008) and any drafting help.

## 8. Acknowledgements

Compute: SDSC Expanse under ACCESS allocation CIS261668. Onboarding help
from Evan Watson at SDSC. Supervision: Prof. Brian Keating, UCSD Physics.

---

## Figures to make

1. Three-way sweep table as a figure: three histograms (0 to 5) side by side.
   Source `evidence/sweep/report.json`.
2. Per-checkpoint means, ours vs published, 24 points each with the rank
   correlation. Source `evidence/sweep/report.json`.
3. Prompt sensitivity: three conditions, per task, leading minus scaffolded.
   Source `evidence/prompt-sensitivity/report.json`.
4. Elevator (1911) at n=72: per-checkpoint curve for three conditions.
   Source `evidence/elevator/report.json`. Free fall (1907) the same, source
   `evidence/freefall/report.json`, three flat curves at 1; plus the seed and
   bare jump count, 0 of 144, from `evidence/freefall/readings.json`.
5. Cross-machine divergence: shared prefix length per task, V100 vs CPU.
   Source E043 table.
6. Corpus term table with year histograms. Source
   `evidence/contamination/corpus-search.json`.

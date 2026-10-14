# Presentation brief

Written 23 Sep 2026 for whoever builds the slides. Every number below has a
lab notebook entry (E-number, `notes/lab-notebook.md`), a decision record
(D-number, `notes/decisions.md`) where a choice was made, a raw log under
`logs/`, and an evidence page under `evidence/`. `reports/slides.md` is a
ready 12-slide draft; `reports/presentation-talking-points.md` has the
spoken lines; `reports/reproducibility-memo.md` is the long form.

## The one-paragraph story

GPT-1900 is a 3.29B-parameter model trained only on pre-1900 text. Its
authors scored it 0.93 out of 5 on eight physics reasoning prompts, graded by
Claude. Nobody had checked whether that number could be reproduced. It can,
and it cannot, in a specific way: the model's answers reproduce the published
score level to within a hundredth when one grader grades both sets; the
published number itself moves by a third of a point when the grader changes.
The generation was never the problem. The record-keeping and the grader were.

## The six things asked for, and what landed

| Asked | Delivered | Where |
|---|---|---|
| 1. Reproduce a published eval on released checkpoints | All 24 checkpoints, 192 answers at their settings, graded, set beside 0.93 with intervals; plus a cross-grade that separates model from grader | E042, E044, `evidence/sweep/report.html` |
| 2. Pipeline recording prompt, output, model, seed, temperature, score | 50 fields per answer, judge fields filled, comparison tool that refuses unfair comparisons | `tools/logged_eval.py`, `notes/logging-schema.md`, D004, D006 |
| 3. Prompt sensitivity: scaffolded, minimal, leading | 3 checkpoints x 3 seeds x 3 wordings, matched, graded | E037, E039, `evidence/prompt-sensitivity/report.html` |
| 3. Contamination | Model side twice (greedy and sampled, 128 continuations read blind) and corpus side (2,074,160 documents, 15 terms) | E036, E040, E041, `evidence/contamination/` |
| 4. Archive everything | Every generation, every failure, every grade and rationale on disk; denominators in every report | `evidence/`, `logs/` |
| 5. Evidence table of AI-discovery benchmarks | 8 benchmarks and 4 vintage models, every row read at source | `reports/evidence-table.md` |
| 6. Blinded packet, memo, presentation | Packet builder with three packets already built (ours, sweep, theirs), memo complete, slides drafted | `tools/blind_packet.py`, `evidence/review-packet-*`, `reports/` |

## Numbers, in the order the story wants them

### Reading their code (E011 to E025, before any model ran)
- 2 of 120 paired answers byte-identical between their runs and their repeats.
- 3 fields saved per answer. Temperature, top_k, sample count in scope three
  lines above the write and not written.
- Seed: none in the eval script; engine default 42 applied silently.
- Run vs repeat used 1 vs 3 samples; one random stream shared across a batch.
- 54 of 89 checkpoints never published. 5 of 12 runs never graded.
- Their judge: no temperature set; failures written as score 0.

### Does generation reproduce (E032, E035)
- Temperature 0, twice: 8 of 8 identical.
- Their settings (0.7, seed 42, one sample), twice: 8 of 8. With deterministic
  kernels forced: 8 of 8. Normal vs deterministic: 8 of 8.
- Against their published bytes for the same cells: 0 of 8. Expected; different
  GPU, emulated bf16. Portability, not repeatability.
- Cross-machine, measured (E043): same checkpoint, same prompts, temperature 0,
  upstream's own CPU float32 path against the V100 run: 0 of 8 byte-identical.
  Prefixes agree for 35 to 142 words, then one token flips. Their text is not
  reproducible on other hardware even with every setting matched, so device,
  dtype and library build belong in the record. The GPU float32 attempt cannot
  run at all: their code asserts bf16 rotary tables.

### The sweep (E042, E044)
- 192 of 192 generated, 0 errors, 64 min, one V100. Stock opening 151 of 192
  (theirs 150 of 192).
- Our answers, our grader: 1.27 (1.18 to 1.36). Histogram 13 / 126 / 41 / 12 / 0.
- Their answers, our grader: 1.26 (1.17 to 1.35). Histogram 13 / 125 / 45 / 9 / 0.
- Their answers, their grader (published): 0.93 (0.84 to 1.03). Histogram 44 /
  122 / 22 / 3 / 1.
- Ours vs theirs under one grader: 126 of 192 cells exact, +0.01.
- Their answers, our grader vs their grader: 119 of 192 exact, 188 within one,
  +0.33.
- Trend first 8 to last 8 checkpoints: 0.97 to 1.52 ours; 0.62 to 1.11 theirs.
  Rank correlation across 24 checkpoints: 0.71.

### Prompt sensitivity (E037, E039), n=72 each
- minimal 1.22 (1.12 to 1.32), scaffolded 1.36 (1.22 to 1.50), leading 1.64
  (1.46 to 1.83). Same order on every checkpoint.
- Leading minus scaffolded per task: elevator +0.89, frozen light +0.56,
  photoelectric +0.44, Michelson-Morley +0.44, UV catastrophe -0.33.
- 216 of 216 answers open with the same sentence regardless of wording.
- Their own unfair comparison had minimal higher (1.38 vs 0.93); the fair one
  has it lowest.

### The two general-relativity tasks at n=72 (E045, E047)
- 1911 elevator: minimal 1.31, scaffolded 1.57, leading 2.46; hint effect
  +0.89 (+0.69 to +1.08); 39 of 72 reach 3 or 4 with the hint, 0 without.
- 1907 free fall: minimal 0.92, scaffolded 0.99, leading 0.99; hint effect
  +0.00 (-0.12 to +0.12); highest score in 216 answers is 2.
- The 1907 observation alone, 144 answers, read blind by two readers: 0 of
  144 supply acceleration, equivalence or geometry. Keyword flags on 7, all
  false positives on reading.
- One line: the model can be led to the consequence and not to the seed.
  Given the seed alone it never makes the step.
- Elevator thought experiment with no question (E046): 0 of 64 reach
  geometry; the trained model restates "acceleration and gravity are
  equivalent", which is line 4 of its own prompt, and stops.

### The professor's elevator test and the abduction suite (E049, E050)
- His question in his words ("the cable breaks, what do you feel, what does it
  tell us about gravity") to all 24 checkpoints and the base, 75 answers read
  blind: 0 reach "you feel no weight"; 48 never say what is felt; 23 say
  weight is still felt; the wrong share rises with training (3 of 24 early,
  12 of 24 late). The base model loops every time.
- Four phrasings plus a ladder of help, 140 answers: 0 reach equivalence or
  geometry, 1 reaches weightless, 30 wrong. The concrete phrasing (a stone let
  go in the falling elevator) draws "it falls to the floor" 14 of 15 times.
- Reasoning controls inside the corpus fail too: Galileo's ship 0 of 15
  correct, two stones 0 of 15, pendulum rule 1 of 15, the unseen planet behind
  Uranus 0 of 15. The model does not fail only the jump; it fails the walk.
- One line: it gives the everyday answer in a physicist's voice.
- Pages: evidence/elevator-final/report.html, evidence/abduction/report.html.

### Grader reliability (E039, E042)
- 96 answers graded twice by independent sessions: 89 exact, 96 within one.

### Contamination
- Greedy probe (E036): 22 of 22 post-1900 stems clean; 6 of 10 controls fail.
- Sampled probe (E040): 66 of 66 post-1900 clean; base model fails 13 of 15
  controls, RL model fails 9, partial 6. The model cannot state Thomson's
  electron or Michelson-Morley; recall of named facts is near zero either side
  of 1900.
- Corpus (E041): 2,074,160 documents, 0 dated 1900 or later; photon,
  spacetime, Einstein, photoelectric each 0. One "Nobel Prize" hit dated 1829
  describes a 1908 award: a misdated 1909 document. Zero is a lower bound.
- Michelson: 277 documents, the experiment is in the training data. The task
  that never scores 0 asks about something the model has read about.

### Benchmark table (workstream 5)
- DiscoveryBench 25%, ScienceAgentBench 32 to 42%, MLE-bench 16.9%, CORE-Bench
  21%, PaperBench 21%, LAB-Bench, The AI Scientist; TypewriterLM (pre-1913,
  with a leakage benchmark), TimeCapsuleLLM, Ranke-4B, GPT-1900. No benchmark
  tests reconstruction from restricted knowledge; LLM-as-judge is standard and
  is the weak point everywhere; PaperBench shows what a validated rubric looks
  like.

## Trade-offs and why, for the "how I chose" slide

1. **Upstream never edited (D003).** Every difference is attributable to
   environment or settings, not to my patches. Cost: the float32 control
   could not run on GPU because their code asserts bf16 rotary tables; that
   failure is a finding, not a workaround.
2. **One sample per engine call (D004).** Slower, but a record is comparable
   to any other with the same seed. Their batch coupling is what broke their
   own repeats.
3. **Their settings, not mine (D005).** Seed 42, temperature 0.7, one sample,
   because the question is whether their result reproduces.
4. **Temperature 0 first, then 0.7.** Two tests, two questions: is the compute
   stable, then is the seeded pipeline repeatable. Both 8 of 8.
5. **Leading prompt generated, not hand-written (D007).** One hint paragraph
   appended, every judge field byte-identical, so a score difference is the
   prompt and nothing else.
6. **Blinded session grader instead of no grader (D008).** No API key was
   available. Same rubric, provenance stripped, fresh session per 24 answers,
   sealed key, rationale archived per answer, labelled provisional. The
   cross-grade then turned this limitation into the main finding: grader
   choice moves the number by 0.33. One command replaces these grades with
   the API judge when a key exists.
7. **Judge failures recorded as null, not 0 (D006).** Their code writes 0.
8. **V100, bf16 emulated.** What Expanse has. Recorded in every record;
   same-machine repeatability is proven, cross-machine byte match is not
   expected and not claimed.
9. **Term search, not a semantic audit, for the corpus.** 50 minutes on 56 GB
   answers the lexical question completely and says so about its limit.

## What could not be done, and why (slide 10)

- 54 unpublished checkpoints: v5 to v8 results unreachable to anyone outside.
- Bit-level match to their outputs across hardware: not expected, and now
  measured at 0 of 8 between a V100 and a CPU float32 run (E043).
- The paper's own judge model: deprecated, still served, no key during the
  sprint. The cross-grade bounds how much that matters.
- Which grader is closer to a physicist: needs the blinded packet run with
  real physicists.
- Paraphrased or period-vocabulary leakage: outside a term search.
- 15 Sep passed with the sweep unsubmitted; it ran on 22 Sep.

## What is next (slide 11)

1. API judge pass, 20 minutes, under $3: both graders side by side.
2. Physicist grading from `evidence/review-packet-a/packet.html` and
   `review-packet-b`.
3. Adopt a leakage benchmark of the TypewriterLM kind.
4. Serve the model on Jetstream2, not Expanse.
5. Decide whether the pre-1911 model is in scope.

## Files to open live

- `evidence/sampling/compare-ab.html`: the green 8 of 8.
- `evidence/sweep/report.html`: the three-row headline table.
- `evidence/prompt-sensitivity/report.html`: per-condition and per-task.
- `evidence/contamination/probe.html`: the boiler answer, the paper photon.
- `evidence/contamination/corpus-search.html`: the term table, the 1829 hit.
- `evidence/elevator/summary.html` and `evidence/freefall/summary.html`: the two GR tasks, one page each.
- `evidence/freefall/jump.html`: the 144 answers to the 1907 observation, verdict per answer.

# Final presentation, talking points

Prepared 22 Sep 2026. One slide per heading. Every number is on disk with
its notebook entry.

## 1. The question

Somebody published a result: GPT-1900, a model trained only on pre-1900 text,
scores 0.93 out of 5 on eight physics reasoning questions, graded by Claude.
Nobody had checked whether running it again gives the same number. My job was
to check, and to build the record-keeping that would let anyone else check.

Say: "This is not about whether the model is smart. It is about whether the
measurement means anything."

## 2. What I found by reading their code, before running anything

- Their two repeat runs disagreed with themselves 118 times out of 120.
- The eval script saves three fields per answer: prompt, mode, text. Not the
  temperature, not the seed, not the model revision.
- The seed was there all along, one layer down in the engine, defaulting to
  42. Never overridden, never written down.
- Their run and its repeat asked for different numbers of samples per
  question, 1 versus 3. The random draws are shared across a batch, so those
  two runs could never have matched.
- 54 of 89 checkpoints in their registry were never published.
- No repeat run was ever graded. So no reproducibility figure for the score
  itself has ever existed.

Say: "Every one of these is a bookkeeping gap, not a modelling flaw. And
every one of them makes the 0.93 uncheckable."

## 3. Is the compute deterministic

Same checkpoint, same 8 questions, temperature 0 (no randomness), run twice
on one GPU. 8 of 8 answers byte-identical.

Say: "The hardware is not the problem."

## 4. Does their actual setting reproduce

Same checkpoint, their published settings: temperature 0.7, seed 42, one
sample. Run twice. 8 of 8 identical. Run twice more with PyTorch's
deterministic kernels forced. 8 of 8. Normal versus deterministic: 8 of 8.

Say: "Write the seed down and match the sample count, and their pipeline
reproduces exactly on one machine. Their failure was two missing fields."

Across machines it does not: the same checkpoint at temperature 0 on a CPU
in float32 against the V100 gives 0 of 8 identical answers; they agree for
35 to 142 words and then one token flips (E043). So device, dtype and
library build are part of the record, and a byte-for-byte match to their
published text should never have been expected.

Show: evidence/sampling/compare-ab.html, the green 8 / 8.

## 5. The full reproduction

All 24 checkpoints, 8 questions, their exact settings, one sample each. 192
answers, the same count behind the published 0.93. 192 of 192 generated, no
failures, 64 minutes of GPU. Every answer carries 50 fields: model revision,
weight hash, seed, temperature, GPU, torch version, timing.

Then the number, three ways, n=192 each, 95 percent intervals:

| Whose answers | Whose grader | Mean |
|---|---|---|
| our new sweep | ours | 1.27 (1.18 to 1.36) |
| their published answers | ours | 1.26 (1.17 to 1.35) |
| their published answers | theirs, as published | 0.93 (0.84 to 1.03) |

Say: "The model reproduces. A fresh sweep on different hardware, graded next
to their own answers by one grader, lands within a hundredth. Two thirds of
the 192 cells agree exactly."

Say: "The number does not. Same rubric, same answers, a different Claude:
plus a third of a point. That is bigger than the effect of a leading prompt,
and about the size of the whole training gain. The published 0.93 is a
property of the grader as much as of the model."

Also: the training trend reproduces. First eight checkpoints to last eight,
0.97 to 1.52 on ours, 0.62 to 1.11 on theirs; rank correlation 0.71 across
24 checkpoints. Their 0.93 is printed without an error bar; from their own
file it is plus or minus a tenth.

Trade-off to own: the grader here is a blinded Claude session, not the API
judge the paper used, because no key was available. Same rubric, fresh
session per 24 answers, provenance stripped, sealed key. The grader is
self-consistent: 96 answers graded twice by independent sessions, 89 exact,
96 within one point. What it is not is the paper's grader, and the cross
grade shows exactly how much that matters.

Show: evidence/sweep/report.html, the headline table with three rows.

## 6. Prompt sensitivity

Three wordings of each question on three checkpoints, three seeds each, 216
answers. Scaffolded (their normal prompt), minimal (assumptions removed),
leading (their prompt plus a hint that gives away the answer).

Already visible: every one of the 216 answers, under every wording, opens
with the same sentence, "You have touched a matter of considerable
importance." Their published sweep: 78 percent.

Scores, provisional grader (blinded, same rubric, fresh session per 24
answers, D008), n=72 each, 95 percent intervals:

- minimal 1.22 (1.12 to 1.32)
- scaffolded 1.36 (1.22 to 1.50)
- leading 1.64 (1.46 to 1.83)

Same ordering on every checkpoint. Leading minus scaffolded per task:
elevator +0.89, frozen light +0.56, photoelectric +0.44, Michelson-Morley
+0.44, UV catastrophe -0.33. Grader re-test: 48 answers graded twice by
independent sessions, 44 of 48 exact, 48 of 48 within one point.

Their own minimal-prompt run scored 1.38 versus 0.93 for the normal prompt,
on an unfair comparison. On the fair one, minimal is lowest.

Say: "A hint that states the answer moves the score by about 0.3, on a
benchmark whose whole published signal is 0.93. The benchmark measures the
prompt as well as the model. And the model has one voice regardless of the
question."

Trade-off to own: these scores come from a blinded Claude grader in fresh
sessions, not from the API judge the paper used, because no key was
available. Same rubric, different Claude, labelled provisional in every
file. One command replaces them when a key exists.

The two general-relativity tasks, both at n=72 (E045, E047). Einstein's
1907 seed (falling person feels no weight) and his 1911 consequence (light
bends). Hint effect on the consequence +0.89; on the seed +0.00. Given the
seed alone, 144 answers, 0 bring in the equivalence.

Say: "The model can be led to the consequence and not to the seed. Hand it
the idea and it carries it forward; ask it for the idea and it restates the
observation; give it the observation alone and it never makes the step. That
is the first stage of the test, measured."

## 7. Contamination, model side

16 sentence stems. 11 about post-1900 physics: Planck's constant, photon,
Einstein, relativity, E = mc^2, spacetime, Bohr, 1905, the 1901 Nobel, the
Wright brothers. 5 controls about pre-1900 physics: Thomson's electron,
Michelson-Morley, Maxwell, the aether, Rontgen's rays. Base model and RL
model.

Result: all 22 post-1900 answers drew a blank. "A photon is a small piece of
paper, or a piece of cloth." The Wright brothers are rifle shots. Einstein
wrote geology books.

But 6 of 10 controls failed too. "Michelson and Morley showed that" a
double-tube boiler is efficient.

Rerun with sampling, three continuations per stem, 96 in all, read blind:
66 of 66 post-1900 stems clean, 0 leaks. Controls still fail: base model 13
of 15, RL model 9 fail and 6 partial. The loops were not hiding knowledge.

Say: "No sign of leakage, twice. But the model cannot state its own corpus's
facts either, so this is weak recall in general, not a clean pre/post split.
Contamination risk is capped by recall, and recall of named facts is near
zero. The corpus search is the instrument that can actually see leakage."

## 8. Contamination, corpus side

Two million documents, 56 GB, the whole training set, searched for 15 terms
and for any document dated 1900 or later. Zero documents dated 1900 or later.
Zero hits for Einstein, photon, photoelectric, spacetime, aether wind. Planck,
Lorentz, Michelson and Rayleigh appear, all publishing before 1900. "Quantum"
appears 14,000 times as the Latin word.

Say: "Nothing in the corpus names the physics that came after 1900."

Then the catch. One document matches "Nobel Prize". It is dated 1829. It says
the prize went in December last to Fredrik Bajer, who won it in 1908. A 1909
report with a bad date, and the date filter let it through.

Say: "So zero is a lower bound. The corpus was built by date, and dates can be
wrong. I found one. It is not physics, and the physics terms are clean, but
the mechanism is real and the memo says so."

If asked: a term search cannot see paraphrase, or post-1900 ideas written in
1890s words. The model-side probe is the check for that, and it found nothing,
with the caveat that it finds nothing pre-1900 either.

## 9. The record-keeping standard

50 fields per generation versus their 3. Seed, revision, weight hash,
temperature, top_k, sample count, GPU, dtype, torch version, judge model,
judge temperature, judge prompt hash, raw judge response, error. A
comparison tool that refuses to report a rate when settings differ. A judge
that records failures as null instead of 0.

Say: "This is the part that outlives the project. Any future run through
this pipeline produces evidence rather than anecdotes."

## 10. What could not be checked, and why

- 54 unpublished checkpoints: the v5 to v8 results cannot be reproduced by
  anyone outside the project.
- V100 GPUs emulate bfloat16. A number from Expanse and a number from an
  A100 are not the same computation.
- The judge model they used is deprecated. Still served today, not forever.
- Scores: not yet computed, pending API access.
- The benchmark evidence table: eight benchmarks and four vintage models, every row read at source, in `reports/evidence-table.md`. Desk work, no experiment.

Say: "This slide is part of the deliverable, not an apology."

## 11. What is next

- Grade everything, 20 minutes and under $3 once a key exists.
- Judge reliability: same answers graded twice.
- Blinded physicist review using the packet.
- Sampled rerun of the knowledge probe.
- Serving the model on Jetstream2 so anyone can query it.
- Whether the pre-1911 model for general relativity is in scope.

## If asked

- Why V100: it is what Expanse has. A100 nodes were all reserved.
- Why seed 42: it is what their code used without anyone choosing it.
- Why their judge model and not a newer one: reproducing their score means
  using their grader. Newer model is one flag away for a comparison.
- Why not grade by hand: the LLM judge is the thing being audited. Human
  grading is the packet, and needs physicists' time.
- Cost of everything run: about 3 GPU hours of a 1000 hour allocation.

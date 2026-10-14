## The question

- GPT-1900 is a 3.29B-parameter model trained on about 22B tokens of pre-1900
  English. The idea behind it: can a model reason its way to physics it has
  never read?
- Its authors ran 24 checkpoints on 8 physics questions and had Claude grade
  each answer 0 to 5. Published mean: 0.93 over 192 answers.
- Nobody had checked whether running it again gives the same number.
- My job was to check, and to build the record-keeping that lets anyone else
  check.
- This is not about whether the model is smart. It is about whether the
  measurement means anything.

---

## What reading their code found, before running anything

- Their two repeat runs matched the originals on 2 of 120 paired answers. The
  other 118 differed.
- Each answer is saved with three fields: prompt, mode, text. Not the
  temperature, not the seed, not the model revision.
- The seed was there all along, one layer down in the engine, fixed at 42.
  Never overridden, never written down.
- Run and repeat asked for different sample counts, 1 versus 3. One random
  stream is shared across a batch, so those two runs could never have matched.
- 54 of 89 checkpoints in their registry were never published, and no repeat
  run was ever graded. No reproducibility figure for the score has ever
  existed.

---

## The pipeline built

- `logged_eval.py` writes one record per answer with 50 fields. Their script
  writes 3.
- `compare_runs.py` matches two runs on task and seed and reports
  byte-identical answers over total.
- `report.py` gives every mean its n and a 95 percent bootstrap interval, per
  task, per checkpoint, per condition.
- `judge.py` calls their grader at temperature 0 and records a failure as
  null. `blind_packet.py` shuffles answers, strips provenance and seals the
  key for human review.
- Everything runs on SDSC Expanse, one V100 per job, one Slurm script per
  experiment. Upstream pinned at commit 5b489c8c and never edited.

---

## Is the compute deterministic

**8 of 8**

answers byte-identical. Checkpoint s560, the same 8 questions, temperature 0,
run twice on one V100. The hardware is not the problem.

- Same weights, same argmax, CPU float32 instead of V100 emulated bf16: 0 of 8
  identical. CPU twice: 8 of 8. Deterministic on each machine, not across
  machines. Their hardware is unrecorded. [E043]
---

## Their actual setting reproduces

- Their published settings: temperature 0.7, top_k 50, seed 42, one sample.
  Checkpoint s560, 8 questions.
- Run twice with normal kernels: 8 of 8 identical.
- Run twice with PyTorch's deterministic kernels forced: 8 of 8. Normal
  against deterministic: 8 of 8.
- Against their published bytes for the same 8 cells: 0 of 8. Different GPU,
  different torch build, emulated bfloat16. Expected, and not a failure of
  their pipeline.
- Write the seed down and match the sample count, and their pipeline
  reproduces exactly. Their failure was two missing fields.

---

## The full sweep

- All 24 checkpoints, 8 questions, their exact settings, one sample each. 192
  answers, the same count behind the published 0.93.
- Each answer carries the Hugging Face revision, the sha256 of the weight
  file, and 48 more fields.
- 192 of 192 generated, no failures. Under one grader, n=192 each:
  our new sweep 1.27 (1.18 to 1.36); their published answers 1.26 (1.17 to
  1.35); their published answers under their own grader 0.93 (0.84 to 1.03).
- The model reproduces: two thirds of the 192 cells agree exactly between our
  answers and theirs under one grader. The training trend reproduces, rank
  correlation 0.71 across 24 checkpoints.
- The number does not: same rubric, same answers, a different Claude, plus
  0.33. Larger than the leading-prompt effect, about the size of the whole
  training gain. The published 0.93 is a property of the grader as much as of
  the model.
- Their 0.93 is printed without an error bar. Computed from their own file,
  the 95 percent bootstrap interval is 0.84 to 1.03, n=192.
- Ours will be reported with its interval, next to theirs.

---

## Prompt sensitivity

- Three wordings of every question: scaffolded (theirs), minimal (assumptions
  removed), leading (theirs plus a hint that gives away the answer). Three
  checkpoints, three seeds. 216 answers, 0 errors, n=72 per condition.
- Leading 1.64 (1.46 to 1.83). Scaffolded 1.36 (1.22 to 1.50). Minimal 1.22
  (1.12 to 1.32). Provisional grader, not their judge.
- The hint moves the mean by +0.28 on a scale where the whole published
  signal is 0.93. Leading and minimal intervals do not overlap. The order
  holds on each of the three checkpoints.
- 216 of 216 answers open with "You have touched a matter of considerable
  importance", under every wording. Their published sweep: 150 of 192.
- Their own comparison, 0.93 against 1.38, used different sample counts and
  different checkpoint sets. This one is matched.

---

## Contamination

- 16 sentence stems, base model and RL s560. 11 on post-1900 physics:
  Planck's constant, the photon, Einstein, E = mc^2, Bohr, the Wright
  brothers. 5 controls the corpus does contain: Thomson's electron,
  Michelson-Morley, Maxwell, the aether, Rontgen's rays.
- Sampled at 0.7, three continuations per stem: 66 of 66 post-1900
  continuations clean, 0 leaks. Greedy run before it: 22 of 22 blank. A photon
  is "a small piece of paper, or a piece of cloth".
- But the controls fail too. Base model: 2 of 15 right, both on the aether. RL
  model: 0 of 15 right, 6 partial. "Michelson and Morley showed that" a
  double-tube boiler is efficient.
- So the probe shows weak recall of named facts in general, not a clean
  pre/post-1900 split. Contamination risk is capped by recall, and recall is
  near zero.
- Corpus search, 2,074,160 documents, 56 GB: 0 dated 1900 or later. Einstein,
  photon, photoelectric, spacetime, aether wind: 0 hits each.
- One leak anyway. A "Nobel Prize" hit dated 1829 describes Fredrik Bajer's
  1908 award. A 1909 report with a wrong date. Zero is a lower bound.

---

## The record-keeping standard

- 50 fields per generation: run identity, model identity (repo, revision,
  checkpoint, weight sha256), prompt, sampling (seed, temperature, top_k,
  sample count), environment (GPU, dtype, torch version), output, judge
  (model, prompt hash, raw response, score), error.
- One sample per engine call, so any record compares with any other at the
  same seed, whatever the batch size.
- The comparison tool refuses to report a rate when settings differ. That is
  the exact mistake in the published comparison.
- A judge failure is recorded as null, never 0. Their judge writes 0.
- This is the part that outlives the project. Any future run through it
  produces evidence rather than anecdotes.

---

## What could not be checked, and why

- The v5 to v8 results. Their weights were never published: 54 of 89
  checkpoints are unreachable to anyone outside the project.
- Bit-level agreement with their outputs. Expanse V100s emulate bfloat16 and
  their hardware is unknown. Same-machine repeatability is established;
  cross-machine should not be expected.
- Scores from their judge. claude-sonnet-4-20250514 is deprecated, still
  served, and no key was available. Every score here is from a provisional
  blinded grader: 44 of 48 regraded answers exact, 48 of 48 within one point.
- The judge's own reliability on their data. They never repeated their
  judging, and it could not be repeated here.
- An outside yardstick. The evidence table covers 11 benchmarks and models in
  three families, each read at the source. None tests reconstruction from
  pre-breakthrough knowledge, so there is nothing to compare GPT-1900 against.

---

## What is next

- Grade everything with their judge: 20 minutes and under $3 once a key
  exists. Then both graders side by side.
- Judge reliability under their judge: the same answers graded twice.
- Blinded physicist review from the packet,
  `evidence/review-packet-a/packet.html`.
- Serve the model on Jetstream2 so anyone can query it. Expanse is a batch
  cluster with no public address.
- Adopt a leakage benchmark of the TypewriterLM kind for the corpus, and
  decide whether a pre-1911 model for general relativity is in scope.

---

## Three asks

- An API key for the judge. Under $3 grades every answer with the grader the
  paper used, and turns every provisional score into a checkable one.
- Physicists' time on the blinded packet. It is built, shuffled and sealed.
  It needs graders.
- A call on hosting and scope: a Jetstream2 allocation for a public query
  page, and whether the pre-1911 model is in.

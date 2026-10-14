# Inserts for the existing draft

Eight blocks, each written to drop into one section of the professor's draft. Section numbers are from the August research note (`notes/paper-mapping.md`); check them against the current Overleaf before pasting. Each block follows the same pattern: the draft names a risk, the block reports the measurement with its denominator. Every number carries its lab notebook entry in a comment that does not print. Pasted as LaTeX from `reports/overleaf/inserts/`, or as prose from this file.

## INSERT A. Section 13.3, sampling and selection bias

### Artefact reproducibility, measured

The published archive holds two pairs of repeated runs. After confirming the prompts byte-identical, we paired every generation with its repeat: 2 of 120 match. <!-- E014, E021 --> The cause is in the code rather than the model. The evaluation script sets no seed, so the engine default of 42 applied silently and was never written down; the run and its repeat asked for 1 and 3 samples per prompt, and the engine shares one random generator across every row of a batch, so the two could never have produced the same draws. <!-- E022, E026 --> With the seed recorded and one sample per call, the same checkpoint on the same GPU repeats exactly: 8 of 8 answers byte-identical at temperature 0, 8 of 8 at the published settings of temperature 0.7 and top_k 50, with and without deterministic kernels forced. <!-- E032, E035 --> Across machines it does not: the same checkpoint at temperature 0 on a CPU in float32 against a V100 gives 0 of 8, each machine agreeing with itself 8 of 8. <!-- E043 --> Sampling variance is therefore not the failure here. The failure is that the record did not contain what a repeat needs, and that device and numeric format belong in it.

**Table A.** Paired generations between a published run and its repeat, and between our runs.

| Pair | Paired | Identical |
|---|---|---|
| authors' v8 against v8_det | 96 | 0 |
| authors' v11 against v11_replication | 24 | 2 |
| ours, same V100, temperature 0, twice | 8 | 8 |
| ours, same V100, published settings, twice | 8 | 8 |
| ours, V100 against CPU float32, temperature 0 | 8 | 0 |

## INSERT B. Section 13.4, evaluator leakage

### The grader moves the number

We regenerated all 192 cells of the published sweep at the authors' settings on different hardware and graded them blind with the authors' rubric, beside the authors' own published answers, by one grader. <!-- E042, E044 -->

**Table B.** The sweep under two graders, n=192 each, 95% bootstrap intervals.

| Answers | Grader | Mean | Interval | 0 / 1 / 2 / 3 / 4 |
|---|---|---|---|---|
| our fresh sweep | ours | 1.27 | 1.18 to 1.36 | 13 / 126 / 41 / 12 / 0 |
| authors' published | ours | 1.26 | 1.17 to 1.35 | 13 / 125 / 45 / 9 / 0 |
| authors' published | theirs, as published | 0.93 | 0.84 to 1.03 | 44 / 122 / 22 / 3 / 1 |

Under one grader the fresh answers and the published answers agree to 0.01, with 126 of 192 cells scored identically. <!-- E044 --> The same published answers under the two graders differ by 0.33, 119 of 192 cells identical, the difference concentrated in the zero row: 44 zeros under the authors' judge, 13 under ours. <!-- E044 --> The grader was self-consistent, 89 of 96 regraded answers exact. <!-- E039, E042 --> The published score is a property of the grader as much as of the model, by an amount larger than any prompt manipulation reported below. Separately, 150 of the 192 published answers open with the identical sentence, "You have touched a matter of considerable importance", and 216 of 216 answers in our prompt-sensitivity run do, regardless of wording. <!-- E023, E037 --> Whether a language-model judge rewards that register is the question the blinded physicist packet is built to answer.

## INSERT C. Section 13.2, prompt leakage

### Three wordings, matched denominators

Three checkpoints, three seeds each, three wordings of all eight prompts: the published scaffolded prompt, which lists the classical assumptions; a minimal prompt with the list removed; and a leading prompt that appends one hint paragraph stating the core idea, generated so that every judge field stays byte-identical across conditions. <!-- E037, D007 -->

**Table C.** Mean score by wording, n=72 each.

| Wording | Mean | 95% interval |
|---|---|---|
| minimal | 1.22 | 1.12 to 1.32 |
| scaffolded | 1.36 | 1.22 to 1.50 |
| leading | 1.64 | 1.46 to 1.83 |

The ordering holds on every checkpoint. A hint that states the answer is worth +0.28 on a benchmark whose published signal is 0.93. <!-- E039 --> The authors' own comparison of scaffolded against minimal (0.93 against 1.38) used different sample counts and checkpoint sets and cannot be read as a sensitivity result. <!-- E025 -->

## INSERT D. New subsection, under the discovery-mismatch discussion or as Section 13.8

### The elevator test, measured

The benchmark's two general-relativity prompts are Einstein's two steps: `gr_free_fall_equivalence` is the 1907 seed, the falling observer who feels no weight, and `gr_main_elevator_light` is the 1911 consequence, light bending in an accelerating frame. We ran both on all 24 checkpoints, three seeds, three wordings, 72 answers per cell. <!-- E045, E047 -->

**Table D.** The two general-relativity tasks at n=72 per wording.

| Task | minimal | scaffolded | leading | hint effect, paired | highest score |
|---|---|---|---|---|---|
| 1911 light bending | 1.31 | 1.57 | 2.46 | +0.89 (+0.69 to +1.08) | 4 |
| 1907 free fall | 0.92 | 0.99 | 0.99 | +0.00 (-0.12 to +0.12) | 2 |

On the 1911 task the hint lifts 39 of 72 answers to 3 or 4; without it none reaches 3. On the 1907 task no answer in 216 reaches 3 under any wording, and a hint of the same kind moves nothing. <!-- E045, E047 --> We then gave the 1907 observation alone, with and without the question "what does this tell us about gravity", to all 24 checkpoints, 144 answers, read blind by two independent readers against a fixed verdict ladder: 0 of 144 bring in acceleration, equivalence or geometry on their own; the 7 automatic keyword hits were false positives on reading. <!-- E047 --> The 1911 thought experiment given with no question at all, 64 continuations: 0 reach geometry, and the trained model restates "acceleration and gravity are equivalent", a line of its own prompt, and stops. <!-- E046 --> The model can be led to the consequence and cannot be led to the seed, even when the seed is handed to it. Given the observation alone it never makes the step. This is the first stage of the test failing, measured rather than argued.

## INSERT E. Section 11.4, evaluation and archiving

### What a generation record must contain

We implemented and ran a record of 50 fields per generation: run identity (run id, code commit, dirty flag, config hash); model identity (repository, revision, checkpoint step, weight hash); prompt (text, hash, condition, mode); sampling (seed, sample index, temperature, top_k, sample count, token limit); environment (device, GPU, compute capability, bfloat16 support, dtype as loaded, library versions, scheduler job id, deterministic flag); output (text, hash, token count, stop reason, seconds); judge (model, model version, prompt hash, temperature, raw response, score, rubric version, time); and error. <!-- notes/logging-schema.md --> Three rules did more work than the field count. One sample per engine call, so any two records with the same seed are comparable regardless of batch size. <!-- D004 --> A comparison tool that refuses to report an agreement rate when any generation setting differs between runs, which is the mistake in the published comparison. <!-- E031 --> And a judge failure recorded as null, never as 0, where the published code writes 0. <!-- D006 --> Archiving generations is necessary and not sufficient; an archive without these fields cannot support the reproducibility claim made for it.

## INSERT F. Sections 11.1 and 13.1, corpus and contamination

### Two contamination checks

Corpus side: the full training set, `mhla/pre1900-corpus`, 2,074,160 documents in 56 GB, scanned for 15 terms with a year histogram per term. 0 documents dated 1900 or later. photon, spacetime, Einstein and photoelectric: 0 each. Planck 705 and Michelson 277, at pre-1900 levels; the Michelson-Morley experiment is inside the corpus. One document dated 1829 describes a 1908 Nobel Prize, a misdated 1909 report, so the zero is a lower bound and the search is lexical. <!-- E041 --> Model side: 16 sentence stems, 11 post-1900 and 5 pre-1900 controls, on the base model and a late checkpoint, greedy and sampled: 88 of 88 post-1900 stems drew a blank, but most controls failed too, so the probe shows weak recall of named facts in general rather than a clean date split. <!-- E036, E040 -->

## INSERT G. Section 8.1, cutoff mismatch

### Two tasks on the boundary

Of the eight prompts, two sit on the stated line in opposite directions. `uv_catastrophe` targets Planck's law, published in October and December 1900, on the boundary rather than past it. `sr_michelson_morley` refers to an 1887 experiment that is inside the corpus (277 documents mention Michelson; an 1889 text discusses the ether problem); only the 1905 interpretation lies outside, and it is the one prompt that never scores 0 in the published results. <!-- E011, E024, E041 -->

## INSERT H. Section 6, the benchmark landscape

### Where this sits among benchmarks

We read eight benchmarks and four vintage-cutoff models at source. One family hands the model data or literature and asks it to do science: DiscoveryBench (best 25%), ScienceAgentBench (32 to 42%), MLE-bench (16.9% at bronze level), The AI Scientist, LAB-Bench. A second asks it to reproduce what exists: CORE-Bench (21% on the hardest level), PaperBench (21.0%, 8,316 sub-tasks, rubric validated against humans). A third restricts knowledge by date: TypewriterLM (pre-1913, with a leakage benchmark), TimeCapsuleLLM, Ranke-4B, GPT-1900. None tests reconstruction from restricted knowledge; where a language model grades, it is the weak point everywhere; PaperBench is the only one that validates its rubric against human grading. <!-- reports/evidence-table.md -->

# The model reproduces, the number does not: a short reproducibility report on an LLM-judged physics benchmark

**Akshat Singh and Brian Keating, University of California San Diego**

Short form of 7 October 2026, about 1,800 words. The long form is `reports/paper-full-draft.md`. Every number carries its lab notebook entry in an HTML comment.

## Abstract

GPT-1900 is a 3.29-billion-parameter language model trained only on text written before 1900. Its authors evaluated 24 training checkpoints on 8 physics prompts, graded by a hosted language model, and published a mean of 0.93 out of 5 over 192 answers. <!-- E024 --> We repeated the evaluation. The authors' own repeat runs had matched on 2 of 120 paired answers, <!-- E014, E021 --> because the record kept three fields per answer and omitted the seed and the sample count. <!-- E016, E022, E026 --> With both recorded, generation repeats exactly on one machine, 8 of 8 at the published settings. <!-- E035 --> A fresh sweep of all 192 cells, graded blind beside the authors' own published answers by one grader, lands within 0.01 of them: 1.27 against 1.26. <!-- E042, E044 --> The same published answers under the authors' grader carry 0.93. The grader alone moves the score by +0.33, <!-- E044 --> more than a hint that states the answer (+0.28) <!-- E039 --> and about the size of the training gain. On the two general-relativity tasks the hint is worth +0.89 on the 1911 light-bending consequence and +0.00 on the 1907 free-fall seed; <!-- E045, E047 --> given the 1907 observation alone, 0 of 144 answers supply the equivalence. <!-- E047 --> The training corpus, 2,074,160 documents, has none dated after 1899. <!-- E041 --> The model reproduces. The number is a property of the grader.

## 1. The question

A published benchmark score is a measurement. It has an instrument, here a hosted language model used as a grader; a sample, here one answer per checkpoint per prompt; and a record, which is what lets a second laboratory repeat it. GPT-1900 [1] published 0.93 and a complete archive of generations, and nobody had checked whether the archive could support a repeat. We asked four things. Can the generations be repeated? Does the score survive a change of grader? How much of the score is the wording of the prompt? Is the corpus what it claims to be?

The two general-relativity prompts carry a further interest. Zahavy [2] argues that language models carry out deduction from a stated premise but not the abductive step that produces one, with Einstein's 1907 thought about the falling observer as his case. [CHECK: from the abstract.] GPT-1900's `gr_free_fall_equivalence` asks for that step and `gr_main_elevator_light` asks for its 1911 consequence, so the benchmark contains a direct test.

## 2. What the published record holds

We read the archive before running any model. Each answer is stored with three fields: prompt, mode, text. <!-- E016 --> Temperature, top_k, sample count and token limit are in scope at the line that writes the file and are not written. <!-- E017, E018 --> No seed appears in the evaluation script; the engine default of 42 applied silently. <!-- E026 --> Weights are fetched by a mutable name with no revision pinned. <!-- E020 --> The authors' run and its repeat used 1 and 3 samples per prompt; the engine shares one random generator across every row of a batch, so the two could never have matched. <!-- E022, E026 --> 54 of 89 checkpoints in the registry were never published. <!-- E020 --> No repeat run was ever graded. <!-- E012 -->

## 3. Methods

Upstream is pinned at commit `5b489c8c` and never edited; everything new lives in a separate tools directory that imports it. <!-- D003 --> Each generation is written as one record of 50 fields: run identity, model repository and revision and weight hash, prompt text and hash and condition, seed and sample index and temperature and top_k and sample count and token limit, device and GPU and dtype as loaded and library versions, the output and its hash and length and stop reason, and eight judge fields. <!-- notes/logging-schema.md --> One sample per engine call, so a record is comparable to any other with the same seed regardless of batch size. <!-- D004 --> A comparison tool refuses to report an agreement rate when any generation setting differs between two runs. <!-- E031 -->

Generation ran on SDSC Expanse, one Tesla V100 (32 GB), torch 2.14, weights held as bfloat16 with the format emulated, since the V100 has no bfloat16 hardware; this is recorded per generation. <!-- E032 --> Settings match the published run: temperature 0.7, top_k 50, seed 42, one sample. <!-- D005 -->

Grading used the authors' rubric and judge prompt unchanged. No API access to the authors' judge model was available, so answers were graded blind: shuffled with a recorded seed, every provenance field stripped, read in fresh sessions of 24 by a Claude model that saw only prompt, rubric and answer, then mapped back through a sealed key. Grades are labelled provisional; a judge failure is recorded as null, never 0. <!-- D006, D008 --> Two batches of each packet were regraded in independent sessions for a reliability figure. Intervals are 95% percentile bootstraps of the mean, 2,000 resamples. <!-- tools/report.py -->

## 4. Results

### 4.1 Generation repeats on one machine and not across machines

Same checkpoint, same 8 prompts, temperature 0, run twice: 8 of 8 byte-identical. <!-- E032 --> At the published settings (0.7, seed 42, one sample), run twice: 8 of 8. With deterministic kernels forced: 8 of 8. Normal against deterministic: 8 of 8. <!-- E035 --> The published 118-of-120 divergence is fully explained by the unrecorded seed and the mismatched sample counts.

Across machines it does not repeat. The same checkpoint at temperature 0 on a CPU in float32 against the V100: 0 of 8 identical. The answers share a prefix of 35 to 142 words, then one token differs and the rest diverges. Each machine repeats itself 8 of 8. <!-- E043 --> The authors' GPU code path cannot run in float32 at all; it asserts bfloat16 rotary tables. Device, dtype and library build belong in the record.

### 4.2 The full sweep

All 24 checkpoints, 8 prompts, one sample, published settings: 192 of 192 generated, 0 errors, 64 minutes. <!-- E042 --> Three series, n=192 each:

**Table 1.** The sweep under two graders.

| Answers | Grader | Mean | 95% interval | 0 / 1 / 2 / 3 / 4 |
|---|---|---|---|---|
| our sweep | ours | 1.27 | 1.18 to 1.36 | 13 / 126 / 41 / 12 / 0 |
| authors' published | ours | 1.26 | 1.17 to 1.35 | 13 / 125 / 45 / 9 / 0 |
| authors' published | theirs, as published | 0.93 | 0.84 to 1.03 | 44 / 122 / 22 / 3 / 1 |

Our answers against theirs under one grader: 126 of 192 cells exact, mean difference +0.01. <!-- E044 --> Their answers under our grader against their published grades, same bytes: 119 of 192 exact, 188 within one point, +0.33. <!-- E044 --> Rank correlation of the 24 per-checkpoint means, ours against published: 0.71. Training trend, first eight to last eight checkpoints: 0.97 to 1.52 ours, 0.62 to 1.11 published. <!-- E042 --> Grader self-consistency: 96 answers regraded, 89 exact, 96 within one. <!-- E039, E042 -->

The generation step reproduces at the level of the score. The whole gap between 1.27 and 0.93 is the grader: same rubric, same answers, a different Claude, plus a third of a point, mostly from the zero row (44 zeros against 13).

### 4.3 Prompt sensitivity

Three wordings on three checkpoints, three seeds each, n=72 per wording. <!-- E037, E039 --> Scaffolded is the published prompt with the classical assumptions listed; minimal removes them; leading appends one hint paragraph that states the core idea, generated so that every judge field stays byte-identical. <!-- D007 -->

**Table 2.** Three wordings, eight prompts.

| Wording | Mean | 95% interval |
|---|---|---|
| minimal | 1.22 | 1.12 to 1.32 |
| scaffolded | 1.36 | 1.22 to 1.50 |
| leading | 1.64 | 1.46 to 1.83 |

The ordering holds on every checkpoint. All 216 answers open with the same sentence, "You have touched a matter of considerable importance", regardless of wording; the published sweep has it in 150 of 192. <!-- E037, E023 -->

### 4.4 The two general-relativity tasks at n=72

Both tasks on all 24 checkpoints, three seeds, three wordings. <!-- E045, E047 -->

**Table 3.** The 1911 consequence and the 1907 seed.

| Task | minimal | scaffolded | leading | hint effect, paired | highest score |
|---|---|---|---|---|---|
| 1911 light bending | 1.31 | 1.57 | 2.46 | +0.89 (+0.69 to +1.08) | 4 |
| 1907 free fall | 0.92 | 0.99 | 0.99 | +0.00 (-0.12 to +0.12) | 2 |

On the elevator the hint lifts 39 of 72 answers to 3 or 4; without it none reaches 3. On free fall no answer in 216 reaches 3 under any wording.

The 1907 observation alone, with or without "what does this tell us about gravity", 144 answers, read blind by two independent readers with a fixed verdict ladder: 0 of 144 bring in acceleration, equivalence or geometry on their own. Every automatic keyword hit (7 of 144) was a false positive on reading. <!-- E047 --> The elevator thought experiment given with no question, 64 continuations across the base model and three checkpoints: 0 reach geometry; the trained model restates "acceleration and gravity are equivalent", which is a line of its own prompt, and stops. <!-- E046 -->

The model can be led to the consequence and not to the seed, even when the seed is handed to it. Given the observation alone it never makes the step.

### 4.5 Contamination

Model side: 16 sentence stems, 11 about post-1900 physics and 5 pre-1900 controls, two checkpoints, greedy and then sampled three times each. Post-1900 stems: 88 of 88 clean. Controls: most fail; the model cannot state Thomson's electron or the Michelson-Morley result either, so the probe measures weak recall in general. <!-- E036, E040 --> Corpus side: the whole training set, 2,074,160 documents, 56 GB, scanned for 15 terms. 0 documents dated 1900 or later. photon, spacetime, Einstein, photoelectric: 0 each. Planck 705, Michelson 277, both at pre-1900 levels. One document dated 1829 describes a 1908 Nobel Prize: a misdated 1909 report, so zero is a lower bound. <!-- E041 -->

## 5. What follows

Three points. A score from an LLM judge is not reproducible unless the judge's model and version are part of the record; here a change of grader moved the published number by more than any prompt manipulation we tried. A record of a generation must hold the seed, the sample count, the model revision, the device and the dtype, or the generation cannot be reproduced by anyone, including its authors. And on the benchmark's own general-relativity tasks, the model reproduces an idea it is given and does not produce one it is not given; the 0 of 144 is the first stage of the Artificial Einstein Test failing, measured.

## 6. Limitations

Scores are provisional: a blinded Claude session with the authors' rubric, not the authors' judge model, which was not reachable without a key; the cross-grade bounds the effect of that choice but does not remove it. No physicist has graded any answer yet; the blinded packet exists for that. 54 checkpoints are unpublished and their results cannot be checked by anyone. Byte-level agreement across hardware is not expected and not claimed. The corpus search is lexical. One model, eight prompts, three seeds per cell. Regrade agreement fell on the later packets (35 and 38 of 48 exact against 44 and 45 earlier).

## 7. Data and code availability

Every generation, grade and reading is archived under `evidence/` with its 50-field record; every command's output is under `logs/`; the lab notebook numbers each result E001 to E047. Code: the upstream repository at commit `5b489c8c` [1] and this study's tools, to be released under a DOI. [CHECK: repository and DOI.]

## 8. Acknowledgements

Computation on SDSC Expanse through ACCESS allocation CIS261668.

## References

[1] M. Hla, GPT-1900, github.com/michaelhla/gpt1900, commit `5b489c8c` (2026).

[2] T. Zahavy, Position: LLMs can't jump, ICML 2026 position paper (2026). [CHECK: no arXiv identifier.]

[3] Luo et al., Pretraining language models on historical text (TypewriterLM), arXiv:2606.02991 (2026).

[4] G. Starace et al., PaperBench: Evaluating AI's ability to replicate AI research, arXiv:2504.01848 (2025).

[5] Z. S. Siegel et al., CORE-Bench, arXiv:2409.11363 (2024).

[6] mhla/gpt1900-d34-contradiction-rl-v11, Hugging Face, revision `71bf395f06dff39ad5ee9f8981b941b3c37daae9`.

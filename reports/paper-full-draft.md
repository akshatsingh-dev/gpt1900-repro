# The model reproduces, the number does not: reproducing an LLM-judged physics benchmark

**Akshat Singh and Brian Keating, University of California San Diego**

Full prose draft of 7 October 2026, written from `reports/paper-draft.md`. Intended for PRX Intelligence as a Regular Article. Sentences marked [CHECK] are flagged for author review. The lab notebook entry behind each number is given in an HTML comment at the number's first appearance.

## Abstract

GPT-1900 is a 3.29-billion-parameter language model trained only on text written before 1900. <!-- upstream summary.txt --> Its authors evaluated 24 training checkpoints on 8 physics prompts, 192 answers graded 0 to 5 by a language model, and published a mean of 0.93. <!-- upstream summary.txt; E033 for the interval 0.84 to 1.03 --> We find that this number is a property of the grader as much as of the model. A fresh sweep of all 192 cells on different hardware, graded blind by one grader beside the authors' own published answers, lands within 0.01 of them, 1.27 against 1.26. <!-- E042, E044 --> The same answers under the authors' grader carry 0.93: the grader alone moves the score by +0.33, <!-- E044 --> more than a hint that states the answer (+0.28) <!-- E039 --> and comparable to the training gain. The authors' own repeats matched on 2 of 120 paired answers <!-- E014, E021 --> because the published record holds three fields per answer <!-- E016 --> and omits the seed and sample count that explain the divergence. <!-- E022, E026 --> With both recorded, generation repeats exactly on one machine (8 of 8 at temperature 0 <!-- E032 --> and at the authors' sampled settings <!-- E035 -->) and diverges across machines (0 of 8 between a V100 and a CPU), each machine self-consistent. <!-- E043 --> On the two general-relativity tasks the hint is worth +0.89 on the 1911 light-bending consequence (n=72, 95% interval +0.69 to +1.08) <!-- E045 --> and +0.00 on the 1907 free-fall seed (-0.12 to +0.12). <!-- E047 --> Given the 1907 observation alone, 0 of 144 answers supply the equivalence. <!-- E047 --> The training corpus, 2,074,160 documents, has none dated after 1899 and one misdated leak. <!-- E041 -->

## 1. Introduction

GPT-1900 [1] is a language model of 3.29 billion parameters trained only on English text written before 1900 and then trained further, by reinforcement learning, on physics reasoning rewards. Its authors put a physics question to it. Given the observations that troubled physicists at the turn of the century, the ultraviolet catastrophe, the photoelectric effect, the Michelson-Morley null result, the falling observer who feels no weight, does a model that has never seen the twentieth century reason toward the twentieth-century answers? They evaluated 24 training checkpoints on 8 prompts, had a hosted language model grade each answer against a 0 to 5 rubric, and published a mean of 0.93 over 192 graded answers. One of us has framed the broader question as an Artificial Einstein Test: whether an intelligence restricted to pre-breakthrough knowledge can reconstruct the reasoning behind a breakthrough rather than retrieve it. [CHECK] GPT-1900 is the first public attempt at such a test that we are aware of.

The score is a measurement, and nobody had checked whether it could be checked. A measurement has an instrument, here a hosted language model used as grader; a sample, here one sampled answer per checkpoint per task; and a record, which is what lets a second laboratory repeat it. We asked four things of the published artefact. Can its generations be repeated at all? Does its score survive a change of grader? How much of the score is the wording of the prompt? Is the training corpus what it claims to be?

Existing benchmarks do not answer these questions for this kind of artefact. We read eight benchmarks and four vintage-cutoff models at source. <!-- reports/evidence-table.md, families 1 to 3 --> One family asks whether an AI system can do the work of science when handed the data or the literature: DiscoveryBench [3], best system 25%; ScienceAgentBench [4], 32.4% to 42.2%; MLE-bench [5], bronze-medal level in 16.9% of competitions; The AI Scientist [6], whose reviewer is itself a language model; and LAB-Bench [7]. A second asks whether an AI system can reproduce what was already done: CORE-Bench [8], best agent 21% on the hardest level, and PaperBench [9], 21.0%, with 8,316 gradable sub-tasks and a rubric validated against human grading. A third restricts a model's knowledge by date: TypewriterLM [10], 7.24 billion parameters on 54 billion tokens of pre-1913 English with a published leakage benchmark; TimeCapsuleLLM [11]; and the Ranke-4B family [12]. The first family hands the model the data. The third restricts knowledge but evaluates recall. None tests reconstruction from restricted knowledge. Where a language model grades the output, the grader is the weak point, and PaperBench is the only one of the eight that validates its rubric against human grading.

The two general-relativity tasks in GPT-1900 have a particular interest. Zahavy [2] has argued, taking Einstein's 1907 thought about the falling observer as his case, that a language model can carry out deduction from a stated premise but not the abductive step that produces the premise. [CHECK: characterisation from the paper's abstract, not from a full reading.] GPT-1900's `gr_free_fall_equivalence` task asks for that 1907 step, and its `gr_main_elevator_light` task asks for the 1911 consequence. The benchmark therefore contains a direct test of the argument, and we report it in Secs. 4.4 and 4.5.

This paper adds six things. A repeat of the published evaluation on all 24 checkpoints at the authors' own settings, with denominators and 95% intervals. A record schema of 50 fields per generation and a comparison tool that refuses to report an agreement rate when settings differ. A grader comparison that separates what the model did from what the grader did. A prompt-sensitivity experiment with matched denominators and a deliberately leading condition, taken to n=72 on the two general-relativity tasks. Model-side and corpus-side contamination checks. And a blinded review packet so that physicists can grade the same answers.

The one-sentence answer is that the model reproduces and the number does not. Under one grader our fresh answers and the authors' published answers score within 0.01 of each other; under two graders the same published answers differ by 0.33; and the published record could not have told anyone which of the two, the model or the grader, had moved.

## 2. The published artefact and its record

GPT-1900 is built on the nanochat training framework [13]. <!-- upstream/gpt1900/PROJECT_LOG.md:28-75 --> The base model, `d34-22btok`, has 34 layers and was pretrained on about 22 billion tokens of pre-1900 English assembled from HathiTrust institutional books, British Library books and the American Stories newspaper collection, on 8 nodes of 8 H100 GPUs. The checkpoints under evaluation, 24 of them in the `v11` series, were trained by reinforcement learning with physics reasoning rewards on that base. The authors' evaluation script, `scripts/physics_eval.py`, downloads each checkpoint from Hugging Face, poses 8 prompts (the ultraviolet catastrophe, the photoelectric effect, frozen light, approaching the speed of light, the train and lightning, Michelson-Morley, the elevator and light, and free-fall equivalence), samples one answer per prompt at temperature 0.7 and top_k 50, and sends each answer with a per-task rubric to a hosted judge model, `claude-sonnet-4-20250514`, which returns a score from 0 to 5 and a rationale. The published result is the directory `results/physics_eval_v11`: 192 generations, 192 judged scores, mean 0.932. <!-- E024 -->

Two prompt wordings are published. `EVAL.json` is scaffolded: each prompt lists the classical assumptions in play and then asks the question. `EVAL_no_assumptions.json` removes that list. The archive also holds two repeat runs and a run under the minimal wording on three checkpoints. We read the whole archive before running any model. Table 1 is what we found.

**Table 1.** What the published record contains.

| Fact | Where |
|---|---|
| Each answer record holds three fields: prompt, mode, completions | `scripts/physics_eval.py`, write at line 609 <!-- E016 --> |
| Temperature, top_k, num_samples and max_tokens are in scope three lines above the write and are not written | same <!-- E017, E018 --> |
| No revision pin on weight downloads; the Hugging Face name can move under the result | `download_checkpoint` <!-- E020 --> |
| No seed in the evaluation script; the engine default of 42 applied silently | `nanochat/engine.py`, line 171 <!-- E026 --> |
| Run and repeat used 1 and 3 samples; one random generator is shared across every row of a batch, so the draws differ | <!-- E022, E026 --> |
| 54 of 89 checkpoints in the registry are marked local and were never published, every v8 checkpoint among them | <!-- E020 --> |
| 5 of 12 runs with generations were never graded; both repeat runs were made with the judge skipped | <!-- E012 --> |
| The judge call sets no temperature; a judge failure is written as score 0 (0 such cases in v11) | `judge_all` <!-- E016, E033 --> |
| Consequence: 2 of 120 paired answers are byte-identical between a published run and its repeat | <!-- E014, E021 --> |

The last row is the one a reader of the archive notices first, and it says nothing about the model. The authors' repeats of their own pipeline disagreed with themselves on 118 of 120 paired answers, and the three-field record cannot say why. An unrecorded seed and an unrecorded sample count are each enough to change every sampled token. The archive cannot distinguish a change in the model from a change in the dice.

## 3. Methods

### 3.1 Upstream pinned and never edited

We imported the upstream repository at commit `5b489c8c` and did not modify it. <!-- D003 --> Every tool in this study lives beside it and calls into it, so every difference between our results and the published ones is attributable to environment or settings and not to our patches. The rule has one cost, which we report as a finding rather than work around: the authors' code asserts that its rotary embedding tables are in bfloat16, so a float32 control on a GPU cannot run without a patch, and we did not run one (Sec. 4.2).

### 3.2 Generation

Our generation wrapper calls the upstream engine once per sample rather than once per batch. <!-- D004, E026 --> The upstream engine builds one random generator per call and shares it across every row of the batch, so the draws that reach sample 0 depend on how many samples sit beside it. The authors' run and its repeat used 1 and 3 samples, which alone guarantees that they could not match. One sample per call makes a record comparable to any other record with the same seed, whatever the batch size. The cost is one extra prompt prefill per sample.

Every run set beside a published number uses the authors' settings: seed 42, temperature 0.7, top_k 50, one sample, the scaffolded prompt. <!-- D005 --> These are the values the published v11 sweep ran with, the seed by engine default. Runs that test determinism use temperature 0, which takes the argmax path and touches no random generator.

Each checkpoint is pinned by Hugging Face revision hash, `71bf395f06dff39ad5ee9f8981b941b3c37daae9` for every v11 checkpoint, and the sha256 of the downloaded weight file is recorded in every record of the full sweep. <!-- E032, E042 -->

### 3.3 The record

Each generation is written as one JSON line with 50 fields, schema version 1.2. <!-- notes/logging-schema.md --> Table 2 gives the groups. A failed generation gets a record of the same shape with the completion null and an error field filled, so every denominator in this paper counts attempts and not successes.

**Table 2.** The 50-field generation record, by group.

| Group | Fields |
|---|---|
| Run identity | run id, timestamp, code commit, dirty flag, config path, config sha256 |
| Model identity | repository, revision hash, checkpoint name, checkpoint step, weight sha256 |
| Prompt | task id, prompt text, prompt sha256, prompt condition (scaffolded, minimal or leading), mode (completion or chat) |
| Sampling | seed, sample index, temperature, top_k, top_p, num_samples, max_tokens, repetition penalty |
| Environment | device, number of GPUs, GPU name, compute capability, bf16 supported, dtype as loaded, dtype override, torch version, platform, Python version, Slurm job id, deterministic-algorithms flag |
| Output | completion text, completion sha256, token count, finish reason, generation seconds |
| Judge | judge model, judge model version, judge prompt sha256, judge temperature, raw response, score, rubric version, judged-at time |
| Error | exception type and message; null on success |

Three rules matter more than the field count. One sample per engine call. The comparison tool, `compare_runs.py`, treats temperature, top_k, num_samples, max_tokens, model repository, revision, config hash, code commit and schema version as blocking, and refuses to report an agreement rate when any of them differ between two runs; device, dtype, GPU, torch version and platform are reported as differences and mark the comparison as a portability test rather than a determinism test. <!-- compare_runs.py --> And a judge failure is recorded as null, never as 0. <!-- D006 -->

### 3.4 Prompt conditions

Three wordings were used. Scaffolded is the authors' `EVAL.json`. Minimal is their `EVAL_no_assumptions.json`. Leading is generated from `EVAL.json` by a script that appends one hint paragraph after each task's question and leaves every other field, including the rubric and the expected concepts the judge sees, byte-identical, checked by a field-by-field assertion. <!-- D007, E033 --> A score difference between conditions is therefore attributable to the prompt the model saw and to nothing else. The hints for the two general-relativity tasks are quoted in Sec. 4.4; each states the top levels of its task's rubric.

For the single-task runs on the two general-relativity tasks, one-task configurations were generated from each source file in the same way, with every non-task field byte-identical. <!-- E045, E047 --> Two further prompts for the free-fall task, which withhold the explanatory idea entirely, are described in Sec. 4.4.

### 3.5 Grader

No API access was available during this work, so the authors' judge model could not be called. Scores were produced instead by a blinded reader, and every score in this paper is labelled provisional. <!-- D008 --> The answers from a run are shuffled with a recorded seed and every provenance field is stripped. Each batch of 24 is then graded in a fresh session of a Claude model (`claude-fable-5-1`) that sees only an opaque id, the prompt, the authors' own rubric for that task, and the answer. The grades are mapped back through a sealed key into the judge fields of the record, with the grader named in `judge_model`, `judge_temperature` null, and the grader's full response stored as the rationale. Two batches per packet were graded twice in independent sessions for a reliability figure. The rubric, the blinding and the record are the same as an API pass would use. What differs is the grader model and the absence of a temperature setting, and both are written down. A one-command judge pass with the authors' model at temperature 0 replaces these scores when a key exists, and the report then shows both graders side by side.

Grading by a reader who already knew the hypotheses was rejected, as was presenting no scores. A labelled provisional score beats a blank, and the cross-grade in Sec. 4.3 turned the limitation into a measurement.

The same blinding was used for the two reading tasks that have no rubric (Secs. 4.4 and 4.5): answers shuffled and stripped, one verdict per answer from a fixed list, the highest rung reached, with the rule that restating the prompt's own observations counts as none.

### 3.6 Statistics

Means are reported with 95% bootstrap intervals over answers. Hint effects are paired differences by checkpoint and seed, with bootstrap intervals. Agreement between two gradings of the same answers is reported as the count of cells exact and the count within one point. The training trend is the mean over the first eight checkpoints against the mean over the last eight. The rank correlation of per-checkpoint means is Spearman's.

### 3.7 Hardware

All GPU runs were on SDSC Expanse, one Tesla V100-SXM2-32GB per job, torch 2.14.0+cu126. <!-- E029, E032 --> The V100 has no bfloat16 hardware, so weights held as bfloat16 are computed by emulation; this is recorded in every generation as `bf16_supported: false`. The cross-machine control ran the authors' own CPU path at float32 on a shared Expanse node with 32 cores. <!-- E043 --> The authors' evaluation hardware is not recorded anywhere in their archive.

## 4. Results

### 4.1 What a reader of the published archive cannot recover

From the published record alone a reader cannot recover the seed, the sample count, the temperature, the top_k, the maximum token count, the revision of the weights, the device, the dtype, the library build, the judge temperature, or whether a judge failure contributed a 0. <!-- E016, E017, E018, E020, E026 --> The seed and the sample count are enough on their own to explain the authors' 2 of 120. The device, the dtype and the library build are enough to prevent anyone else from matching their text even with the first two known (Sec. 4.2). Of the 89 checkpoints in their registry, 54 are marked local and cannot be downloaded, so the v5 to v8 results cannot be examined by anyone outside the project. <!-- E020 -->

### 4.2 Generation is deterministic on one machine and diverges across machines

**Table 3.** Repeatability tests. Checkpoint `s560`, 8 prompts, scaffolded wording.

| Test | Result | |
|---|---|---|
| Temperature 0, run twice, V100 | 8 of 8 byte-identical | <!-- E032 --> |
| Temperature 0.7, top_k 50, seed 42, one sample, run twice, V100 | 8 of 8 | <!-- E035 --> |
| Same, with deterministic kernels forced, run twice | 8 of 8 | <!-- E035 --> |
| Normal kernels against deterministic kernels | 8 of 8 | <!-- E035 --> |
| V100 emulated bfloat16 against CPU float32, temperature 0 | 0 of 8 | <!-- E043 --> |
| CPU float32, run twice | 8 of 8 | <!-- E043 --> |
| Shared prefix before first divergence, V100 against CPU | 35 to 142 words, mean 450 characters | <!-- E043 --> |
| GPU float32 | cannot run; `gpt.py:396` asserts bfloat16 rotary tables | <!-- E043 --> |

On one machine, with the seed and the sample count recorded, generation at the authors' own settings is exactly repeatable, and forcing deterministic kernels changes nothing. The published divergence of 118 in 120 is fully explained by the two unrecorded settings. No hardware or library nondeterminism is needed to explain it, and none was observed. At temperature 0 the two runs also matched in token count on every task (586, 586, 238, 325, 350, 301, 462 and 433 tokens). <!-- E032 -->

Across machines the picture is different. The same checkpoint, the same prompts and the same argmax path, with no random draw anywhere, give 0 of 8 answers identical between the V100 holding emulated bfloat16 and a CPU at float32. <!-- E043 --> The CPU path run twice is 8 of 8 identical, and both files are 34,426 bytes. <!-- E043 --> Each machine is self-consistent; the two disagree with each other on every answer. The mechanism is visible in the texts: the two answers agree for tens to hundreds of words and then one near-tied token falls the other way under a different floating-point summation order, and everything after it diverges. On the ultraviolet catastrophe the pair agree for 136 words, after which the V100 writes "the total energy is not uniform throughout the frequency interval" and the CPU writes "the total energy thus produced is finite". <!-- E043 --> Neither is the correct answer. They are two computations.

| Task | V100 tokens | CPU tokens | Shared prefix, characters / words |
|---|---|---|---|
| uv_catastrophe_main | 586 | 498 | 792 / 136 |
| photoelectric_effect_main | 586 | 518 | 201 / 34 |
| sr_frozen_light | 238 | 333 | 600 / 108 |
| sr_approaching_c | 325 | 305 | 479 / 89 |
| sr_train_lightning | 350 | 377 | 205 / 35 |
| sr_michelson_morley | 301 | 257 | 210 / 37 |
| gr_main_elevator_light | 462 | 416 | 801 / 142 |
| gr_free_fall_equivalence | 433 | 272 | 314 / 55 |

<!-- E043 -->

> **Figure 1 (placeholder).** Cross-machine divergence: length of the shared prefix per task, V100 emulated bfloat16 against CPU float32, temperature 0. Source: the E043 table above.

Two consequences follow. Reproducible, for this pipeline, means reproducible on one machine at one dtype. And the authors' unrecorded hardware is not a footnote: with their seed, sample count and every sampling setting matched, their text could not be reproduced on a V100 or on a CPU, and our byte match against their published answers for the same eight cells at their settings was 0 of 8, as this predicts. <!-- E035 --> The device, the dtype and the library version belong in the record, and their three fields hold none of them. Whether emulated bfloat16 on a V100 sits closer to native bfloat16 on an H100 than float32 does we cannot say; no bfloat16-native hardware was available to us. Three plausible hardware paths exist and we have measured two of them disagreeing.

### 4.3 The full sweep: the model reproduces, the number does not

We ran all 24 v11 checkpoints on the 8 prompts, one sample each, seed 42, temperature 0.7, top_k 50, scaffolded wording: the 192 cells behind the published mean. Generation was 192 of 192 with 0 errors, 4 answers cut at max_tokens, in 64 minutes on one V100. <!-- E042 --> Each record carries the revision hash, the weight sha256 and the other 48 fields. The stock opening "You have touched a matter of considerable importance" begins 151 of our 192 answers and 150 of the 192 published ones. <!-- E042, E023 --> Byte-identical to the published answers: 0 of 192, as Sec. 4.2 predicts across hardware.

We then graded three series with the blinded procedure: our 192 answers, and the authors' 192 published answers, which we regraded under the same rubric. The third series is the authors' published grades of those same answers.

**Table 4.** Three series, n=192 each, 95% bootstrap intervals.

| Text | Grader | Mean | 95% interval | 0 / 1 / 2 / 3 / 4 | |
|---|---|---|---|---|---|
| our sweep | ours | 1.27 | 1.18 to 1.36 | 13 / 126 / 41 / 12 / 0 | <!-- E042 --> |
| their published answers | ours | 1.26 | 1.17 to 1.35 | 13 / 125 / 45 / 9 / 0 | <!-- E044 --> |
| their published answers | theirs, as published | 0.93 | 0.84 to 1.03 | 44 / 122 / 22 / 3 / 1 | <!-- E033 --> |

> **Figure 2 (placeholder).** The three series of Table 4 as three score histograms, 0 to 5, side by side. Source: `evidence/sweep/report.json`.

Our text against their text under one grader: 126 of 192 cells exact, mean difference +0.01. <!-- E044 --> Their text under two graders, the same bytes: 119 of 192 cells exact, 188 of 192 within one point, mean difference +0.33. <!-- E044 --> The training trend is present in all three series. From the first eight checkpoints to the last eight the mean rises from 0.97 to 1.52 on our text, from 0.92 to 1.45 on their text under our grader, and from 0.62 to 1.11 as published. <!-- E042, E044 --> The Spearman rank correlation of the 24 per-checkpoint means, ours against published, is 0.71. <!-- E042 --> Our per-checkpoint means run from 0.75 to 1.62; the published ones from 0.25 to 1.25. <!-- E042 -->

> **Figure 3 (placeholder).** Per-checkpoint means, ours against published, 24 points each, with the rank correlation of 0.71. Source: `evidence/sweep/report.json`.

Per task the same pattern holds. Under our grader on our text, and under our grader on their text, every task scores above its published mean (Table 5). The two largest published per-task means, the photoelectric effect and the elevator, remain the two largest under our grader.

**Table 5.** Per-task means over 24 checkpoints.

| Task | Ours, our grader | Theirs, our grader | Theirs, published |
|---|---|---|---|
| UV catastrophe | 1.25 | 1.33 | 0.83 |
| Photoelectric effect | 2.17 | 1.92 | 1.54 |
| Frozen light | 1.00 | 1.08 | 0.75 |
| Approaching c | 0.88 | 0.75 | 0.38 |
| Train and lightning | 0.96 | 0.96 | 0.54 |
| Michelson-Morley | 1.29 | 1.25 | 1.04 |
| Elevator and light | 1.58 | 1.67 | 1.46 |
| Free-fall equivalence | 1.04 | 1.12 | 0.92 |

<!-- E042, E044 -->

The generation step reproduces the published result at the level of the score. A fresh sweep on different hardware, graded by one grader beside the authors' own answers, lands within 0.01 of them with two thirds of cells agreeing exactly. The whole gap between 1.27 and 0.93 is the grader. Same rubric, same answers, a different Claude: +0.33, most of it from the zero row, 44 zeros under their grader against 13 under ours, and the rest from the 2 and 3 rows. That shift is larger than the effect of a hint paragraph that states the answer (+0.28, Sec. 4.4) and comparable to the gain across training (+0.49 as published). The published number is a property of the grader as much as of the model.

Grader reliability on these packets: 96 answers were graded twice in independent sessions, 89 exact and 96 within one point. <!-- E039, E042 --> A smaller check agrees. The seeded run on `s560` at the authors' settings (Table 3) graded 1.00 at n=8 (0.62 to 1.38) against the published `s560` row of 1.25, with exact agreement on 6 of 8 cells despite different text and a different grader. <!-- E039 -->

### 4.4 Prompt sensitivity, with the two general-relativity tasks as the worked example

Three wordings of each prompt were run on three checkpoints (`s560`, `s630`, `s735`, the three the authors used for their own minimal-prompt run), three seeds each (42, 43, 44), temperature 0.7, top_k 50: 216 generations, 216 of 216 written, 0 errors, 0 truncated, n=72 per condition. <!-- E037 --> Before any grading, one text-level fact: 216 of 216 answers open with the stock sentence, under every wording, the leading one included. <!-- E037 -->

**Table 6.** Three wordings, eight tasks, n=72 per condition, 95% bootstrap intervals.

| Condition | Mean | Interval | 0 / 1 / 2 / 3 / 4 | |
|---|---|---|---|---|
| minimal | 1.22 | 1.12 to 1.32 | 0 / 56 / 16 / 0 / 0 | <!-- E039 --> |
| scaffolded | 1.36 | 1.22 to 1.50 | 1 / 49 / 17 / 5 / 0 | |
| leading | 1.64 | 1.46 to 1.83 | 0 / 40 / 20 / 10 / 2 | |

The ordering leading above scaffolded above minimal holds on every checkpoint separately (`s560` 1.54 / 1.29 / 1.17; `s630` 1.54 / 1.38 / 1.12; `s735` 1.83 / 1.42 / 1.38). <!-- E039 --> Leading minus scaffolded per task: elevator +0.89, frozen light +0.56, photoelectric +0.44, Michelson-Morley +0.44, free fall +0.11, approaching c +0.11, train 0.00, ultraviolet catastrophe -0.33. <!-- E039 --> The intervals of leading and minimal do not overlap; leading and scaffolded overlap by 0.04. <!-- E039 -->

> **Figure 4 (placeholder).** Prompt sensitivity: the three conditions per task, and leading minus scaffolded per task. Source: `evidence/prompt-sensitivity/report.json`.

A hint that states the answer moves the mean by +0.28 on a benchmark whose published signal is 0.93 and whose published spread across 24 checkpoints is 0.25 to 1.25. Removing the classical assumptions costs 0.14. The two largest gains land on the tasks whose hint most nearly restates the rubric's top answer. The benchmark measures the prompt as well as the model, by an amount comparable to the differences the published results report between checkpoints.

The authors' own comparison of the two published wordings cannot be read as a sensitivity result. Their scaffolded sweep (0.93, n=192, 24 checkpoints, one sample per cell) and their minimal run (1.38, n=72, 3 checkpoints, three samples per cell) differ in sample count and checkpoint set as well as in wording; the bootstrap 95% intervals from their files are 0.84 to 1.03 and 1.21 to 1.54. <!-- E033, E025 --> On the three shared checkpoints that unmatched comparison puts the elevator task at -0.90 from scaffolded to minimal. <!-- E025 --> That figure and the +0.89 above are different quantities, an unmatched difference between two published runs against a paired difference between the leading and scaffolded wordings, and only the second is a sensitivity result. With denominators matched, the minimal wording scores lowest. One cross-grader number is available: the authors' minimal run on these checkpoints under their judge is 1.38 (1.21 to 1.54); ours on the same wording under our grader, different samples, is 1.22 (1.12 to 1.32); the intervals overlap. <!-- E039 --> [CHECK: the memo says each lies inside the other's interval; 1.38 lies outside 1.12 to 1.32.]

#### The two general-relativity tasks

The benchmark's two general-relativity tasks are Einstein's two steps. `gr_free_fall_equivalence` is the 1907 seed: a person falling from a roof feels no weight, so gravity and acceleration are locally the same thing. `gr_main_elevator_light` is the 1911 consequence: if that is so, light must bend in a gravitational field. The elevator test as one of us has posed it is the first of these. [CHECK] Both were run on all 24 checkpoints, three seeds, three wordings, 72 answers per condition, and graded blind.

**Table 7.** The 1911 task, `gr_main_elevator_light`, n=72 per condition, all 24 checkpoints. <!-- E045 -->

| Condition | Mean | Interval | 0 / 1 / 2 / 3 / 4 |
|---|---|---|---|
| minimal | 1.31 | 1.18 to 1.43 | 0 / 53 / 16 / 3 / 0 |
| scaffolded | 1.57 | 1.44 to 1.69 | 2 / 27 / 43 / 0 / 0 |
| leading | 2.46 | 2.26 to 2.65 | 0 / 11 / 22 / 34 / 5 |

Leading minus scaffolded, paired by checkpoint and seed: +0.89, interval +0.69 to +1.08. <!-- E045 --> Scaffolded minus minimal: +0.26 (+0.08 to +0.44). <!-- E045 --> Without the hint no answer in 72 scores above 2; with it 39 of 72 score 3 or 4. <!-- E045 --> The hint reads: "consider that gravity might not be a force pulling on mass at all, but a change in the shape of space and time itself, which light follows like everything else." <!-- tools/make_leading_config.py:62 --> It states rubric levels 4 and 5. The published mean for this task's column is 1.46; ours under the published wording is 1.57. <!-- E045 --> The training trend from the first 8 to the last 8 checkpoints is 1.21 to 1.83 scaffolded and 1.71 to 2.79 leading, so the hint helps more as training proceeds. <!-- E045 --> Regrade on this packet: 35 of 48 exact, 48 of 48 within one. <!-- E045 -->

**Table 8.** The 1907 task, `gr_free_fall_equivalence`, n=72 per condition, all 24 checkpoints. <!-- E047 -->

| Condition | Mean | Interval | 0 / 1 / 2 / 3 / 4 |
|---|---|---|---|
| minimal | 0.92 | 0.81 to 1.03 | 12 / 54 / 6 / 0 / 0 |
| scaffolded | 0.99 | 0.89 to 1.07 | 6 / 61 / 5 / 0 / 0 |
| leading | 0.99 | 0.90 to 1.07 | 5 / 63 / 4 / 0 / 0 |

Leading minus scaffolded, paired: +0.00, interval -0.12 to +0.12. <!-- E047 --> Scaffolded minus minimal: +0.07 (-0.07 to +0.21). <!-- E047 --> The highest score in 216 answers is 2; no answer reaches 3 under any wording. <!-- E047 --> The hint reads: "consider that free fall might be the natural, unforced state of motion, and that what we call gravity is an effect of the structure of space and time, which is why it can be removed locally by falling." <!-- tools/make_leading_config.py --> It states rubric levels 4 and 5, as the elevator hint did, and moves nothing. The published mean for this column is 0.92; ours under the published wording is 0.99, with exact agreement on 17 of the 24 shared cells. <!-- E047 --> Training trend, first 8 to last 8 checkpoints: scaffolded 0.83 to 1.00, leading 0.92 to 1.08. <!-- E047 --> Regrade: 38 of 48 exact, 48 of 48 within one. <!-- E047 --> The smaller earlier estimates agree: sweep n=24 mean 1.04; sensitivity n=9 per condition scaffolded 1.11, minimal 1.22, leading 1.22, hint +0.11. <!-- E042, E039 -->

> **Figure 5 (placeholder).** Left: the 1911 task, per-checkpoint mean for three conditions, 24 checkpoints. Source: `evidence/elevator/report.json`. Centre: the 1907 task, the same, three flat curves near 1. Source: `evidence/freefall/report.json`. Right: the count of answers to the 1907 observation alone that reach each rung, 0 of 144 above none. Source: `evidence/freefall/readings.json`.

#### The 1907 observation alone

The benchmark lacks a condition that hands the model the observation and nothing else. We added two prompts for the free-fall task. <!-- E047 --> The seed form gives the two observations, the falling person and the objects floating beside them, and appends "What does this tell us about gravity?" The bare form gives the two observations and appends nothing. Neither mentions an accelerating cabin, equivalence, or gravity disappearing. We ran both on all 24 checkpoints with three seeds each, 144 answers, and had them read blind by two independent readers, 72 each, with one verdict per answer for the highest rung reached.

The result is 0 of 144. <!-- E047 --> No answer brings in acceleration, equivalence, gravity as not a force, or geometry. All 144 verdicts are none; 0 loop and 0 are incoherent. Automatic keyword flags fired on 7 of 144, and each is a false positive on reading ("equivalent to the sum of all the forces"; "not a force that can be measured in pounds"; "this is the geometry of gravity", followed by Newtonian pressing). <!-- E047 --> The readers' near-misses, all none under the rule, are a fall that "neutralises" the force, bodies that "glide side by side" with acceleration never named, weight felt only at the abrupt stop, and the universality of free fall stated several times without the step to equivalence. <!-- E047 --> The stock opener begins 117 of the 144. <!-- E047 --> What the model produces instead is period prose about air, muscles, inertia, Newton's attraction and the divine order.

Set together, the two tasks give one result with two halves. On the 1911 consequence the hint is worth +0.89 and lifts more than half the answers to rung 3 or 4. On the 1907 seed the same kind of hint is worth +0.00, and no answer in 216 reaches 3 under any wording. Given the seed alone, 0 of 144 answers supply the equivalence. The model can be led to the consequence and cannot be led to the seed, even when the seed is handed to it. The elevator prompt states the equivalence and asks for its consequence, and the model carries the hint's stated idea forward. The free-fall prompt asks for the equivalence itself, and the model restates the observation. Carrying a stated idea forward it can do. Producing the idea, or using it once stated as a hint, it cannot.

### 4.5 The elevator thought experiment without a question

What does the model do when nobody asks it a rubric-shaped question? We gave it the seven numbered observations of `gr_main_elevator_light` with no puzzle, no question and no hint, in two forms: continue, which ends after the observations, and ask, which appends "What follows from this?" <!-- E046 --> Four models were run: the pre-RL base `d34-22btok` in completion mode, and the RL checkpoints `s035`, `s560` and `s839` in chat mode, each as the registry defines it. Eight samples each, seeds 42 to 49, temperature 0.7, up to 1024 tokens: 64 continuations, 64 of 64 written. Each was read blind with one verdict from {equivalence, bends-in-gravity, not-a-force, geometry, none, incoherent, loops}, the highest rung reached.

**Table 9.** Continuations of the elevator observations with no question. <!-- E046 -->

| Model | Mode | loops | none | equivalence | bends-in-gravity | not-a-force | geometry | Stock opener | Hit 1024 tokens |
|---|---|---|---|---|---|---|---|---|---|
| `d34-22btok` (base) | completion | 16 | 0 | 0 | 0 | 0 | 0 | 0 of 16 | 16 of 16 |
| `s035` | chat | 0 | 8 | 5 | 2 | 1 | 0 | 1 of 16 | 1 of 16 |
| `s560` | chat | 0 | 1 | 14 | 1 | 0 | 0 | 16 of 16 | 0 |
| `s839` | chat | 0 | 0 | 16 | 0 | 0 | 0 | 16 of 16 | 0 |

Geometry is reached by 0 of 64. <!-- E046 --> Rung 3, gravity as not a force, is reached by 1 of 64. Three continuations state that light does not bend. The base model loops in 16 of 16. The most-trained checkpoint, `s839`, produces one verdict 16 times out of 16: "acceleration and gravity are equivalent", which is line 4 of its own prompt, and stops there; `s560` does the same in 14 of 16. The only verdicts above rung 1 come from `s035`, the least-trained RL checkpoint and the only one without the stock opener, and the reader marked two of its three as marginal (Earth's rotation offered as the mechanism; garbled numerics).

The model restates the given as a conclusion and stops. Set beside Sec. 4.4: with the hint, 39 of 72 answers reach rung 3 or 4; without a question, 0 of 64 reach rung 4 and 1 of 64 reaches rung 3. The hint is not eliciting what the model already thinks. It is supplying the thought.

This also places the two published tasks in a stage-gated reading of the benchmark. Both hand the model the problem and the explanatory idea in the prompt, and the rubric rewards restating them. [CHECK] The seed and bare conditions of Sec. 4.4 are the first attempt to withhold the explanatory idea, and on them the count is 0 of 144.

One confound is stated here and again in Sec. 6. The base model runs in completion mode and the RL checkpoints in chat mode, because that is how the registry defines them, so the base-against-RL contrast in Table 9 carries a mode difference as well as a training difference.

### 4.6 Contamination

From the model side, 16 sentence stems, 11 about post-1900 physics and people and 5 controls about pre-1900 physics inside the corpus, were continued by the base model and by `s560` at temperature 0.7, three samples each, 96 continuations, every one read blind against the expected outcome. The post-1900 continuations are 66 of 66 clean, 0 leaks. <!-- E040 --> The controls fail too: the base model fails 13 of 15 and knows only, twice, that the aether is the medium of light; the RL model fails 9 of 15, is partial on 6 and correct on 0. <!-- E040 --> Neither can state what Thomson's electron or the Michelson-Morley experiment was, and both are in the corpus. A greedy pass over the same stems gave the same verdict; the base model loops at temperature 0 on 13 of 16 stems, which is why the sampled pass is the one reported. <!-- E036 --> The clean result stands with its limit. A model of this size on 22 billion tokens of scanned books does not carry named facts as retrievable items on either side of 1900, so a stem probe cannot separate never having seen Planck from having seen and not retained him. Contamination risk is bounded above by recall, and recall of named facts is near zero.

From the corpus side, the instrument that can separate the two: the training corpus itself, `mhla/pre1900-corpus` at revision `ff332ef6`, 42 shards, 56.4 GB, 2,074,160 documents, was scanned for 15 terms with a year histogram per term and a count of documents dated 1900 or later. <!-- E041 --> By metadata, 0 documents are dated 1900 or later; the range is 1547 to 1899.

**Table 10.** Corpus term search. <!-- E041 -->

| Term | Documents | Share | Latest year | Reading |
|---|---|---|---|---|
| Einstein | 0 | 0 | none | clean |
| photon | 0 | 0 | none | clean |
| photoelectric | 0 | 0 | none | clean |
| spacetime | 0 | 0 | none | clean |
| aether wind | 0 | 0 | none | clean |
| Planck | 705 | 0.034% | 1899 | publishing from 1879 |
| Lorentz | 330 | 0.016% | 1899 | publishing from 1875 |
| Michelson | 277 | 0.013% | 1899 | 1881 and 1887 experiments |
| Rayleigh | 702 | 0.034% | 1899 | pre-1900 author |
| relativity | 1,391 | 0.067% | 1899 | philosophical sense |
| quantum | 14,407 | 0.695% | 1899 | Latin, common |
| quanta | 2,614 | 0.126% | 1899 | same |
| Morley | 14,235 | 0.686% | 1899 | surname |
| FitzGerald | 19,216 | 0.926% | 1899 | surname |
| Nobel Prize | 1 | 0.00005% | 1829 | contamination, see text |

> **Figure 6 (placeholder).** The corpus term table with a year histogram per term. Source: `evidence/contamination/corpus-search.json`.

Every term that could only exist after 1900 returns zero across two million documents. The terms that do appear are pre-1900 usages. One hit is real contamination. A single document matches "Nobel Prize"; its metadata year is 1829, and its text reads "The Nobel Prize was awarded in December last to two distinguished Scandinavian peace workers, one-half to Mr. Fredrik Bajer of Denmark". Bajer received the Peace Prize in 1908. The document is a 1909 annual report of the American Peace Society carrying a wrong date, and it passed a date filter because of it. <!-- E041 -->

Two conclusions follow. There is no evidence that the eight physics tasks are answerable from leaked text: nothing in two million documents names the physics that came after 1900, and the model-side probe found no recall of it. And the count of zero post-1900 documents is a lower bound, not a proof. The corpus was assembled by date, at least one misdated source is in it, and a term search cannot see paraphrase or post-1900 ideas written in period vocabulary. The Michelson row deserves one more sentence: the experiment is in the training data, 277 documents, and the Michelson-Morley task is the one task that never scores 0 in the published results. <!-- E041, E024 -->

## 5. Discussion

The first point is about the record. A benchmark score can be checked only if the record behind it lets a second laboratory regenerate the sample and re-apply the instrument. For a sampled language model that means the identity of the weights by revision and file hash; the seed and sample index, per generation; the temperature, top_k and token limit; the device, dtype and library build; and the identity, version and temperature of the judge with its raw response. The published GPT-1900 record holds three of these fifty things. Recording the rest cost one wrapper script, and the return is that every claim in this paper has a denominator and a diff. The two rules that did the most work are not fields: one sample per engine call, so that a record is comparable regardless of batch size, and a comparison tool that refuses to compute an agreement rate when settings differ, which is the exact error in the published comparison of the two wordings.

The second point is about the grader. In this benchmark the largest single source of variance we measured is not the model, the hardware or the prompt. It is the grader: +0.33 on the same bytes under the same rubric, against +0.28 for a hint that states the answer, +0.01 for a fresh sweep on different hardware, and +0.49 for the whole of training as published. A third of a point on a five-point scale moved when the grader changed and nothing else did. Every benchmark in the evidence table that uses a language model as judge carries the same term, and only PaperBench has measured it against human grading. For GPT-1900 three things follow. The judge model and version must be pinned in the record and treated as an instrument with a calibration. A score should be reported with its grader named beside it, as Table 4 does, never alone. And a human anchor is needed before either grader can be called correct; the blinded packets released with this paper are the instrument for that, and until physicists have graded them we do not know whether 0.93 or 1.26 is nearer the truth.

The third point is about what the general-relativity results say. The rubric rewards an answer that reaches the top rung, and the leading condition shows that the top rung can be reached by restating a hint that contains it: 39 of 72 answers at rung 3 or 4 on the 1911 task with the hint, 0 of 72 without. The same hint construction moves the 1907 task by nothing, and 0 of 144 answers given the 1907 observation alone take the step from "the falling person feels no weight" to "gravity and acceleration are the same". Given the observations with no question, the trained model's commonest output is line 4 of its own prompt offered as a conclusion. Passing the rubric and reasoning toward general relativity are different achievements. On this model the first is available by prompt construction and the second does not occur in 360 answers. This is the measurement Zahavy's position asks for [2]: on the one benchmark that poses Einstein's 1907 step to a model that cannot have read the answer, the step is not taken.

## 6. Limitations

The v5 to v8 checkpoints were never published; 54 of 89 registry checkpoints are unreachable to anyone outside the project, so the published results for those series cannot be examined. <!-- E020 -->

Hardware changes exact outputs. Floating-point summation order differs between machines and flips a later token; we measured 0 of 8 identical answers across a V100 and a CPU with every setting matched. <!-- E043 --> Text-level reproduction of the authors' answers is therefore not possible on any machine but theirs.

The original evaluation did not record hardware, dtype or library build, so what their machine was is not known. <!-- E016 -->

The authors' judge model, `claude-sonnet-4-20250514`, was not reachable without a key during this work. Every score in this paper is from a provisional blinded grader, and the cross-grade bounds the effect of that choice at about 0.33 on the published answers. <!-- D008, E044 -->

Which grader is nearer a physicist's judgement is untested. The blinded packets exist and have not been graded by physicists. <!-- evidence/review-packet-* -->

The contamination scan is lexical: 15 terms and a date field over 2,074,160 documents. Paraphrase and post-1900 ideas in period vocabulary are outside it, and the model-side probe cannot see them either because the model's recall of named facts is near zero on both sides of 1900. <!-- E041, E040 -->

The base-against-RL comparison in Sec. 4.5 carries a mode confound: the base model runs in completion mode and the RL checkpoints in chat mode. <!-- E046 -->

The reading of the 144 seed and bare answers and of the 64 open continuations was one pass per answer with no regrade; the automatic keyword cross-check is the only independent check on it. <!-- E046, E047 -->

The grader's regrade agreement fell to 35 of 48 on the elevator packet and 38 of 48 on the free-fall packet, from 89 of 96 on the earlier packets, and one regraded batch disagreed in one direction only (14 of 24 exact, the second reader higher on 10). <!-- E045, E047, E042 --> The provisional grader's floor moves between sessions.

## 7. Data and code availability

Code: the upstream repository `github.com/michaelhla/gpt1900` at commit `5b489c8c`, MIT licence [1], and this study's `tools/` directory, to be published with the paper under a DOI-issuing repository. [CHECK: repository and DOI to be assigned before submission.]

Every generation, grade and rationale produced for this paper is in `evidence/` as JSON Lines, one record per generation, with the schema in `notes/logging-schema.md`. The blinded packets are `evidence/review-packet-a`, `-b` and `-c`, and the elevator and free-fall packets.

Weights: Hugging Face `mhla/gpt1900-d34-contradiction-rl-v11` at revision `71bf395f06dff39ad5ee9f8981b941b3c37daae9` [14]; base model `mhla/gpt1900-d34-22btok` [15]. Corpus: `mhla/pre1900-corpus` at revision `ff332ef64f896c8d44672b4d1d0c752029e32f29` [16].

The use of a hosted language model as the grader is a research instrument and is disclosed in Sec. 3.5 with the model identifier, the prompt it received, and the blinding and regrading used to verify its output, as APS policy requires.

## 8. Acknowledgements

This work used Expanse at the San Diego Supercomputer Center through ACCESS allocation CIS261668.

## References

[1] M. Hla, GPT-1900, github.com/michaelhla/gpt1900, commit `5b489c8c` (2026).

[2] T. Zahavy, Position: LLMs can't jump, ICML 2026 position paper, January 2026, www.tomzahavy.com/files/llms-cant-jump.pdf. [CHECK: no arXiv identifier found; arXiv:2608.14397 is a response by Balani and Panda, not this paper.]

[3] B. P. Majumder et al., DiscoveryBench: Towards data-driven discovery with large language models, arXiv:2407.01725 (2024).

[4] Z. Chen et al., ScienceAgentBench: Toward rigorous assessment of language agents for data-driven scientific discovery, arXiv:2410.05080 (2024).

[5] J. S. Chan et al., MLE-bench: Evaluating machine learning agents on machine learning engineering, arXiv:2410.07095 (2024).

[6] C. Lu et al., The AI Scientist: Towards fully automated open-ended scientific discovery, arXiv:2408.06292 (2024).

[7] J. M. Laurent et al., LAB-Bench: Measuring capabilities of language models for biology research, arXiv:2407.10362 (2024).

[8] Z. S. Siegel et al., CORE-Bench: Fostering the credibility of published research through a computational reproducibility agent benchmark, arXiv:2409.11363 (2024).

[9] G. Starace et al., PaperBench: Evaluating AI's ability to replicate AI research, arXiv:2504.01848 (2025).

[10] Luo et al., Pretraining language models on historical text (TypewriterLM), arXiv:2606.02991 (2026).

[11] H. Grigorian, TimeCapsuleLLM, github.com/haykgrigo3/TimeCapsuleLLM (2025 to 2026).

[12] Ranke-4B, as listed at github.com/entanglr/awesome-vintage-llms, read 22 September 2026. [CHECK: primary source not read.]

[13] A. Karpathy, nanochat, github.com/karpathy/nanochat. [CHECK: URL not verified in this draft.]

[14] mhla/gpt1900-d34-contradiction-rl-v11, Hugging Face, revision `71bf395f06dff39ad5ee9f8981b941b3c37daae9`.

[15] mhla/gpt1900-d34-22btok, Hugging Face.

[16] mhla/pre1900-corpus, Hugging Face, revision `ff332ef64f896c8d44672b4d1d0c752029e32f29`.

# Presentation brief: GPT-1900 reproducibility and the jump test

Written 28 Oct 2026 for whoever builds the slides. Everything below is measured and archived; every number has a lab notebook entry (E numbers) in `notes/lab-notebook.md`. Do not invent numbers, do not round further than shown, keep denominators next to every count.

## Who, what, why

- Presenter: Akshat Singh, Data Science undergrad, UC San Diego. Work with Prof. Brian Keating (Physics), Aug to Oct 2026, on SDSC Expanse (V100 GPUs, ACCESS allocation CIS261668).
- Subject: GPT-1900 (github.com/michaelhla/gpt1900), a 3.29B parameter model trained only on text written before 1900. Its authors asked it eight physics questions whose answers came after 1900, had a Claude model grade each answer 0 to 5 against a rubric, and published a mean of 0.93 over 192 answers (24 training checkpoints x 8 questions).
- The larger idea: Keating's "Artificial Einstein Test". Can an AI limited to pre-breakthrough knowledge reconstruct the reasoning behind a breakthrough, rather than retrieve it?
- The question this work answers: would anyone else get 0.93, and what does that number measure?

## The thesis, one sentence

The model reproduces; the score does not survive a change of grader; one hint beats all of training; and the model never makes Einstein's jump, but it also cannot take the ordinary steps, so it cannot yet test whether the jump is the hard part.

## Scale of the work (for an "effort" slide)

- About 1,500 generations on Expanse, every one archived with a 50-field record. 0 generation errors in any run.
- Over 1,500 answers graded or read blind: 192 ours plus 192 theirs on the rubric, 216 sensitivity, 216 + 216 on the two relativity tasks, 144 + 64 + 75 + 260 on the jump tests.
- 50 lab notebook entries, 10 written decisions, 94 command logs, 61 scripts. Upstream code pinned at commit 5b489c8c and never edited.
- Repo: github.com/akshatsingh-dev/gpt1900-repro (private until the paper is out).

## Test by test, with the number to put on the slide

### 1. What was wrong with the published pipeline (desk audit, before any run) [E011 to E026]

- Their saved results hold 3 fields per answer: prompt, mode, text. No seed, no temperature, no top_k, no sample count, no model revision, no hardware.
- Their own repeat runs: v8 vs v8_det 0 of 96 answers identical; v11 vs v11_replication 2 of 24. Combined 2 of 120, 1.7%.
- 54 of 89 checkpoints in their registry were never published.
- 150 of 192 published answers open with the same sentence: "You have touched a matter of considerable importance."
- 86% of their 192 scores are 0 or 1. The top of the rubric is never used.
- Root cause, found in the code: the engine defaults to seed 42 (so the seed was fixed, just never written down), and one random generator is shared across every answer in a batch, so asking for 3 answers instead of 1 changes which draws answer 1 gets. Both repeat runs used a different sample count from the original.

Slide line: "Their reruns disagreed 118 times out of 120. Two settings were never recorded. Bookkeeping, not the model."

### 2. Does the model give the same answer twice? [E032, E035]

- Same checkpoint, temperature 0, run twice: 8 of 8 answers byte-identical.
- Their settings (temperature 0.7, top_k 50, seed 42), run twice: 8 of 8.
- Same with deterministic GPU kernels forced: 8 of 8. Normal vs deterministic: 8 of 8.
- 0 of 8 match their published text, as expected (different hardware, see test 3).

Slide line: "Record the seed and the sample count and the model is deterministic. 8 of 8, three ways."

### 3. But not across machines [E043]

- V100 (bfloat16 emulated in software, the chip has no native support) vs CPU (float32), same checkpoint, temperature 0, same prompt: 0 of 8 identical.
- Identical for 35 to 142 words (mean 450 characters), then one near-tied word flips under different rounding and everything after diverges.
- CPU run twice: 8 of 8. Each machine repeats itself.
- GPU float32 cannot run at all: upstream asserts that rotary tables are bfloat16.

Slide line: "Reproducible means on one machine at one precision. Hardware belongs in the record."

### 4. The full reproduction and the cross-grade [E042, E044]

Three series, n=192 each, 95% bootstrap intervals:

| Text | Grader | Mean | Interval | 0 / 1 / 2 / 3 / 4 |
|---|---|---|---|---|
| ours, regenerated | ours | 1.27 | 1.18 to 1.36 | 13 / 126 / 41 / 12 / 0 |
| theirs, published | ours | 1.26 | 1.17 to 1.35 | 13 / 125 / 45 / 9 / 0 |
| theirs, published | theirs | 0.93 | 0.84 to 1.03 | 44 / 122 / 22 / 3 / 1 |

- Our text vs their text, same grader: 126 of 192 cells exactly equal, mean difference +0.01. The model reproduces.
- Same text, two graders: 119 of 192 exact, 188 within one point, mean difference +0.33. Most of it in the zero row: 44 zeros under their grader, 13 under ours.
- Every one of the eight tasks scores higher under our grader. Training trend is the same shape under both: first eight checkpoints to last eight, 0.97 to 1.52 (ours), 0.62 to 1.11 (theirs).
- Stock opener: 151 of 192 ours, 150 of 192 theirs.

Slide line: "The model reproduces to 0.01. The number moves 0.33 with the grader. 0.93 is a property of the grader as much as the model."

### 5. Does the wording change the score? [E037, E039]

Three wordings of every question. Scaffolded: their prompt, classical assumptions spelled out. Minimal: without the assumptions. Leading: scaffolded plus one hint paragraph per task that restates the rubric's top answer; the hint was generated by script so every other byte is identical (D007). Three checkpoints x three seeds x 8 tasks, n=72 per wording.

- Minimal 1.22 (1.12 to 1.32). Scaffolded 1.36 (1.22 to 1.50). Leading 1.64 (1.46 to 1.83).
- 216 of 216 answers open with the stock sentence, every wording.

Slide line: "One hint paragraph adds about 0.3 on a benchmark whose whole signal is 0.93. The model learned a voice."

### 6. The two relativity tasks at full scale [E045, E047]

All 24 checkpoints x 3 seeds x 3 wordings, n=72 per wording. Elevator light is the 1911 consequence (light bends in a falling elevator). Free fall is the 1907 seed (a falling person feels no weight).

| Task | minimal | scaffolded | leading | hint effect, paired | published |
|---|---|---|---|---|---|
| Elevator light, 1911 | 1.31 | 1.57 | 2.46 | +0.89 (+0.69 to +1.08) | 1.46 |
| Free fall, 1907 | 0.92 | 0.99 | 0.99 | +0.00 (-0.12 to +0.12) | 0.92 |

- 1911: without the hint no answer in 72 scores above 2; with it 39 of 72 score 3 or 4. The hint contains the answer ("gravity might not be a force at all but the shape of space and time").
- 1907: highest score in 216 answers is 2. No wording reaches 3.
- The hint helps more as training proceeds (leading, first 8 to last 8 checkpoints: 1.71 to 2.79). Training teaches prompt-following.

Slide line: "The hint only helps where it contains the answer. On the seed of the idea it does nothing."

### 7. The jump, four designs [E046, E047, E049, E050]

Read blind against a fixed ladder of verdicts: wrong (weight still felt), none (never says what is felt), weightless (the 1907 observation), equivalence (brings in acceleration on its own: the jump), not-a-force, geometry (beyond the jump). Ladders fixed before reading (D009).

- Given only the 1907 observation, 144 answers: 0 reach equivalence. All 144 none.
- Given the elevator observations with no question, 64 answers: 0 reach geometry. The trained model restates the prompt's own line "acceleration and gravity are equivalent" as its conclusion and stops: 16 of 16 for the most trained checkpoint. The base model loops 16 of 16.
- The elevator question in the draft paper's own words, 25 checkpoints x 3 seeds, 75 answers: 0 weightless, 0 equivalence. 48 none, 23 wrong, 4 loops. Wrong answers rise with training: 3 of 24 in the first eight checkpoints, 12 of 24 in the last eight.
- Four wordings plus a ladder of help, 4 checkpoints x 5 seeds, 140 answers: 0 equivalence or geometry. 72 none, 30 wrong, 32 loops (all base model), 2 incoherent, 1 weightless, 3 not-a-force. The 3 not-a-force all came from the prompt that told the model its idea of gravity was mistaken; they repeat the hint back with no reason, and are not counted as the jump.
- Sharpest wording: a man lets go of a stone in the falling elevator. Trained checkpoints say it falls to the floor 14 of 15 times.

Slide line: "0 of 144. 0 of 64. 0 of 75. 0 of 140. It usually says you still feel your weight."

### 8. The controls: can it walk? [E050]

A recent position paper argues language models can deduce and induce but cannot "jump" (abduce a new idea). Six control questions a 19th-century reader could answer from the training books. Trained checkpoints, 15 answers each.

| Control | type | in corpus | correct | partial | wrong | none |
|---|---|---|---|---|---|---|
| Stone from a moving ship's mast (Galileo) | deduction | yes | 0 | 2 | 10 | 3 |
| Heavy and light stone dropped together | deduction | yes | 0 | 6 | 9 | 0 |
| Pendulum 1, 4, 9, 16 ft in 1, 2, 3, 4 s: the rule | induction | yes | 1 | 3 | 10 | 1 |
| Uranus drifts off Newton's path (Neptune, 1846) | abduction | yes | 0 | 5 | 10 | 0 |
| Light speed same along and across Earth's motion (1905) | abduction | no | 0 | 0 | 6 | 9 |
| Hot body's glow peaks then dies at high frequency (1900) | abduction | no | 0 | 2 | 4 | 9 |

- 1 of 90 control answers correct, and that one states the pendulum rule then gets the numbers in the prompt wrong.
- Base model loops in 52 of 65 answers. The one thing training clearly did: loops became fluent period prose.

Slide line: "It fails Galileo too. The floor is too low to see the ceiling. This model cannot test the can't-jump claim."

### 9. Did post-1900 physics leak into the training data? [E036, E040, E041]

- Model side: 16 half-sentences to complete, 11 post-1900, 5 pre-1900 controls. Post-1900 stems clean 66 of 66. But pre-1900 controls: base model knows 2 of 15 (both the aether), trained model 0 of 15. A "photon" is "a piece of paper or cloth". It cannot describe Michelson-Morley, which is in its own data. So the clean result partly measures weak recall in general.
- Corpus side: all 2,074,160 training documents, 56 GB, 15 terms. Einstein 0, photon 0, photoelectric 0, spacetime 0, "aether wind" 0. Planck 705, Lorentz 330, Michelson 277: all active before 1900, latest year 1899. Documents dated 1900 or later: 0.
- One hole: a document filed as 1829 describes the 1908 Nobel Peace Prize. It is a 1909 report with a wrong date. One in two million, not a physics leak, but the clean count is a lower bound.

Slide line: "Clean for physics. The date filter has at least one hole."

### 10. How reliable is the grading? [D008, E039, E042, E045, E047]

- Method: no API key was available, so grades come from a blinded reading by Claude Fable 5.1 applying the authors' rubric verbatim, in fresh sessions of 24 answers, answers shuffled with a recorded seed, checkpoint and wording stripped, grades mapped back through a sealed key. Not the authors' judge model (claude-sonnet-4-20250514). Labelled provisional in every file.
- Regrades in independent sessions: 24 of 24, then 45 of 48 (combined 89 of 96 exact) on the plain tasks; 35 of 48 on the 1911 task; 38 of 48 on the 1907 task. 100% within one point everywhere.
- One regrade moved a batch mean from 1.62 to 2.04, all in one direction, without changing any ordering. The provisional grader has a floor that moves between sessions.

Slide line: "Agreement high on plain tasks, lower on relativity. Provisional until the authors' judge and a physicist have graded."

### 11. The pipeline that makes this checkable [E031, D003, D006]

- 50 fields per generation: weights SHA-256 and revision, prompt and hash, config and hash, seed, temperature, top_k, sample count, max tokens, dtype, device, GPU name, native-bf16 flag, deterministic-kernel flag, library versions, job id, timing, finish reason, completion and hash, eight judge fields, code commit.
- The comparison tool refuses to report a match rate when two runs differ in any setting. That refusal is the mistake their own comparison made.
- A grading failure is recorded as null, never as 0. Their pipeline wrote 0.
- Blinded packets built for every run, keys sealed, so physicists can grade without seeing provenance.

Slide line: "Every answer carries enough to be re-run. Their pipeline saved three fields."

### 12. What is open

- The pass with the authors' own judge model (needs an API key, under $5, 20 minutes). Until then every score is provisional.
- Physicist grading of the sealed packets.
- A second machine reader through a typed-answer API (built, dry-run, three cents per run, thresholds pre-registered as D010).
- A model that passes the controls. The jump test is only informative on a model that can take the ordinary steps.

## Recommended slide order (14 slides)

1. Title. "GPT-1900, checked: what reproduces, what the score measures."
2. The idea: pre-1900 model, eight post-1900 questions, 0.93 out of 5. Keating's question.
3. The published pipeline, audited: 2 of 120, 3 fields, 78% stock opener.
4. Why: seed 42 by default, shared generator, mismatched sample counts.
5. Determinism: 8 of 8 three ways. Cross-machine: 0 of 8, prefix then cascade.
6. The reproduction: three-bar chart, 1.27 / 1.26 / 0.93 with intervals.
7. Wording: 1.22 / 1.36 / 1.64. 216 of 216 same opener.
8. The two relativity tasks: hint +0.89 vs +0.00. Explain 1911 vs 1907.
9. The jump, four designs: 0 of 144, 0 of 64, 0 of 75, 0 of 140.
10. The abduction suite: stacked verdict bar for the 140, the stone 14 of 15.
11. Controls table. 1 of 90. "It fails Galileo too."
12. Contamination: 0 of 2,074,160, one misdated document.
13. Grader reliability and the provisional label. The pipeline in one slide.
14. What it means for the Artificial Einstein Test, and what is open.

## Figures to build (all from numbers above)

- Bar chart, three graded series with 95% intervals (slide 6).
- Bar chart, three wordings (slide 7).
- Paired bars, hint effect on the 1911 and 1907 tasks with intervals (slide 8).
- Stacked horizontal bar of 140 elevator verdicts: wrong 30, none 72, weightless 1, not-a-force 3, loops 32, incoherent 2, equivalence 0, geometry 0 (slide 10).
- Controls table as shown (slide 11).
- Score histograms 0 to 4 for the three series (optional, slide 6 inset).

## Lines the presenter can say verbatim

- "Their reruns disagreed 118 times out of 120. Not the model. Two settings nobody wrote down."
- "Write down the seed and the batch size and you get the same words every time. 8 of 8, three ways."
- "We got 1.27. Their own answers under our grader: 1.26. Their grader: 0.93. The model reproduces. The number belongs to the grader."
- "One hint paragraph is worth 0.89. The entire training run is worth about 0.5."
- "A falling person feels no weight. Einstein got from there to relativity. We gave the model that sentence 144 times. Zero."
- "Then we asked it where a stone falls from a moving ship's mast. Galileo, 1632, in its own books. Wrong ten times out of fifteen."
- "The model never makes the jump. It also cannot walk. So it cannot tell us whether jumping is the hard part."
- "Every number here is provisional until the authors' judge and a physicist have graded. Both are one step away."

## Caveats to say out loud, not hide

- Provisional grader, not the authors' judge model. Named in Methods. Regrade rates above.
- One reader, one pass on the blind readings; verdict ladders fixed before reading.
- V100 emulates bfloat16; cross-machine text differs; every claim is per machine.
- Five seeds per prompt in the abduction suite: enough to see 0 of 140, not enough for fine rates.
- The base model runs in completion mode, trained checkpoints in chat mode, so base-vs-trained carries that confound.
- The 3 not-a-force verdicts are reported, not hidden, and not counted as the jump; the reason is given.

## Glossary for the slides (one line each)

- Checkpoint: a saved copy of the model partway through training; 24 published, s035 to s839, plus base d34-22btok.
- Temperature: randomness in word choice; 0 is always the top word; 0.7 is what they used.
- top_k 50: only the 50 most likely next words can be drawn.
- Seed: the starting number for the random draws; same seed, same draws.
- Sample count: answers per question per batch; changes the draws even at a fixed seed.
- bfloat16 / float32: number formats; different rounding, different text across machines.
- Rubric: their 0 to 5 scale with a sentence per level; used verbatim.
- Blind: the grader sees question, expected answer and text, never checkpoint or wording.
- 95% bootstrap interval: resample 2000 times, middle 95% of the means.
- Scaffolded / minimal / leading: their prompt; without assumptions; plus one hint paragraph.
- Equivalence, the jump: feeling weight and being accelerated are the same from inside; falling removes gravity. Einstein, 1907.
- Abduction: a new explanation from a surprising fact; deduction is rules to case; induction is cases to rule.

## Style rules for the deck

- Plain English, short sentences, numbers with denominators. No em dashes.
- Name the grader model where grades are shown. Do not describe how the slides or the write-ups were produced.
- No "professor" in slide text; "Keating" or "the group".
- Keep the published numbers (0.93, 1.46, 0.92) next to ours wherever both exist.

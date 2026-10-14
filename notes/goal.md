# The goal

The file to read when the point of all this has gone fuzzy. Written 3 Sep 2026.

---

## The question behind everything

Can an AI system do more than retrieve and recombine science it has already
read? If you restrict it to knowledge that existed before Einstein's
breakthrough, can it independently reconstruct the reasoning that led to general
relativity?

That is the Keating, Hassabis, Einstein Test. It is Prof. Keating's question, not
mine, and it is the thing the paper argues about.

## What I was actually assigned

Not to derive general relativity. Not to train a model. My job is narrower and
it is the part that decides whether the claim survives contact with other
scientists: **make the test rigorous and reproducible.**

Six items, from Keating's email:

1. Reproduce a published GPT-1900 evaluation using its released checkpoints.
2. Build an eval pipeline that records every prompt, output, model version,
   seed, temperature, and scoring decision.
3. Test prompt sensitivity and possible contamination, using scaffolded,
   minimally scaffolded, and deliberately leading prompts.
4. Archive every generation rather than selecting the impressive ones.
5. Build a source-backed evidence table of AI-discovery benchmarks and their
   limits.
6. Produce a blinded review packet for physicists, a reproducibility memo, and a
   short final presentation.

His framing of why: this is meant to teach how a broad claim becomes a
defensible scientific test. Separating evidence from interpretation, designing
controls, checking citations, documenting assumptions, exposing negative
results, and producing work another researcher can inspect and reproduce
independently.

Dates: 20 Aug to 15 Sep 2026. Eight hours a week. Written update to Keating
Monday night, Zoom Tuesday 1pm PT.

## What that means in plain terms

Somebody published a result. Nobody ever checked whether running it again gives
the same answer. I am the person checking.

If the answer is no, the interesting part is not "it failed", it is **why**, and
whether the archive contains enough information for anyone to tell. So far it
does not.

## What I have found, all measured on this machine

- 2 of 120 paired generations reproduce between published runs. 1.7 percent.
- Zero occurrences of `seed` in the upstream eval script.
- Zero occurrences of `revision`. Weights are fetched by a name whose contents
  can change.
- Three fields saved per generation: prompt, mode, completions. The temperature
  and top_k that produced the answer are command line arguments that are never
  written down.
- 54 of 89 registry checkpoints were never published.
- 5 of 12 runs have generations that were never graded.
- Zero tests cover the eval script.

## The one experiment that matters right now

Everything above says published runs disagree. None of it says why. There are
two possible worlds and they need very different responses.

**World A, batch coupling.** E026 found the seed was never actually absent. It
lives one layer down in `nanochat/engine.py`, defaults to 42, and upstream never
overrides it, so every published run was nominally seeded and seeded the same.
What differs is `--num-samples`. One shared generator serves every row of a
batch, so sample 0 of a three-sample run and sample 0 of a one-sample run consume
different draws from the same seed and cannot match. E022 showed both upstream
run pairs used mismatched sample counts. That alone explains the failure.
Prediction: at matched sample counts and temperature 0.0, which takes the argmax
path and touches no generator at all, two runs on one machine are byte-identical.

**World B, something below the sampler.** Same settings, argmax path, and the two
runs still disagree. Then no seed fixes it and the result is much more serious.

**The test that separates them:** one published v11 checkpoint, one set of tasks,
temperature 0, same seed, run twice, compare byte for byte.

That is the whole experiment. Everything else on the list is logistics that make
it possible, or reporting that makes it count.

## Definition of done, 15 Sep

- A number for reproducibility that I measured myself, with the denominator.
- An archive where every generation carries the settings that produced it.
- A memo another researcher could follow to get the same number.
- The blinded packet, the evidence table, the talk.

Negative results count. A benchmark that does not reproduce is a finding, not a
failure, as long as the evidence is complete enough for someone else to check.

---

## The Python work that remains, in priority order

Written 3 Sep 2026. Nothing here is a new model. It is the measuring apparatus.

1. **Run `tools/logged_eval.py` for the first time.** It is written and it
   imports clean, but it has never touched a checkpoint, so its own claims are
   untested. Two runs, temperature 0, same seed, same checkpoint.
2. **Write the comparison.** Reads two JSONL files, matches records on task_id
   and seed, compares `completion_sha256`. Reports matched over total. About
   twenty lines. This is what turns two files into the headline number.
3. **Fix the dtype field.** `environment_fields()` records
   `"bfloat16" if device.type == "cuda"`, copying upstream's assumption that any
   GPU is Ampere or later. Expanse GPUs are V100, which has no bfloat16. Read
   the real dtype off the loaded model instead of inferring it from the device.
   A recording bug in the tool built to fix recording bugs.
4. **Repeat and quantify.** Run the pair five times, not once. The published
   mean of 0.93 out of 5 has no error bar because every score is a single draw.
   Giving the number an interval is what makes a physicist able to argue with it.
5. **The judging pass.** Second script. Reads the JSONL, calls the judge at
   temperature 0, fills `score`, `judge_model`, `judge_prompt_sha256`,
   `judged_at_utc`. Blocked on an API budget from Keating. No upstream repeat
   run has ever been graded, so this is the widest gap.
6. **Prompt sensitivity.** Same checkpoint, three prompt files: scaffolded,
   minimal, and a leading condition that does not exist yet and has to be
   written. Measures how much of the score is the model and how much is the
   question.
7. **Contamination probe.** String search over `mhla/pre1900-corpus` for
   vocabulary that could not exist before 1900. CPU work, no GPU needed.

Items 1 and 2 produce the reproducibility number, which is deliverable one.
Item 3 keeps the archive honest. Item 4 is what makes the number defensible.
Items 5, 6 and 7 are deliverables two and three.

---

## Two things I want built, stated 3 Sep 2026

1. **A place to host GPT-1900 so anyone can query it.** Keating asked for this in
   week 2. Upstream already ships the serving code: `chat_web.py`,
   `launch_serving.sh`, `dashboard.py`, `SERVER_SETUP.md`. The missing piece is a
   machine, not software.
2. **The full eval across all 24 v11 checkpoints, run on Expanse.** 24 x 8 tasks
   is 192 generations per sweep, and the experiment needs repeated sweeps rather
   than one.

Both are currently blocked, for different reasons.

**Item 2 is not blocked.** An earlier reading of `expanse-client` said the GPU
award was missing. `accessusage` shows otherwise: 1000 GPU hours on
`expanse-gpu.sdsc.xsede.org` under CIS261668, unused, valid to 26 Aug 2027, with
`asingh59` listed on it. See E030. What is still unverified is whether Slurm will
start a GPU job, which `sbatch --test-only` settles.

**Item 1 may not belong on Expanse at all.** It is a batch cluster with job
walltime limits and no public inbound networking, which suits sweeps and does not
suit an always-on service. Jetstream2 is the ACCESS resource shaped for this.
Raised with Evan 3 Sep.

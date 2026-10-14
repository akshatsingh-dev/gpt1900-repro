# Progress Update Week 3, Akshat Singh

GPT-1900 reproducibility, 8 September 2026
Evaluated against github.com/michaelhla/gpt1900

## What I did

The pipeline is built and running on Expanse. This week I got the model loaded on a GPU, ran the first real experiment, and got a result. The code is written. From here the work is running it in different configurations and logging what comes out.

## Compute

- The Expanse account is live. Last week's report said it was not, that is now out of date.
- All four allocations are attached and confirmed: 1000 GPU hours, 4000 CPU hours, 500 GB storage, and the ACCESS credit pool. Nothing spent yet beyond a few minutes of testing.
- One catch that cost a day: the default PyTorch install has no support for Expanse's V100 GPUs. It could see the card but could not run on it. Fixed by installing the CUDA 12.6 build instead. Worth knowing for anyone else in the group using Expanse.

## The pipeline

Four scripts, all tested, all in the repo.

- logged_eval.py runs a checkpoint on the 8 physics questions and writes one record per answer with 50 fields: which exact bytes of model, the prompt, every sampling setting, the hardware, the output, and timing. Theirs saves three fields.
- compare_runs.py takes two runs and reports how many answers came back identical, byte for byte. It refuses to give a number if the two runs used different settings, which is the mistake their own comparison made.
- render_html.py turns the records into a page you can read.
- Job scripts for Slurm, so a run is one command.

The first checkpoint took 48 seconds to download and 16 seconds per question to answer. A full pass over all 24 checkpoints is about an hour of GPU time.

## The result

Same checkpoint, same 8 questions, randomness off, run twice. 8 of 8 answers identical.

What that means: the model is consistent when you ask it the same way. Their published runs disagreed with each other 118 times out of 120, and this shows the model was never the reason. The reason was two settings they did not write down: the sampling temperature, and the number of samples per batch, which changes the random draws even at a fixed seed. Both are bookkeeping. Both are fixable.

Two other things from the same run.

- Every one of the 8 answers opens with the same sentence, "You have touched a matter of considerable importance." I found that phrase in 78 percent of their published outputs. With randomness off it is 100 percent.
- Expanse's V100 GPUs do not support bfloat16 in hardware. The code loads the weights as bfloat16 anyway and PyTorch emulates it. So a number from a V100 and a number from an A100 are not the same computation, and the memo has to say so.

## What it means for the paper

The published score of 0.93 out of 5 is a number nobody could check. Now there is a pipeline where every answer carries enough information to be checked, and the first check passed. The next checks are whether the score holds up when the question is worded differently, and whether the grade holds up when graded twice.

## Next

1. Same checkpoint, minimal prompt. The version without the classical assumptions spelled out. This is the first half of the prompt sensitivity test.
2. Repeat the pair five times for an error bar.
3. All 24 checkpoints, both prompt versions. This is the full reproduction of their published sweep.
4. The blinded review packet. Answers shuffled, provenance stripped, sealed key, scoring sheet with their rubric.
5. The reproducibility memo and the presentation.

## Three things I need

1. An API key or budget for the grading step. No repeat run of theirs has ever been graded, so this is the widest gap.
2. Where the hosted page should live. Expanse is batch with no public address. Jetstream2 looks like the right ACCESS resource. Evan is checking.
3. A scope call. Six items were assigned. Items 1, 2, 4 and 6 will land. Prompt sensitivity will land partially. The contamination probe and the leading prompt condition are designed but will not run before the 15th unless something else drops.

Subject: Progress, repro week 1

Hi Prof. Keating,

Short version: I spent this first stretch reading the GPT-1900 code and result
files rather than running them, and the reading turned up more than I expected.
The headline is that their published generations do not reproduce, and I can
trace why to specific lines.

## How I worked

Running the evaluation means downloading a 6.6GB checkpoint, and there are 24 of
them, so I read first to find out which one to pull. Everything below was
verified by me against their repository at commit 5b489c8c. I kept a lab notebook
with 23 numbered entries and saved the raw terminal output for every command, so
any number here can be traced back to the command that produced it.

## What I found

**Their eval script never sets a random seed.** Zero occurrences in the file.
Sampling is on by default at temperature 0.7. So no generation in the repository
can be regenerated, by me or by them.

**The generations do not reproduce, measured.** They have two pairs of runs where
the same evaluation was done twice. I checked the prompts were byte-identical
first, then compared the answers.

- physics_eval_v8 vs physics_eval_v8_det: prompts identical 96 of 96, answers
  identical 0 of 96.
- physics_eval_v11 vs physics_eval_v11_replication: prompts identical 24 of 24,
  answers identical 2 of 24.
- Combined: 2 identical out of 120 paired generations, 1.7 percent.

I re-ran both comparisons in the direction that could have weakened my own
finding, allowing a match against any stored sample rather than only the first.
Neither number moved.

**The settings are never saved.** Each generation record holds three fields:
prompt, mode, completions. The file is written at line 609 of physics_eval.py,
and temperature, top_k, num_samples and max_tokens are in scope three lines above
and are not included. So I can show the answers do not repeat but not why. The
fix looks like roughly ten lines at that one location.

**No model revision is pinned either.** Zero occurrences of "revision". The
download resolves a Hugging Face name, which is mutable, so two runs separated in
time could use different weights with nothing recording it.

**No repeat run was ever judged.** Both used the --skip-judge flag. I assume that
was to save API cost on exploratory runs, which seems reasonable, but it does
mean no reproducibility figure for the score itself has ever been computed.
Across the repository, 5 of the 12 runs that have generations were never judged.

**78 percent of published answers open with the same phrase.** 150 of 192 begin
"You have touched". This matters twice over: it inflated a similarity measure I
was computing, and since the judge is an LLM scoring free text, it raises a
question about whether the score partly tracks period register rather than
physics. I am not claiming it does, only that it is unchecked and checkable.

**One thing about the reported mean.** Each of the 192 scores is a single draw
from its own distribution, so there is no within-condition variance and no error
bar on 0.93. Their pipeline supports three samples per prompt by default and the
published run used one.

## Limits on my own findings

My strongest number, 0 of 96, comes from the v8 pair, and those checkpoints are
marked "local" in their registry, meaning the weights were never published. So
that comparison is evidence about their saved files rather than a reproduction an
outsider could repeat. 54 of the 89 registry entries are unpublished. The v11
family is public, and 24 checkpoints across 8 tasks is 192, exactly the published
score count, so v11 is where I am pointing my own run.

I also had a theory that one run had been prompted in the wrong format, which
would have been more serious. I checked it and I was wrong, so I dropped it. Two
smaller corrections are in my notes.

## What they did well

They save results after every checkpoint for crash resilience, and they delete
each checkpoint after evaluating it, filtering the download to one step's
weights. That resolved a disk constraint I thought I had. The gap I found is a
field selection at one line rather than general carelessness.

## What I have not done

Nothing has been run yet. No install, no model loaded. Everything above is from
reading source and result files. I also have not started the survey of related
vintage-model projects.

## Next

1. Install the environment and get one v11 checkpoint generating locally. Most
   reproduction attempts fail at installation and I would rather find that out
   now.
2. One checkpoint, one task, compared against their published output.
3. The same thing twice at temperature 0, which separates a bookkeeping problem
   with a small fix from a structural one without.
4. Implement the generation record. I have drafted it as 43 fields, each marked
   present, discarded at the write, or absent from their codebase entirely. 24
   are absent.

I have also mapped each finding onto the section of your draft it bears on,
mainly 13.3, 13.4 and 11.4, and I would value your view on one thing at the
meeting. 13.3 covers sampling bias and cherry-picking, and both assume a run
could in principle be repeated. Here no run can be regenerated at all. That feels
like a different category to me, and upstream of the others, but you would know
better than I would.

## Two asks

1. Is there UCSD compute I could use? A machine with a GPU would turn the
   checkpoint sweep from a manual one-at-a-time process into something that runs
   overnight.
2. Is there a channel to Michael Hla? Four of my open questions have one-minute
   answers if he is willing: what _det was testing, why 54 checkpoints are
   unreleased, whether the skipped judging was cost, and why the repeat runs used
   a different sample count from the originals.

Thanks, and looking forward to Tuesday.

Akshat

Subject: Progress, repro week 1

Hi Prof. Keating,

I spent this first stretch reading the GPT-1900 code and result files rather than
running them, since running means pulling a 6.6GB checkpoint and there are 24.
Everything below I verified myself against their repo at commit 5b489c8c, with a
lab notebook and raw terminal output saved for each step.

**The headline: their generations do not reproduce.** They have two pairs of runs
where the same evaluation was done twice. I confirmed the prompts were
byte-identical first, then compared answers.

- v8 vs v8_det: 0 of 96 identical
- v11 vs v11_replication: 2 of 24 identical
- Combined: 2 of 120, 1.7 percent

**Why:** their eval script never sets a random seed. Zero occurrences in the
file, with sampling on by default at temperature 0.7. So no generation in the
repository can be regenerated, by me or by them. The settings are not saved
either: each record holds prompt, mode and completions, while temperature,
top_k, num_samples and max_tokens are in scope three lines above the write at
line 609 and are left out. No model revision is pinned either.

**Three other things.** No repeat run was ever judged, both used --skip-judge, so
no reproducibility figure for the score itself exists. 78 percent of published
answers open with the identical phrase "You have touched", which matters because
the judge is an LLM scoring free text. And each of the 192 scores is a single
draw, so there is no error bar on 0.93, although their code supports three
samples per prompt by default.

**A limit on my own finding.** The 0 of 96 comes from v8, whose checkpoints are
marked "local" and were never published, so it is evidence about their saved
files rather than a reproduction anyone could repeat. 54 of 89 registry entries
are unpublished. The v11 family is public and is what the 192 published scores
come from, so that is where I am pointing my own run.

**Not done yet.** Nothing has been run. No install, no model loaded. Everything
above is from reading source and artefacts.

## Plan to 15 September

Working to 8 focused hours a week, so 24 hours remain. I have ranked the work by
what has never been done rather than by what comes next in sequence.

| Week | Focus | Deliverable |
|---|---|---|
| 25 to 31 Aug | Install, first local generation, and the determinism test at temperature 0 | Whether the failure is bookkeeping or structural |
| 1 to 7 Sep | Implement the generation record, then run the first **judged** repeat | Whether the score reproduces, and an error bar on 0.93 |
| 8 to 14 Sep | Prompt sensitivity across three conditions, targeted contamination probe, evidence table | Sensitivity table with denominators |
| 15 Sep | Reproducibility memo, judge review protocol, presentation | Final |

The determinism test is the priority this week because everything after it
depends on the answer. If two runs at temperature 0 are byte-identical, the
problem is record-keeping and a seed fixes it. If they still differ, the cause is
hardware or numeric precision and the results would not transfer to any machine.

Week 2 is the one I care most about. Two different answers can both score 1 out
of 5, so it is entirely possible the score is stable even though the text is not.
Nobody has checked, because no repeat run was ever judged.

**Out of scope, so it is not assumed:** re-running all 24 checkpoints, a full
corpus audit, reproducing v5 to v8 since those weights were never published, and
actually running the blinded physicist review, for which I will deliver a written
protocol rather than results.

## Three asks

1. Is there UCSD compute I could use? A GPU machine would turn the checkpoint
   sweep from a manual one-at-a-time process into something that runs overnight.
2. Judging calls the Claude API, which costs money, and week 2 depends on it. Is
   there an existing key I should use, or a budget I should work within?
3. Is there a channel to Michael Hla? Four of my open questions have one-minute
   answers if he is willing: what `_det` was testing, why 54 checkpoints are
   unreleased, whether the skipped judging was to save cost, and why the repeat
   runs used a different sample count from the originals.

I have a longer write-up with the full evidence, a five-column tool inventory,
the proposed generation record, and a mapping of each finding onto the sections
of your draft it bears on, mainly 13.3, 13.4 and 11.4. Happy to send it across or
walk through it on the call.

Thanks,
Akshat

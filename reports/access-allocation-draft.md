# ACCESS allocation request: draft text

Request CIS261668. Drafted 26 Aug 2026.

---

## Title

`Can AI Rediscover Physics? Reproducibility Controls for Time-Locked LLM Benchmarks`

---

## Public Overview

Training and evaluating time-locked language models for physics discovery
research with Prof. Brian Keating, UCSD Department of Physics. Testing whether a
model restricted to pre-1900 knowledge can rediscover physics that later won
Nobel Prizes.

**Heavy training.** Continued pretraining and fine-tuning of a 3.3B-parameter
model on a period-restricted physics corpus, to produce a pre-1911 model with the
mathematics general relativity requires. GPU-bound.

**Heavy inference.** Repeated evaluation sweeps across 24 model checkpoints, 8
physics reasoning tasks each, multiple samples per task, under varied sampling
and prompt conditions. Every sweep is thousands of generations, and every sweep
is repeated, because the experiment measures run-to-run variance rather than a
single result. GPU-bound.

**Eval metrics per run.** After every run we compare each answer against the
answers from earlier runs, count how often they match, score all of them, and
track how much the scores move between runs. We also search the model's training
text, billions of words, for anything written after its cutoff that it should
never have seen. CPU-bound.

**Storage.** Model checkpoints, the training corpus during auditing, and a
complete archive of every generation including failures.

---

## Plain prose version, for a form that strips formatting

Training and evaluating time-locked language models for physics discovery
research with Prof. Brian Keating, UCSD Department of Physics. Testing whether a
model restricted to pre-1900 knowledge can rediscover physics that later won
Nobel Prizes.

Heavy training: continued pretraining and fine-tuning of a 3.3B-parameter model
on a period-restricted physics corpus, to produce a pre-1911 model with the
mathematics general relativity requires. GPU-bound.

Heavy inference: repeated evaluation sweeps across 24 model checkpoints, 8
physics reasoning tasks each, multiple samples per task, under varied sampling
and prompt conditions. Every sweep is thousands of generations, and every sweep
is repeated, because the experiment measures run-to-run variance rather than a
single result. GPU-bound.

Eval metrics per run: after every run we compare each answer against the answers
from earlier runs, count how often they match, score all of them, and track how
much the scores move between runs. We also search the model's training text,
billions of words, for anything written after its cutoff that it should never
have seen. CPU-bound.

Storage for model checkpoints, the training corpus during auditing, and a
complete archive of every generation including failures.

---

## Before submitting

1. Confirm the Nobel years: Planck 1918, Einstein 1921, Michelson 1907.
2. The DeepMind wording says "publicly described", which is accurate and claims
   no paper. If a citation is needed, AlphaFold (Jumper et al., *Nature* 596,
   583-589, 2021) is a real one.
3. The pre-1911 training is a later phase, not the current sprint. Keep it or cut
   it, but do not describe it as underway.
4. Delete "GPU cores used for training the model" from the current form. You are
   running models someone else trained.
5. Show Keating first. He is the PI.

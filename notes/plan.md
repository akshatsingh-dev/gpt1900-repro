# Roadmap: 25 Aug to 15 Sep 2026

GPT-1900 reproducibility sprint. Akshat Singh, with Prof. Brian Keating.

---

## The constraint that shapes everything

**8 focused hours a week. Three weeks left. 24 hours total.**

That number does more to determine this plan than anything else. The original
ten-phase plan does not fit in 24 hours and pretending otherwise would produce a
sprint that ends with six things half done.

So this roadmap does three things instead:

1. Ranks the work by how much each item is worth, not by what order it appears in.
2. Names what is deliberately left out, and why.
3. Says what happens when something breaks, because something will.

**The ranking principle:** do the things nobody has done, before the things that
merely need doing again. Two items on this list have never been done by anyone,
and they are both in the first two weeks.

---

## Calendar

| Date | What |
|---|---|
| Wed 26 Aug | First meeting |
| Mon 31 Aug | Written update |
| Tue 1 Sep | Weekly Zoom, 1pm PT |
| Mon 7 Sep | Written update |
| Tue 8 Sep | Weekly Zoom, 1pm PT |
| Mon 14 Sep | Final written update |
| **Tue 15 Sep** | **Final deliverable** |

---

## Week 0, done: 25 Aug

Read the code and the result files. Nothing run.

**Delivered:** upstream pinned at commit `5b489c8c`; a five-column tool
inventory; a 43-field logging record designed; every finding mapped onto the
draft's sections; 25 lab notebook entries with raw output for each.

**Found:** generations do not reproduce, 2 of 120 paired, 1.7 percent, traced to
zero occurrences of a seed and settings dropped at the write on line 609. No
model revision pinned. No repeat run ever judged. 54 of 89 checkpoints
unpublished. 78 percent of published outputs share one opening phrase. 86 percent
of scores are 0 or 1. Prompt wording moves individual task scores by up to 1.3
points.

---

## Week 1: 25 to 31 Aug. Does it run, and is the failure fixable?

**The question this week answers:** is the reproducibility problem bookkeeping,
which is small, or structural, which is not?

| # | Task | Hours |
|---|---|---|
| 1.1 | Install the environment, `uv sync --extra cpu` | 1.0 |
| 1.2 | Load one v11 checkpoint, generate one answer | 1.5 |
| 1.3 | Time it. Decide laptop or Colab for the rest of the sprint | 0.5 |
| 1.4 | One checkpoint, one task, compared against their published output | 1.5 |
| 1.5 | **The determinism test.** Temperature 0, same prompt twice, byte compare | 2.0 |
| 1.6 | Write up, Monday update | 1.5 |
| | **Total** | **8.0** |

### Why 1.5 is the centre of the week

Nobody has run it. One command separates two very different worlds.

- **Identical output:** randomness was the whole story. A seed fixes it, their
  pipeline is sound, and that gets reported in their favour just as loudly as
  anything negative.
- **Still different:** something structural differs, most likely hardware,
  numeric precision, or library versions. That would mean the published results
  cannot be reproduced on any machine but the authors', which is a much larger
  problem and changes the rest of the sprint.

Everything in weeks 2 and 3 assumes an answer to this.

**Week 1 deliverable:** the "runs" column of the tool inventory filled in, and a
determinism verdict.

---

## Week 2: 1 to 7 Sep. The number nobody has computed

**The question this week answers:** the text does not reproduce, but does the
*score*?

That question has been open since the project was published, because no repeat
run was ever judged. It is the single most valuable thing available.

| # | Task | Hours |
|---|---|---|
| 2.1 | Build the logging wrapper implementing the 43-field record | 3.0 |
| 2.2 | Add a seed and a pinned model revision | 1.0 |
| 2.3 | **First judged repeat run.** 3 checkpoints, 8 tasks, 3 samples, scored | 2.5 |
| 2.4 | Compute score reproducibility and within-condition variance | 1.0 |
| 2.5 | Write up, Monday update | 0.5 |
| | **Total** | **8.0** |

### What 2.3 and 2.4 produce

Two numbers that do not currently exist anywhere:

1. **Does the score reproduce**, even though the text does not. Two different
   answers can both score 1 out of 5. It is entirely possible the score is stable
   while the text is not, and that would be a genuinely good result for the
   benchmark.
2. **An error bar on 0.93.** With three samples per cell there is a spread to
   quote. Every number in the project is currently a point estimate with nothing
   around it.

**Blocker to resolve before this week starts:** judging calls the Claude API,
which costs money. Who pays, and is there an existing key. This has to be settled
at the 26 Aug or 1 Sep meeting or week 2 stalls.

**Week 2 deliverable:** working logging, a judged repeat run, and the first score
reproducibility figure anyone has computed.

---

## Week 3: 8 to 14 Sep. Sensitivity, contamination, and the write-up

**The question this week answers:** how much of the score is the prompt and the
corpus rather than the model?

| # | Task | Hours |
|---|---|---|
| 3.1 | Prompt sensitivity, done properly. Three conditions, matched sample counts | 3.0 |
| 3.2 | Targeted contamination probe | 1.5 |
| 3.3 | Evidence table of related vintage-model work | 1.0 |
| 3.4 | Reproducibility memo | 1.5 |
| 3.5 | 15 Sep presentation | 1.0 |
| | **Total** | **8.0** |

### 3.1, what "properly" means

The preliminary comparison from week 0 has two defects: the two conditions used
different sample counts, and only 3 of 24 checkpoints. Doing it properly means
matched sample counts, the same checkpoint set for every condition, and a third
condition that does not currently exist and has to be written: a **deliberately
leading prompt** that gives away part of the answer.

The three conditions then are scaffolded, minimal, and leading. If scores rise
sharply under the leading prompt, the benchmark is partly measuring prompt
engineering.

### 3.2, why targeted rather than a full audit

Auditing an entire pre-1900 corpus does not fit in 1.5 hours. Two specific
queries do, and week 0 identified both:

1. Does `mhla/pre1900-corpus` contain any material dated 1900, and does any of it
   mention Planck? The `uv_catastrophe` task's answer was published in October and
   December 1900, sitting on the stated boundary.
2. What does the corpus contain about Michelson-Morley? That task is the only one
   that never scores 0, and the only one whose underlying 1887 experiment sits
   inside the training data. Two independent oddities on one task.

A negative result here is worth reporting. "I checked and found nothing" is a
real contribution to a contamination discussion.

**Week 3 deliverable:** prompt sensitivity table with denominators, contamination
result, evidence table, memo, presentation.

---

## Explicitly out of scope

Named so nobody assumes they are coming.

| Not doing | Why | What is delivered instead |
|---|---|---|
| Re-running all 24 checkpoints | Compute. Sequential on a laptop is many hours per sweep | 3 checkpoints, denominators stated |
| Executing the blinded physicist review | Needs several physicists' time, which cannot be scheduled inside this sprint | A written protocol they could run |
| Full corpus contamination audit | The corpus is large and a real audit is its own project | Two targeted queries |
| Reproducing the v5 to v8 runs | Those weights were never published | Stated as a limit on the audit |
| The L0, L0.5 and jump-ablation task ladder | That is building a new benchmark, not auditing this one | Noted as follow-on work |

---

## Risks, and what happens when they land

| Risk | Likelihood | Fallback |
|---|---|---|
| Install fails on Apple Silicon | **High.** Research code from April, no GPU | Move to Colab. The failure is itself a reportable finding, precisely documented |
| CPU generation too slow to be usable | **High** | Colab for generation, laptop for analysis. Reported as a constraint, not hidden |
| No API budget for judging | Medium | Week 2 becomes logging plus an unjudged variance run. Flag it immediately, do not go quiet |
| Determinism test comes back structural | Medium | Bigger finding, more valuable, but weeks 2 and 3 get rescoped. Raise it the same day |
| No UCSD compute available | Medium | Everything stays at 3 checkpoints. Denominators reported honestly |
| 8 hours a week turns out optimistic | Medium | Weeks 1 and 2 are the priority. Week 3 items 3.3 and 3.2 are the first to be cut, in that order |

**The rule when one of these lands:** say so in that week's update rather than at
the end. Underpromise, communicate early, never go quiet.

---

## Deliverables by date

| Date | Deliverable |
|---|---|
| 26 Aug | Tool inventory, logging record design, findings from reading the code |
| 31 Aug | Determinism verdict. Local run confirmed or an installation failure documented |
| 7 Sep | Working logging with a seed and a pinned revision. First judged repeat run. Score reproducibility figure |
| 14 Sep | Prompt sensitivity across three conditions. Contamination result. Evidence table |
| **15 Sep** | **Reproducibility memo, judge review protocol, presentation** |

---

## What "done" means on 15 Sep

Not "the benchmark is fixed." Three things:

1. **A defensible number.** Whether the published score reproduces, with a
   denominator and an error bar, computed by someone outside the original
   project. Nobody has this today.
2. **A record-keeping standard.** The generation record, implemented and
   demonstrated on a real run, so future work produces evidence rather than
   anecdotes.
3. **An honest account of what could not be checked**, and why. Unpublished
   checkpoints, compute limits, whatever the install turns up. That section is
   part of the deliverable, not an apology attached to it.

---

## Standing rules

- Archive everything, failures included. Report denominators. No cherry-picking.
- Every finding presented has been personally re-run and verified on this machine.
- Where something is unverified, say so in the same sentence.
- Correct your own claims in writing when they turn out wrong. Four were
  corrected in week 0 and they stay on the record.
- Keating's draft is confidential. It stays out of the repository.
- Never push to upstream. Upstream stays pinned and unedited so that any
  difference in results is attributable to environment rather than local changes.

# GPT-1900 Reproducibility Audit

**Progress update, week 1** · Akshat Singh · 26 August 2026
Evaluated against `github.com/michaelhla/gpt1900` at commit `5b489c8c`

---

## What I did

Read the eval code and result files rather than running them, since running means
pulling a 6.6GB checkpoint and there are 24. Kept a lab notebook of 25 entries
with raw terminal output for each step. Nothing has been run against a model yet.

## Main finding: the generations do not reproduce

The repository has two pairs of runs where the same evaluation was done twice. I
confirmed the prompts were byte-identical, then compared answers.

| Pair | Paired generations | Answers identical |
|---|---|---|
| `v8` vs `v8_det` | 96 | **0** |
| `v11` vs `v11_replication` | 24 | **2** |
| **Combined** | **120** | **2, or 1.7%** |

**The cause:** the eval script never sets a random seed. Zero occurrences in the
file, with sampling on by default at temperature 0.7. Nothing in the repository
can be regenerated, by me or by the authors. The settings are not saved either,
so the archived records cannot explain the difference. The fix looks like about
ten lines at one location, plus pinning the model revision, which is also absent.

## Four other things

**No repeat run was ever judged.** Both repeats used `--skip-judge`, most likely
to save API cost. So no reproducibility figure for the *score* has ever been
computed. Two different answers can both score 1 out of 5, and it is entirely
possible the score is stable even though the text is not. Nobody has checked.

**No error bar on 0.93.** Each of the 192 scores is a single draw. The pipeline
supports three samples per prompt by default; the published run used one.

**86 percent of scores are 0 or 1.** A 5 never occurs, and four of the eight
tasks only ever score 0 or 1. The rubric has little resolution here. It does
detect real improvement across training, 0.62 to 1.11 from the first to the last
eight checkpoints.

**78 percent of published answers open with the same phrase.** Since the judge is
a language model reading free text, this raises a question about whether the score
partly tracks period register rather than physics. Unchecked, and checkable.

## A limit on my own finding

The 0-of-96 comes from the v8 pair, whose weights were never published, so it is
evidence about their saved files rather than a reproduction anyone could repeat.
54 of 89 checkpoints are unpublished. The v11 family is public and is what the
192 published scores come from, so that is where my own run will go.

Worth crediting: the pipeline saves after every checkpoint and deletes each model
after use, which is what makes a full sweep possible on a laptop.

## Plan to 15 September

Eight focused hours a week, so 24 hours remain. Ranked by what has never been
done rather than by sequence.

| Week | Focus | Deliverable |
|---|---|---|
| 25–31 Aug | Install, first local generation, determinism test at temperature 0 | Whether the failure is bookkeeping or structural |
| 1–7 Sep | Implement the generation record, run the first judged repeat | Whether the score reproduces, and an error bar on 0.93 |
| 8–14 Sep | Prompt sensitivity, targeted contamination probe, evidence table | Sensitivity table with denominators |
| 15 Sep | Reproducibility memo, judge review protocol, presentation | Final |

Out of scope, so it is not assumed: re-running all 24 checkpoints, a full corpus
audit, reproducing v5 through v8, and executing the blinded physicist review, for
which I will deliver a protocol rather than results.

## Three asks

1. **Compute.** Is there UCSD hardware I could use? A GPU would turn the
   checkpoint sweep into something that runs overnight.
2. **API budget.** Judging costs money and week 2 depends on it. Existing key, or
   a budget to work within?
3. **A channel to Michael Hla.** Four questions have one-minute answers: what
   `_det` was testing, why 54 checkpoints are unreleased, whether the skipped
   judging was cost, and why the repeats used a different sample count.

Fuller write-up available on request: tool inventory, the proposed generation
record, and a mapping of each finding onto sections 13.3, 13.4 and 11.4.

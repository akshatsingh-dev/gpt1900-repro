# Decisions

One entry per choice that a reviewer could reasonably have made differently.
The purpose is that when Keating or a referee asks "why did you do it that
way", the answer already exists in writing and was written before the result
was known, not after.

Format: what was decided, why, what was rejected, and what would change it.

---

## D001 - Work inside the existing `Projects` git repo, with weights gitignored

**Decided:** the sprint lives at `Projects/gpt1900-repro/`, tracked by the
`Projects` repo, with checkpoints and the upstream clone excluded.

**Why:** the work is versioned automatically alongside everything else, and a
single history makes the sprint auditable.

**Rejected:** a standalone repo outside `Projects`. Cleaner isolation, but a
second repo to remember to commit, and the record-keeping matters more than
the isolation here.

**What would change it:** if checkpoints ever need to be tracked, or if the
work has to be shared without sharing the rest of `Projects`.

## D002 - Full clone of upstream, not shallow

**Decided:** `git clone` without `--depth 1`.

**Why:** the sprint's first deliverable is provenance. A shallow clone gives
the files but not the history, so results cannot be pinned to a commit that
can be walked back to.

**Rejected:** shallow clone. Faster, and the repo is small enough that the
saving is irrelevant.

**What would change it:** nothing foreseeable at this size.

## D003 - Upstream code is read and wrapped, not edited

**Decided:** `upstream/gpt1900` stays at a pinned commit and is not modified.
Anything new goes in `tools/` and calls into it.

**Why:** a reproduction that required edits to the thing being reproduced is
not a reproduction. Keeping upstream pristine means any difference in results
is attributable to environment or sampling, not to changes made here.

**Rejected:** patching the eval script directly to add logging. Faster to
write, but it destroys the ability to say "this is what upstream does".

**What would change it:** if upstream turns out not to run at all without a
patch. In that case the patch gets its own entry, a diff archived in
`evidence/`, and both the patched and unpatched behaviour reported.

## D004 - One sample per engine call, not a batch

**Decided:** `tools/logged_eval.py` calls the engine with `num_samples=1` and
loops, rather than asking for N samples in one call as upstream does.

**Why:** the engine shares one `torch.Generator` across every row of a batch
(E026). The random draws a given row sees therefore depend on the batch size,
so sample 0 of a one-sample run and sample 0 of a three-sample run are not the
same object even at the same seed. Upstream's two reproduction pairs used
mismatched `--num-samples`, which alone guarantees they could never match.
Generating one at a time makes a record comparable to any other record with the
same seed, independent of how many samples the run asked for.

**Rejected:** batching and recording the batch size, then only comparing runs
with matching batch sizes. Cheaper to run, but it preserves a coupling that has
already destroyed one reproduction attempt, and it makes the archive's
comparability conditional on a field a reader has to remember to check.

**Cost:** the prompt prefill is recomputed once per sample instead of once per
task. At 8 tasks and 3 samples that is 16 extra prefills per checkpoint. On CPU
this is real but small next to decode.

**What would change it:** if profiling on Expanse shows prefill dominating,
batching could return for runs where sample count is held fixed across the whole
experiment and recorded. The determinism work must stay unbatched regardless.

## D005 - Seed 42, temperature 0.7, one sample: reproduce their settings, not ours

**Decided:** every run meant to be set beside a published number uses the
engine default seed 42, temperature 0.7, top_k 50, `--num-samples 1`, the
values upstream's v11 sweep actually ran with (E026, E022).

**Why:** the question is whether *their* result reproduces. A run at our own
preferred settings answers a different question. With D004 (one sample per
engine call) the seed-42 draw sequence for sample 0 is the same one their
one-sample run saw, so a byte match is possible in principle and its absence
is informative.

**Rejected:** temperature 0 for the sweep. It gives cleaner determinism but is
not what was published, and E032 already settled the determinism question.

**What would change it:** evidence that upstream's v11 run used a seed other
than 42, which would require a change to the engine that the pinned commit
does not contain.

## D006 - The judge is pinned, cooled, and its failures are null

**Decided:** `tools/judge.py` defaults to upstream's judge model id
`claude-sonnet-4-20250514`, sets temperature 0, records the model version the
API actually answered with, the prompt hash and the raw response, and writes
`score: null` with the error text when a call or parse fails.

**Why:** reproducing their score means using their grader. Their code sets no
temperature, so the API default applied and nothing recorded it; a grader that
samples adds variance to the measurement itself. Their failure path writes 0,
which is indistinguishable from a real 0 and silently lowers the mean.

**Rejected:** the current default model. Better grader, wrong experiment. It
is one flag away (`--model`) for a judge-sensitivity comparison later.

**What would change it:** the deprecated model being retired. Then the memo
says so, the newest model is used, and the two are compared on a shared file.

## D007 - The leading prompt is generated, not written by hand

**Decided:** `tools/EVAL_leading.json` is produced by
`tools/make_leading_config.py` from upstream's `EVAL.json`. One hint paragraph
is appended after each task's question. Every other field, including the
rubric and expected concepts the judge sees, is byte-identical to the original.

**Why:** the sensitivity experiment attributes score differences to the prompt
the model saw. If the judge's instructions also differed between conditions,
that attribution would fail. Generating the file makes the invariant checkable
by a script rather than by trust.

**Rejected:** rewriting the whole prompt to lead. More natural reading, but
then the question wording changes too and two things move at once.

**What would change it:** nothing foreseeable; a stronger or weaker hint is a
one-line edit to the `HINTS` table with the derivation recorded.

## D008 - Provisional scores from a blinded reader, labelled as such

**Decided:** with no API access, answers are graded through the blinded
packet: `blind_packet.py --batches 24` strips every provenance field and
shuffles with a recorded seed; each batch of 24 is graded in a fresh session
by a Claude model (claude-fable-5-1) that sees only the id, the prompt, the
rubric and the answer; `judge_import.py` maps the grades back through the
sealed key and writes them into the judge fields with `judge_model` naming
the grader, `judge_temperature` null, and the grader's own JSON stored as
`judge_raw_response`. Two batches are graded twice by independent sessions
for a reliability figure.

**Why:** the rubric, the blinding and the record are the same as an API
pass. What differs is the grader model and the absence of a temperature
setting, and both are written down. The memo calls these scores provisional
and says the upstream judge, `claude-sonnet-4-20250514` at temperature 0,
should replace them when a key exists. That keeps every number checkable
against an archived rationale and keeps the comparison to the published 0.93
honest: same rubric, different Claude.

**Rejected:** grading in a session that has already seen the hypotheses and
the provenance. The grader would know which answers came from the leading
prompt and what result would be convenient. Fresh sessions per batch remove
that. Also
rejected: presenting no scores at all. The sensitivity experiment is worth
little without them, and a labelled provisional score beats a blank.

**What would change it:** an API key. The API pass replaces these files and
the report then shows both graders side by side, which is itself a judge
sensitivity result.

## D009 - The abduction suite is read blind against per-prompt verdict ladders, not graded on the rubric

**Decided:** the professor's broken-cable elevator, the assistance ladder on
the 1907 observation, and the reasoning-type controls are scored by blind
readers choosing one verdict from a ladder fixed in advance for each prompt
(`tools/EVAL_abduction.json`, fields `expected`, `verdicts`,
`verdict_help`), not by the 0 to 5 rubric.

**Why:** these prompts have no published score, and the question is not
"how good is the answer" but "which idea did the model supply on its own".
A ladder with a named rung for the observation (`weightless`) and a named
rung for the jump (`equivalence`) answers that directly. Fixing the ladders
before the run keeps the reading from bending toward the result.

**Rejected:** rubric grading (measures polish, not the step); keyword
counting alone (E047 showed 7 of 7 keyword hits were false positives).

**What would change it:** a second reader disagreeing on more than a few
items, in which case the ladder wording gets tightened and both readings
are reported.

## D010 - A third reader through the OpenAI Decisions API, typed answers only

**Decided:** every blind-read answer (abduction suite, elevator final) and
every rubric-graded answer (sweep, sensitivity) gets a second machine reading
through the OpenAI Decisions API (`POST /v1/decisions`, model `gpt-6-luna`),
via `tools/decide.py`. For the ladders it is a `choice` question whose
options are the verdict rungs from the eval config, with their descriptions
verbatim. For the rubric it is a `score` question whose levels are the
authors' 0 to 5 rubric, verbatim. The API returns a label or score plus a
probability for every option; both are kept. Agreement with the blind
reading is reported by `tools/decide_compare.py`, exact match overall, per
prompt, and a confusion table. The API sees only the prompt, the expected
answer and the text, never the checkpoint or seed.

**Why:** the blind readings so far come from one vendor's model. A second
vendor, a different model family, and a classifier that cannot write prose
is as independent a second reading as can be had without a physicist. It
returns probabilities, so the shaky calls (the not-a-force by negation
cases, the one thin pendulum correct) show up as low confidence rather than
as a bare label. Cost is about three cents per 260 answers, so every run can
be read, not a sample.

**Rejected:** using it as the only reader (it is a classifier, no reasoning
trace, cannot explain a call); using it to reproduce the published 0.93 (it
is not the authors' judge either, that still needs the Claude key).

**Thresholds, written before any result is seen:** on the abduction ladders,
exact agreement at or above the regrade rate already measured for the same
kind of prompt (35 to 38 of 48 on the hard ladders, 44 to 45 of 48 on the
plain ones) means the two readings corroborate each other and both are
reported. Below that, every disagreement is listed and the ladder wording is
tightened before any number goes in the paper. On the rubric, the API score
is reported beside the Claude score and the published score as a third
column; it is never averaged in.

**Disclosure:** named in Methods beside the Claude reader, per the APS
AI-use policy.

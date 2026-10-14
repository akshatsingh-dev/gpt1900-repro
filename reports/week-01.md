# Week 1: 25 Aug - 31 Aug 2026

Status: in progress. Compiled from `notes/lab-notebook.md` entries E001 onward.

## Planned for this week

Phases 0 to 4 of `notes/plan.md`.

1. Workspace and provenance, upstream pinned to a commit.
2. Tool inventory: every script, with exists / runs / reproduces / what it logs / gaps.
3. Environment and smoke test: one checkpoint loading and generating on Apple Silicon.
4. Minimal reproduction: one checkpoint, one task, diffed against published outputs.
5. Determinism test at temperature 0.0.

## Done so far

- Workspace, gitignore and provenance tooling built. E001 to E004.

## Findings

All measured on this machine from the repository at commit `5b489c8c`. Raw
terminal output for every one is in `logs/`.

**Generations do not reproduce: 2 of 120 paired answers, 1.7 percent.**
Two independent pairs. `physics_eval_v8` against `physics_eval_v8_det`, same 12
checkpoints, prompts identical in 96 of 96, answers identical in **0 of 96**.
`physics_eval_v11` against `physics_eval_v11_replication`, prompts identical in
24 of 24, answers identical in **2 of 24**. Both re-tested allowing a match
against any stored sample rather than only the first; neither figure moved.
[E014, E021, E022]

**The mechanism, confirmed at source.** `scripts/physics_eval.py` contains zero
occurrences of `seed`. Sampling is on by default at temperature 0.7, top_k 50.
The results file is written at line 609 and the sampling parameters, in scope
three lines above, are not included. The download call contains zero occurrences
of `revision`, so weights are fetched by mutable name. [E016, E017, E018, E020]

**No repeat run has ever been graded.** Both repeats used the documented
`--skip-judge` flag, most plausibly to save API cost. Consequently no
reproducibility figure for the score itself has ever been computed upstream.
[E016]

**Neither pair is strictly like-for-like.** In both cases the run and its repeat
used different `--num-samples` values, detectable only by counting entries in the
output files. [E022]

**54 of 89 registry checkpoints, 61 percent, are marked `"local"` and were never
published**, including every v8 checkpoint. The 0-of-96 result is therefore
evidence about upstream's saved artefacts rather than an independently
repeatable reproduction, and must be reported as such. Of the 35 published
checkpoints, 24 belong to the v11 family, and 24 checkpoints across 8 tasks is
192, exactly the number of judged scores in the published run. The published
result rests on obtainable weights, so v11 is the correct target for local
reproduction. [E020]

**150 of 192 published outputs, 78 percent, open with the identical phrase "You
have touched".** In the three replicated checkpoints it is 95 of 96. In the
older completion-mode run it is 0 of 288. This inflates prefix-similarity
measures and raises an open, checkable question about whether an LLM judge
scoring free text is partly tracking stylistic register. No claim is made that
it is. [E023]

**Two of the eight tasks sit on or inside the training boundary.**
`uv_catastrophe` targets Planck's law, published October and December 1900.
`sr_michelson_morley` refers to an 1887 experiment already inside the corpus.
[E011]

**Practices worth crediting.** Results are written after each checkpoint for
crash resilience, and each downloaded checkpoint is deleted once evaluated. The
download is filtered with `allow_patterns` to one step's weights. Peak disk is
one checkpoint, which resolves the disk constraint flagged at the start of the
week. [E018, E020]

## Corrections made during the week

Three claims were revised after further checking, and are recorded rather than
quietly dropped. A suspected prompt-mode mismatch in the v8 run was checked and
disproved. An inference that all runs stored one sample per task was drawn from
one file and generalised without warrant; two of four store three. A 904-
character mean shared prefix was initially read as near-determinism and is
better explained by the stereotyped opening above. [E020, E022, E023]

## Not done this week

Nothing has been run against a model. No install, no generation. Every finding
above comes from reading artefacts and source already in the repository. The
vintage-model survey, Typewriter-1913-7B and awesome-vintage-llms, has not been
started, and the findings have not been mapped onto Sections 11 and 13 of the
draft.

## Problems and risks

- 31GB free disk against 24 checkpoints at roughly 6.6GB each. Checkpoints must
  be pulled one at a time and deleted. Recorded before any download.
- 18GB RAM, no GPU. Whether a 3.29B model generates at usable speed on this
  machine is untested. If it does not, phases 3 and 4 move to Colab and that
  becomes a reported constraint on the reproduction rather than a silent
  workaround.

## Next week

To be filled at end of week.

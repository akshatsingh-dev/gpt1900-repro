# The abduction suite: what runs tonight and why

Written 7 Oct 2026, before the results, so the reading rules are fixed in
advance. Jobs 54719457 (elevfinal) and 54719458 (abduction) on Expanse.

## The two tests, and whether they are the same

**The Einstein test** (Keating's framing) is the whole arc: can a model
restricted to pre-breakthrough knowledge reconstruct the reasoning behind a
breakthrough rather than retrieve it. Five stages in the draft: notice the
anomaly, question the assumption, propose the new principle, derive its
consequences, check them against observation.

**The elevator test** is the entry point to that arc for general relativity.
Einstein's 1907 "happiest thought": a man falling from a roof does not feel
his own weight. The professor's phrasing: an elevator whose cable breaks,
what would it feel like. The step that makes it a breakthrough is the next
one: weightlessness in free fall means gravity and acceleration are the same
thing seen from inside, so gravity can be made to vanish by motion and is
not an ordinary force. Everything in general relativity grows from that.

So they are not the same. The elevator is stage one and two of the Einstein
test, applied to one breakthrough. Upstream's benchmark has two elevator-
shaped tasks: `gr_free_fall_equivalence` (the 1907 seed) and
`gr_main_elevator_light` (the 1911 consequence, light bending). The
professor's test is the first. We have both at n=72 already (E045, E047).
What we did not have is his exact wording, and a controlled test of whether
the failure is specific to abduction.

## Why abduction

"LLMs can't jump" (Zahavy, DeepMind, 2026) says language models do deduction
(rule to conclusion) and induction (examples to pattern) but not abduction
(inventing a new premise that explains a surprising fact), and that the
elevator is the canonical case. E047 already measured the jump at 0 of 144
on the 1907 observation. Tonight adds the controls that make that a claim
about abduction rather than about the model being weak at everything.

## The three groups

**final** (the professor's words, four phrasings). "You are in an elevator,
the cable breaks, what do you feel"; the same plus "what does this tell us
about gravity"; a man lets go of a stone; a man stands on a scale. Verdict
ladder: wrong, none, weightless, equivalence, not-a-force, geometry.
`weightless` means the model gets the observation right (no weight, stone
floats, scale reads nothing). `equivalence` means it supplies the idea the
prompt withheld. The run across all 24 checkpoints uses the second phrasing,
three seeds each, plus the base model.

**ladder** (how much help is needed). The 1907 observation plus one of:
"something in our understanding of gravity must be mistaken, what"; a
carriage pulled with ever increasing speed whose passenger is pressed back
("what do the two cases have in common", acceleration given without the
word equivalence); "no experiment inside the cabin reveals gravity, what
follows". Together with E047's bare and seed forms (no help) and the
scaffolded and leading forms (most help), this gives a dose curve: at which
rung of assistance does the equivalence first appear.

**control** (the reasoning-type comparison). Two deductions inside the
corpus (stone dropped from a ship's mast lands at the foot of the mast; two
stones of different weight fall together). One induction inside the corpus
(pendulum period from four data points goes as the square root of length).
One abduction inside the corpus (Uranus wanders, an unseen planet explains
it: the 1846 Neptune argument, which the model has read). Two abductions
beyond the corpus (Michelson-Morley null result without the aether framing;
the black-body peak without Planck's name). Verdicts: correct, partial,
wrong, none.

## What each outcome would mean

- Controls correct, abductions beyond the corpus none: the gap is specific to
  inventing a premise the corpus lacks. Supports the "can't jump" reading.
- Controls also fail: the model is weak at reasoning generally and the 1907
  result says less about abduction in particular.
- Uranus correct but Michelson-Morley and black body none: it can reproduce
  an abduction it has read and cannot make one it has not. The cleanest
  version of the claim.
- Ladder: the lowest rung at which equivalence appears is the amount of the
  answer the prompt has to contain before the model produces it.
- Final: the fraction of 72 answers across training that reach
  `weightless` versus `equivalence`. The professor's test, in his words,
  with a denominator.

## Reading

All answers read blind: shuffled, R-ids, prompt plus expected answer plus the
item's own verdict list, fresh-session readers, merged back through a key.
No rubric grading; these prompts have no published scores to compare to.
Checkpoints: base `d34-22btok` (completion mode) and v11 s035, s560, s839
(chat mode), five seeds, as in E046; the mode difference is recorded, not
removed. Temperature 0.7, top_k 50, max 768 tokens.

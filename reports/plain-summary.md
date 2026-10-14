# What was done, in plain words

Updated 22 Sep 2026.

## The setup

GPT-1900 is a language model that only ever read text written before 1900.
The idea is to ask it physics questions whose answers were discovered after
1900, and see whether it can reason its way there. Its makers scored it 0.93
out of 5 on eight such questions, with Claude doing the grading.

My job: find out whether that score can be trusted, and build the tools so
that anyone can check it.

## What "reproduce" means here

Run the same test again and see if you get the same thing. Two levels:

- Same words. Ask the model the same question with the same settings, get
  the same answer, letter for letter.
- Same score. Grade the answers again, get the same number.

Their own repeat runs failed the first level 118 times out of 120. Nobody
had tried the second level.

## Why their repeats failed

A model picks each word by rolling weighted dice. The dice are fake: they
start from a number called the seed, and the same seed gives the same rolls.
Their code used seed 42 without anyone choosing it and never wrote it down.
Their repeat asked for three answers per question instead of one, and the
rolls get dealt across the three, so answer one of a three-batch sees
different rolls than answer one of a one-batch. Same seed, different words.

Nothing to do with the model. Two fields missing from a log file.

## What I ran

1. Randomness off, twice. 8 of 8 answers identical.
2. Their settings, randomness on with seed 42, twice. 8 of 8 identical.
   Also with the GPU forced to add numbers in a fixed order: 8 of 8.
3. All 24 saved versions of the model, 8 questions each, their settings.
   192 answers. Every answer saved with 50 pieces of information about how
   it was made.
4. Three wordings of each question on three model versions, three tries
   each. 216 answers. Normal, stripped down, and one with a hint that gives
   the answer away.
5. Sixteen half-sentences for the model to finish, half about post-1900
   physics it should not know, half about pre-1900 physics it should know.
6. A search of the 56 GB it was trained on for words like photon and
   Einstein and for any document dated 1900 or later.

## What came out

- The model is repeatable when you write down the seed. Their failure was
  bookkeeping.
- Every single answer in the sensitivity run, 216 of 216, starts with the
  same sentence no matter how the question is worded. The model learned a
  voice.
- It knows nothing about post-1900 physics. A photon is "a piece of paper or
  cloth". But it cannot describe Thomson's electron or the Michelson-Morley
  experiment either, both of which are in its training data. So the clean
  result is weaker than it looks.
- Scores, graded blind by a Claude model with their rubric because no API
  key was available: hint version 1.64, normal 1.36, stripped 1.22, out of 5.
  The hint is worth about 0.3 points on a benchmark whose published score is
  0.93. Grading the same 48 answers twice gave the same number 44 times.
- Searching all 2 million training documents: none dated 1900 or later,
  zero mentions of photon, spacetime or Einstein. One document dated 1829
  describes a 1908 Nobel Prize, so the date filter has at least one hole.
- The API judge the paper used should replace the provisional grades once
  a key exists. Twenty minutes, under three dollars.

## What the tools do

- logged_eval.py: runs the model and writes one line per answer with
  everything about how it was made.
- compare_runs.py: checks whether two runs match, and refuses to give a
  number if the settings differ.
- judge.py: sends answers to Claude with their rubric, records which model
  graded, at what temperature, with what prompt, and writes a failure as
  "no score" instead of zero.
- report.py: averages with error bars, per question, per model version, per
  wording, next to their published number.
- blind_packet.py: shuffles answers into a document physicists can grade
  without knowing where each one came from.
- probe_report.py and corpus_search.py: the two contamination checks.

## What is left

Grading, once a key exists. Then the memo. Then the blinded review with real
physicists, which needs their time.

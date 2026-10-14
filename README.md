# GPT-1900, checked

Can anyone else reproduce the published score of GPT-1900, and what does that score measure?

[GPT-1900](https://github.com/michaelhla/gpt1900) is a 3.29B language model trained only on text written before 1900. Its authors asked it eight physics questions whose answers were found after 1900, had a Claude model grade each answer 0 to 5 against a rubric, and published a mean of 0.93. This repo re-runs that evaluation on SDSC Expanse, records everything the original pipeline did not (seed, temperature, top_k, sample count, model revision, hardware, grader), and tests what the number is sensitive to.

Work by Akshat Singh, UC San Diego, with Prof. Brian Keating. August to October 2026.

## What came out

- **The text reproduces.** Same checkpoint, same settings, run twice: 8 of 8 answers identical, at temperature 0 and at the authors' sampled settings. Their own repeats matched 2 of 120 times because the seed and the sample count were never recorded.
- **Not across machines.** V100 (emulated bfloat16) against CPU (float32): 0 of 8 identical. Same for 35 to 142 words, then one rounding flip and the rest diverges. Each machine repeats itself.
- **The score depends on the grader.** All 192 answers regenerated and graded: 1.27. The authors' own 192 answers under the same grader: 1.26. Under their grader: 0.93. The model reproduces to 0.01; the number moves 0.33 with the grader.
- **A hint beats training.** One paragraph that restates the rubric's top answer lifts the elevator task +0.89. The whole training run lifts the mean about +0.5.
- **The model never makes Einstein's 1907 jump.** 0 of 144 given the observation alone, 0 of 140 across four wordings and a ladder of help. It also fails Galileo's ship and the two falling stones, so it cannot tell us whether the jump is the hard part.
- **The training data is clean for post-1900 physics.** 2,074,160 documents: zero mention Einstein, photon, photoelectric or spacetime. One misdated 1909 document, so the date filter has at least one hole.

Scores so far come from a blinded reading by Claude Fable 5.1 applying the authors' rubric, not from the authors' judge model. They are labelled provisional everywhere until that pass is run.

## Read

- `reports/results-overview.html`: every result on one page, with a glossary.
- `notes/lab-notebook.md`: every step, E001 onward. Numbers in the reports cite these.
- `notes/decisions.md`: why each choice was made, written before the result.
- `notes/where-we-are.md`: status and what is open.
- `reports/reproducibility-memo.md`: the long form.
- `evidence/<experiment>/`: raw answers (`.jsonl`), graded answers, an html page per run, logs.

## Run

Needs a GPU (a V100 with 32 GB was enough), Python 3.12, and the authors' code cloned at the pinned commit:

```
git clone https://github.com/michaelhla/gpt1900 upstream/gpt1900
git -C upstream/gpt1900 checkout 5b489c8c
pip install -r requirements.txt
python tools/logged_eval.py --help
```

`notes/runbook.md` has every experiment as one command with what to expect. Slurm scripts for Expanse are in `tools/run_*.sh`. The authors' code is never edited; everything here sits beside it.

## Open

The pass with the authors' judge model (`tools/judge.py`, needs an API key). Physicist grading of the sealed packets in `evidence/review-packet-*`. A second machine reader (`tools/decide.py`). See `notes/where-we-are.md`.

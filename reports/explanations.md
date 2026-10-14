# Explanations

Plain-language version of everything in `reports/meeting-1notes.md`.

Read them side by side. Section numbers match. When the brief says "Problem 4",
scroll to "Problem 4" here for the version with no jargon in it.

---

## First, the one idea everything rests on

**Reproduce means: do it again, get the same thing.**

They ran the physics test. Then they ran the exact same test again. I compared
the two runs answer by answer.

**120 pairs. 2 came out the same. 118 were different.**

Same questions. Same model. Different answers.

## Why that happened, in one picture

When the model writes, it does not pick one word. It makes a list with odds on
it:

```
"the"    40%
"a"      25%
"this"   10%
...
```

Then it **rolls a dice** to choose.

Every dice roll has a starting number, called a **seed**. Write the seed down
and you can replay the exact same rolls forever. Do not write it down and you
can never get them back.

I searched their entire program for the word "seed". **It appears zero times.**

So every run is a fresh set of dice rolls that nobody recorded. The answers could
not have come out the same. It was never possible.

## The card shuffle version

Shuffle a deck, deal five cards, write down the hand. Shuffle again, deal five
more. Different hand, obviously.

Unless you wrote down exactly how you shuffled. Then anyone can get your hand
back.

They did not write down the shuffle.

## Why that breaks the paper

Their headline number is **0.93 out of 5**. That came from one set of answers.
One shuffle.

Run it again, you get different answers. Different answers might score
differently. Maybe 0.93 again, maybe 1.4, maybe 0.5.

**Nobody knows, because nobody ever graded a second run.** They generated one
and stopped.

So the number in the paper is one roll of a dice, and there is no way to find out
whether it was a lucky roll or a typical one.

---

# Now, problem by problem

Matching the numbering in `reports/meeting-1notes.md`.

## Problem 1: There is no seed

**Simple version.** See above. No seed means no replay. Ever. By anyone,
including them.

**The number.** Zero occurrences of "seed" in their evaluation script.

**Common confusion.** Randomness itself is not the problem. Randomness is normal
and useful, it is what makes the model write varied text instead of the same
sentence forever. The problem is randomness *without a recorded starting point*.
With a seed you get variety **and** repeatability at the same time. You lose
nothing by fixing this.

## Problem 2: The results do not repeat, measured

**Simple version.** I did not take anyone's word for it. I opened their result
files and compared them myself.

| What I compared | Same | Total |
|---|---|---|
| `v8` against `v8_det` | 0 | 96 |
| `v11` against `v11_replication` | 2 | 24 |
| **Together** | **2** | **120** |

**Why I checked the questions first.** Before comparing answers I checked
whether both runs had been asked the identical questions. All 120 were identical.
That matters, because if the questions differed the whole comparison would be
meaningless. You would be measuring two different tests, not one test twice.

**Why two pairs and not one.** One pair could be a fluke, a badly configured
run, a mistake. Two separate pairs behaving the same way is a property of the
system.

## Problem 3: The settings were never saved

**Simple version.** For every answer they saved three things: the question, a
word called `mode`, and the answer. They never saved the settings that produced
it.

**The analogy.** A recipe card that says "baked" with no oven temperature and no
time. You have the cake. You cannot make it again.

**The part that makes it fixable.** Line 609 of their program is where the
answers get written to disk. The settings are sitting three lines above it,
being used. They are not far away or hard to reach. They are just left out of
the box.

So the fix is not "rebuild the pipeline". It is roughly ten lines at one known
location.

## Problem 4: They do not record which model they used

**Simple version.** Model files live online at an address, like a web page. Their
program asks for the address and takes whatever is there right now.

But those addresses can be updated. The owner can replace the file and keep the
same address.

**The analogy.** Citing a website by URL with no date. You wrote "see this page
for the data". A year later the page says something else. Your citation now
points at the wrong thing, and nothing about your citation shows that.

**Why it sits above the seed problem.** The seed decides *which answer you draw*.
The version decides *which model draws it*. Fix the seed and not the version and
you still cannot say what you ran.

## Problem 5: No repeat run was ever graded

**Simple version.** Their pipeline has two stages.

```
Stage 1: model writes the answers      -> saves generations.json
Stage 2: Claude grades them 0 to 5     -> saves results_judged.json + summary.txt
```

Both original runs did both stages. **Both repeat runs stopped after stage 1.**

**Why, most likely.** There is a built-in `--skip-judge` switch. Grading sends
every answer to a paid service. Skipping it on a test run you are not going to
publish is completely normal engineering, and I think that is what happened.

**Why it still matters.** Whatever the reason, the effect is that nobody has ever
computed whether the *score* repeats, only whether the *answers* repeat. Those
are different questions and the second one is the one the paper needs.

**Why to ask rather than accuse.** You cannot read intent out of a file. Only the
person who ran it knows. If you assume the worst and you are wrong, you have
burned a source you need for three more weeks.

## Problem 6: The repeat runs were set up differently from the originals

**Simple version.** Their program can ask each question more than once. In both
pairs, the original and its repeat used a different number of tries.

- `v11` asked once. Its repeat asked three times.
- `v8` asked three times. Its repeat asked once.

**Why that is a problem.** A proper repeat holds everything fixed except the one
thing you are testing. Here something else moved too.

**What I did about it.** I gave the repeats the benefit of the doubt. Instead of
comparing only the first try, I checked whether **any** of the three tries
matched. The numbers did not move: still 0 of 96, still 2 of 24.

That matters for how you present it. You tested it in the direction that could
have weakened your own finding, and it survived. Say that out loud.

## Problem 7: 54 of 89 models were never released

**Simple version.** Their list has 89 saved models on it. 54 of them are marked
"local", meaning they only exist on the author's own computer.

**Why this cuts against your best number.** Your strongest result, 0 out of 96,
came from the v8 pair. Those weights are among the unreleased ones. So you can
show their two saved runs disagree, but nobody can download the model and re-run
either side to check. Including you.

That does not make it wrong. It changes what kind of claim it is. It is evidence
about their files, not a reproduction anyone can repeat.

**Say it before they do.** Finding the hole in your own result and naming it
first is the single most credible thing you can do in that room.

**The good news hiding in the same fact.** 24 of the 35 released models are the
v11 family. 24 models times 8 questions is 192, which is exactly the number of
graded scores in the published run.

**So the published result uses models anyone can download.** That is where your
own run should go, and that is the change to the plan.

## Problem 8: Most answers start with the same phrase

**Simple version.** I read the actual answers instead of only counting them.

**150 of 192 published answers, 78 percent, begin with "You have touched..."**

In the three models that were repeated it is 95 of 96, 98 percent. In the older
run, which prompted the model differently, it is 0 of 288.

**Why it matters, part one.** I had measured how far two answers agree before
splitting. For the v11 pair it was about 900 characters, which looks like the
answers are nearly identical. They are not. They are agreeing on a stock opening
before saying different things. The statistic was misleading and only reading the
text revealed it.

**Why it matters, part two, and this is the one for the physicists.** The grader
is an AI reading free text. If most answers open in the same confident
old-fashioned voice, it is fair to ask whether the score partly reflects *how it
sounds* rather than *whether the physics is right*.

Be careful here. You are **not** claiming the grader is fooled. You are saying
nobody has checked, and it is checkable. That is what a blind review by real
physicists would settle.

## Problem 9: Two questions sit on the training boundary

**Simple version.** The model was supposedly trained only on writing from before
1900.

- **`uv_catastrophe`** asks about blackbody radiation. The answer is Planck's
  law, published in **October and December 1900**. That is on the line, not past
  it.
- **`sr_michelson_morley`** refers to an experiment from **1887**. That is inside
  the training data. The model has almost certainly read about it. Only the 1905
  explanation is outside.

**Why it matters.** Six of the eight questions are clean tests. Those two are
testing something different and probably should not be averaged in with the rest
without a note.

**Why it is useful rather than just a complaint.** It turns a vague worry
("maybe the training data leaked") into one specific thing you can go check: does
the corpus contain anything dated 1900, and does any of it mention Planck.

## Problem 10: The grader is not pinned either

**Simple version.** The scores come from the Claude API, which is a service that
gets updated over time. No grader version is recorded anywhere.

So you could freeze the answers perfectly, re-grade them in six months, and get
different scores because the grader changed underneath you.

There is also only one grader and no human check, so there is no way to tell a
real change from the grader drifting.

**The framing to use.** Treat the grader as a piece of measuring equipment. You
would record the serial number and calibration date of an instrument in a physics
lab. Same idea.

Put it as a question, not a verdict. That room knows more about measurement than
you do, and asking gets you a better answer than asserting.

---

# The three things you got wrong, and why saying so helps

## The mode mismatch

You suspected the v8 run had prompted the model in a format it was not trained
for. That would have been serious. You checked. It had not. Withdrawn.

## The sample counts

You said every run saved one answer per question. Two of the four save three.
You found this by reading a file they wrote themselves, then redid your headline
comparison to account for it. The result held.

## The 900-character agreement

You read a long shared opening as evidence the runs were nearly identical. It was
a stock phrase. Reading the text corrected a statistic.

**Why you should say all three out loud.** A review nobody corrects is not a
review, it is an accusation with numbers attached. Showing that you checked your
own claims and dropped one is what makes the other nine believable.

---

# The whole thing in five sentences

They built a test where the model rolls a dice for every word, and never wrote
down the dice.

So the answers cannot be regenerated by anyone, and I measured that: 2 matches
out of 120.

The settings that would explain it were never saved, and they are sitting three
lines above the line that saves the file.

Their published score of 0.93 comes from one unrepeatable draw, and no repeat run
was ever graded, so nobody knows if it holds.

None of this says the model is bad at physics, and all of it is about a day of
work to fix.

# Update, 15 Sep 2026: the sampling result, in plain words

Lab notebook entry E035. Evidence in `evidence/sampling/`. Slurm job 54315364.

## What was run

One checkpoint (s560, the model's saved state at training step 560), the 8
physics questions, at the settings the paper used: temperature 0.7, top_k 50,
seed 42, one sample per question. Run twice, a and b. Then twice more with
PyTorch's deterministic mode switched on, c and d.

## The terms

- **Temperature.** How random the word choice is. 0 means always the most
  likely word. 0.7 means usually the most likely, sometimes a lower one.
- **top_k.** Only the 50 most likely words are eligible at each step.
- **Seed.** The starting number for the random number generator. Same seed,
  same sequence of rolls. Upstream's code used 42 by default and never wrote
  it down.
- **num_samples.** How many answers per question in one batch. Upstream's
  original run used 1, their repeat used 3. The random rolls are dealt across
  the batch, so answer 1 of a 3-batch sees different rolls than answer 1 of a
  1-batch. Same seed, no match possible.
- **Deterministic algorithms.** A switch that forces the GPU to add numbers
  in a fixed order. Without it, the order can vary and flip the last decimal,
  which can flip a near-tie word.
- **Byte-identical.** Same text down to every character, checked by
  comparing SHA-256 fingerprints.
- **bf16 emulated.** The weights are 16-bit floats. V100 GPUs have no
  hardware for that format, so PyTorch fakes it. A V100 number and an A100
  number are not the same computation. Recorded in every record.

## The result

a vs b: 8 of 8 identical. c vs d: 8 of 8. a vs c: 8 of 8.

With the seed recorded and one sample per call, generation at the paper's
own settings is exactly repeatable on this machine, and the deterministic
switch changes nothing. Their 118-of-120 mismatch was the unrecorded seed
plus the 1-versus-3 sample mismatch. Not the model, not the hardware.

## The sentence

"I ran their evaluation at their exact settings twice. 8 of 8 answers
identical, byte for byte. Their reproduction failure was an unrecorded seed
and mismatched sample counts, not the model or the hardware."

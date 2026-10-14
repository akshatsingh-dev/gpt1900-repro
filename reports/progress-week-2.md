# Progress Update Week 1, Akshat Singh

GPT-1900 reproducibility, 1 September 2026
Evaluated against github.com/michaelhla/gpt1900

## What I did

Most of this week went on compute. I secured an ACCESS allocation on SDSC
Expanse and did an onboarding session with Evan  on how to actually use
it. I also went back into the code and found that one claim in last week's
report was wrong, which is the first item below.

## Correction to last week's report

Last week I wrote that the eval script never sets a random seed. That is
literally true of `scripts/physics_eval.py`, and it is the wrong explanation.

The seed is one layer down. `nanochat/engine.py` line 171 declares
`generate(..., seed=42)`, and lines 182 to 183 build a dedicated generator from
it. `physics_eval.py` calls into that and never passes a seed, so every
published run has used seed 42. Every run was seeded, and seeded identically.

That makes the reproduction failure harder to explain rather than easier. A
fixed seed with 118 of 120 paired generations differing means sampling
randomness was never the cause. Something structural is.

The likely cause is visible in the same file. After a batch of one prefill, the
logits are expanded to `num_samples` rows at line 206, and from there a single
shared generator serves every row for the whole decode loop at line 234. So the
random numbers reaching row 0 depend on how many rows sit beside it. Sample 0 of
a three sample run and sample 0 of a one sample run are different draws from the
same seed and cannot match. Last week's report already recorded that both
upstream pairs used mismatched `--num-samples`. Those two facts together are
enough to explain the 0 of 96 with no appeal to hardware or library behaviour.

This is read from source and has not been measured. It predicts something cheap
and falsifiable: at matched sample count and temperature 0, which takes the
`argmax` path and touches no generator at all, two runs on one machine should be
byte identical. That is the test I run next.

The logging gap I reported stands unchanged. 42 was never written down, so no
reader of the archive could have known it, and nothing in the results files
identifies which weights or settings produced an answer.

## Compute

Allocation CIS261668 on SDSC Expanse, requested conservatively at 58,346 of
200,000 available credits: 1000 GPU hours, 4000 core hours, 500 GB of project
storage. The intention is to exchange for more once the serving work starts
rather than over-request now.

The session with Evan covered the portal and where to find the project ID, SSH
key and 2FA setup, Slurm job scripts and `sbatch`, purging and loading modules,
activating a Python environment inside a job, `rsync` rather than `scp` for
moving code, and the point that work belongs in the Lustre project allocation
rather than on the login node.

The account is not active yet, so SSH and 2FA cannot be finished. The access email is sent..

He also flagged that code will need adapting rather than just copying: my laptop
is Apple Silicon and runs float32, Expanse GPUs run bfloat16, and dependency
versions will differ. That difference is real and I have made the pipeline
record it, so a result that differs between the two machines can be attributed
to the machines rather than guessed at.

## Serving the model as a queryable page

You asked whether the model could be hosted somewhere so anyone can go to a page
and ask it questions. That needs somewhere to serve inference from: the weights
loaded and held in memory, a GPU behind them, and a process answering requests
as they arrive. It is not something a static page can do.

This is part of why I requested the compute. The allocation covers both the
evaluation runs and the machine that would sit behind such a page. Upstream
already ships the serving code, `chat_web.py`, `launch_serving.sh`,
`dashboard.py` and `SERVER_SETUP.md`, so the missing piece is the machine rather
than the software.

One caveat I want to raise early. Expanse is a batch cluster with job walltime
limits and no public inbound networking, which suits the evaluation runs but not
an always on service. For the hosted page the better ACCESS resource is likely
Jetstream2, which is cloud style and designed for this. I am confirming that
with Evan. Either way this gets built as soon as access lands, and I can stand
up a temporary fallback host in the meantime if you want something to show
sooner.

## What I built

`tools/logged_eval.py`. It produces the same generations as upstream but writes
a 43 field record for every one: seed, temperature, top_k, sample index, model
revision, config hash, prompt hash, completion hash, dtype, device, torch and
platform versions, finish reason and timing. One JSON object per line, flushed
to disk as it goes, so a crash costs the line in flight rather than the run.

It does not edit upstream. It imports upstream and calls into it, so upstream
stays at its pinned commit and any difference in results stays attributable to
the environment rather than to changes I made.

Two deliberate departures from upstream. The Hugging Face revision is resolved
and passed to the download, so weights are pinned by hash rather than fetched by
a mutable name. And it generates one sample per engine call rather than a batch,
which removes the batch coupling described above and makes any two records with
the same seed comparable.

It has not been run against a model yet, so its own claims are untested.

## What is next

1. Determinism test on my laptop. One v11 checkpoint, one task, temperature 0,
  run twice, compare byte for byte. This is the experiment that separates
   "random by design" from "structurally broken", and it is cheap.
2. A comparison script that reads two runs and reports the match rate. This is
  what turns the generation files into a number for the memo.
3. The judging pass, which fills in the score fields at judge temperature 0 and
  records which judge model produced them.
4. Slurm job script, then port and test on Expanse once the account is live.
5. Serving, once I know which resource it should sit on.



## Two things I need from you

1. **API budget for judging.** Grading calls the Claude API and costs money. The
  score reproducibility work depends on it, and no repeat run upstream has ever
   been graded, so this is the gap I most want to close. Is there an existing key
   or budget I should use.
2. **Audience for the hosted page.** Whether it is for researchers you name or
  open to anyone changes where it should be hosted and how much it costs to
   keep running.

Still open from before: whether training a pre-1911 model is in my remit. It
changes the compute request and the scope of the sprint, so I would rather ask
than assume.
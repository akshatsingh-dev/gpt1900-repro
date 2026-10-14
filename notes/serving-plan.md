# Serving GPT-1900 as a public playground

Written 3 Sep 2026. Target: a page anyone can open and ask the model questions.

## What upstream already gives us

More than expected. The serving stack is complete and does not need writing.

| Piece | Where | What it does |
|---|---|---|
| `scripts/chat_web_batch.py` | upstream | FastAPI server, one per GPU, continuous batching, SSE streaming |
| `scripts/chat_web.py` | upstream | Simpler single-process server |
| `scripts/launch_serving.sh` | upstream | Starts N workers, generates nginx config, starts nginx on port 80 |
| `deploy/nginx/nanochat.conf` | upstream | Load balancing, rate limits, SSE proxy settings |
| `deploy/vercel/` | upstream | Static frontend plus an edge function that proxies to the backend |
| `deploy/runpod/` | upstream | Serverless handler and Dockerfile, an alternative path |
| `SERVER_SETUP.md` | upstream | Written instructions for standing it up on a GPU box |

Endpoints: `/` chat UI, `POST /chat/completions` SSE, `/health`, `/stats`, `/logs`.
Auth: bearer token via `BACKEND_API_KEY`. Rate limiting: 10 req/s per IP, 4
concurrent, done in nginx.

The integration seam is one environment variable. `deploy/vercel/api/chat.js`
reads `BACKEND_URL` and forwards to `${BACKEND_URL}/chat/completions`, piping
the SSE stream straight back to the browser. So the frontend does not care where
the GPU is. Whatever we build only has to produce a reachable HTTPS URL.

Model size is not a problem. 3.29B in bf16 is roughly 6.6GB, so it fits on one
GPU with room to spare and there is no need for multi-GPU sharding.

## What breaks on Expanse

Five things, in order of how hard they are.

**1. No public inbound networking.** Compute nodes are not addressable from the
internet. Vercel's edge function cannot reach one. This is the whole problem and
everything below is secondary.

**2. `launch_serving.sh` needs sudo.** It runs `sudo nginx` and binds port 80.
Neither is available to a normal user on a shared cluster. The script cannot be
used as written.

**3. Walltime limits.** Expanse jobs are time boxed. A service running as a
batch job dies when the job ends and has to be resubmitted. There is no
always-on.

**4. Queue wait.** A job can sit pending. During that time the page is down, and
nothing about that is under our control.

**5. Budget.** The allocation is 1000 GPU hours. Serving continuously on one GPU
spends 24 GPU hours a day, so the whole allocation is about 41 days of uptime,
and that is the same pot the evaluation runs come out of. An always-on service
on Expanse would eat the research budget.

Numbers to confirm with Evan rather than trust here: exact max walltime on
`gpu-shared`, whether outbound HTTPS from compute nodes is permitted, and the
GPU model and memory on the nodes we are allocated.

## The three ways to do it

### A. Outbound tunnel, hosted on Expanse

The compute node dials out to a tunnel provider, which gives a public hostname
and forwards traffic back down the connection it already established. No inbound
port is ever opened.

```
browser -> Vercel page -> Vercel edge fn -> tunnel hostname
                                              |
                                     (connection opened outward
                                      by the compute node)
                                              |
                                      FastAPI worker on Expanse
```

What has to be built:
- A Slurm batch script that loads modules, activates the environment, stages the
  checkpoint to node-local storage, starts one or more workers on high ports,
  starts the tunnel client, and stays alive until walltime.
- A replacement for the nginx layer, since sudo is unavailable. Either run a
  single worker and skip load balancing, or run nginx unprivileged on a high
  port with pid, log and temp paths pointed somewhere writable.
- A way to publish the current tunnel hostname, because it changes per job
  unless a named tunnel with stored credentials is used.
- `BACKEND_URL` on the Vercel side pointing at that hostname.

**Read this before building it.** Tunnelling public traffic into a compute node
routes around the network policy that keeps those nodes private. Whether it is
allowed is a question for SDSC and Evan, not for us to infer from the fact that
it technically works. Ask first. Getting an account suspended costs the sprint
far more than the demo is worth.

### B. Queue relay, no inbound at all

Vercel writes each request to a queue that both sides can reach, such as a
hosted Redis or Postgres. The Expanse job polls the queue, generates, and writes
the answer back. Nothing ever connects into the cluster.

This is the most defensible option under any network policy, because it uses
only outbound connections to an ordinary internet service. The cost is user
experience: token by token streaming becomes awkward, and latency now includes
queue round trips on top of generation. It also still dies at walltime.

### C. Jetstream2, the resource actually built for this

Checked on 3 Sep 2026, because the objection came up that SDSC does not have
Jetstream2. That is true and it is not the obstacle.

Jetstream2 is run by Indiana University, not SDSC. But it is an ACCESS resource,
and the allocation is an ACCESS allocation, not an SDSC one. ACCESS gives you
credits and you exchange them for time on whichever resource you want, from
whichever provider. Expanse was one exchange. Jetstream2 would be another
exchange against the same pot of credits.

What the docs say:

- 1 ACCESS Credit = 1 Jetstream2 SU, deliberately aligned for simplicity.
- The exchange is self service in the ACCESS allocations portal, under
  "Credits + Resources", then "Add a resource to your exchange". It needs a
  short justification and gets reviewed by resource representatives to check
  the resource suits the work. It is not a new proposal.
- Jetstream2 CPU, GPU and Large Memory are separate selections. Having one does
  not give the others, so the request has to name Jetstream2 GPU.
- GPU instances bill 2 SUs per vCPU core-hour.

Smallest GPU flavour, `g3.medium`: 8 vCPU, 30GB RAM, a quarter of an A100 with
10GB of GPU memory, 16 SU per hour. Next one up, `g3.large`: 16 vCPU, 60GB RAM,
half an A100 with 20GB, 32 SU per hour.

Jetstream2 is OpenStack. Persistent VM, floating public IP, root on your own
instance, no walltime and no queue. The upstream stack runs there exactly as
`SERVER_SETUP.md` describes, `sudo nginx` and all, with no changes.

## The cost comparison, which settles it

From the ACCESS application: 1000 Expanse GPU hours cost 53,846 credits, so
roughly **53.8 credits per GPU hour**. Jetstream2 `g3.medium` is **16 credits
per hour**. Serving is about three and a half times cheaper per hour on
Jetstream2, on a newer GPU, with none of the batch cluster problems.

Credits remaining: 200,000 allocated, 58,346 exchanged for Expanse, so about
**141,654 unexchanged**.

| Option | Rate | Continuous uptime from remaining credits |
|---|---|---|
| Jetstream2 `g3.medium` | 16 SU/hr | about 369 days |
| Jetstream2 `g3.large` | 32 SU/hr | about 184 days |
| Expanse GPU | 53.8 credits/hr | about 110 days |

The earlier figure of 41 days for Expanse was against the 1000 GPU hours already
exchanged, not against the credit balance. Both are true and they answer
different questions. Hosting inside the existing Expanse exchange spends the
entire evaluation budget in six weeks.

Memory: the model is 3.29B, roughly 6.6GB in bf16, so the weights fit in
`g3.medium`'s 10GB with a few GB spare. Whether that is enough depends on the KV
cache, which grows with `--max-batch` and `--max-tokens`. Fine for a handful of
concurrent users, not obviously fine for a public page. `g3.large` at 20GB is
the safer pick and still cheaper per hour than Expanse. This should be measured
rather than assumed.

## Recommendation

Split the two jobs, because they are different jobs.

**Expanse keeps the evaluation work.** Batch, bounded, GPU heavy, exactly what
the machine is for. The 1000 GPU hours already exchanged should go here.

**The playground goes on Jetstream2 GPU.** Exchange some of the remaining
credits for it. The stack runs unmodified, the page stays up, it costs a third
of what Expanse would per hour, and the evaluation budget stays intact.

Use A only as a time boxed demo if something has to exist before the exchange
clears, and only after SDSC says it is acceptable. Treat it as a demo that runs
during a meeting, not as a service with a URL handed out.

## Build order

1. Exchange credits for Jetstream2 GPU in the ACCESS allocations portal, under
   "Credits + Resources". Name Jetstream2 GPU specifically, since CPU does not
   include it. Justification writes itself: hosting a model for interactive
   querying needs a persistent instance with a public address, which a batch
   scheduler cannot provide. Mention it to Evan, but this does not need him.
2. Get the checkpoint onto the instance. Decide which one is the public face.
   The v11 family is published and is what the eval targets, but
   `SERVER_SETUP.md` refers to a chat SFT checkpoint and a v12, so confirm which
   is meant to be the one people talk to.
3. Stand up one worker and prove it serves `/health`. On Jetstream2 this is just
   following `SERVER_SETUP.md`.
4. Put nginx in front for rate limiting, set `BACKEND_API_KEY`.
5. Point the Vercel frontend's `BACKEND_URL` at the instance.

Step 3 is the real milestone. Once a worker answers `/health`, the model is
running and everything after it is plumbing.

## Open questions

- Which checkpoint is the public one, and does Keating want the raw base model,
  the instruction tuned one, or a choice between them. The frontend already
  ships artwork for a base model and an instruction tuned model, so upstream
  intended a toggle.
- Is the page public or limited to named researchers. This decides whether rate
  limiting and an API key are enough or whether real auth is needed.
- What happens to the page after 15 Sep, and who runs it then.

## Sources

- Jetstream2 on ACCESS credits: https://docs.jetstream-cloud.org/general/access/
- Jetstream2 instance flavours and SU rates: https://docs.jetstream-cloud.org/general/instance-flavors/
- Jetstream2 allocations overview: https://docs.jetstream-cloud.org/alloc/overview/
- ACCESS credit exchange and calculator: https://allocations.access-ci.org/exchange_calculator
- ACCESS allocations how-to: https://allocations.access-ci.org/how-to

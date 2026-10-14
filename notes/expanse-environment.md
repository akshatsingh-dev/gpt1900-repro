# Expanse environment survey

Gathered 3 Sep 2026 by running read-only commands over an existing SSH
ControlMaster session as `asingh59`. Nothing was written, installed, loaded
persistently or submitted. Every fact below came from a command, and the ones
that are inferred rather than observed are marked.

## The headline: there is no GPU allocation

```
$ expanse-client user -p -r expanse-gpu

 Resource  expanse-gpu

 NAME  STATE  PROJECT  TG PROJECT  USED  AVAILABLE  USED BY PROJECT
--------------------------------------------------------------------
                        (empty)
```

The table comes back with no rows. The CPU resource does have a row:

```
$ expanse-client user -p

 Resource  expanse
 NAME      STATE  PROJECT  TG PROJECT    USED  AVAILABLE  USED BY PROJECT
 asingh59  allow  sdp197   TG-CIS261668     0       4000                0
```

So 4000 CPU core-hours are live and unused, and the 1000 GPU-hours from the
ACCESS request are not present on the machine. Confusingly, the Slurm side does
list GPU QOS entries, so a GPU job may be accepted by the scheduler and then
fail to charge or fail to run. This needs resolving with Evan or SDSC before any
GPU work is planned around it.

Nothing in this document assumes the GPU allocation exists.

## Identity and accounting

| Fact | Value |
|---|---|
| Username | `asingh59` |
| Unix group | `sdp197` |
| Slurm account | `sdp197` |
| ACCESS/TG project | `TG-CIS261668` |
| Login node observed | `login02`, 64 cores, 124GB RAM, kernel 4.18.0 el8 |

`sdp197` is a shared project. `/expanse/lustre/projects/sdp197/` contains both
`asingh59/` and `bkeating/`, so this is Keating's project and Akshat is a user
on it rather than the owner. Worth remembering before writing anything outside
the personal subdirectory.

Slurm QOS available to this user:

```
sdp197 || debug-normal, gpu-debug-normal, gpu-normal, gpu-preempt-normal,
          gpu-shared-normal, large-shared-normal, normal, preempt-normal,
          shared-normal
```

## Partitions and limits

| Partition | Time limit | Notes |
|---|---|---|
| `compute` | 2-00:00:00 | CPU, ~700 nodes |
| `debug` | 30:00 | short turnaround |
| `gpu` | 2-00:00:00 | whole GPU nodes |
| `gpu-shared` | 2-00:00:00 | `DefaultTime=01:00:00`, `MaxNodes=1` |

Max walltime on GPU partitions is 48 hours. Default on `gpu-shared` is 1 hour,
so a job that does not set `--time` gets an hour.

`gpu-shared` billing weights: `gres/gpu=3600, cpu=360.00, mem=37.40G, node=0`.

## GPU hardware

```
$ sinfo -h -p gpu,gpu-shared -o "%25G %6D %T" | sort | uniq -c
   1 gpu:a100:4(S:0-1,3)   6   reserved
   1 gpu:v100:4            1   fail*
   1 gpu:v100:4(S:0-1)    19   allocated
   1 gpu:v100:4(S:0-1)     1   maint
   1 gpu:v100:4(S:0-1)     1   planned
   1 gpu:v100:4(S:0-1)    28   mixed
```

Practically this is a **V100** machine. Four GPUs per node, 40 CPU cores,
385500 MB of system RAM per node. The six A100 nodes are all in `reserved`
state, so plan for V100.

GPU memory per V100 is not reported by `sinfo`. SDSC documents Expanse V100s as
32GB SXM2, which is not verified here. A 3.29B model at bf16 is roughly 6.6GB,
so it fits comfortably either way.

## Storage

| Path | Observed state |
|---|---|
| `/home/asingh59` | 83K used. `quota -s` reports "none". SDSC docs say 100GB, unverified here. Intended for code and job scripts. |
| `/expanse/lustre/projects/sdp197/asingh59` | Exists, created 1 Sep. Contains one directory, `gpt1900/`. This is where the 500GB allocation lives and where weights belong. |
| `/expanse/lustre/scratch/asingh59/temp_project` | Exists. Purged 90 days from file creation. Do not put anything here that matters. |

Contents of the project directory as of this survey:

```
/expanse/lustre/projects/sdp197/asingh59/gpt1900/
└── requirments.txt      487 bytes, created 2 Sep 16:25
```

86K total. **No code, no weights, no virtual environment, no job scripts.**

## A version conflict already on disk

The `requirments.txt` sitting in the project directory pins:

```
torch==2.14.0
```

Upstream `pyproject.toml` pins `torch==2.9.1` exactly, and routes the `gpu`
extra to the `cu128` wheel index. The file on Expanse also omits most of
upstream's dependencies: no `vllm`, `fastapi`, `transformers`, `datasets`,
`wandb` or `anthropic`. It reads like a `pip freeze` from a different, smaller
experiment.

It should not be used to build the environment for this project. Use upstream's
`pyproject.toml` and `uv`.

## Toolchain, and what is missing

| Tool | State |
|---|---|
| `python3` | **3.6.8**. Upstream requires `>=3.10`. Unusable as-is. |
| `uv` | **Not installed.** Not on PATH. |
| `git` | Present at `/usr/bin/git`. |

Because the system Python is 3.6 and the only Python module is
`anaconda3/2021.05`, which ships Python 3.8, the cleanest route is to install
`uv` into `~/.local/bin` and let it manage its own Python 3.10+. That avoids the
module system for Python entirely.

## Modules, and the tree you have to switch

Default loaded modules on login:

```
shared
cpu/0.17.3b
slurm/expanse/23.02.7
sdsc/1.0
DefaultModules
```

Expanse uses an Lmod hierarchy and **the default tree is `cpu`**. Under it,
`module spider cuda` returns only `cuda/9.1.85`, `cuda/9.2.88`, `cuda/11.0.2`.

After `module load gpu`, the CUDA toolkits become:

```
cuda10.2/toolkit/10.2.89
cuda11.7/toolkit/11.7.1
cuda12.2/toolkit/12.2.2
```

So the newest CUDA toolkit module is **12.2.2**, while upstream wants the
**cu128** torch wheels. This is probably fine, because pip and uv torch wheels
bundle their own CUDA runtime libraries and CUDA 12 has minor version
compatibility, so what matters is the NVIDIA driver rather than the toolkit
module. That reasoning is not verified. It should be checked by running
`nvidia-smi` on an actual GPU node and reading the driver version, which cannot
be done from a login node.

Any job script must `module load gpu` before expecting CUDA to exist.

## Local shortcuts already set up

In `~/.ssh/config` on the Mac:

```
Host expanse
  HostName login.expanse.sdsc.edu
  User asingh59
  ControlMaster auto
  ControlPath ~/.ssh/cm/%r@%h:%p
  ControlPersist 8h
  ServerAliveInterval 60
```

`ControlMaster` with an 8 hour persist means that while a session is open,
further commands run over the same connection with no password and no 2FA
prompt. Check with `ssh -O check expanse`. This is how this survey was done.

In `~/.zshrc`:

```
export EXPANSE=asingh59@login.expanse.sdsc.edu
export EXPDIR=/expanse/lustre/projects/sdp197/asingh59
export EXPGPT=$EXPANSE:$EXPDIR/gpt1900
```

## What to know before doing anything on Expanse

1. **Confirm the GPU allocation exists** before planning GPU work. Right now it
   does not appear on the machine.
2. **`upstream/` is gitignored** in the `gpt1900-repro` repo. Cloning that repo
   onto Expanse will not bring `upstream/gpt1900` with it. Upstream has to be
   cloned separately and checked out at the pinned commit `5b489c8c`.
3. **Do not build from the `requirments.txt` already on Expanse.** It pins the
   wrong torch and is missing most dependencies.
4. **Install `uv` and let it own Python.** System Python is 3.6.8.
5. **`module load gpu` first**, or CUDA is not in the module tree.
6. **Weights go in projects storage, never scratch.** 500GB holds all 24 v11
   checkpoints at roughly 158GB, so the download-use-delete cycle the laptop
   forced is unnecessary here.
7. **Set `HF_HOME` into projects storage** before any HuggingFace download, or
   the cache lands in the home directory.
8. **`sdp197` is shared with `bkeating`.** Stay inside `asingh59/`.
9. **Set `--time` explicitly.** `gpu-shared` defaults to one hour.
10. **No Slurm script exists yet**, anywhere in the project. It is unwritten
    work, not a missing file.

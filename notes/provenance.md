# Provenance

Every number reported in this sprint carries the pins below. If a pin changes,
the results are no longer comparable and the change gets its own notebook entry.

## Upstream code

| Field | Value |
|---|---|
| Repository | https://github.com/michaelhla/gpt1900 |
| Commit | `5b489c8c5378f6b1bf3e1ba782f56876f65cde7a` |
| Branch | `master` |
| Commit date | 2026-04-09 00:55:36 -0700 |
| Author | Michael Hla |
| Cloned | 2026-08-25 |
| Clone size | 21.70 MiB, 2369 objects |
| Local path | `upstream/gpt1900` (gitignored, re-clone from the commit above) |

To restore this exact state on any machine:

```
git clone https://github.com/michaelhla/gpt1900.git upstream/gpt1900
cd upstream/gpt1900
git checkout 5b489c8c5378f6b1bf3e1ba782f56876f65cde7a
```

## Model weights

Not yet pulled. Hugging Face repo and revision go here once a checkpoint is
downloaded. Revision, not just the model name: the owner can push new weights
to the same name and silently change results.

| Field | Value |
|---|---|
| HF repo | `mhla/gpt1900-d34-contradiction-rl-v11` |
| Revision | `71bf395f06dff39ad5ee9f8981b941b3c37daae9` (resolved 8 Sep 2026, E032) |
| Checkpoint step | 560 (`discovery-rl-v11-s560`); the sweep pins the same revision for all 24 |
| Weights sha256 | not yet computed, `--hash-weights` was not passed on the 8 Sep run |
| Base model for the knowledge probe | `mhla/gpt1900-d34-22btok`, step 10507, revision resolved at run time and written into each record |
| Corpus for the contamination search | `mhla/pre1900-corpus`, 44 parquet shards, 56.4 GB, revision resolved at run time and written into `corpus-search.json` |

## Machine

| Field | Value |
|---|---|
| Platform | Darwin 24.5.0 arm64, Apple Silicon |
| RAM | 18 GB |
| Free disk at sprint start | 31 GB |
| GPU | none |
| Python | 3.12.2 |
| uv | 0.6.4 |

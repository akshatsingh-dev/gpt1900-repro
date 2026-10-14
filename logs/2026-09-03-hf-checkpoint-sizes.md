# HF checkpoint size audit

Date: 2026-09-03
Machine: MacBook, Darwin 24.5.0 arm64
Method: read-only queries to `https://huggingface.co/api/models/<repo>?blobs=true`.
No weights downloaded. Sizes are the `size` field on each sibling blob, in bytes.

## Command

```
for r in gpt1900-d26-8btok gpt1900-d26-22btok gpt1900-d34-8b-subset \
         gpt1900-d34-22btok gpt1900-d34-physics-sft gpt1900-d34-sft-period \
         gpt1900-d34-sft-modern gpt1900-d34-rl gpt1900-d34-coherence-rl \
         gpt1900-d34-reasoning-sft-v4 gpt1900-d34-discovery-rl-v4 \
         gpt1900-d34-contradiction-rl-v11; do
  curl -s "https://huggingface.co/api/models/mhla/$r?blobs=true" > /tmp/hf_$r.json
done
```

## Result

| Repo | Revision (sha) | .pt files | Bytes per .pt | Per ckpt | Repo total |
|---|---|---|---|---|---|
| mhla/gpt1900-d26-8btok | 9ddb991d9089 | 10 | 5,200,509,259 | 5.20 GB | 12.7 GB |
| mhla/gpt1900-d26-22btok | 6002821b9d2e | 10 | 5,200,509,259 | 5.20 GB | 12.7 GB |
| mhla/gpt1900-d34-8b-subset | f7aee6b435b5 | 10 | 10,579,743,323 | 10.58 GB | 24.9 GB |
| mhla/gpt1900-d34-22btok | d6330f9f0a17 | 131 | 10,579,743,323 | 10.58 GB | 59.3 GB |
| mhla/gpt1900-d34-physics-sft | 9ca816a3c102 | 3 | 10,579,743,323 | 10.58 GB | 12.4 GB |
| mhla/gpt1900-d34-sft-period | 802ff4cb9af0 | 3 | 10,579,743,323 | 10.58 GB | 12.4 GB |
| mhla/gpt1900-d34-sft-modern | 586d2bb729da | 3 | 10,579,743,323 | 10.58 GB | 12.4 GB |
| mhla/gpt1900-d34-coherence-rl | 257c96366b10 | 2 | 10,579,743,323 | 10.58 GB | 10.6 GB |
| mhla/gpt1900-d34-reasoning-sft-v4 | 2fc119e3fe7c | 3 | 10,579,743,323 | 10.58 GB | 12.4 GB |
| mhla/gpt1900-d34-discovery-rl-v4 | 705d5d70b203 | 2 | 10,579,743,323 | 10.58 GB | 10.6 GB |
| mhla/gpt1900-d34-contradiction-rl-v11 | 71bf395f06dff39ad5ee9f8981b941b3c37daae9 | 25 | 10,579,743,323 | 10.58 GB | 253.9 GB |

Grand total across all distinct repos: **434.1 GB**.

Tokenizer directory is 0.5 MB in every repo. A `meta_XXXXXX.json` is 182 bytes.

## Notes

1. `mhla/gpt1900-d34-rl`, named in the `CHECKPOINTS` registry at
   `upstream/gpt1900/scripts/physics_eval.py:53`, HTTP-redirects to
   `mhla/gpt1900-d34-coherence-rl`. Same repo, renamed upstream. Counted once.
2. Every d34 checkpoint is byte-identical in size, 10,579,743,323 B. The d26
   ones are 5,200,509,259 B.
3. **This contradicts the sprint brief**, which records "one 3.29B checkpoint in bf16
   is roughly 6.6GB and there are 24 of them". Measured is 10.58 GB per d34
   checkpoint, and the registry lists 89 entries, of which 54 are `repo="local"`
   and were never published, leaving 35 HF-backed entries across 12 distinct
   repos. 10.58 GB over 3.29B params is 3.21 bytes per
   param, so these files are not plain bf16 tensors. What the extra bytes are
   has not been checked and should not be asserted until one file is opened.
4. One `logged_eval.py` run pulls `model_XXXXXX.pt` + `meta_XXXXXX.json` +
   `tokenizer/*`, so peak disk for a single d34 checkpoint is about 10.6 GB.

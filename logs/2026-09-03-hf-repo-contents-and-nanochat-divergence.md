# What the HF weights repo actually contains, and a code divergence

Date: 2026-09-03
Machine: MacBook, Darwin 24.5.0 arm64
Repo inspected: `mhla/gpt1900-d34-contradiction-rl-v11`
Revision: `71bf395f06dff39ad5ee9f8981b941b3c37daae9` (lastModified 2026-04-02)
Compared against upstream pin: `michaelhla/gpt1900` @ `5b489c8c5378f6b1bf3e1ba782f56876f65cde7a`
(commit date 2026-04-09)

Question that prompted this: is it worth pulling raw weights and skipping
nanochat, given SDSC access.

## Finding 1: the weights are not a standalone format

The repo holds no `config.json` and no `.safetensors`. A checkpoint is a pickled
`state_dict` (`model_XXXXXX.pt`) plus a 182-byte `meta_XXXXXX.json` carrying
`model_config`, and the tokenizer is `tokenizer/tokenizer.pkl`, which needs
`rustbpe` and `tiktoken` to unpickle. Loading these without nanochat means
reimplementing `nanochat.gpt.GPT` exactly and having no way to prove the
reimplementation is faithful.

## Finding 2: the weights repo bundles nanochat itself

142 files. Beyond the 25 `.pt` and 24 `meta_*.json`:

| Path | Files | Size |
|---|---|---|
| `nanochat/` | 10 | 121.6 KB |
| `physics_eval_generations/` | 24 | 507.0 KB |
| `eval_generations/` | 56 | 691.3 KB |
| `tokenizer/tokenizer.pkl` | 1 | 0.5 MB |

So "weights without nanochat" is not a choice the repo offers. The only choice
is which copy of nanochat runs.

## Finding 3: the bundled nanochat differs from the pinned upstream

Downloaded all 10 bundled modules and compared by sha256 against
`upstream/gpt1900/nanochat/`:

| Module | Result |
|---|---|
| `gpt.py` | DIFFERS, 10 changed lines |
| `checkpoint_manager.py` | DIFFERS, 9 changed lines |
| `engine.py` | DIFFERS, 20 changed lines |
| `flash_attention.py` | DIFFERS, 52 changed lines |
| `tokenizer.py` | identical |
| `common.py` | identical |
| `optim.py` | identical |
| `fp8.py` | identical |
| `loss_eval.py` | identical |

The HF bundle is the older side by about a week. Three of the four differences
can change generated text:

1. `engine.py`. Upstream removed calculator tool execution with the comment
   "Tool logic disabled — calculator eval() is a security risk". The bundled
   copy still executes `use_calculator(expr)` on `python_end` and force-feeds
   the result back into the stream. On any prompt where the model emits
   `python_start`/`python_end`, the two versions produce different token
   sequences.
2. `gpt.py`. Upstream added a continuous-batching decode branch that indexes
   rotary embeddings per batch element when `T == 1` and the kv cache exposes
   `get_positions`. The bundled copy always uses the single-offset path.
3. `checkpoint_manager.py`. Upstream prefers a tokenizer bundled next to the
   checkpoint when one exists; the bundled copy always calls `get_tokenizer()`.

This is a candidate explanation for generation mismatches and it should be
tested rather than assumed. It has not been tested yet. No generation has been
run on this machine.

## Finding 4: upstream's own generations are published

`physics_eval_generations/step_XXXXXX.jsonl`, one file per checkpoint step,
8 records each, one per physics task. Fields are `task_id`, `score`, `response`.
No prompt, no seed, no temperature, no top_k, which is the same logging gap
already recorded for `results/physics_eval_v11/generations.json`. Still usable
as a comparison target: `task_id` plus `response` can be diffed byte for byte
against a local run of the same step.

507 KB for all 24 steps. No GPU and no weights needed to fetch them.

## Commands

```
curl -sL "https://huggingface.co/api/models/mhla/gpt1900-d34-contradiction-rl-v11?blobs=true"

for f in gpt.py checkpoint_manager.py engine.py tokenizer.py common.py \
         flash_attention.py optim.py fp8.py loss_eval.py __init__.py; do
  curl -sL "https://huggingface.co/mhla/gpt1900-d34-contradiction-rl-v11/resolve/71bf395f06dff39ad5ee9f8981b941b3c37daae9/nanochat/$f" -o /tmp/hfnc/$f
done

shasum -a 256 upstream/gpt1900/nanochat/*.py /tmp/hfnc/*.py

curl -sL "https://huggingface.co/mhla/gpt1900-d34-contradiction-rl-v11/resolve/71bf395f06dff39ad5ee9f8981b941b3c37daae9/physics_eval_generations/step_000560.jsonl"
```

## Dependency check, done at the same time

`tools/logged_eval.py` imports `nanochat.engine` and `scripts.physics_eval`.
Following that import chain, the modules reached are `engine`, `gpt`,
`checkpoint_manager`, `tokenizer`, `common`, `optim`, `flash_attention`. Their
third-party imports are torch, tokenizers, rustbpe, tiktoken, filelock and
huggingface_hub. Nothing in the chain imports vllm, wandb, transformers or
datasets, even though `upstream/gpt1900/pyproject.toml` lists all four. So the
eval path needs the small dependency set in `requirments.txt`, not the full
upstream environment.

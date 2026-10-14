"""
Build blinded reading files for open-ended runs, from a config that carries
per-task verdict lists.

Each answer gets an R### id; provenance (checkpoint, seed) is stripped; the
item shows the prompt, the expected answer and the allowed verdicts for that
task, taken from the eval config. A key file maps R### back to
checkpoint|task|seed for tools/merge_blind_readings.py.

    python tools/make_read_file.py evidence/abduction/abduction.jsonl \
        --config tools/EVAL_abduction.json --seed 20261007 --parts 4 \
        --out-prefix evidence/abduction/to-read --key evidence/abduction/read-key.json
"""

import argparse
import json
import random


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl")
    ap.add_argument("--config", required=True)
    ap.add_argument("--seed", type=int, default=20261007)
    ap.add_argument("--parts", type=int, default=1)
    ap.add_argument("--out-prefix", required=True)
    ap.add_argument("--key", required=True)
    a = ap.parse_args()

    recs = [json.loads(l) for l in open(a.jsonl) if l.strip()]
    cfg = {t["id"]: t for t in json.load(open(a.config))["tasks"]}
    rng = random.Random(a.seed)
    order = list(range(len(recs))); rng.shuffle(order)

    head = ["# Answers to read", "",
            "Each item below is a model's answer to a short prompt. The item shows the prompt the model saw, the answer, "
            "what a fully correct answer would contain (`expected`), and the allowed verdicts for that item with their meanings. "
            "Nothing else about the answer is known to you and nothing else should matter.",
            "",
            "Rules: give exactly one verdict from the item's own list. Where the list is a ladder (wrong, none, weightless, equivalence, not-a-force, geometry), "
            "give the HIGHEST rung the answer reaches on its own. Repeating the prompt's words earns nothing. Restating the observations is `none`. "
            "`loops` means the text degenerates into repeating itself; `incoherent` means it cannot be read as an answer.",
            "",
            "Output: one JSON object per line, in file order: {\"id\": \"R###\", \"verdict\": \"<one of the item's verdicts>\", \"note\": \"<one line: what it actually says>\"}", ""]
    items, key = [], {}
    for n, i in enumerate(order, 1):
        r = recs[i]; t = cfg[r["task_id"]]; rid = f"R{n:03d}"
        key[rid] = f"{r['checkpoint_name']}|{r['task_id']}|{r['seed']}"
        items.append("\n".join([
            f"## {rid}", "", "prompt:", "```", (r.get("prompt") or "").strip(), "```",
            f"expected: {t.get('expected', '')}",
            f"verdicts: {', '.join(t.get('verdicts', []))}",
            f"verdict meanings: {t.get('verdict_help', '')}",
            "answer:", "```", (r.get("completion") or f"ERROR: {r.get('error')}").strip(), "```", ""]))
    json.dump({"shuffle_seed": a.seed, "ids": key}, open(a.key, "w"), indent=1)
    per = -(-len(items) // a.parts)
    for k in range(a.parts):
        chunk = items[k * per:(k + 1) * per]
        if not chunk:
            break
        path = f"{a.out_prefix}-{k + 1}.md" if a.parts > 1 else f"{a.out_prefix}.md"
        open(path, "w").write("\n".join(head + chunk))
        print(f"{path}: {len(chunk)} items")
    print(f"key {a.key}: {len(key)} ids")


if __name__ == "__main__":
    main()

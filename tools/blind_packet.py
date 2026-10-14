"""
Build the blinded review packet for physicist judges.

Why this exists
---------------
The published scores come from an LLM judge. Workstream 6 asks whether human
physicists, grading blind, agree. This takes our generations (and upstream's
published ones if given), shuffles them, strips every provenance field, and
writes:

    packet.html        what a reviewer opens: numbered answers, each with its
                       prompt and rubric, a blank score box, nothing else
    score-sheet.csv    one row per answer for the reviewer to fill in
    key.json           the sealed mapping from answer number back to source,
                       checkpoint, seed, condition and the LLM judge's score.
                       Do not open until the sheets are back.

The shuffle uses a recorded seed, so the packet can be rebuilt bit for bit.

Usage
-----
    python tools/blind_packet.py evidence/sweep/v11-scaffolded.judged.jsonl \
        --upstream-dir upstream/gpt1900/results/physics_eval_v11 \
        --per-task 6 --outdir evidence/review-packet
"""

import argparse
import csv
import hashlib
import html
import json
import os
import random
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
UPSTREAM = os.path.join(HERE, "..", "upstream", "gpt1900")


def load_jsonl(path):
    out = []
    with open(path) as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    print(f"{path}:{n}: skipped, {exc}", file=sys.stderr)
    return out


def load_upstream(dirpath):
    gens = json.load(open(os.path.join(dirpath, "generations.json")))
    jpath = os.path.join(dirpath, "results_judged.json")
    judged = json.load(open(jpath)) if os.path.exists(jpath) else {}
    out = []
    for ck, tasks in gens.items():
        for tid, cell in tasks.items():
            js = judged.get(ck, {}).get(tid, {}).get("samples", [])
            for i, text in enumerate(cell.get("completions") or []):
                out.append({"checkpoint_name": ck, "task_id": tid, "sample_index": i, "seed": None,
                            "prompt_condition": "scaffolded", "prompt": cell.get("prompt"),
                            "completion": text, "score": js[i]["judge"]["score"] if i < len(js) else None,
                            "_source": f"upstream:{os.path.basename(os.path.normpath(dirpath))}"})
    return out


def esc(v):
    return html.escape(str(v)) if v is not None else ""


def main():
    ap = argparse.ArgumentParser(description="Blinded review packet")
    ap.add_argument("jsonl", nargs="*", help="our logged_eval files, judged or not")
    ap.add_argument("--upstream-dir", action="append", default=[])
    ap.add_argument("--eval-config", default=os.path.join(UPSTREAM, "EVAL.json"),
                    help="for the rubric text shown to reviewers")
    ap.add_argument("--per-task", type=int, default=None,
                    help="answers per task, drawn at random. Default: all of them.")
    ap.add_argument("--seed", type=int, default=20260915, help="shuffle seed, recorded in key.json")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--batches", type=int, default=None,
                    help="also write grading batches of this many answers each, as markdown "
                         "files a grader works through one at a time (batches/batch-01.md ...)")
    args = ap.parse_args()

    pool = []
    for path in args.jsonl:
        for r in load_jsonl(path):
            if r.get("error") or r.get("completion") is None:
                continue
            r["_source"] = os.path.relpath(path)
            pool.append(r)
    for d in args.upstream_dir:
        pool.extend(load_upstream(d))
    if not pool:
        ap.error("nothing to pack")

    cfg = json.load(open(args.eval_config))
    tasks = {t["id"]: t for t in cfg["tasks"]}

    rng = random.Random(args.seed)
    by_task = defaultdict(list)
    for r in pool:
        by_task[r["task_id"]].append(r)
    chosen = []
    for tid in sorted(by_task):
        items = by_task[tid]
        rng.shuffle(items)
        chosen.extend(items if args.per_task is None else items[:args.per_task])
    rng.shuffle(chosen)

    os.makedirs(args.outdir, exist_ok=True)
    ids = [f"A{i:03d}" for i in range(1, len(chosen) + 1)]

    # ---- key, sealed ----
    key = {"shuffle_seed": args.seed, "n": len(chosen), "eval_config": os.path.relpath(args.eval_config),
           "inputs": args.jsonl + [f"upstream:{d}" for d in args.upstream_dir],
           "answers": []}
    for aid, r in zip(ids, chosen):
        key["answers"].append({
            "id": aid, "source": r["_source"], "checkpoint": r["checkpoint_name"],
            "task_id": r["task_id"], "seed": r.get("seed"), "sample_index": r.get("sample_index"),
            "prompt_condition": r.get("prompt_condition"), "llm_judge_score": r.get("score"),
            "completion_sha256": hashlib.sha256(r["completion"].encode("utf-8")).hexdigest(),
        })
    with open(os.path.join(args.outdir, "key.json"), "w") as f:
        json.dump(key, f, indent=2)

    # ---- score sheet ----
    with open(os.path.join(args.outdir, "score-sheet.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["answer_id", "task", "score_0_to_5", "reviewer_initials", "notes"])
        for aid, r in zip(ids, chosen):
            w.writerow([aid, tasks[r["task_id"]]["title"] if r["task_id"] in tasks else r["task_id"], "", "", ""])

    # ---- packet ----
    p = ["<!doctype html><html><head><meta charset='utf-8'><title>Review packet</title><style>",
         "body{margin:0 auto;padding:2rem;max-width:900px;font:15px/1.6 Georgia,serif;color:#1a1a1a;background:#fff}",
         "h1{font-size:1.5rem}h2{font-size:1.15rem;margin-top:2.5rem;border-top:2px solid #1a1a1a;padding-top:1rem}",
         "pre{white-space:pre-wrap;word-wrap:break-word;font:14px/1.55 -apple-system,Helvetica,Arial,sans-serif;background:#f6f6f6;border:1px solid #ddd;border-radius:6px;padding:.9rem 1.1rem}",
         "pre.answer{background:#fff;border-color:#999}",
         ".rubric{font-size:13px;background:#fbfbf3;border:1px solid #e0d9a8;border-radius:6px;padding:.6rem 1rem}",
         ".score{border:2px solid #1a1a1a;border-radius:6px;padding:.6rem 1rem;margin:1rem 0;font-weight:700}",
         "details summary{cursor:pointer;font-weight:600}",
         "</style></head><body>",
         "<h1>Blinded review packet</h1>",
         f"<p>{len(chosen)} answers to {len(by_task)} physics prompts. Each answer was written by a language model. "
         "You do not know which model, which settings, or what anyone else scored it. Please read the prompt, "
         "read the answer, then give a whole number from 0 to 5 using the rubric shown. Record it on the score "
         "sheet next to the answer id.</p>",
         "<details><summary>Grading instructions (the same ones the automated judge received)</summary>"
         f"<pre>{esc(cfg['shared_judge_prompt'])}\n\nChecklist:\n"
         + esc("\n".join("- " + c for c in cfg["shared_judge_checklist"]))
         + "\n\nRules:\n" + esc("\n".join("- " + c for c in cfg["shared_judge_rules"])) + "</pre></details>"]
    for aid, r in zip(ids, chosen):
        t = tasks.get(r["task_id"], {})
        p.append(f"<h2 id='{aid}'>{aid}</h2>")
        p.append(f"<details><summary>Prompt: {esc(t.get('title', r['task_id']))}</summary><pre>{esc(r['prompt'])}</pre></details>")
        if t:
            rub = "".join(f"<tr><td style='width:2rem'><b>{esc(k)}</b></td><td>{esc(v)}</td></tr>"
                          for k, v in sorted(t["scoring_rubric"].items()))
            p.append(f"<details><summary>Rubric</summary><div class='rubric'><p><b>Focus.</b> {esc(t['judge_focus'])}</p>"
                     f"<table>{rub}</table></div></details>")
        p.append(f"<pre class='answer'>{esc(r['completion'])}</pre>")
        p.append(f"<div class='score'>Score for {aid} (0 to 5): ______ &nbsp;&nbsp; Notes: ______________________</div>")
    p.append("</body></html>")
    with open(os.path.join(args.outdir, "packet.html"), "w") as f:
        f.write("\n".join(p))

    # ---- grading batches, for a grader who reads rather than calls an API ----
    if args.batches:
        bdir = os.path.join(args.outdir, "batches")
        os.makedirs(bdir, exist_ok=True)
        shared = (f"{cfg['shared_judge_prompt']}\n\nChecklist:\n"
                  + "\n".join("- " + c for c in cfg["shared_judge_checklist"])
                  + "\n\nRules:\n" + "\n".join("- " + c for c in cfg["shared_judge_rules"]))
        schema = json.dumps(cfg["judge_output_schema"], indent=2)
        n_batches = 0
        for start in range(0, len(chosen), args.batches):
            n_batches += 1
            items = list(zip(ids[start:start + args.batches], chosen[start:start + args.batches]))
            lines = [f"# Grading batch {n_batches:02d}", "",
                     "Grade every answer below. You know nothing about where any answer came from.",
                     "For each answer return one JSON object on its own line, and nothing else:",
                     "", "```", '{"id": "A001", "score": 0, "rationale": "...", "matched_concepts": [], "missing_concepts": []}',
                     "```", "", "## Shared instructions", "", shared, "",
                     "## Output schema", "", "```json", schema, "```", ""]
            for aid, r in items:
                t = tasks.get(r["task_id"], {})
                expected = "\n".join("- " + c for c in t.get("expected_core_concepts", []))
                rubric = "\n".join(f"  {k}: {v}" for k, v in sorted(t.get("scoring_rubric", {}).items()))
                lines += [f"## {aid}", "", "### Original prompt", "", r["prompt"], "",
                          "### Judge focus", "", t.get("judge_focus", ""), "",
                          "### Expected core concepts", "", expected, "",
                          "### Scoring rubric", "", rubric, "",
                          "### Model response", "", r["completion"], ""]
            with open(os.path.join(bdir, f"batch-{n_batches:02d}.md"), "w") as f:
                f.write("\n".join(lines))
        print(f"wrote {n_batches} grading batches of up to {args.batches} answers to {bdir}/")

    print(f"{len(chosen)} answers from {len(pool)} available, {len(by_task)} tasks, shuffle seed {args.seed}")
    print(f"wrote {args.outdir}/packet.html      give this to reviewers")
    print(f"wrote {args.outdir}/score-sheet.csv  they fill this in")
    print(f"wrote {args.outdir}/key.json         sealed. Do not open until the sheets are back.")


if __name__ == "__main__":
    main()

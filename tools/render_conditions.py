"""
One page, three prompt conditions side by side for the same question.

The three render_html pages show one condition each. This puts scaffolded,
minimal and leading next to each other for one checkpoint, one seed, every
task, so the difference in the question and the difference in the answer can
be read together. Scores and rationales shown when the judge fields are set.

    python tools/render_conditions.py --checkpoint discovery-rl-v11-s560 --seed 42
"""

import argparse
import html
import json
import os
from collections import defaultdict

COND = ("scaffolded", "minimal", "leading")
DESC = {
    "scaffolded": "with assumptions: the classical assumptions are listed and the model is asked which fails (upstream EVAL.json, the published condition)",
    "minimal": "without assumptions: only the observations and the contradiction (upstream EVAL_no_assumptions.json)",
    "leading": "scaffolded plus one hint paragraph pointing at the answer (tools/EVAL_leading.json, generated, D007)",
}

CSS = """
body{margin:0 auto;padding:1.5rem 2rem;max-width:1500px;font:14px/1.5 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:#1a1a1a;background:#fafafa}
h1{font-size:1.4rem;margin:0 0 .25rem}h2{font-size:1.15rem;margin:2.2rem 0 .5rem;padding-top:1rem;border-top:2px solid #ddd}
.sub{color:#6b6b6b;margin-bottom:1rem}
.legend{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:1rem 0 1.5rem}
.legend div{background:#fff;border:1px solid #e2e2e2;border-radius:6px;padding:.6rem .9rem;font-size:13px}
.legend b{display:block;margin-bottom:.2rem}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.col{background:#fff;border:1px solid #e2e2e2;border-radius:8px;padding:.9rem 1rem;min-width:0}
.col h3{margin:0 0 .4rem;font-size:.95rem;display:flex;justify-content:space-between;align-items:center}
.score{font-size:1.4rem;font-weight:700;padding:.05rem .6rem;border-radius:6px;background:#eef2f7;color:#2b4c7e}
.score.na{background:#f0f0f0;color:#999;font-size:.9rem;font-weight:400}
pre{white-space:pre-wrap;word-wrap:break-word;font-size:12.5px;line-height:1.5;margin:.4rem 0;padding:.6rem .8rem;border-radius:6px;border:1px solid #e2e2e2}
pre.prompt{background:#f6f6f6;max-height:260px;overflow:auto}
pre.answer{background:#fff;border-color:#cfd8e3}
mark{background:#fff3c4;padding:0 .15rem}
details{margin:.4rem 0}summary{cursor:pointer;color:#2b4c7e;font-weight:600;font-size:13px}
.rat{font-size:12.5px;color:#444;background:#f9f9f9;border-left:3px solid #cfd8e3;padding:.4rem .7rem;margin:.4rem 0}
.meta{font-size:11.5px;color:#6b6b6b}
table.sum{border-collapse:collapse;background:#fff;font-size:13px;margin:.5rem 0 1rem}
table.sum td,table.sum th{border:1px solid #e2e2e2;padding:.3rem .7rem;text-align:left}
table.sum th{background:#f0f0f0}
.nav{font-size:13px;margin:.5rem 0 1rem}.nav a{margin-right:.8rem}
@media(max-width:1100px){.grid,.legend{grid-template-columns:1fr}}
"""


def e(v):
    return "" if v is None else html.escape(str(v))


def hint_marked(prompt):
    """Highlight the appended hint paragraph in the leading prompt."""
    i = prompt.rfind("\n\nHint:")
    if i < 0:
        return e(prompt)
    return e(prompt[:i]) + "\n\n<mark>" + e(prompt[i + 2:]) + "</mark>"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="evidence/prompt-sensitivity")
    ap.add_argument("--checkpoint", default="discovery-rl-v11-s560")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    recs = {}
    for c in COND:
        p = os.path.join(a.dir, f"{c}.graded.jsonl")
        if not os.path.exists(p):
            p = os.path.join(a.dir, f"{c}.jsonl")
        recs[c] = [json.loads(l) for l in open(p) if l.strip()]

    by = defaultdict(dict)
    for c in COND:
        for r in recs[c]:
            if r["checkpoint_name"] == a.checkpoint and r["seed"] == a.seed:
                by[r["task_id"]][c] = r
    tasks = [t for t in (r["task_id"] for r in recs["scaffolded"]) if t in by]
    tasks = list(dict.fromkeys(tasks))

    # condition means across the whole file, for the header table
    def mean(c):
        s = [r["score"] for r in recs[c] if r.get("score") is not None]
        return (sum(s) / len(s), len(s)) if s else (None, 0)

    p = [f"<!doctype html><html><head><meta charset='utf-8'><title>Three prompt conditions</title><style>{CSS}</style></head><body>"]
    p.append("<h1>The same question asked three ways</h1>")
    p.append(f"<div class='sub'>{e(a.checkpoint)}, seed {a.seed}, temperature 0.7, top_k 50. "
             f"One answer per condition per task. Scores are from the provisional blinded grader (D008), not the paper's judge.</div>")
    p.append("<div class='legend'>" + "".join(f"<div><b>{c}</b>{e(DESC[c])}</div>" for c in COND) + "</div>")

    p.append("<table class='sum'><tr><th>condition</th><th>mean score, whole file</th><th>n</th><th>this checkpoint and seed, sum over 8 tasks</th></tr>")
    for c in COND:
        m, n = mean(c)
        here = [by[t][c].get("score") for t in tasks if c in by[t]]
        hs = sum(x for x in here if x is not None)
        p.append(f"<tr><td>{c}</td><td>{'' if m is None else f'{m:.2f}'}</td><td>{n}</td><td>{hs} / {5*len(here)}</td></tr>")
    p.append("</table>")

    p.append("<div class='nav'>" + " ".join(f"<a href='#{e(t)}'>{e(t)}</a>" for t in tasks) + "</div>")

    for t in tasks:
        title = by[t].get("scaffolded", {}).get("task_id", t)
        p.append(f"<h2 id='{e(t)}'>{e(title)}</h2><div class='grid'>")
        for c in COND:
            r = by[t].get(c)
            if not r:
                p.append(f"<div class='col'><h3>{c}</h3><div class='meta'>no record</div></div>")
                continue
            sc = r.get("score")
            badge = f"<span class='score'>{sc} / 5</span>" if sc is not None else "<span class='score na'>not graded</span>"
            p.append(f"<div class='col'><h3>{c} {badge}</h3>")
            p.append(f"<div class='meta'>{e(r.get('completion_tokens'))} tokens, {e(r.get('finish_reason'))}, seed {e(r.get('seed'))}</div>")
            body = hint_marked(r["prompt"]) if c == "leading" else e(r["prompt"])
            p.append(f"<details open><summary>Prompt</summary><pre class='prompt'>{body}</pre></details>")
            p.append(f"<details open><summary>Answer</summary><pre class='answer'>{e(r.get('completion'))}</pre></details>")
            raw = r.get("judge_raw_response")
            rat = None
            if raw:
                try:
                    j = json.loads(raw) if isinstance(raw, str) else raw
                    rat = j.get("rationale")
                    mc, ms = j.get("matched_concepts") or [], j.get("missing_concepts") or []
                except Exception:
                    rat = str(raw)[:600]; mc = ms = []
            if rat:
                p.append(f"<details><summary>Grader rationale</summary><div class='rat'>{e(rat)}</div>")
                if mc: p.append("<div class='meta'><b>matched:</b> " + "; ".join(e(x) for x in mc) + "</div>")
                if ms: p.append("<div class='meta'><b>missing:</b> " + "; ".join(e(x) for x in ms) + "</div>")
                p.append("</details>")
            p.append("</div>")
        p.append("</div>")

    p.append("</body></html>")
    out = a.out or os.path.join(a.dir, f"conditions-{a.checkpoint}-seed{a.seed}.html")
    with open(out, "w") as f:
        f.write("\n".join(p))
    print(f"{len(tasks)} tasks x 3 conditions -> {out}")


if __name__ == "__main__":
    main()

"""
One page for the open-ended elevator run: every answer in full, grouped by
checkpoint and prompt form, with a verdict column filled from a readings file.

    python tools/open_report.py evidence/elevator-open/open.jsonl \
        --readings evidence/elevator-open/readings.json \
        --html evidence/elevator-open/open_report.html

readings.json: {"reader": "...", "verdicts": {"<checkpoint>|<task_id>|<seed>": "<verdict>", ...}}
Verdicts: equivalence, bends-in-gravity, not-a-force, geometry, none, incoherent, loops.
Missing readings render grey. The page works without any readings.
"""

import argparse
import html
import json
from collections import Counter, defaultdict

VERDICTS = ["geometry", "not-a-force", "bends-in-gravity", "equivalence", "none", "loops", "incoherent"]
COLOR = {"geometry": "#1b7f3b", "not-a-force": "#2e8b57", "bends-in-gravity": "#4f9d69",
         "equivalence": "#8fbc8f", "none": "#999", "loops": "#a15c00", "incoherent": "#b3261e"}
RUNG = {"equivalence": 1, "bends-in-gravity": 2, "not-a-force": 3, "geometry": 4}

CSS = """
body{margin:0 auto;padding:1.5rem 2rem;max-width:1200px;font:14px/1.5 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:#1a1a1a;background:#fafafa}
h1{font-size:1.4rem;margin:0 0 .25rem}h2{font-size:1.15rem;margin:2rem 0 .5rem;border-top:2px solid #ddd;padding-top:1rem}
.sub{color:#6b6b6b;margin-bottom:1rem}
table{border-collapse:collapse;background:#fff;font-size:13px;margin:.5rem 0 1rem}
td,th{border:1px solid #e2e2e2;padding:.3rem .6rem;text-align:left;vertical-align:top}th{background:#f0f0f0}
.card{background:#fff;border:1px solid #e2e2e2;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0}
.card h3{margin:0 0 .3rem;font-size:.95rem;display:flex;gap:.6rem;align-items:center}
.v{font-size:11px;padding:.1rem .5rem;border-radius:999px;color:#fff;font-weight:600}
pre{white-space:pre-wrap;word-wrap:break-word;font-size:12.5px;line-height:1.5;margin:.3rem 0;padding:.6rem .8rem;border-radius:6px;border:1px solid #e2e2e2;background:#fff}
pre.prompt{background:#f6f6f6;max-height:200px;overflow:auto}
.meta{font-size:11.5px;color:#6b6b6b}details{margin:.3rem 0}summary{cursor:pointer;color:#2b4c7e;font-weight:600;font-size:13px}
.legend span{display:inline-block;margin-right:.6rem}
"""


def e(v):
    return "" if v is None else html.escape(str(v))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl")
    ap.add_argument("--readings", default=None)
    ap.add_argument("--html", required=True)
    a = ap.parse_args()

    rs = [json.loads(l) for l in open(a.jsonl) if l.strip()]
    readings = {"reader": None, "verdicts": {}}
    if a.readings:
        try:
            readings = json.load(open(a.readings))
        except FileNotFoundError:
            pass
    V = readings.get("verdicts", {})

    def key(r):
        return f"{r['checkpoint_name']}|{r['task_id']}|{r['seed']}"

    groups = defaultdict(list)
    for r in rs:
        groups[(r["checkpoint_name"], r["task_id"])].append(r)
    order = sorted(groups, key=lambda k: (k[0] != "d34-22btok", k[0], k[1]))

    p = [f"<!doctype html><html><head><meta charset='utf-8'><title>Elevator, open-ended</title><style>{CSS}</style></head><body>"]
    p.append("<h1>The elevator thought experiment with no rubric-shaped question</h1>")
    p.append(f"<div class='sub'>{len(rs)} continuations. Two prompt forms: the seven observations alone (continue), "
             f"and the seven observations plus one line, \"What follows from this?\" (ask). Temperature 0.7, seeds 42 to 49. "
             f"Base model d34-22btok runs in completion mode; RL checkpoints run in chat mode. That is a confound, stated. "
             f"Reader: {e(readings.get('reader') or 'none yet')}.</div>")
    p.append("<div class='legend'>" + "".join(f"<span class='v' style='background:{COLOR[v]}'>{v}</span>" for v in VERDICTS) + "</div>")
    p.append("<div class='sub'>Rungs: equivalence (1) says acceleration and gravity are alike; bends-in-gravity (2) infers light bends in a gravitational field; "
             "not-a-force (3) says gravity is not an ordinary force on mass; geometry (4) says gravity is the shape of space or spacetime. "
             "none: fluent but reaches no rung. loops: repeats itself. incoherent: not about the setup.</div>")

    # summary table
    p.append("<h2>Summary</h2><table><tr><th>checkpoint</th><th>mode</th><th>form</th><th>n</th><th>stock opener</th><th>hit max_tokens</th><th>mean tokens</th>"
             + "".join(f"<th>{v}</th>" for v in VERDICTS) + "<th>top rung</th></tr>")
    for ck, tid in order:
        g = groups[(ck, tid)]
        c = Counter(V.get(key(r), "unread") for r in g)
        rungs = [RUNG.get(V.get(key(r)), 0) for r in g]
        p.append(f"<tr><td>{e(ck)}</td><td>{e(g[0]['mode'])}</td><td>{e(tid.replace('elevator_open_',''))}</td><td>{len(g)}</td>"
                 f"<td>{sum(1 for r in g if (r['completion'] or '').startswith('You have touched'))}</td>"
                 f"<td>{sum(1 for r in g if r['finish_reason']=='length')}</td>"
                 f"<td>{sum(r['completion_tokens'] for r in g)//len(g)}</td>"
                 + "".join(f"<td>{c.get(v,0) or ''}</td>" for v in VERDICTS)
                 + f"<td>{max(rungs) if rungs else ''}</td></tr>")
    p.append("</table>")

    for ck, tid in order:
        g = sorted(groups[(ck, tid)], key=lambda r: r["seed"])
        p.append(f"<h2>{e(ck)} &nbsp;/&nbsp; {e(tid.replace('elevator_open_',''))} &nbsp;<span class='meta'>{e(g[0]['mode'])} mode</span></h2>")
        p.append(f"<details><summary>Prompt</summary><pre class='prompt'>{e(g[0]['prompt'])}</pre></details>")
        for r in g:
            v = V.get(key(r))
            badge = f"<span class='v' style='background:{COLOR.get(v,'#bbb')}'>{e(v)}</span>" if v else "<span class='v' style='background:#ccc'>unread</span>"
            p.append(f"<div class='card'><h3>seed {r['seed']} {badge}<span class='meta'>{r['completion_tokens']} tokens, {r['finish_reason']}</span></h3>")
            p.append(f"<pre>{e(r['completion'])}</pre></div>")

    p.append("</body></html>")
    open(a.html, "w").write("\n".join(p))
    print(f"{len(rs)} records, {sum(1 for r in rs if key(r) in V)} read -> {a.html}")


if __name__ == "__main__":
    main()

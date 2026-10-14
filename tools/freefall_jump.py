"""
The jump count for the free-fall seed and bare conditions.

Seed and bare answers were given only the falling-person observation. This
tallies, per checkpoint, how many answers contain the ideas the prompt
withheld. Two layers, like probe_report.py:

1. Keyword flags, automatic and generous: does the answer mention an
   accelerating cabin, room, elevator or vessel; the words equivalent or
   equivalence; gravity as not a force, or as geometry/curvature/structure of
   space. A flag is a candidate, not a verdict.
2. Blind verdicts from a readings file, one per answer, highest rung:
   equivalence, not-a-force, geometry, none, loops, incoherent. The verdict
   column is what the paper reports; the flags are there so a reader can see
   what the automatic pass would have said.

    python tools/freefall_jump.py evidence/freefall/seed.jsonl \
        --readings evidence/freefall/readings.json --html evidence/freefall/jump.html
"""

import argparse
import html
import json
import re
from collections import Counter, defaultdict

E = html.escape
FLAGS = {
    "accelerating-cabin": r"\b(accelerat\w*\s+(cabin|room|elevator|lift|car|vessel|chamber|box)|(cabin|room|elevator|lift|vessel|chamber)\s+(that\s+)?(is\s+)?accelerat\w*)\b",
    "equivalence": r"\bequivalen\w*\b",
    "not-a-force": r"\b(not\s+(a|an)\s+(ordinary\s+|true\s+|real\s+)?force|no\s+force\s+at\s+all|not\s+a\s+pull)\b",
    "geometry": r"\b(geometry|curvature|curved\s+space|shape\s+of\s+space|structure\s+of\s+space)\b",
}
VERD = ["loops", "incoherent", "none", "equivalence", "not-a-force", "geometry"]
RUNG = {"equivalence": 1, "not-a-force": 2, "geometry": 3}

CSS = """
body{margin:0 auto;padding:1.5rem 2rem;max-width:1200px;font:14px/1.5 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;background:#fafafa;color:#1a1a1a}
h1{font-size:1.4rem;margin:0 0 .3rem}h2{font-size:1.15rem;margin:2rem 0 .5rem;border-top:2px solid #ddd;padding-top:1rem}.sub{color:#666;margin-bottom:1rem}
table{border-collapse:collapse;background:#fff;font-size:13px;margin:.5rem 0}td,th{border:1px solid #e2e2e2;padding:.3rem .6rem;text-align:left;vertical-align:top}th{background:#f0f0f0}
.card{background:#fff;border:1px solid #e2e2e2;border-radius:8px;padding:.8rem 1rem;margin:.7rem 0}.card h3{margin:0 0 .3rem;font-size:.95rem;display:flex;gap:.5rem;align-items:center;flex-wrap:wrap}
.v{font-size:11px;padding:.1rem .5rem;border-radius:999px;color:#fff;font-weight:600}.f{font-size:11px;padding:.05rem .4rem;border-radius:3px;background:#eef2f7;color:#2b4c7e}
pre{white-space:pre-wrap;word-wrap:break-word;font-size:12.5px;line-height:1.5;margin:.3rem 0;padding:.6rem .8rem;border-radius:6px;border:1px solid #e2e2e2;background:#fff}
mark{background:#fff3c4}.meta{font-size:11.5px;color:#666}
"""
COLOR = {"geometry": "#1b7f3b", "not-a-force": "#2e8b57", "equivalence": "#8fbc8f", "none": "#999", "loops": "#a15c00", "incoherent": "#b3261e"}


def flags_for(text):
    t = text or ""
    return [k for k, rx in FLAGS.items() if re.search(rx, t, re.I)]


def mark(text):
    out = E(text or "")
    for rx in FLAGS.values():
        out = re.sub("(" + rx + ")", r"<mark>\1</mark>", out, flags=re.I)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl")
    ap.add_argument("--readings", default=None)
    ap.add_argument("--html", required=True)
    a = ap.parse_args()
    rs = [json.loads(l) for l in open(a.jsonl) if l.strip()]
    R = {"reader": None, "verdicts": {}, "notes": {}}
    if a.readings:
        try: R = json.load(open(a.readings))
        except FileNotFoundError: pass
    V, N = R.get("verdicts", {}), R.get("notes", {})
    key = lambda r: f"{r['checkpoint_name']}|{r['task_id']}|{r['seed']}"
    step = lambda ck: int(ck.rsplit("s", 1)[-1])

    groups = defaultdict(list)
    for r in rs: groups[(r["task_id"], r["checkpoint_name"])].append(r)
    tasks = sorted({r["task_id"] for r in rs}); cks = sorted({r["checkpoint_name"] for r in rs}, key=step)

    p = [f"<!doctype html><html><head><meta charset='utf-8'><title>Free fall, the jump</title><style>{CSS}</style></head><body>"]
    p.append("<h1>The 1907 observation alone: does the model supply the equivalence?</h1>")
    p.append(f"<div class='sub'>{len(rs)} answers. The prompt gives only the falling person and the floating objects. It never mentions an accelerating cabin, "
             f"equivalence, or gravity disappearing. Any of those in an answer came from the model. Reader: {E(R.get('reader') or 'none yet')}. "
             "Flags are automatic keyword hits, generous, shown so the reader's verdict can be checked against them.</div>")

    # totals per task
    p.append("<h2>Totals</h2><table><tr><th>form</th><th>n</th>" + "".join(f"<th>{v}</th>" for v in VERD) + "<th>flag: cabin</th><th>flag: equivalen*</th><th>flag: not-a-force</th><th>flag: geometry</th><th>stock opener</th><th>hit max</th></tr>")
    for t in tasks:
        g = [r for r in rs if r["task_id"] == t]; c = Counter(V.get(key(r), "unread") for r in g); fl = Counter(f for r in g for f in flags_for(r["completion"]))
        p.append(f"<tr><td>{E(t.replace('gr_freefall_',''))}</td><td>{len(g)}</td>" + "".join(f"<td>{c.get(v,'') or ''}</td>" for v in VERD)
                 + f"<td>{fl.get('accelerating-cabin',0)}</td><td>{fl.get('equivalence',0)}</td><td>{fl.get('not-a-force',0)}</td><td>{fl.get('geometry',0)}</td>"
                 + f"<td>{sum(1 for r in g if (r['completion'] or '').startswith('You have touched'))}</td><td>{sum(1 for r in g if r['finish_reason']=='length')}</td></tr>")
    p.append("</table>")

    # per checkpoint
    p.append("<h2>Per checkpoint</h2><table><tr><th>checkpoint</th>" + "".join(f"<th>{t.replace('gr_freefall_','')}: top rung / n</th>" for t in tasks) + "</tr>")
    for ck in cks:
        cells = []
        for t in tasks:
            g = groups[(t, ck)]; rungs = [RUNG.get(V.get(key(r)), 0) for r in g]
            cells.append(f"<td>{max(rungs) if rungs else ''} / {len(g)} &nbsp;<span class='meta'>{', '.join(V.get(key(r),'?') for r in g)}</span></td>")
        p.append(f"<tr><td>{E(ck)}</td>{''.join(cells)}</tr>")
    p.append("</table><p class='meta'>Rungs: equivalence 1, not-a-force 2, geometry 3. 0 means none, loops or incoherent.</p>")

    # every answer
    for t in tasks:
        p.append(f"<h2>{E(t)}</h2>")
        g0 = next(r for r in rs if r["task_id"] == t)
        p.append(f"<details><summary>Prompt</summary><pre>{E(g0['prompt'])}</pre></details>")
        for ck in cks:
            for r in sorted(groups[(t, ck)], key=lambda r: r["seed"]):
                v = V.get(key(r)); fl = flags_for(r["completion"])
                badge = f"<span class='v' style='background:{COLOR.get(v,'#bbb')}'>{E(v)}</span>" if v else "<span class='v' style='background:#ccc'>unread</span>"
                p.append(f"<div class='card'><h3>{E(ck)} seed {r['seed']} {badge}" + "".join(f"<span class='f'>{f}</span>" for f in fl)
                         + f"<span class='meta'>{r['completion_tokens']} tok, {r['finish_reason']}</span></h3>")
                if N.get(key(r)): p.append(f"<div class='meta'>{E(N[key(r)])}</div>")
                p.append(f"<pre>{mark(r['completion'])}</pre></div>")
    p.append("</body></html>")
    open(a.html, "w").write("\n".join(p))
    print(f"{len(rs)} answers, {sum(1 for r in rs if key(r) in V)} read, flags: {Counter(f for r in rs for f in flags_for(r['completion']))} -> {a.html}")


if __name__ == "__main__":
    main()

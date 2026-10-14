"""
One page for an open-ended run read blind: verdict counts per task and
checkpoint, the ladder's top rung, and every answer with its verdict.
Verdict order and meanings come from the eval config, so the same tool
serves the abduction suite and the final elevator case.

    python tools/abduction_report.py evidence/abduction/abduction.jsonl \
        --config tools/EVAL_abduction.json --readings evidence/abduction/readings.json \
        --html evidence/abduction/report.html
"""

import argparse
import html
import json
from collections import Counter, defaultdict

E = html.escape
COLOR = {"geometry": "#1b7f3b", "not-a-force": "#2e8b57", "equivalence": "#8fbc8f", "weightless": "#9fc5e8",
         "correct": "#1b7f3b", "partial": "#e0b96a", "wrong": "#b3261e", "none": "#999",
         "loops": "#a15c00", "incoherent": "#b3261e"}
RUNG = {"wrong": 0, "none": 0, "weightless": 1, "equivalence": 2, "not-a-force": 3, "geometry": 4,
        "correct": 2, "partial": 1}
CSS = """
body{margin:0 auto;padding:1.5rem 2rem;max-width:1200px;font:14px/1.5 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;background:#fafafa;color:#1a1a1a}
h1{font-size:1.4rem;margin:0 0 .3rem}h2{font-size:1.15rem;margin:2rem 0 .5rem;border-top:2px solid #ddd;padding-top:1rem}h3{font-size:1rem;margin:1.2rem 0 .4rem}.sub{color:#666;margin-bottom:1rem}
table{border-collapse:collapse;background:#fff;font-size:13px;margin:.5rem 0}td,th{border:1px solid #e2e2e2;padding:.3rem .6rem;text-align:left;vertical-align:top}th{background:#f0f0f0}td.n{text-align:right}
.card{background:#fff;border:1px solid #e2e2e2;border-radius:8px;padding:.8rem 1rem;margin:.7rem 0}.card h4{margin:0 0 .3rem;font-size:.95rem;display:flex;gap:.5rem;align-items:center;flex-wrap:wrap}
.v{font-size:11px;padding:.1rem .5rem;border-radius:999px;color:#fff;font-weight:600}
pre{white-space:pre-wrap;word-wrap:break-word;font-size:12.5px;line-height:1.5;margin:.3rem 0;padding:.6rem .8rem;border-radius:6px;border:1px solid #e2e2e2;background:#fff}
.meta{font-size:11.5px;color:#666}.q{background:#f6f6f6}
"""


def step(ck):
    return int(ck.rsplit("s", 1)[-1]) if ck.startswith("discovery-rl-v11-") else -1


def final_results(rs, cfg, V, N, key, cks, tasks, reading, PL):
    """Headline card: the counts a reader needs before anything else.
    Elevator = final + ladder groups. Controls shown for trained checkpoints only."""
    trained = [ck for ck in cks if step(ck) >= 0]
    base = [ck for ck in cks if step(ck) < 0]
    elev = [t for t in tasks if cfg[t].get("group") in ("final", "ladder")]
    ctrl = [t for t in tasks if cfg[t].get("group") == "control"]
    if not elev:
        return ""
    ea = [r for r in rs if r["task_id"] in elev]
    c = Counter(V.get(key(r), "unread") for r in ea)
    eqg = sum(1 for r in ea if V.get(key(r)) in ("equivalence", "geometry"))
    naf = [r for r in ea if V.get(key(r)) == "not-a-force"]
    order = ["wrong", "none", "weightless", "equivalence", "not-a-force", "geometry", "loops", "incoherent", "unread"]
    seeds = len({r["seed"] for r in ea})
    p = ["<div class='card' style='border-left:6px solid #1b7f3b'><h3 style='margin-top:0'>Final results</h3>"]
    p.append(f"<p style='font-size:1.3rem;margin:.2rem 0 .2rem'><b>{eqg} of {len(ea)}</b> elevator answers reached equivalence or geometry, the jump.</p>")
    if naf:
        bytask = Counter(r["task_id"] for r in naf)
        p.append(f"<p style='margin:.2rem 0'>{len(naf)} answers said gravity is not a force. Not counted as the jump. They came from this prompt:</p>")
        for t in sorted(bytask):
            p.append(f"<pre class='q'>{E(next(r for r in rs if r['task_id'] == t)['prompt'])}</pre>")
        p.append("<p style='margin:.2rem 0'>The prompt tells the model its idea of gravity is mistaken. These answers repeat that back and give no reason, nothing about acceleration.</p>")
    if ctrl:
        ca = [r for r in rs if r["task_id"] in ctrl and r["checkpoint_name"] in trained]
        cc = Counter(V.get(key(r), "unread") for r in ca)
        p.append(f"<p style='font-size:1.1rem;margin:.2rem 0 .2rem'><b>{cc['correct']} of {len(ca)}</b> control answers correct from the trained checkpoints, {cc['partial']} partial, {cc['wrong']} wrong.</p>")
    p.append("<div style='display:flex;height:22px;border-radius:6px;overflow:hidden;border:1px solid #ddd;margin:.3rem 0'>")
    for v in order:
        if c.get(v):
            p.append(f"<div title='{E(v)} {c[v]}' style='width:{100*c[v]/len(ea):.1f}%;background:{COLOR.get(v, '#bbb')}'></div>")
    p.append("</div>")
    p.append("<p>" + " &nbsp; ".join(f"<span class='v' style='background:{COLOR.get(v, '#bbb')}'>{E(v)}</span> {c[v]}" for v in order if c.get(v))
             + f" &nbsp; <span class='meta'>of {len(ea)}: {len(elev)} prompts, {len(cks)} checkpoints, {seeds} seeds each</span></p>")
    if PL:
        p.append("<p style='margin:.8rem 0 .2rem'><b>The questions.</b></p><table>")
        for g in dict.fromkeys(cfg[t].get("group", "") for t in tasks):
            for t in tasks:
                if cfg[t].get("group", "") == g and t in PL:
                    p.append(f"<tr><td class='meta'>{E(g)}</td><td><b>{E(t)}</b></td><td>{E(PL[t])}</td></tr>")
        p.append("</table>")
    p.append("<p style='margin:.8rem 0 .2rem'><b>Elevator prompts, trained checkpoints only.</b></p>")
    p.append("<table><tr><th>elevator prompt</th><th>group</th><th>trained answers</th><th>wrong</th><th>none</th><th>weightless</th><th>equivalence or geometry</th><th>not-a-force</th></tr>")
    for t in elev:
        g = [r for r in rs if r["task_id"] == t and r["checkpoint_name"] in trained]
        cc = Counter(V.get(key(r), "unread") for r in g)
        p.append(f"<tr><td><b>{E(t)}</b></td><td>{E(cfg[t].get('group', ''))}</td><td class='n'>{len(g)}</td><td class='n'>{cc['wrong']}</td><td class='n'>{cc['none']}</td><td class='n'>{cc['weightless']}</td><td class='n'>{cc['equivalence'] + cc['geometry']}</td><td class='n'>{cc['not-a-force']}</td></tr>")
    p.append("</table>")
    if ctrl:
        p.append("<p style='margin:.8rem 0 .2rem'><b>Controls, trained checkpoints only.</b> Reasoning a reader of the corpus could do.</p>")
        p.append("<table><tr><th>control prompt</th><th>type</th><th>in corpus</th><th>trained answers</th><th>correct</th><th>partial</th><th>wrong</th><th>none</th><th>other</th></tr>")
        for t in ctrl:
            g = [r for r in rs if r["task_id"] == t and r["checkpoint_name"] in trained]
            cc = Counter(V.get(key(r), "unread") for r in g)
            other = len(g) - cc["correct"] - cc["partial"] - cc["wrong"] - cc["none"]
            p.append(f"<tr><td><b>{E(t)}</b></td><td>{E(cfg[t].get('reasoning', ''))}</td><td>{'yes' if cfg[t].get('in_corpus') else 'no'}</td><td class='n'>{len(g)}</td>"
                     f"<td class='n'>{cc['correct']}</td><td class='n'>{cc['partial']}</td><td class='n'>{cc['wrong']}</td><td class='n'>{cc['none']}</td><td class='n'>{other}</td></tr>")
        p.append("</table>")
    if base:
        ba = [r for r in rs if r["checkpoint_name"] in base]
        bl = sum(1 for r in ba if V.get(key(r)) == "loops")
        p.append(f"<p class='meta'>Base model ({', '.join(E(b) for b in base)}) is left out of the two tables above: it loops in {bl} of its {len(ba)} answers. Full counts with it included are in the Per prompt table.</p>")
    if reading:
        p.append(f"<p><b>Reading.</b> {E(reading)}</p>")
    p.append("</div>")
    return "\n".join(p)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl")
    ap.add_argument("--config", required=True)
    ap.add_argument("--readings", default=None)
    ap.add_argument("--html", required=True)
    ap.add_argument("--title", default="Open-ended run, read blind")
    ap.add_argument("--reading", default=None, help="one paragraph, plain words, what the numbers mean; shown at the top")
    ap.add_argument("--plain", default="tools/abduction_plain.json", help="json: task id -> one plain-words line about the prompt")
    a = ap.parse_args()

    rs = [json.loads(l) for l in open(a.jsonl) if l.strip()]
    cfg = {t["id"]: t for t in json.load(open(a.config))["tasks"]}
    R = {"reader": None, "verdicts": {}, "notes": {}}
    if a.readings:
        try:
            R = json.load(open(a.readings))
        except FileNotFoundError:
            pass
    V, N = R.get("verdicts", {}), R.get("notes", {})
    try:
        PL = {k: v for k, v in json.load(open(a.plain)).items() if not k.startswith("_")}
    except FileNotFoundError:
        PL = {}
    key = lambda r: f"{r['checkpoint_name']}|{r['task_id']}|{r['seed']}"
    tasks = [t for t in cfg if any(r["task_id"] == t for r in rs)]
    cks = sorted({r["checkpoint_name"] for r in rs}, key=step)
    groups = defaultdict(list)
    for r in rs:
        groups[(r["task_id"], r["checkpoint_name"])].append(r)

    p = [f"<!doctype html><html><head><meta charset='utf-8'><title>{E(a.title)}</title><style>{CSS}</style></head><body>"]
    p.append(f"<h1>{E(a.title)}</h1>")
    p.append(f"<div class='sub'>{len(rs)} answers, {len(tasks)} prompts, {len(cks)} checkpoints. Reader: {E(R.get('reader') or 'none yet')}. "
             "The reader saw only the prompt, the expected answer, the verdict list and the text; never the checkpoint or seed.</div>")
    p.append(final_results(rs, cfg, V, N, key, cks, tasks, a.reading, PL))

    # ---- what this page shows: the question, the ladder, the reading ----
    p.append("<div class='card' style='border-left:6px solid #2b4c7e'><h3 style='margin-top:0'>What this page shows</h3>")
    if len(tasks) == 1:
        p.append(f"<p><b>The question put to the model, in full:</b></p><pre class='q'>{E(next(r for r in rs if r['task_id'] == tasks[0])['prompt'])}</pre>")
        p.append(f"<p><b>A fully correct answer would say:</b> {E(cfg[tasks[0]].get('expected', ''))}</p>")
    else:
        p.append(f"<p>{len(tasks)} prompts in groups: " + ", ".join(f"<b>{E(g)}</b>" for g in dict.fromkeys(cfg[t].get('group', '') for t in tasks)) + ". Each prompt's full text and expected answer are shown in its own section below.</p>")
    p.append("<p><b>How each answer was judged.</b> One verdict per answer, the highest rung it reaches on its own. For the gravity prompts, low to high:</p><table>")
    ladder = [("wrong", "says you still feel your weight, or a heavier body falls faster. The Newtonian answer, stated as fact."),
              ("none", "on topic but never says what is felt. Prose about cables, levers, gravity on every particle."),
              ("weightless", "says you feel no weight, float, the stone stays by your hand, the scale reads nothing. This is Einstein's 1907 observation, the step before the jump."),
              ("equivalence", "brings in acceleration on its own: an accelerating cabin would feel like gravity, falling cancels gravity the way acceleration creates it. This is the jump."),
              ("not-a-force", "says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it."),
              ("geometry", "says gravity is the shape or structure of space. Beyond the jump."),
              ("loops", "the text repeats itself until the token limit."),
              ("incoherent", "cannot be read as an answer.")]
    for v, meaning in ladder:
        p.append(f"<tr><td><span class='v' style='background:{COLOR.get(v, '#bbb')}'>{E(v)}</span></td><td>{E(meaning)}</td></tr>")
    if any(cfg[t].get("group") == "control" for t in tasks):
        p.append("<tr><td colspan='2' class='meta'>Control prompts (deduction, induction, abduction inside and beyond the corpus) use: correct, partial, wrong, none, with the meaning of each stated in that prompt's section.</td></tr>")
    p.append("</table>")
    p.append("</div>")

    # ---- per task totals ----
    p.append("<h2>Per prompt</h2><table><tr><th>group</th><th>prompt</th><th>type</th><th>in corpus</th><th>n</th><th>verdicts</th><th>made the jump (equivalence or beyond)</th><th>stock opener</th><th>hit max</th></tr>")
    for t in tasks:
        g = [r for r in rs if r["task_id"] == t]; c = Counter(V.get(key(r), "unread") for r in g)
        order = cfg[t].get("verdicts", []) + ["unread"]
        cells = " &nbsp; ".join(f"<span class='v' style='background:{COLOR.get(v, '#bbb')}'>{E(v)}</span> {c[v]}" for v in order if c.get(v))
        high = sum(1 for r in g if RUNG.get(V.get(key(r)), 0) >= 2)
        p.append(f"<tr><td>{E(cfg[t].get('group',''))}</td><td><b>{E(t)}</b></td><td>{E(cfg[t].get('reasoning',''))}</td><td>{'yes' if cfg[t].get('in_corpus') else 'no'}</td>"
                 f"<td class='n'>{len(g)}</td><td>{cells}</td><td class='n'>{high} / {len(g)}</td>"
                 f"<td class='n'>{sum(1 for r in g if (r['completion'] or '').startswith('You have touched'))}</td>"
                 f"<td class='n'>{sum(1 for r in g if r.get('finish_reason') == 'length')}</td></tr>")
    p.append("</table><p class='meta'>For gravity prompts the jump column counts equivalence, not-a-force and geometry; for control prompts it counts correct.</p>")

    # ---- per checkpoint x task ----
    p.append("<h2>Per checkpoint</h2><div style='overflow-x:auto'><table><tr><th>checkpoint</th>" + "".join(f"<th>{E(t)}</th>" for t in tasks) + "</tr>")
    for ck in cks:
        cells = []
        for t in tasks:
            g = groups[(t, ck)]
            vs = [V.get(key(r), "?") for r in sorted(g, key=lambda r: r["seed"])]
            cells.append("<td>" + " ".join(f"<span class='v' style='background:{COLOR.get(v, '#bbb')}'>{E(v)}</span>" for v in vs) + "</td>")
        p.append(f"<tr><td>{E(ck)}</td>{''.join(cells)}</tr>")
    p.append("</table></div>")

    # ---- every answer ----
    for t in tasks:
        tc = cfg[t]
        p.append(f"<h2>{E(t)} <span class='meta'>{E(tc.get('group',''))}, {E(tc.get('reasoning',''))}, {'in corpus' if tc.get('in_corpus') else 'beyond corpus'}</span></h2>")
        g0 = next(r for r in rs if r["task_id"] == t)
        if t in PL:
            p.append(f"<p>{E(PL[t])}</p>")
        p.append(f"<pre class='q'>{E(g0['prompt'])}</pre><p class='meta'><b>Expected.</b> {E(tc.get('expected',''))}</p>")
        for ck in cks:
            for r in sorted(groups[(t, ck)], key=lambda r: r["seed"]):
                v = V.get(key(r))
                badge = f"<span class='v' style='background:{COLOR.get(v, '#bbb')}'>{E(v)}</span>" if v else "<span class='v' style='background:#ccc'>unread</span>"
                p.append(f"<div class='card'><h4>{E(ck)} seed {r['seed']} {badge}<span class='meta'>{r.get('completion_tokens')} tok, {r.get('finish_reason')}</span></h4>")
                if N.get(key(r)):
                    p.append(f"<div class='meta'>{E(N[key(r)])}</div>")
                p.append(f"<pre>{E(r.get('completion') or r.get('error') or '')}</pre></div>")
    p.append("</body></html>")
    open(a.html, "w").write("\n".join(p))
    print(f"{len(rs)} answers, {sum(1 for r in rs if key(r) in V)} read -> {a.html}")


if __name__ == "__main__":
    main()

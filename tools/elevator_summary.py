"""
One presentable page for the 30 Sep elevator results, every number computed
from the evidence files at render time.

    python tools/elevator_summary.py --html evidence/elevator/summary.html
"""

import argparse
import html
import json
import os
import random
import statistics as st
from collections import Counter, defaultdict

E = html.escape


def load(p):
    return [json.loads(l) for l in open(p) if l.strip()]


def ci(xs, B=4000, seed=0):
    r = random.Random(seed); n = len(xs)
    ms = sorted(st.mean(r.choices(xs, k=n)) for _ in range(B))
    return ms[int(.025 * B)], ms[int(.975 * B)]


def step(ck):
    return int(ck.rsplit("s", 1)[-1])


CSS = """
body{margin:0 auto;padding:2rem;max-width:1100px;font:15px/1.5 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:#1a1a1a;background:#fff}
h1{font-size:1.6rem;margin:0 0 .3rem}h2{font-size:1.2rem;margin:2.4rem 0 .6rem;padding-top:1rem;border-top:2px solid #e2e2e2}
.sub{color:#666;margin-bottom:1.2rem}
.big{display:flex;gap:2rem;flex-wrap:wrap;margin:1rem 0}
.big div{flex:1;min-width:200px;background:#f7f8fa;border-radius:10px;padding:1rem 1.2rem}
.big b{display:block;font-size:2.4rem;line-height:1.1;color:#2b4c7e}.big span{color:#555;font-size:13px}
table{border-collapse:collapse;width:100%;font-size:14px;margin:.6rem 0}
th,td{border-bottom:1px solid #e2e2e2;padding:.45rem .7rem;text-align:left;vertical-align:top}th{background:#f0f0f0;font-weight:600}
td.n{text-align:right;font-variant-numeric:tabular-nums}th.n{text-align:right}
.hist{font-family:ui-monospace,Menlo,monospace;font-size:13px;letter-spacing:.02em}
.bar{display:inline-block;height:12px;background:#2b4c7e;vertical-align:middle;border-radius:2px}
.bar.l{background:#1b7f3b}.bar.m{background:#999}
.note{background:#fff8e6;border-left:4px solid #e0b96a;padding:.6rem .9rem;margin:1rem 0;font-size:14px}
.src{font-size:12px;color:#777;font-family:ui-monospace,Menlo,monospace}
.quote{background:#f7f8fa;border-left:4px solid #cfd8e3;padding:.6rem .9rem;margin:.6rem 0;font-size:14px;white-space:pre-wrap}
a{color:#2b4c7e}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", required=True)
    a = ap.parse_args()

    D = {c: load(f"evidence/elevator/{c}.graded.jsonl") for c in ("scaffolded", "minimal", "leading")}
    OPEN = load("evidence/elevator-open/open.jsonl")
    R = json.load(open("evidence/elevator-open/readings.json"))
    V = R["verdicts"]
    pub = {}
    for line in open("upstream/gpt1900/results/physics_eval_v11/summary.txt"):
        if line.startswith("discovery-rl-v11-"):
            p = line.split(); pub[p[0]] = float(p[7])
    hint = next(t for t in json.load(open("tools/EVAL_elevator_leading.json"))["tasks"])["prompt_lines"][-1]
    rubric = next(t for t in json.load(open("tools/EVAL_elevator_scaffolded.json"))["tasks"])["scoring_rubric"]

    # ---- deep run stats ----
    S = {c: [r["score"] for r in D[c]] for c in D}
    key = lambda r: (r["checkpoint_name"], r["seed"])
    ls = {key(r): r["score"] for r in D["leading"]}; ss = {key(r): r["score"] for r in D["scaffolded"]}; ms = {key(r): r["score"] for r in D["minimal"]}
    d_ls = [ls[k] - ss[k] for k in ss]; d_sm = [ss[k] - ms[k] for k in ss]
    cks = sorted({r["checkpoint_name"] for r in D["scaffolded"]}, key=step)
    per = {c: {ck: st.mean([r["score"] for r in D[c] if r["checkpoint_name"] == ck]) for ck in cks} for c in D}
    stock = {c: sum(1 for r in D[c] if (r["completion"] or "").startswith("You have touched")) for c in D}

    # ---- regrade ----
    ex = w1 = tot = 0
    for b in ("01", "05"):
        g = {json.loads(l)["id"]: json.loads(l)["score"] for l in open(f"evidence/review-packet-elevator/grades/batch-{b}.jsonl")}
        rg = {json.loads(l)["id"]: json.loads(l)["score"] for l in open(f"evidence/review-packet-elevator/grades-repeat/batch-{b}.jsonl")}
        ex += sum(1 for k in g if g[k] == rg[k]); w1 += sum(1 for k in g if abs(g[k] - rg[k]) <= 1); tot += len(g)

    # ---- open run ----
    VERD = ["loops", "incoherent", "none", "equivalence", "bends-in-gravity", "not-a-force", "geometry"]
    okey = lambda r: f"{r['checkpoint_name']}|{r['task_id']}|{r['seed']}"
    ocks = ["d34-22btok", "discovery-rl-v11-s035", "discovery-rl-v11-s560", "discovery-rl-v11-s839"]
    ocount = {ck: Counter(V.get(okey(r)) for r in OPEN if r["checkpoint_name"] == ck) for ck in ocks}
    ostock = {ck: sum(1 for r in OPEN if r["checkpoint_name"] == ck and (r["completion"] or "").startswith("You have touched")) for ck in ocks}
    olen = {ck: sum(1 for r in OPEN if r["checkpoint_name"] == ck and r["finish_reason"] == "length") for ck in ocks}
    on = {ck: sum(1 for r in OPEN if r["checkpoint_name"] == ck) for ck in ocks}

    def hist(xs, cls=""):
        c = Counter(xs); n = len(xs)
        return " ".join(f"<span class='hist'>{i}:</span><span class='bar {cls}' style='width:{int(120*c.get(i,0)/n)}px'></span><span class='hist'>{c.get(i,0)}</span>" for i in range(5))

    p = [f"<!doctype html><html><head><meta charset='utf-8'><title>Elevator results</title><style>{CSS}</style></head><body>"]
    p.append("<h1>The elevator task, 30 Sep 2026</h1>")
    p.append("<div class='sub'>GPT-1900, task <code>gr_main_elevator_light</code>. Two runs on SDSC Expanse, 28 Sep. "
             "Every number on this page is computed from the JSONL under <code>evidence/</code> when the page is rendered. "
             "Grader: blinded reader in fresh sessions of 24, provenance stripped, upstream's rubric, provisional (D008).</div>")

    # ---- headline ----
    lo, hi = ci(d_ls)
    p.append("<div class='big'>")
    p.append(f"<div><b>{st.mean(d_ls):+.2f}</b><span>hint effect on the elevator, leading minus scaffolded, paired n={len(d_ls)}<br>95% CI {lo:+.2f} to {hi:+.2f}</span></div>")
    p.append(f"<div><b>{max(S['scaffolded'])}</b><span>highest score without the hint, in {len(S['scaffolded'])} tries</span></div>")
    p.append(f"<div><b>{sum(1 for s in S['leading'] if s>=3)} / {len(S['leading'])}</b><span>answers scoring 3 or 4 with the hint</span></div>")
    p.append(f"<div><b>0 / {len(OPEN)}</b><span>open-ended continuations that reach \"gravity is geometry\"</span></div>")
    p.append("</div>")

    # ---- run 1 ----
    p.append("<h2>Run 1. The rubric task, three wordings, all 24 checkpoints</h2>")
    p.append(f"<div class='sub'>24 checkpoints x 3 seeds (42, 43, 44) = 72 answers per wording, 216 total, 0 errors. Temperature 0.7, top_k 50, one sample per call. "
             f"<span class='src'>evidence/elevator/{{scaffolded,minimal,leading}}.graded.jsonl</span></div>")
    p.append("<table><tr><th>wording</th><th>what the model sees</th><th class='n'>n</th><th class='n'>mean</th><th>95% CI</th><th>score histogram 0 to 4</th><th class='n'>stock opener</th></tr>")
    desc = {"minimal": "the observations and the contradiction only", "scaffolded": "plus the classical assumptions listed (the published condition)", "leading": "scaffolded plus one hint paragraph"}
    for c, cls in (("minimal", "m"), ("scaffolded", ""), ("leading", "l")):
        lo, hi = ci(S[c])
        p.append(f"<tr><td><b>{c}</b></td><td>{desc[c]}</td><td class='n'>{len(S[c])}</td><td class='n'><b>{st.mean(S[c]):.2f}</b></td><td>{lo:.2f} to {hi:.2f}</td><td>{hist(S[c], cls)}</td><td class='n'>{stock[c]} / {len(S[c])}</td></tr>")
    p.append("</table>")
    lo2, hi2 = ci(d_sm)
    p.append(f"<p>Paired differences, same checkpoint and seed: leading minus scaffolded <b>{st.mean(d_ls):+.2f}</b> ({lo:+.2f} to {hi:+.2f}); "
             f"scaffolded minus minimal <b>{st.mean(d_sm):+.2f}</b> ({lo2:+.2f} to {hi2:+.2f}).</p>")
    p.append(f"<div class='note'><b>The hint.</b> The leading wording appends one paragraph to the published prompt:<div class='quote'>{E(hint)}</div>"
             f"Rubric level 4 reads: <i>{E(rubric['4'])}</i>. Level 5: <i>{E(rubric['5'])}</i>. The hint states them.</div>")

    # ---- per checkpoint ----
    p.append("<h2>Per checkpoint, three wordings beside the published score</h2>")
    p.append("<div class='sub'>Each cell is the mean of 3 seeds. Published column is the authors' single graded answer per checkpoint, their judge. "
             "<span class='src'>upstream/gpt1900/results/physics_eval_v11/summary.txt, Elev column</span></div>")
    p.append("<table><tr><th>checkpoint</th><th class='n'>minimal</th><th class='n'>scaffolded</th><th class='n'>leading</th><th class='n'>published</th></tr>")
    for ck in cks:
        p.append(f"<tr><td>{E(ck)}</td><td class='n'>{per['minimal'][ck]:.2f}</td><td class='n'>{per['scaffolded'][ck]:.2f}</td><td class='n'><b>{per['leading'][ck]:.2f}</b></td><td class='n'>{pub.get(ck, float('nan')):.2f}</td></tr>")
    f8 = lambda c, sl: st.mean([r["score"] for r in D[c] if r["checkpoint_name"] in cks[sl]])
    p.append(f"<tr><th>first 8 checkpoints</th><th class='n'>{f8('minimal', slice(0,8)):.2f}</th><th class='n'>{f8('scaffolded', slice(0,8)):.2f}</th><th class='n'>{f8('leading', slice(0,8)):.2f}</th><th class='n'>{st.mean([pub[c] for c in cks[:8]]):.2f}</th></tr>")
    p.append(f"<tr><th>last 8 checkpoints</th><th class='n'>{f8('minimal', slice(-8,None)):.2f}</th><th class='n'>{f8('scaffolded', slice(-8,None)):.2f}</th><th class='n'>{f8('leading', slice(-8,None)):.2f}</th><th class='n'>{st.mean([pub[c] for c in cks[-8:]]):.2f}</th></tr>")
    p.append(f"<tr><th>all 24</th><th class='n'>{st.mean(S['minimal']):.2f}</th><th class='n'>{st.mean(S['scaffolded']):.2f}</th><th class='n'>{st.mean(S['leading']):.2f}</th><th class='n'>{st.mean(pub.values()):.2f}</th></tr>")
    p.append("</table>")

    # ---- run 2 ----
    p.append("<h2>Run 2. The thought experiment with no question</h2>")
    p.append("<div class='sub'>The seven numbered observations only: no puzzle, no question, no hint. Two forms: <i>continue</i> (nothing appended) and <i>ask</i> (\"What follows from this?\" appended). "
             "8 samples each, seeds 42 to 49, temperature 0.7, max 1024 tokens. Read blind, one verdict per continuation, highest rung reached. "
             f"Reader: {E(R['reader'])}. <span class='src'>evidence/elevator-open/open.jsonl, readings.json</span></div>")
    p.append("<table><tr><th>model</th><th>mode</th><th class='n'>n</th>" + "".join(f"<th class='n'>{v}</th>" for v in VERD) + "<th class='n'>stock opener</th><th class='n'>hit 1024 tokens</th></tr>")
    mode = {ck: next(r["mode"] for r in OPEN if r["checkpoint_name"] == ck) for ck in ocks}
    for ck in ocks:
        p.append(f"<tr><td>{E(ck)}</td><td>{mode[ck]}</td><td class='n'>{on[ck]}</td>" + "".join(f"<td class='n'>{ocount[ck].get(v,'') or ''}</td>" for v in VERD) + f"<td class='n'>{ostock[ck]}</td><td class='n'>{olen[ck]}</td></tr>")
    p.append("</table>")
    p.append("<p>Rungs, in order: <b>equivalence</b> says acceleration and gravity are alike (this is line 4 of the prompt); <b>bends-in-gravity</b> infers light bends in a real gravitational field; "
             "<b>not-a-force</b> says gravity is not an ordinary force on mass; <b>geometry</b> says gravity is the shape of space or spacetime. "
             "<b>none</b>: on topic, no rung. <b>loops</b>: repeats itself.</p>")
    p.append("<div class='note'><b>Reading.</b> The base model loops every time. The trained model restates line 4 of the prompt as its conclusion and stops: "
             f"{ocount['discovery-rl-v11-s839'].get('equivalence',0)} of {on['discovery-rl-v11-s839']} for s839. "
             "The reader's notes record three continuations that say light does <i>not</i> bend. The only verdicts above rung 1 came from s035, the least-trained checkpoint, and two of the three are marked marginal. "
             "The base model runs in completion mode and the RL checkpoints in chat mode; that difference is a confound and is stated here, not removed.</div>")

    # ---- reliability + caveats ----
    p.append("<h2>Grader reliability and caveats</h2>")
    p.append(f"<p>Two batches of 24 graded a second time by independent blind readers: <b>{ex} of {tot} exact</b>, <b>{w1} of {tot} within one point</b>. "
             f"<span class='src'>evidence/review-packet-elevator/grades-repeat/</span></p>")
    p.append("<ul>"
             "<li>Every score is from the provisional grader (D008), not the paper's own judge model. The API key is still the open ask.</li>"
             "<li>This task is upstream's light-bending elevator (1911 consequence). Einstein's happiest thought, the falling person who feels no weight (1907), is upstream's other GR task, <code>gr_free_fall_equivalence</code>. Existing numbers there: sweep n=24 mean 1.04; sensitivity n=9 scaffolded 1.11, minimal 1.22, leading 1.22; published 0.92. The hint moves that task by +0.11. It has not been run at n=72.</li>"
             "<li>Neither upstream task is the five-stage test. Both hand the model the problem and the explanatory idea in the prompt; the rubric rewards restating them. Stages 3 to 5 are absent from the benchmark.</li>"
             "<li>Open-ended verdicts: one reader, one pass, no regrade.</li>"
             "</ul>")
    p.append("<p class='src'>Pages: evidence/elevator/report.html, evidence/elevator/conditions-*.html, evidence/elevator-open/open_report.html. Notebook: E045, E046.</p>")
    p.append("</body></html>")
    with open(a.html, "w") as f:
        f.write("\n".join(p))
    print(f"wrote {a.html}")


if __name__ == "__main__":
    main()

"""
One presentable page for the free-fall results, every number computed from
the evidence files at render time. Same shape as elevator_summary.py.

    python tools/freefall_summary.py --html evidence/freefall/summary.html
"""

import argparse
import html
import json
import random
import statistics as st
from collections import Counter

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

    D = {c: load(f"evidence/freefall/{c}.graded.jsonl") for c in ("scaffolded", "minimal", "leading")}
    SEED = load("evidence/freefall/seed.jsonl")
    R = json.load(open("evidence/freefall/readings.json"))
    V = R["verdicts"]
    pub = {}
    for line in open("upstream/gpt1900/results/physics_eval_v11/summary.txt"):
        if line.startswith("discovery-rl-v11-"):
            p = line.split(); pub[p[0]] = float(p[8])          # Fall column
    hint = next(t for t in json.load(open("tools/EVAL_freefall_leading.json"))["tasks"])["prompt_lines"][-1]
    rubric = next(t for t in json.load(open("tools/EVAL_freefall_scaffolded.json"))["tasks"])["scoring_rubric"]
    seed_prompt = {t["id"]: "\n".join(t["prompt_lines"]) for t in json.load(open("tools/EVAL_freefall_seed.json"))["tasks"]}

    S = {c: [r["score"] for r in D[c]] for c in D}
    key = lambda r: (r["checkpoint_name"], r["seed"])
    ls = {key(r): r["score"] for r in D["leading"]}; ss = {key(r): r["score"] for r in D["scaffolded"]}; ms = {key(r): r["score"] for r in D["minimal"]}
    d_ls = [ls[k] - ss[k] for k in ss]; d_sm = [ss[k] - ms[k] for k in ss]
    cks = sorted({r["checkpoint_name"] for r in D["scaffolded"]}, key=step)
    per = {c: {ck: st.mean([r["score"] for r in D[c] if r["checkpoint_name"] == ck]) for ck in cks} for c in D}
    stock = {c: sum(1 for r in D[c] if (r["completion"] or "").startswith("You have touched")) for c in D}

    ex = w1 = tot = 0
    for b in ("01", "05"):
        g = {json.loads(l)["id"]: json.loads(l)["score"] for l in open(f"evidence/review-packet-freefall/grades/batch-{b}.jsonl") if l.strip()}
        rg = {json.loads(l)["id"]: json.loads(l)["score"] for l in open(f"evidence/review-packet-freefall/grades-repeat/batch-{b}.jsonl") if l.strip()}
        ex += sum(1 for k in g if g[k] == rg.get(k)); w1 += sum(1 for k in g if k in rg and abs(g[k] - rg[k]) <= 1); tot += len(g)

    VERD = ["loops", "incoherent", "none", "equivalence", "not-a-force", "geometry"]
    RUNG = {"equivalence": 1, "not-a-force": 2, "geometry": 3}
    skey = lambda r: f"{r['checkpoint_name']}|{r['task_id']}|{r['seed']}"
    forms = ["gr_freefall_seed", "gr_freefall_bare"]
    fcount = {t: Counter(V.get(skey(r)) for r in SEED if r["task_id"] == t) for t in forms}
    fn = {t: sum(1 for r in SEED if r["task_id"] == t) for t in forms}
    fstock = {t: sum(1 for r in SEED if r["task_id"] == t and (r["completion"] or "").startswith("You have touched")) for t in forms}
    flen = {t: sum(1 for r in SEED if r["task_id"] == t and r["finish_reason"] == "length") for t in forms}
    jumped = {t: sum(1 for r in SEED if r["task_id"] == t and RUNG.get(V.get(skey(r)), 0) >= 1) for t in forms}
    top = {t: {ck: max([RUNG.get(V.get(skey(r)), 0) for r in SEED if r["task_id"] == t and r["checkpoint_name"] == ck] or [0]) for ck in cks} for t in forms}

    def hist(xs, cls=""):
        c = Counter(xs); n = len(xs)
        return " ".join(f"<span class='hist'>{i}:</span><span class='bar {cls}' style='width:{int(120*c.get(i,0)/n)}px'></span><span class='hist'>{c.get(i,0)}</span>" for i in range(5))

    p = [f"<!doctype html><html><head><meta charset='utf-8'><title>Free fall results</title><style>{CSS}</style></head><body>"]
    p.append("<h1>The free-fall task, Einstein's 1907 observation</h1>")
    p.append("<div class='sub'>GPT-1900, task <code>gr_free_fall_equivalence</code> and two new one-observation forms. One job on SDSC Expanse, 30 Sep (54546826). "
             "Every number on this page is computed from the JSONL under <code>evidence/freefall/</code> when the page is rendered. "
             "Grader: blinded reader in fresh sessions of 24, provenance stripped, upstream's rubric, provisional (D008).</div>")

    lo, hi = ci(d_ls)
    p.append("<div class='big'>")
    p.append(f"<div><b>{st.mean(d_ls):+.2f}</b><span>hint effect, leading minus scaffolded, paired n={len(d_ls)}<br>95% CI {lo:+.2f} to {hi:+.2f}</span></div>")
    p.append(f"<div><b>{max(S['scaffolded'])}</b><span>highest score without the hint, in {len(S['scaffolded'])} tries</span></div>")
    p.append(f"<div><b>{jumped['gr_freefall_seed']} / {fn['gr_freefall_seed']}</b><span>answers to the observation plus a question that bring in acceleration on their own</span></div>")
    p.append(f"<div><b>{jumped['gr_freefall_bare']} / {fn['gr_freefall_bare']}</b><span>answers to the bare observation that bring in acceleration on their own</span></div>")
    p.append("</div>")

    p.append("<h2>Run 1. The rubric task, three wordings, all 24 checkpoints</h2>")
    p.append(f"<div class='sub'>24 checkpoints x 3 seeds (42, 43, 44) = 72 answers per wording, 216 total, 0 errors. Temperature 0.7, top_k 50, one sample per call. "
             f"<span class='src'>evidence/freefall/{{scaffolded,minimal,leading}}.graded.jsonl</span></div>")
    p.append("<table><tr><th>wording</th><th>what the model sees</th><th class='n'>n</th><th class='n'>mean</th><th>95% CI</th><th>score histogram 0 to 4</th><th class='n'>stock opener</th></tr>")
    desc = {"minimal": "falling person, floating objects, accelerating cabin; no statement that gravity can disappear", "scaffolded": "plus the sentence that gravity can be made to disappear by motion (the published condition)", "leading": "scaffolded plus one hint paragraph"}
    for c, cls in (("minimal", "m"), ("scaffolded", ""), ("leading", "l")):
        lo_, hi_ = ci(S[c])
        p.append(f"<tr><td><b>{c}</b></td><td>{desc[c]}</td><td class='n'>{len(S[c])}</td><td class='n'><b>{st.mean(S[c]):.2f}</b></td><td>{lo_:.2f} to {hi_:.2f}</td><td>{hist(S[c], cls)}</td><td class='n'>{stock[c]} / {len(S[c])}</td></tr>")
    p.append("</table>")
    lo2, hi2 = ci(d_sm)
    p.append(f"<p>Paired differences, same checkpoint and seed: leading minus scaffolded <b>{st.mean(d_ls):+.2f}</b> ({lo:+.2f} to {hi:+.2f}); "
             f"scaffolded minus minimal <b>{st.mean(d_sm):+.2f}</b> ({lo2:+.2f} to {hi2:+.2f}).</p>")
    p.append(f"<div class='note'><b>The hint.</b> The leading wording appends one paragraph to the published prompt:<div class='quote'>{E(hint)}</div>"
             f"Rubric level 4 reads: <i>{E(rubric['4'])}</i>. Level 5: <i>{E(rubric['5'])}</i>.</div>")

    p.append("<h2>Per checkpoint, three wordings beside the published score</h2>")
    p.append("<div class='sub'>Each cell is the mean of 3 seeds. Published column is the authors' single graded answer per checkpoint, their judge. "
             "<span class='src'>upstream/gpt1900/results/physics_eval_v11/summary.txt, Fall column</span></div>")
    p.append("<table><tr><th>checkpoint</th><th class='n'>minimal</th><th class='n'>scaffolded</th><th class='n'>leading</th><th class='n'>published</th><th class='n'>seed: top rung</th><th class='n'>bare: top rung</th></tr>")
    for ck in cks:
        p.append(f"<tr><td>{E(ck)}</td><td class='n'>{per['minimal'][ck]:.2f}</td><td class='n'>{per['scaffolded'][ck]:.2f}</td><td class='n'><b>{per['leading'][ck]:.2f}</b></td><td class='n'>{pub.get(ck, float('nan')):.2f}</td>"
                 f"<td class='n'>{top['gr_freefall_seed'][ck]}</td><td class='n'>{top['gr_freefall_bare'][ck]}</td></tr>")
    f8 = lambda c, sl: st.mean([r["score"] for r in D[c] if r["checkpoint_name"] in cks[sl]])
    p.append(f"<tr><th>first 8 checkpoints</th><th class='n'>{f8('minimal', slice(0,8)):.2f}</th><th class='n'>{f8('scaffolded', slice(0,8)):.2f}</th><th class='n'>{f8('leading', slice(0,8)):.2f}</th><th class='n'>{st.mean([pub[c] for c in cks[:8]]):.2f}</th><th></th><th></th></tr>")
    p.append(f"<tr><th>last 8 checkpoints</th><th class='n'>{f8('minimal', slice(-8,None)):.2f}</th><th class='n'>{f8('scaffolded', slice(-8,None)):.2f}</th><th class='n'>{f8('leading', slice(-8,None)):.2f}</th><th class='n'>{st.mean([pub[c] for c in cks[-8:]]):.2f}</th><th></th><th></th></tr>")
    p.append(f"<tr><th>all 24</th><th class='n'>{st.mean(S['minimal']):.2f}</th><th class='n'>{st.mean(S['scaffolded']):.2f}</th><th class='n'>{st.mean(S['leading']):.2f}</th><th class='n'>{st.mean(pub.values()):.2f}</th><th></th><th></th></tr>")
    p.append("</table>")

    p.append("<h2>Run 2. The observation alone: does the model supply the equivalence?</h2>")
    p.append("<div class='sub'>Two forms, 24 checkpoints x 3 seeds each. <i>seed</i>: the falling person and the floating objects, then \"What does this tell us about gravity?\". "
             "<i>bare</i>: the same two observations and nothing else. Neither mentions an accelerating cabin, equivalence, or gravity disappearing. "
             f"Read blind, one verdict per answer, highest rung reached. Reader: {E(R['reader'])}. <span class='src'>evidence/freefall/seed.jsonl, readings.json, jump.html</span></div>")
    p.append("<table><tr><th>form</th><th class='n'>n</th>" + "".join(f"<th class='n'>{v}</th>" for v in VERD) + "<th class='n'>any rung</th><th class='n'>stock opener</th><th class='n'>hit 1024 tokens</th></tr>")
    for t in forms:
        p.append(f"<tr><td><b>{t.replace('gr_freefall_','')}</b></td><td class='n'>{fn[t]}</td>" + "".join(f"<td class='n'>{fcount[t].get(v,'') or ''}</td>" for v in VERD)
                 + f"<td class='n'><b>{jumped[t]}</b></td><td class='n'>{fstock[t]}</td><td class='n'>{flen[t]}</td></tr>")
    p.append("</table>")
    p.append(f"<details><summary>The two prompts</summary><div class='quote'>{E(seed_prompt['gr_freefall_seed'])}</div><div class='quote'>{E(seed_prompt['gr_freefall_bare'])}</div></details>")
    p.append("<p>Rungs: <b>equivalence</b> brings in acceleration on its own (an accelerating cabin would feel like gravity; gravity and acceleration are alike); "
             "<b>not-a-force</b> says gravity is not an ordinary force; <b>geometry</b> says gravity is the shape of space. <b>none</b>: on topic, no rung. <b>loops</b>: repeats itself.</p>")

    p.append("<h2>Grader reliability and caveats</h2>")
    p.append(f"<p>Two batches of 24 graded a second time by independent blind readers: <b>{ex} of {tot} exact</b>, <b>{w1} of {tot} within one point</b>. "
             f"<span class='src'>evidence/review-packet-freefall/grades-repeat/</span></p>")
    p.append("<ul>"
             "<li>Every score is from the provisional grader (D008), not the paper's own judge model.</li>"
             "<li>The seed and bare forms are new prompts; no published number exists for them. The jump count is a reader's verdict, one pass, no regrade.</li>"
             "<li>All 24 checkpoints are RL checkpoints in chat mode; the untrained base model is not in this run (it loops on open prompts, E046).</li>"
             "</ul>")
    p.append("<p class='src'>Pages: evidence/freefall/report.html, evidence/freefall/jump.html. Notebook: E047.</p>")
    p.append("</body></html>")
    open(a.html, "w").write("\n".join(p))
    print(f"wrote {a.html}")


if __name__ == "__main__":
    main()

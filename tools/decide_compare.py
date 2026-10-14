"""
Agreement between the Decisions API verdicts and the blind readings.

    python tools/decide_compare.py evidence/abduction/decisions.jsonl \
        --readings evidence/abduction/readings.json --html evidence/abduction/decisions.html

Prints exact agreement overall, per prompt, and a confusion table. The html is
the same, plus every disagreement with both labels and the API's probabilities.
"""

import argparse
import html
import json
from collections import Counter, defaultdict

E = html.escape


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("decisions")
    ap.add_argument("--readings", required=True)
    ap.add_argument("--html", default=None)
    a = ap.parse_args()
    D = [json.loads(l) for l in open(a.decisions) if l.strip()]
    R = json.load(open(a.readings))
    V = R.get("verdicts", {})
    rk = lambda d: f"{d['checkpoint_name']}|{d['task_id']}|{d['seed']}"
    pairs = [(d, V.get(rk(d))) for d in D if "verdict" in d and V.get(rk(d))]
    agree = sum(1 for d, v in pairs if d["verdict"] == v)
    print(f"{len(D)} decisions, {len(pairs)} paired with a blind reading, exact agreement {agree}/{len(pairs)}"
          + (f" = {100 * agree / len(pairs):.0f}%" if pairs else ""))
    per = defaultdict(lambda: [0, 0])
    conf = Counter()
    for d, v in pairs:
        per[d["task_id"]][1] += 1; per[d["task_id"]][0] += d["verdict"] == v
        conf[(v, d["verdict"])] += 1
    for t, (x, n) in per.items():
        print(f"  {t:24s} {x}/{n}")
    labels = sorted({v for v, _ in conf} | {w for _, w in conf})
    print("confusion (rows = blind reading, cols = API):")
    print(" " * 14 + "".join(f"{l[:10]:>11s}" for l in labels))
    for v in labels:
        print(f"{v[:13]:13s} " + "".join(f"{conf[(v, w)]:>11d}" for w in labels))
    if a.html:
        p = [f"<!doctype html><meta charset='utf-8'><title>Decisions API vs blind reading</title>"
             "<style>body{font:14px/1.5 -apple-system,Helvetica,Arial;max-width:1100px;margin:0 auto;padding:1.5rem 2rem}"
             "table{border-collapse:collapse;font-size:13px}td,th{border:1px solid #e2e2e2;padding:.3rem .6rem;vertical-align:top}th{background:#f0f0f0}pre{white-space:pre-wrap;font-size:12.5px;background:#fff;border:1px solid #e2e2e2;padding:.5rem}</style>",
             f"<h1>Decisions API ({E(D[0].get('decision_model', ''))}) against the blind reading ({E(R.get('reader') or '')})</h1>",
             f"<p><b>Exact agreement {agree} of {len(pairs)}</b>" + (f" ({100 * agree / len(pairs):.0f}%)." if pairs else ".")
             + " The API saw the prompt, the expected answer and the text, nothing else.</p>",
             "<h2>Per prompt</h2><table><tr><th>prompt</th><th>agree</th><th>n</th></tr>"]
        for t, (x, n) in per.items():
            p.append(f"<tr><td>{E(t)}</td><td>{x}</td><td>{n}</td></tr>")
        p.append("</table><h2>Confusion, rows blind reading, columns API</h2><table><tr><th></th>" + "".join(f"<th>{E(l)}</th>" for l in labels) + "</tr>")
        for v in labels:
            p.append(f"<tr><th>{E(v)}</th>" + "".join(f"<td>{conf[(v, w)] or ''}</td>" for w in labels) + "</tr>")
        p.append("</table><h2>Disagreements</h2>")
        for d, v in pairs:
            if d["verdict"] != v:
                probs = ", ".join(f"{k} {x:.2f}" for k, x in sorted(d.get("probabilities", {}).items(), key=lambda kv: -kv[1])[:4])
                p.append(f"<p><b>{E(d['task_id'])}</b> {E(d['checkpoint_name'])} seed {d['seed']}: blind <b>{E(v)}</b>, API <b>{E(d['verdict'])}</b> (confidence {d.get('confidence')}; {E(probs)})</p>")
        open(a.html, "w").write("\n".join(p)); print(f"-> {a.html}")


if __name__ == "__main__":
    main()

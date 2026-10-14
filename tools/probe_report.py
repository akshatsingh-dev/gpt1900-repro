"""
Read the contamination probe generations and say, per stem, whether the
answer was what a pre-1900 model should give.

Why this exists
---------------
The probe asks the model to continue sentence stems. Half are about things a
pre-1900 corpus cannot contain, half are controls it should know. Two layers
of reading:

1. Keyword flags, automatic: does the answer use a post-1900 word, or cite a
   year of 1900 or later? A flag whose word was already in the stem is marked
   "echo": the model repeated the prompt, which proves nothing.
2. Human verdict, from a readings file written after reading every answer:
   for post-1900 stems, "clean" (no knowledge shown) or "leak"; for control
   stems, "knows", "partial" or "fails".

Row colour follows the verdict, not the flag. Red is bad news either way:
a leak on a post-1900 stem, or a failure on a control. Green is the expected
outcome. Amber is partial. Grey means no reading yet.

    python tools/probe_report.py evidence/contamination/probe.jsonl \
        --config tools/probe_knowledge.json \
        --readings evidence/contamination/probe-readings.json \
        --out evidence/contamination/probe.json --html evidence/contamination/probe.html
"""

import argparse
import html
import json
import re
import sys
from collections import Counter, defaultdict

FLAG_TERMS = [
    "photon", "photons", "spacetime", "space-time", "planck", "einstein",
    "relativity", "relativistic", "bohr", "nobel", "quantum mechanics",
    "quanta", "quantized", "quantised", "wright brothers", "aeroplane",
    "airplane", "radioactivity", "radioactive", "nuclear", "electron volt",
    "wavefunction", "uncertainty principle", "general relativity",
    "special relativity", "e = mc", "e=mc",
]
YEAR_RE = re.compile(r"\b(19[0-9]{2}|20[0-9]{2})\b")

# verdict -> (row class, plain-words meaning)
VERDICTS = {
    "clean":   ("good", "post-1900 stem, no post-1900 knowledge shown. Expected."),
    "leak":    ("bad",  "post-1900 stem answered with real post-1900 knowledge. Contamination."),
    "knows":   ("good", "pre-1900 stem answered correctly. Expected."),
    "partial": ("mid",  "pre-1900 stem, answer in the right area but not the fact."),
    "fails":   ("bad",  "pre-1900 stem, answer wrong or unrelated. The model should know this."),
}


def load(path):
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


def word_in(term, text):
    return re.search(r"(?<![a-z])" + re.escape(term) + r"(?![a-z])", text.lower()) is not None


def flags_in(text, stem):
    """(hits, years). Each hit is (term, echo) where echo means the stem had it too."""
    hits = [(t, word_in(t, stem)) for t in FLAG_TERMS if word_in(t, text)]
    stem_years = set(YEAR_RE.findall(stem))
    years = [(y, y in stem_years) for y in sorted(set(YEAR_RE.findall(text)))]
    return hits, years


def esc(v):
    return html.escape(str(v)) if v is not None else "<span style='color:#bbb'>—</span>"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl")
    ap.add_argument("--config", required=True, help="tools/probe_knowledge.json: group and expected per stem")
    ap.add_argument("--readings", default=None, help="hand-written verdict per checkpoint/stem")
    ap.add_argument("--out", required=True)
    ap.add_argument("--html", required=True)
    args = ap.parse_args()

    records = load(args.jsonl)
    cfg = json.load(open(args.config))
    task_cfg = {t["id"]: t for t in cfg["tasks"]}
    readings = json.load(open(args.readings))["readings"] if args.readings else {}

    rows = []
    summary = defaultdict(Counter)
    for r in records:
        t = task_cfg.get(r["task_id"], {})
        grp = t.get("group", "?")
        # readings are keyed checkpoint/stem/sample; a file without sample
        # indices (the greedy run) falls back to checkpoint/stem
        key = f"{r['checkpoint_name']}/{r['task_id']}/{r.get('sample_index', 0)}"
        reading = readings.get(key) or readings.get(f"{r['checkpoint_name']}/{r['task_id']}", {})
        verdict = reading.get("verdict")
        if r.get("error") or r.get("completion") is None:
            hits, years = [], []
            verdict = verdict or "error"
        else:
            hits, years = flags_in(r["completion"], r.get("prompt") or "")
        non_echo = [h for h, echo in hits if not echo] + [y for y, echo in years if not echo]
        rows.append({"checkpoint": r["checkpoint_name"], "task": r["task_id"], "group": grp,
                     "expected": t.get("expected"), "flags": hits, "years": years,
                     "non_echo_flags": non_echo, "verdict": verdict,
                     "echo": bool(reading.get("echo")), "note": reading.get("note"), "record": r})
        summary[(r["checkpoint_name"], grp)][verdict or "unread"] += 1

    # ---- terminal ----
    print("=" * 62)
    print("CONTAMINATION PROBE, MODEL SIDE")
    print("=" * 62)
    for (ck, grp), c in sorted(summary.items()):
        print(f"{ck:26} {grp:10} " + "  ".join(f"{v} {n}" for v, n in sorted(c.items())))
    print()
    n_non_echo = sum(1 for row in rows if row["non_echo_flags"])
    print(f"keyword flags from words NOT in the stem: {n_non_echo} of {len(rows)}")
    for row in rows:
        if row["verdict"] in ("leak", "fails"):
            print(f"  {row['verdict'].upper():6} {row['checkpoint']}/{row['task']}: {row['note']}")

    with open(args.out, "w") as f:
        json.dump({"source": args.jsonl, "flag_terms": FLAG_TERMS,
                   "summary": [{"checkpoint": ck, "group": grp, **dict(c)} for (ck, grp), c in sorted(summary.items())],
                   "non_echo_flag_rows": n_non_echo,
                   "rows": [{k: v for k, v in row.items() if k != "record"} for row in rows]}, f, indent=2)

    # ---- html ----
    p = ["<!doctype html><html><head><meta charset='utf-8'><title>Contamination probe</title><style>",
         "body{margin:0 auto;padding:2rem;max-width:1200px;font:14px/1.5 -apple-system,Helvetica,Arial,sans-serif;color:#1a1a1a;background:#fafafa}",
         "table{border-collapse:collapse;width:100%;background:#fff;font-size:13px}th,td{text-align:left;padding:.4rem .6rem;border-bottom:1px solid #e2e2e2;vertical-align:top}th{background:#f0f0f0}",
         "tr.bad td{background:#fdecea}tr.good td{background:#eef7f0}tr.mid td{background:#fff6e5}",
         ".card{background:#fff;border:1px solid #e2e2e2;border-radius:8px;padding:1rem 1.25rem;margin:1rem 0}",
         ".card.bad{border-left:6px solid #b3261e}.card.good{border-left:6px solid #1b7f3b}.card.mid{border-left:6px solid #a15c00}",
         "pre{white-space:pre-wrap;word-wrap:break-word;background:#f6f6f6;border:1px solid #e2e2e2;border-radius:6px;padding:.75rem 1rem;font-size:13px;line-height:1.55}",
         ".badge{font-size:11px;padding:.1rem .45rem;border-radius:999px;border:1px solid;font-weight:600;margin-left:.3rem}",
         ".badge.echo{color:#6b6b6b;border-color:#bbb}.badge.hit{color:#b3261e;border-color:#b3261e}",
         ".v{font-weight:700}.v.bad{color:#b3261e}.v.good{color:#1b7f3b}.v.mid{color:#a15c00}",
         ".muted{color:#6b6b6b}.legend td{padding:.2rem .6rem}",
         "</style></head><body><h1>Contamination probe, model side</h1>",
         f"<p class='muted'>{esc(args.jsonl)} &middot; {len(records)} generations, temperature 0 (greedy), 200 tokens max.</p>",
         "<div class='card'><b>How to read this page.</b> Each stem has an <i>expected</i> outcome. Post-1900 stems should draw a blank: "
         "the model is supposed to know nothing after 1899. Control stems are pre-1900 facts it should know. "
         "The <i>verdict</i> is a human reading of the full answer, not the keyword filter. Row colour follows the verdict.<br>"
         "<table class='legend'>"
         + "".join(f"<tr><td class='v {cls}'>{v}</td><td>{esc(meaning)}</td></tr>" for v, (cls, meaning) in VERDICTS.items())
         + "</table>"
         "<p class='muted' style='margin:.4rem 0 0'>Keyword badges: <span class='badge hit'>word</span> = post-1900 word or year in the answer. "
         "<span class='badge echo'>word (echo)</span> = the same word was in the stem, so the model repeated it. Echoes prove nothing.</p></div>"]

    p.append("<h2>Summary</h2><table><tr><th>checkpoint</th><th>group</th><th>verdicts</th></tr>")
    for (ck, grp), c in sorted(summary.items()):
        cells = " &nbsp; ".join(f"<span class='v {VERDICTS.get(v, ('', ''))[0]}'>{esc(v)}</span> {n}" for v, n in sorted(c.items()))
        p.append(f"<tr><td>{esc(ck)}</td><td>{esc(grp)}</td><td>{cells}</td></tr>")
    p.append(f"</table><p class='muted'>Keyword flags from words the stem did not contain: {n_non_echo} of {len(rows)}.</p>")

    p.append("<h2>Every stem</h2><table><tr><th>#</th><th>checkpoint</th><th>stem</th><th>expected</th><th>what it said</th><th>verdict</th><th>keywords</th><th>tokens</th></tr>")
    for i, row in enumerate(rows, 1):
        cls = VERDICTS.get(row["verdict"], ("", ""))[0]
        badges = "".join(f"<span class='badge {'echo' if e else 'hit'}'>{esc(t)}{' (echo)' if e else ''}</span>" for t, e in row["flags"] + row["years"])
        p.append(f"<tr class='{cls}'><td><a href='#p{i}'>{i}</a></td><td>{esc(row['checkpoint'])}</td>"
                 f"<td>{esc(row['task'])}</td><td class='muted'>{esc(row['expected'])}</td>"
                 f"<td>{esc(row['note'])}</td><td class='v {cls}'>{esc(row['verdict'] or 'unread')}</td>"
                 f"<td>{badges}</td><td>{esc(row['record'].get('completion_tokens'))}</td></tr>")
    p.append("</table><h2>Continuations</h2>")
    for i, row in enumerate(rows, 1):
        r = row["record"]
        cls = VERDICTS.get(row["verdict"], ("", ""))[0]
        badges = "".join(f"<span class='badge {'echo' if e else 'hit'}'>{esc(t)}{' (echo)' if e else ''}</span>" for t, e in row["flags"] + row["years"])
        p.append(f"<div class='card {cls}' id='p{i}'><h3>#{i} {esc(row['checkpoint'])} &nbsp;/&nbsp; {esc(row['task'])} "
                 f"<span class='v {cls}'>{esc(row['verdict'] or 'unread')}</span>{badges}</h3>")
        p.append(f"<p><b>Stem.</b> {esc(r.get('prompt'))}</p>")
        p.append(f"<p class='muted'><b>Expected.</b> {esc(row['expected'])}</p>")
        if row["note"]:
            p.append(f"<p><b>What it said.</b> {esc(row['note'])}</p>")
        p.append(f"<pre>{esc(r.get('error') or r.get('completion'))}</pre></div>")
    p.append("</body></html>")
    with open(args.html, "w") as f:
        f.write("\n".join(p))
    print(f"\nwrote {args.out}\nwrote {args.html}")


if __name__ == "__main__":
    main()

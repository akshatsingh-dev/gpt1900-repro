"""
Render logged_eval JSONL into one self-contained HTML page.

Why this exists
---------------
A JSONL archive is the right format for evidence and the wrong format for eyes.
One record is a 6KB line with the answer buried in the middle of fifty fields.
This turns a run into a page: a summary table with one row per generation, then
every answer in full, with its prompt and all of its fields one click away.

No external CSS, JS or fonts. The page works offline, from a USB stick, in ten
years, which is the standard the archive itself is held to.

Usage
-----
    python tools/render_html.py evidence/probe.jsonl
    python tools/render_html.py evidence/run-a.jsonl evidence/run-b.jsonl -o evidence/determinism.html

Then open the .html file in a browser.
"""

import argparse
import html
import json
import os
import sys
from collections import Counter

# Shown in the summary table, in this order. Everything else is in the per-record
# fold-out. Chosen for "what would I want to see across twenty rows at once".
SUMMARY_COLUMNS = [
    ("checkpoint_name", "checkpoint"),
    ("task_id", "task"),
    ("prompt_condition", "condition"),
    ("seed", "seed"),
    ("sample_index", "sample"),
    ("temperature", "temp"),
    ("dtype", "dtype"),
    ("gpu_name", "gpu"),
    ("completion_tokens", "tokens"),
    ("finish_reason", "finish"),
    ("generation_seconds", "seconds"),
    ("score", "score"),
    ("completion_sha256", "answer hash"),
    ("error", "error"),
]


def load(paths):
    records = []
    for path in paths:
        with open(path) as f:
            for n, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError as exc:
                    print(f"{path}:{n}: skipped, {exc}", file=sys.stderr)
                    continue
                r["_source_file"] = os.path.basename(path)
                records.append(r)
    return records


def esc(v):
    """HTML-escape any value. None becomes a muted dash rather than 'None'."""
    if v is None:
        return '<span class="null">—</span>'
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, float):
        return f"{v:.2f}"
    return html.escape(str(v))


def short_hash(v):
    return esc(v[:10]) if isinstance(v, str) else esc(v)


def flags_for(r):
    """Things worth a coloured badge on the card header."""
    out = []
    if r.get("error"):
        out.append(("bad", "ERROR"))
    if r.get("dtype") == "bfloat16" and r.get("bf16_supported") is False:
        out.append(("warn", "bf16 emulated"))
    if r.get("finish_reason") == "length":
        out.append(("warn", "hit max_tokens"))
    if r.get("code_dirty"):
        out.append(("warn", "code dirty"))
    if r.get("score") is not None:
        out.append(("ok", f"score {r['score']}"))
    return out


CSS = """
:root { --bg:#fafafa; --fg:#1a1a1a; --muted:#6b6b6b; --line:#e2e2e2; --card:#fff;
        --ok:#1b7f3b; --warn:#a15c00; --bad:#b3261e; --accent:#2b4c7e; }
* { box-sizing:border-box }
body { margin:0; padding:2rem; font:14px/1.5 -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
       background:var(--bg); color:var(--fg); max-width:1200px; margin:0 auto }
h1 { font-size:1.4rem; margin:0 0 .25rem } h2 { font-size:1.1rem; margin:2rem 0 .5rem }
.sub { color:var(--muted); margin-bottom:1.5rem }
table { border-collapse:collapse; width:100%; background:var(--card); font-size:13px }
th, td { text-align:left; padding:.4rem .6rem; border-bottom:1px solid var(--line); vertical-align:top }
th { background:#f0f0f0; font-weight:600; position:sticky; top:0 }
tr.err td { background:#fdecea }
.wrap { overflow-x:auto; border:1px solid var(--line); border-radius:6px }
.card { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:1rem 1.25rem; margin:1rem 0 }
.card h3 { margin:0 0 .5rem; font-size:1rem; display:flex; gap:.5rem; align-items:center; flex-wrap:wrap }
.badge { font-size:11px; padding:.1rem .45rem; border-radius:999px; border:1px solid; font-weight:600 }
.badge.ok { color:var(--ok); border-color:var(--ok) } .badge.warn { color:var(--warn); border-color:var(--warn) }
.badge.bad { color:var(--bad); border-color:var(--bad) }
.meta { color:var(--muted); font-size:12px; margin-bottom:.75rem }
pre { white-space:pre-wrap; word-wrap:break-word; background:#f6f6f6; padding:.75rem 1rem;
      border-radius:6px; border:1px solid var(--line); margin:.5rem 0; font-size:13px; line-height:1.55 }
pre.answer { background:#fff; border-color:#cfd8e3 }
details { margin:.5rem 0 } summary { cursor:pointer; color:var(--accent); font-weight:600 }
.kv { font-size:12px } .kv td:first-child { color:var(--muted); width:220px; font-family:ui-monospace, Menlo, monospace }
.null { color:#bbb } .hash { font-family:ui-monospace, Menlo, monospace }
.counts { display:flex; gap:1.5rem; flex-wrap:wrap; margin:.5rem 0 1rem } .counts div b { display:block; font-size:1.3rem }
"""


def render(records, title):
    n = len(records)
    errors = sum(1 for r in records if r.get("error"))
    ckpts = Counter(r.get("checkpoint_name") for r in records)
    tasks = Counter(r.get("task_id") for r in records)
    runs = Counter(r.get("run_id") for r in records)
    secs = [r["generation_seconds"] for r in records if isinstance(r.get("generation_seconds"), (int, float))]

    parts = [f"<!doctype html><html><head><meta charset='utf-8'><title>{html.escape(title)}</title>",
             f"<style>{CSS}</style></head><body>",
             f"<h1>{html.escape(title)}</h1>",
             f"<div class='sub'>{n} generation{'s' if n != 1 else ''} from "
             f"{len(runs)} run{'s' if len(runs) != 1 else ''}, "
             f"{', '.join(sorted({r['_source_file'] for r in records}))}</div>",
             "<div class='counts'>",
             f"<div><b>{n}</b>records</div>",
             f"<div><b>{errors}</b>errors</div>",
             f"<div><b>{len(ckpts)}</b>checkpoints</div>",
             f"<div><b>{len(tasks)}</b>tasks</div>",
             f"<div><b>{(sum(secs)/len(secs)):.1f}s</b>mean per generation</div>" if secs else "",
             "</div>"]

    # ---- summary table -----------------------------------------------------
    parts.append("<h2>Summary</h2><div class='wrap'><table><thead><tr><th>#</th>")
    parts += [f"<th>{html.escape(label)}</th>" for _, label in SUMMARY_COLUMNS]
    parts.append("</tr></thead><tbody>")
    for i, r in enumerate(records, 1):
        cls = " class='err'" if r.get("error") else ""
        parts.append(f"<tr{cls}><td><a href='#rec{i}'>{i}</a></td>")
        for key, _ in SUMMARY_COLUMNS:
            v = r.get(key)
            cell = short_hash(v) if key.endswith("sha256") else esc(v)
            if key == "error" and v:
                cell = esc(str(v).splitlines()[-1][:80])
            parts.append(f"<td>{cell}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table></div>")

    # ---- one card per record ----------------------------------------------
    parts.append("<h2>Generations</h2>")
    for i, r in enumerate(records, 1):
        badges = "".join(f"<span class='badge {c}'>{html.escape(t)}</span>" for c, t in flags_for(r))
        parts.append(f"<div class='card' id='rec{i}'>")
        parts.append(f"<h3>#{i} &nbsp; {esc(r.get('checkpoint_name'))} &nbsp;/&nbsp; "
                     f"{esc(r.get('task_id'))} {badges}</h3>")
        parts.append(
            "<div class='meta'>"
            f"condition {esc(r.get('prompt_condition'))} · seed {esc(r.get('seed'))} · "
            f"sample {esc(r.get('sample_index'))} · temp {esc(r.get('temperature'))} · "
            f"top_k {esc(r.get('top_k'))} · {esc(r.get('dtype'))} on {esc(r.get('gpu_name') or r.get('device'))} · "
            f"{esc(r.get('completion_tokens'))} tokens in {esc(r.get('generation_seconds'))}s · "
            f"{esc(r.get('finish_reason'))} · run {esc(r.get('run_id'))}"
            "</div>")
        if r.get("error"):
            parts.append(f"<pre style='border-color:#e8a19c'>{esc(r['error'])}</pre>")
        if r.get("completion") is not None:
            parts.append(f"<pre class='answer'>{esc(r['completion'])}</pre>")
        parts.append(f"<details><summary>Prompt</summary><pre>{esc(r.get('prompt'))}</pre></details>")
        parts.append("<details><summary>All fields</summary><table class='kv'>")
        for k, v in r.items():
            if k in ("prompt", "completion", "_source_file"):
                continue
            cell = f"<span class='hash'>{esc(v)}</span>" if k.endswith("sha256") or k in ("code_commit", "model_revision") else esc(v)
            parts.append(f"<tr><td>{html.escape(k)}</td><td>{cell}</td></tr>")
        parts.append("</table></details></div>")

    parts.append("</body></html>")
    return "\n".join(parts)


def main():
    ap = argparse.ArgumentParser(description="Render logged_eval JSONL as a single HTML page")
    ap.add_argument("jsonl", nargs="+", help="one or more JSONL files")
    ap.add_argument("-o", "--out", default=None,
                    help="output .html path. Default: first input with .html extension")
    ap.add_argument("--title", default=None)
    args = ap.parse_args()

    records = load(args.jsonl)
    if not records:
        ap.error("no records found")
    out = args.out or os.path.splitext(args.jsonl[0])[0] + ".html"
    title = args.title or f"GPT-1900 generations: {', '.join(os.path.basename(p) for p in args.jsonl)}"
    with open(out, "w") as f:
        f.write(render(records, title))
    print(f"{len(records)} records → {out}")


if __name__ == "__main__":
    main()

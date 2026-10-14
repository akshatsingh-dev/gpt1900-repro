"""
Compare two logged_eval runs and report how many generations reproduce.

Why this exists
---------------
`logged_eval.py` produces evidence. This turns evidence into the number the
sprint is about: given the same checkpoint, the same prompt and the same
settings, how often does the same answer come back?

Upstream could not answer that question about its own runs, because the archive
does not record what produced an answer. This one can, and it refuses to report
a rate when the two runs are not actually comparable.

Records are matched on the things that must agree for a comparison to mean
anything: checkpoint, task, prompt condition, mode, seed and sample index.
Answers are compared by `completion_sha256`, not by diffing text, so a match is
byte equality and nothing softer.

Usage
-----
    python tools/compare_runs.py evidence/determinism/run-a.jsonl \
                                 evidence/determinism/run-b.jsonl

    # write the per-record verdicts out for the archive
    python tools/compare_runs.py a.jsonl b.jsonl --out evidence/determinism/compare.json
"""

import argparse
import html as _html
import json
import sys
from collections import Counter

# Two records describe the same trial only if all of these agree. Anything that
# differs here means the runs are answering different questions.
KEY_FIELDS = ("checkpoint_name", "task_id", "prompt_condition", "mode",
              "seed", "sample_index")

# Settings that must match for a reproduction rate to be meaningful. E022 found
# upstream compared runs with different --num-samples, which alone guarantees a
# mismatch, and nothing in their archive would have revealed it.
MUST_MATCH = ("temperature", "top_k", "num_samples", "max_tokens",
              "model_repo", "model_revision", "eval_config_sha256",
              "code_commit")

# Settings that legitimately differ across machines. Not errors, but a
# comparison that spans them is a portability test, not a determinism test.
WORTH_NOTING = ("schema_version", "device", "dtype", "dtype_override", "gpu_name", "compute_capability",
                "bf16_supported", "torch_version", "platform", "python_version",
                "deterministic_algorithms", "code_dirty")


def load(path):
    """Read JSONL. One bad line should name itself rather than kill the run."""
    records = []
    with open(path) as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                print(f"{path}:{n}: skipped unparseable line, {exc}", file=sys.stderr)
    return records


def key_of(record):
    return tuple(record.get(f) for f in KEY_FIELDS)


def index_by_key(records, path):
    """Key to record, warning on duplicates rather than silently keeping one."""
    out = {}
    for record in records:
        k = key_of(record)
        if k in out:
            print(f"{path}: duplicate key {k}, keeping the first", file=sys.stderr)
            continue
        out[k] = record
    return out


def settings_of(records, fields):
    """Every distinct value each field took across a run."""
    return {f: sorted({repr(r.get(f)) for r in records}) for f in fields}


def main():
    parser = argparse.ArgumentParser(
        description="Compare two logged_eval JSONL runs by completion hash")
    parser.add_argument("run_a")
    parser.add_argument("run_b")
    parser.add_argument("--out", default=None,
                        help="Optional JSON file for the per-record verdicts.")
    parser.add_argument("--html", default=None,
                        help="Optional HTML page: the rate, what differed, and every "
                             "mismatching pair side by side.")
    parser.add_argument("--upstream", default=None,
                        help="Upstream generations.json. Adds their published answer for the "
                             "same checkpoint and task as a third column on the page.")
    parser.add_argument("--eval-config", default=None,
                        help="EVAL.json. Adds each task's judge focus and 0-5 rubric beside the prompt.")
    parser.add_argument("--show", type=int, default=5,
                        help="How many mismatching records to describe. Default 5.")
    parser.add_argument("--force", action="store_true",
                        help="Report a rate even when the two runs used different "
                             "settings. The rate will not mean what it looks like.")
    args = parser.parse_args()

    a_records, b_records = load(args.run_a), load(args.run_b)

    upstream = {}
    if args.upstream:
        with open(args.upstream) as f:
            raw = json.load(f)
        # shape: {checkpoint_name: {task_id: {prompt, mode, completions}}}
        for ck, tasks in raw.items():
            for tid, rec in tasks.items():
                comps = rec.get("completions") or []
                upstream[(ck, tid)] = {"completion": comps[0] if comps else None,
                                       "n_completions": len(comps),
                                       "prompt": rec.get("prompt")}

    rubric = {}
    if args.eval_config:
        with open(args.eval_config) as f:
            cfg = json.load(f)
        for t in cfg.get("tasks", []):
            rubric[t["id"]] = {"title": t.get("title"), "judge_focus": t.get("judge_focus"),
                               "expected": t.get("expected_core_concepts", []),
                               "failures": t.get("common_failure_modes", []),
                               "scale": t.get("scoring_rubric", {})}
    if not a_records or not b_records:
        parser.error("one of the runs is empty")

    line = "=" * 62
    print(line)
    print("RUN COMPARISON")
    print(line)
    print(f"A  {args.run_a}   {len(a_records)} records")
    print(f"B  {args.run_b}   {len(b_records)} records")
    print()

    # --- are these two runs even comparable ---------------------------------
    a_set, b_set = settings_of(a_records, MUST_MATCH), settings_of(b_records, MUST_MATCH)
    blocking = {f: (a_set[f], b_set[f]) for f in MUST_MATCH if a_set[f] != b_set[f]}

    if blocking:
        print("SETTINGS DIFFER. These must match for a reproduction rate to mean anything:")
        for f, (va, vb) in blocking.items():
            print(f"  {f:22} A={','.join(va)}   B={','.join(vb)}")
        print()
        if not args.force:
            print("Refusing to report a rate. Re-run with matched settings, or pass")
            print("--force if you specifically want the number anyway and will say so.")
            print(line)
            return 2

    a_note, b_note = settings_of(a_records, WORTH_NOTING), settings_of(b_records, WORTH_NOTING)
    env_diff = {f: (a_note[f], b_note[f]) for f in WORTH_NOTING if a_note[f] != b_note[f]}
    if env_diff:
        print("Environment differs between the runs. This is a portability comparison,")
        print("not a determinism test, and should be reported as one:")
        for f, (va, vb) in env_diff.items():
            print(f"  {f:26} A={','.join(va)}   B={','.join(vb)}")
        print()

    # --- match records ------------------------------------------------------
    a_by_key, b_by_key = index_by_key(a_records, args.run_a), index_by_key(b_records, args.run_b)
    shared = sorted(set(a_by_key) & set(b_by_key))
    only_a, only_b = set(a_by_key) - set(b_by_key), set(b_by_key) - set(a_by_key)

    verdicts, reasons = [], Counter()
    matched = 0
    for k in shared:
        ra, rb = a_by_key[k], b_by_key[k]
        if ra.get("error") or rb.get("error"):
            verdict, reason = False, "error in one or both records"
        elif ra.get("completion_sha256") is None or rb.get("completion_sha256") is None:
            verdict, reason = False, "missing completion hash"
        elif ra["completion_sha256"] == rb["completion_sha256"]:
            verdict, reason = True, "identical"
        else:
            verdict, reason = False, "different completion"
        matched += verdict
        reasons[reason] += 1
        verdicts.append({
            "key": dict(zip(KEY_FIELDS, k)),
            "match": verdict,
            "reason": reason,
            "sha_a": ra.get("completion_sha256"),
            "sha_b": rb.get("completion_sha256"),
            "tokens_a": ra.get("completion_tokens"),
            "tokens_b": rb.get("completion_tokens"),
            "prompt": ra.get("prompt"),
            "upstream": upstream.get((k[0], k[1])),
            "completion_a": ra.get("completion"),
            "completion_b": rb.get("completion"),
            "error_a": ra.get("error"),
            "error_b": rb.get("error"),
        })

    # --- the number ---------------------------------------------------------
    total = len(shared)
    print(f"paired records    {total}")
    if only_a or only_b:
        print(f"unpaired          {len(only_a)} only in A, {len(only_b)} only in B")
        print("                  unpaired records are excluded from the rate below.")
    print()
    for reason, count in reasons.most_common():
        print(f"  {reason:32} {count}")
    print()
    if total:
        print(f"REPRODUCTION RATE  {matched} / {total}  = {100.0 * matched / total:.1f}%")
    else:
        print("REPRODUCTION RATE  no paired records, nothing to report")
    print(line)

    # --- what actually differed --------------------------------------------
    mismatches = [v for v in verdicts if not v["match"]]
    if mismatches and args.show:
        print(f"\nFirst {min(args.show, len(mismatches))} mismatches:")
        for v in mismatches[:args.show]:
            k = v["key"]
            print(f"  {k['checkpoint_name']} / {k['task_id']} / seed {k['seed']} "
                  f"/ sample {k['sample_index']}")
            print(f"    {v['reason']}, {v['tokens_a']} vs {v['tokens_b']} tokens")
            print(f"    A {v['sha_a']}")
            print(f"    B {v['sha_b']}")

    if args.out:
        with open(args.out, "w") as f:
            json.dump({
                "run_a": args.run_a,
                "run_b": args.run_b,
                "paired": total,
                "matched": matched,
                "rate": (matched / total) if total else None,
                "unpaired_a": len(only_a),
                "unpaired_b": len(only_b),
                "blocking_setting_differences": {k: list(v) for k, v in blocking.items()},
                "environment_differences": {k: list(v) for k, v in env_diff.items()},
                "verdicts": [{k: v for k, v in vd.items()
                              if k not in ("prompt", "upstream", "completion_a", "completion_b")} for vd in verdicts],
            }, f, indent=2)
        print(f"\nwrote {args.out}")

    if args.html:
        write_html(args.html, args.run_a, args.run_b, total, matched, only_a, only_b,
                   blocking, env_diff, verdicts, a_records, b_records, rubric)
        print(f"wrote {args.html}")

    return 0 if total and matched == total else 1


# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------

_CSS = """
body{margin:0 auto;padding:2rem;max-width:1200px;font:14px/1.5 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:#1a1a1a;background:#fafafa}
h1{font-size:1.4rem;margin:0 0 .25rem}h2{font-size:1.1rem;margin:2rem 0 .5rem}
.sub{color:#6b6b6b;margin-bottom:1rem}
.rate{font-size:2.6rem;font-weight:700;margin:.5rem 0}
.rate.ok{color:#1b7f3b}.rate.bad{color:#b3261e}.rate.na{color:#6b6b6b}
table{border-collapse:collapse;width:100%;background:#fff;font-size:13px}
th,td{text-align:left;padding:.4rem .6rem;border-bottom:1px solid #e2e2e2;vertical-align:top}
th{background:#f0f0f0;font-weight:600}
tr.match td{background:#eef7f0}tr.mismatch td{background:#fdecea}
.wrap{overflow-x:auto;border:1px solid #e2e2e2;border-radius:6px}
.hash{font-family:ui-monospace,Menlo,monospace;font-size:12px}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
.pair pre{white-space:pre-wrap;word-wrap:break-word;background:#fff;border:1px solid #cfd8e3;border-radius:6px;padding:.75rem 1rem;font-size:13px;line-height:1.55;margin:0}
.pair h4{margin:.25rem 0;font-size:.9rem;color:#2b4c7e}
.card{background:#fff;border:1px solid #e2e2e2;border-radius:8px;padding:1rem 1.25rem;margin:1rem 0}
.warn{background:#fff6e5;border:1px solid #e0b96a;border-radius:6px;padding:.75rem 1rem;margin:1rem 0}
.bad{background:#fdecea;border:1px solid #e8a19c;border-radius:6px;padding:.75rem 1rem;margin:1rem 0}
"""


def _e(v):
    if v is None:
        return "<span style='color:#bbb'>\u2014</span>"
    return _html.escape(str(v))


def _settings_table(rows, a_label, b_label):
    out = [f"<div class='wrap'><table><tr><th>setting</th><th>{_e(a_label)}</th><th>{_e(b_label)}</th></tr>"]
    for f, (va, vb) in rows.items():
        out.append(f"<tr><td>{_e(f)}</td><td>{_e(', '.join(va))}</td><td>{_e(', '.join(vb))}</td></tr>")
    out.append("</table></div>")
    return "".join(out)


def _prov_row(label, val):
    return f"<tr><td style='color:#6b6b6b;width:200px;font-family:ui-monospace,Menlo,monospace'>{_e(label)}</td><td class='hash'>{_e(val)}</td></tr>"


def write_html(path, run_a, run_b, total, matched, only_a, only_b,
               blocking, env_diff, verdicts, a_records, b_records, rubric=None):
    """A page a reader can take in at a glance: the rate, then why, then the texts."""
    p = []
    p.append(f"<!doctype html><html><head><meta charset='utf-8'><title>Run comparison</title>"
             f"<style>{_CSS}</style></head><body>")
    p.append("<h1>Run comparison</h1>")
    p.append(f"<div class='sub'>A = {_e(run_a)} ({len(a_records)} records) &nbsp;&nbsp; "
             f"B = {_e(run_b)} ({len(b_records)} records)</div>")

    # What exactly ran. Every value here is read from the records, not typed in.
    r0 = a_records[0] if a_records else {}
    r1 = b_records[0] if b_records else {}
    p.append("<details open><summary style='cursor:pointer;color:#2b4c7e;font-weight:600'>What ran</summary>"
             "<div class='wrap'><table style='font-size:12px'>")
    for label, key in (("checkpoint", "checkpoint_name"), ("model repo", "model_repo"),
                       ("model revision", "model_revision"), ("upstream commit", "code_commit"),
                       ("eval config sha256", "eval_config_sha256"), ("prompt condition", "prompt_condition"),
                       ("temperature", "temperature"), ("top_k", "top_k"), ("seed", "seed"),
                       ("num_samples", "num_samples"), ("max_tokens", "max_tokens"),
                       ("dtype", "dtype"), ("gpu", "gpu_name"), ("compute capability", "compute_capability"),
                       ("bf16 supported", "bf16_supported"), ("torch", "torch_version"),
                       ("deterministic algorithms", "deterministic_algorithms"), ("schema", "schema_version")):
        p.append(_prov_row(label, r0.get(key)))
    p.append(_prov_row("run id A", r0.get("run_id")))
    p.append(_prov_row("run id B", r1.get("run_id")))
    p.append(_prov_row("slurm job A / B", f"{r0.get('slurm_job_id')} / {r1.get('slurm_job_id')}"))
    p.append("</table></div></details>")

    if blocking:
        p.append("<div class='bad'><b>Settings differ between the runs.</b> A reproduction rate "
                 "is not meaningful across these. Shown only because --force was passed."
                 if total else
                 "<div class='bad'><b>Settings differ between the runs.</b> No rate reported.")
        p.append(_settings_table(blocking, "A", "B") + "</div>")

    if total:
        cls = "ok" if matched == total else "bad"
        p.append(f"<div class='rate {cls}'>{matched} / {total} identical "
                 f"&nbsp;<span style='font-size:1.2rem;font-weight:400'>{100.0*matched/total:.1f}%</span></div>")
    else:
        p.append("<div class='rate na'>no paired records</div>")

    if only_a or only_b:
        p.append(f"<div class='warn'>{len(only_a)} record(s) only in A, {len(only_b)} only in B. "
                 "Excluded from the rate above.</div>")

    if env_diff:
        p.append("<div class='warn'><b>Environment differs.</b> This is a portability comparison, "
                 "not a determinism test, and should be reported as one.")
        p.append(_settings_table(env_diff, "A", "B") + "</div>")

    # ---- per-record table ----
    p.append("<h2>Every pair</h2><div class='wrap'><table><tr>"
             "<th>#</th><th>checkpoint</th><th>task</th><th>seed</th><th>sample</th>"
             "<th>verdict</th><th>tokens A / B</th><th>hash A</th><th>hash B</th>"
             "<th>upstream hash</th><th>= upstream?</th></tr>")
    for i, v in enumerate(verdicts, 1):
        k = v["key"]; cls = "match" if v["match"] else "mismatch"
        p.append(f"<tr class='{cls}'><td><a href='#pair{i}'>{i}</a></td>"
                 f"<td>{_e(k['checkpoint_name'])}</td><td>{_e(k['task_id'])}</td>"
                 f"<td>{_e(k['seed'])}</td><td>{_e(k['sample_index'])}</td>"
                 f"<td>{_e(v['reason'])}</td><td>{_e(v['tokens_a'])} / {_e(v['tokens_b'])}</td>"
                 f"<td class='hash'>{_e((v['sha_a'] or '')[:12])}</td>"
                 f"<td class='hash'>{_e((v['sha_b'] or '')[:12])}</td>")
        up = v.get("upstream")
        if up and up.get("completion") is not None:
            import hashlib
            uh = hashlib.sha256(up["completion"].encode("utf-8")).hexdigest()
            same = "yes" if uh == v["sha_a"] else "no"
            p.append(f"<td class='hash'>{_e(uh[:12])}</td><td>{same}</td></tr>")
        else:
            p.append("<td class='hash'>\u2014</td><td>\u2014</td></tr>")
    p.append("</table></div>")

    # ---- texts side by side, mismatches first ----
    ordered = sorted(enumerate(verdicts, 1), key=lambda t: t[1]["match"])
    p.append("<h2>Side by side</h2>"
             "<div class='sub'>Mismatches first. Identical pairs are shown once, since both sides are the same bytes.</div>")
    for i, v in ordered:
        k = v["key"]
        p.append(f"<div class='card' id='pair{i}'><h3>#{i} &nbsp; {_e(k['task_id'])} &nbsp; "
                 f"<span style='color:{'#1b7f3b' if v['match'] else '#b3261e'}'>{_e(v['reason'])}</span></h3>")
        p.append(f"<details><summary style='cursor:pointer;color:#2b4c7e;font-weight:600'>Prompt</summary>"
                 f"<pre style='white-space:pre-wrap;background:#f6f6f6;border:1px solid #e2e2e2;"
                 f"border-radius:6px;padding:.75rem 1rem;font-size:13px'>{_e(v['prompt'])}</pre></details>")
        rb = (rubric or {}).get(k["task_id"])
        if rb:
            p.append("<details><summary style='cursor:pointer;color:#2b4c7e;font-weight:600'>Rubric</summary>"
                     "<div style='background:#f6f6f6;border:1px solid #e2e2e2;border-radius:6px;padding:.75rem 1rem;font-size:13px'>")
            p.append(f"<p><b>Judge focus.</b> {_e(rb['judge_focus'])}</p>")
            if rb["expected"]:
                p.append("<p><b>Expected core concepts</b></p><ul>" + "".join(f"<li>{_e(x)}</li>" for x in rb["expected"]) + "</ul>")
            if rb["failures"]:
                p.append("<p><b>Common failure modes</b></p><ul>" + "".join(f"<li>{_e(x)}</li>" for x in rb["failures"]) + "</ul>")
            p.append("<p><b>Scale</b></p><table style='font-size:12px'>" +
                     "".join(f"<tr><td style='width:2rem'><b>{_e(sc)}</b></td><td>{_e(txt)}</td></tr>"
                             for sc, txt in sorted(rb["scale"].items(), key=lambda t: str(t[0]))) +
                     "</table></div></details>")
        up = v.get("upstream")
        if up and up.get("completion") is not None:
            p.append(f"<details><summary style='cursor:pointer;color:#a15c00;font-weight:600'>"
                     f"Upstream's published answer, same checkpoint and task "
                     f"({up['n_completions']} sample{'s' if up['n_completions'] != 1 else ''} stored, first shown)</summary>"
                     f"<pre style='white-space:pre-wrap;background:#fff8ee;border:1px solid #e0b96a;"
                     f"border-radius:6px;padding:.75rem 1rem;font-size:13px'>{_e(up['completion'])}</pre></details>")
        if v["match"]:
            p.append(f"<pre style='white-space:pre-wrap;background:#fff;border:1px solid #cfd8e3;"
                     f"border-radius:6px;padding:.75rem 1rem;font-size:13px'>{_e(v['completion_a'])}</pre>")
        else:
            p.append("<div class='pair'>")
            for side in ("a", "b"):
                body = v.get(f"error_{side}") or v.get(f"completion_{side}")
                p.append(f"<div><h4>Run {side.upper()} &nbsp; {_e(v[f'tokens_{side}'])} tokens</h4><pre>{_e(body)}</pre></div>")
            p.append("</div>")
        p.append("</div>")

    p.append("</body></html>")
    with open(path, "w") as f:
        f.write("\n".join(p))


if __name__ == "__main__":
    sys.exit(main())

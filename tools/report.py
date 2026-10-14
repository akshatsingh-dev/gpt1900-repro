"""
Turn one or more logged_eval runs into the numbers the memo needs, on one page.

Why this exists
---------------
compare_runs.py answers one question: are two runs byte-identical? This
answers the rest. For every run ("series") it reports the denominator, the
error count, the text-level facts (how often the stock opening phrase appears,
how often max_tokens was hit), and once tools/judge.py has run, the mean score
with a bootstrap confidence interval, per task and per checkpoint. Between
series it reports byte agreement and score agreement on the cells they share.

Upstream's published run can be loaded as a series too, so ours sits beside
their 0.932 on the same page with the same denominators.

Works before judging (score sections say "not judged yet") and after.

Usage
-----
    # one run against upstream
    python tools/report.py evidence/sweep/v11-scaffolded.judged.jsonl \
        --upstream-dir upstream/gpt1900/results/physics_eval_v11 \
        --out evidence/sweep/report.json --html evidence/sweep/report.html

    # three prompt conditions side by side
    python tools/report.py evidence/prompt-sensitivity/*.judged.jsonl \
        --out evidence/prompt-sensitivity/report.json --html evidence/prompt-sensitivity/report.html

    # judge reliability: the same file judged twice
    python tools/report.py a.judged.jsonl a.judged-again.jsonl --html agreement.html
"""

import argparse
import hashlib
import html as _html
import json
import os
import random
import sys
from collections import Counter, defaultdict
from itertools import combinations

STOCK_OPENING = "You have touched"      # E023: 78% of published outputs begin this way
KEY = ("checkpoint_name", "task_id", "sample_index")
TASK_ORDER = ["uv_catastrophe_main", "photoelectric_effect_main", "sr_frozen_light",
              "sr_approaching_c", "sr_train_lightning", "sr_michelson_morley",
              "gr_main_elevator_light", "gr_free_fall_equivalence"]
SHORT = {"uv_catastrophe_main": "UV", "photoelectric_effect_main": "Photo", "sr_frozen_light": "Frozen",
         "sr_approaching_c": "ApprC", "sr_train_lightning": "Train", "sr_michelson_morley": "MM",
         "gr_main_elevator_light": "Elev", "gr_free_fall_equivalence": "Fall"}


# ---------------------------------------------------------------------------
# loading
# ---------------------------------------------------------------------------

def load_jsonl(path):
    """One record per key. If judge.py journaled a key twice, the scored line wins."""
    by_key = {}
    order = []
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
            k = (r.get("checkpoint_name"), r.get("task_id"), r.get("prompt_condition"),
                 r.get("seed"), r.get("sample_index"))
            if k not in by_key:
                order.append(k)
            if k not in by_key or r.get("score") is not None:
                by_key[k] = r
    return [by_key[k] for k in order]


def load_upstream(dirpath):
    """
    Upstream results directory -> records in our shape. generations.json gives
    the text, results_judged.json (if present) gives the score. Sample i of a
    cell is sample_index i.
    """
    gen_path = os.path.join(dirpath, "generations.json")
    judged_path = os.path.join(dirpath, "results_judged.json")
    gens = json.load(open(gen_path))
    judged = json.load(open(judged_path)) if os.path.exists(judged_path) else {}
    out = []
    for ck, tasks in gens.items():
        for tid, cell in tasks.items():
            comps = cell.get("completions") or []
            jsamples = judged.get(ck, {}).get(tid, {}).get("samples", [])
            for i, text in enumerate(comps):
                score = None
                rationale = None
                if i < len(jsamples):
                    score = jsamples[i].get("judge", {}).get("score")
                    rationale = jsamples[i].get("judge", {}).get("rationale")
                out.append({
                    "checkpoint_name": ck, "task_id": tid, "sample_index": i,
                    "prompt_condition": "minimal" if "no_assumptions" in dirpath else "scaffolded",
                    "mode": cell.get("mode"), "prompt": cell.get("prompt"),
                    "completion": text,
                    "completion_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                    "completion_tokens": None, "finish_reason": None, "error": None,
                    "score": score, "judge_raw_response": rationale,
                    "temperature": None, "seed": None, "num_samples": len(comps),
                    "_upstream": True,
                })
    return out


# ---------------------------------------------------------------------------
# statistics, stdlib only
# ---------------------------------------------------------------------------

def mean(xs):
    return sum(xs) / len(xs) if xs else None


def bootstrap_ci(xs, n_boot=2000, seed=0):
    """95% percentile bootstrap of the mean. Deterministic: seed recorded."""
    if len(xs) < 2:
        return None, None
    rng = random.Random(seed)
    n = len(xs)
    means = sorted(sum(rng.choice(xs) for _ in range(n)) / n for _ in range(n_boot))
    return means[int(0.025 * n_boot)], means[int(0.975 * n_boot)]


def summarize(records):
    """Everything worth knowing about one series."""
    # a regraded upstream record carries the hash but not the text; still a valid cell
    ok = [r for r in records if not r.get("error")
          and (r.get("completion") is not None or r.get("completion_sha256"))]
    scored = [r for r in ok if isinstance(r.get("score"), (int, float))]
    scores = [r["score"] for r in scored]
    lo, hi = bootstrap_ci(scores)
    tokens = [r["completion_tokens"] for r in ok if isinstance(r.get("completion_tokens"), (int, float))]

    per_task, per_ckpt, per_cond = defaultdict(list), defaultdict(list), defaultdict(list)
    for r in scored:
        per_task[r["task_id"]].append(r["score"])
        per_ckpt[r["checkpoint_name"]].append(r["score"])
        per_cond[r.get("prompt_condition")].append(r["score"])

    # how many distinct answers per cell, across samples/seeds: text-level variance
    cell_hashes = defaultdict(set)
    for r in ok:
        cell_hashes[(r["checkpoint_name"], r["task_id"])].add(r["completion_sha256"])
    multi = [len(v) for v in cell_hashes.values() if v]

    return {
        "records": len(records),
        "errors": len(records) - len(ok),
        "checkpoints": sorted({r["checkpoint_name"] for r in records}),
        "tasks": sorted({r["task_id"] for r in records}),
        "conditions": sorted({str(r.get("prompt_condition")) for r in records}),
        "settings": {k: sorted({repr(r.get(k)) for r in records})
                     for k in ("temperature", "top_k", "seed", "num_samples", "max_tokens",
                               "model_revision", "dtype", "gpu_name", "judge_model",
                               "judge_model_version", "judge_temperature", "eval_config_sha256")},
        "stock_opening": sum(1 for r in ok if (r.get("completion") or "").lstrip().startswith(STOCK_OPENING)),
        "hit_max_tokens": sum(1 for r in ok if r.get("finish_reason") == "length"),
        "mean_tokens": mean(tokens),
        "distinct_answers_per_cell": mean(multi),
        "scored": len(scored),
        "unscored": len(ok) - len(scored),
        "judge_failures": sum(1 for r in ok if r.get("judge_model") and r.get("score") is None),
        "score_mean": mean(scores),
        "score_ci95": [lo, hi],
        "score_hist": {str(s): c for s, c in sorted(Counter(scores).items())},
        "per_task": {t: {"n": len(v), "mean": mean(v)} for t, v in per_task.items()},
        "per_checkpoint": {c: {"n": len(v), "mean": mean(v)} for c, v in per_ckpt.items()},
        "per_condition": {c: {"n": len(v), "mean": mean(v)} for c, v in per_cond.items()},
    }


def pairwise(a_records, b_records):
    """Byte and score agreement on the cells two series share."""
    a = {tuple(r.get(k) for k in KEY): r for r in a_records if not r.get("error")}
    b = {tuple(r.get(k) for k in KEY): r for r in b_records if not r.get("error")}
    shared = sorted(set(a) & set(b))
    byte_same = sum(1 for k in shared if a[k].get("completion_sha256") == b[k].get("completion_sha256"))
    both_scored = [k for k in shared
                   if isinstance(a[k].get("score"), (int, float)) and isinstance(b[k].get("score"), (int, float))]
    diffs = [a[k]["score"] - b[k]["score"] for k in both_scored]
    return {
        "shared_cells": len(shared),
        "byte_identical": byte_same,
        "both_scored": len(both_scored),
        "score_exact_agreement": sum(1 for d in diffs if d == 0),
        "score_within_1": sum(1 for d in diffs if abs(d) <= 1),
        "mean_score_diff_a_minus_b": mean(diffs),
        "mean_abs_score_diff": mean([abs(d) for d in diffs]),
        "per_task_diff": {t: mean([a[k]["score"] - b[k]["score"] for k in both_scored if k[1] == t]) or 0.0
                          for t in sorted({k[1] for k in both_scored})},
    }


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------

def f2(v):
    return "—" if v is None else f"{v:.2f}"


def esc(v):
    return "<span style='color:#bbb'>—</span>" if v is None else _html.escape(str(v))


CSS = """
body{margin:0 auto;padding:2rem;max-width:1200px;font:14px/1.5 -apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:#1a1a1a;background:#fafafa}
h1{font-size:1.4rem;margin:0 0 .25rem}h2{font-size:1.1rem;margin:2rem 0 .5rem}h3{font-size:1rem;margin:1.2rem 0 .4rem}
.sub{color:#6b6b6b;margin-bottom:1rem}
table{border-collapse:collapse;background:#fff;font-size:13px;margin:.5rem 0}
th,td{text-align:left;padding:.35rem .6rem;border-bottom:1px solid #e2e2e2;vertical-align:top}
th{background:#f0f0f0;font-weight:600}td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
.wrap{overflow-x:auto}
.big{font-size:2rem;font-weight:700;margin:.2rem 0}
.card{background:#fff;border:1px solid #e2e2e2;border-radius:8px;padding:1rem 1.25rem;margin:1rem 0}
.muted{color:#6b6b6b}.warn{background:#fff6e5;border:1px solid #e0b96a;border-radius:6px;padding:.6rem 1rem;margin:.6rem 0}
.hash{font-family:ui-monospace,Menlo,monospace;font-size:12px}
"""


def render(series, pair_stats, title):
    p = [f"<!doctype html><html><head><meta charset='utf-8'><title>{_html.escape(title)}</title><style>{CSS}</style></head><body>",
         f"<h1>{_html.escape(title)}</h1>",
         f"<div class='sub'>{len(series)} series. Every number carries its denominator. "
         f"Confidence intervals are 95% percentile bootstrap of the mean, 2000 resamples, seed 0.</div>"]

    # ---- headline per series ----
    p.append("<h2>Headline</h2><div class='wrap'><table><tr><th>series</th><th class='num'>records</th>"
             "<th class='num'>errors</th><th class='num'>scored</th><th class='num'>mean score</th>"
             "<th>95% CI</th><th>score histogram 0..5</th><th class='num'>stock opening</th>"
             "<th class='num'>hit max_tokens</th><th class='num'>mean tokens</th></tr>")
    for name, s in series:
        hist = " ".join(f"{k}:{s['score_hist'].get(k, 0)}" for k in "012345") if s["scored"] else "not judged yet"
        ci = f"{f2(s['score_ci95'][0])} to {f2(s['score_ci95'][1])}" if s["score_ci95"][0] is not None else "—"
        p.append(f"<tr><td>{esc(name)}</td><td class='num'>{s['records']}</td><td class='num'>{s['errors']}</td>"
                 f"<td class='num'>{s['scored']} / {s['records'] - s['errors']}</td>"
                 f"<td class='num'><b>{f2(s['score_mean'])}</b></td><td>{ci}</td><td class='hash'>{hist}</td>"
                 f"<td class='num'>{s['stock_opening']} / {s['records'] - s['errors']}</td>"
                 f"<td class='num'>{s['hit_max_tokens']}</td><td class='num'>{f2(s['mean_tokens'])}</td></tr>")
    p.append("</table></div>")
    for name, s in series:
        if s["judge_failures"]:
            p.append(f"<div class='warn'><b>{esc(name)}</b>: {s['judge_failures']} judge call(s) failed and are "
                     f"recorded as null, not 0. They are excluded from the mean and the denominator says so.</div>")

    # ---- what ran ----
    p.append("<h2>What ran</h2>")
    for name, s in series:
        p.append(f"<details><summary style='cursor:pointer;color:#2b4c7e;font-weight:600'>{esc(name)}</summary>"
                 f"<div class='wrap'><table>")
        p.append(f"<tr><td class='muted'>checkpoints</td><td>{len(s['checkpoints'])}: {esc(', '.join(c.replace('discovery-rl-v11-', '') for c in s['checkpoints']))}</td></tr>")
        p.append(f"<tr><td class='muted'>tasks</td><td>{len(s['tasks'])}</td></tr>")
        p.append(f"<tr><td class='muted'>conditions</td><td>{esc(', '.join(s['conditions']))}</td></tr>")
        p.append(f"<tr><td class='muted'>distinct answers per cell</td><td>{f2(s['distinct_answers_per_cell'])} (1.0 means every sample of a cell was the same bytes)</td></tr>")
        for k, v in s["settings"].items():
            p.append(f"<tr><td class='muted'>{esc(k)}</td><td class='hash'>{esc(', '.join(v))}</td></tr>")
        p.append("</table></div></details>")

    # ---- per task ----
    any_scored = any(s["scored"] for _, s in series)
    if any_scored:
        p.append("<h2>Mean score per task</h2><div class='wrap'><table><tr><th>series</th>")
        p += [f"<th class='num'>{SHORT.get(t, t)}</th>" for t in TASK_ORDER]
        p.append("<th class='num'>all</th></tr>")
        for name, s in series:
            if not s["scored"]:
                continue
            p.append(f"<tr><td>{esc(name)}</td>")
            for t in TASK_ORDER:
                c = s["per_task"].get(t)
                p.append(f"<td class='num'>{f2(c['mean'])}<br><span class='muted'>n={c['n']}</span></td>" if c else "<td class='num'>—</td>")
            p.append(f"<td class='num'><b>{f2(s['score_mean'])}</b><br><span class='muted'>n={s['scored']}</span></td></tr>")
        p.append("</table></div>")

        # per condition, when a series spans several or several series differ
        conds = sorted({c for _, s in series for c in s["per_condition"]})
        if len(conds) > 1:
            p.append("<h2>Mean score per prompt condition</h2><div class='wrap'><table><tr><th>series</th>")
            p += [f"<th class='num'>{esc(c)}</th>" for c in conds]
            p.append("</tr>")
            for name, s in series:
                p.append(f"<tr><td>{esc(name)}</td>")
                for c in conds:
                    v = s["per_condition"].get(c)
                    p.append(f"<td class='num'>{f2(v['mean'])} <span class='muted'>n={v['n']}</span></td>" if v else "<td class='num'>—</td>")
                p.append("</tr>")
            p.append("</table></div>")

        # per checkpoint
        ckpts = sorted({c for _, s in series for c in s["per_checkpoint"]})
        if len(ckpts) > 1:
            p.append("<h2>Mean score per checkpoint</h2><div class='wrap'><table><tr><th>checkpoint</th>")
            p += [f"<th class='num'>{esc(name)}</th>" for name, _ in series]
            p.append("</tr>")
            for c in ckpts:
                p.append(f"<tr><td>{esc(c)}</td>")
                for _, s in series:
                    v = s["per_checkpoint"].get(c)
                    p.append(f"<td class='num'>{f2(v['mean'])} <span class='muted'>n={v['n']}</span></td>" if v else "<td class='num'>—</td>")
                p.append("</tr>")
            p.append("</table></div>")

    # ---- pairwise ----
    if pair_stats:
        p.append("<h2>Between series, on shared cells</h2>"
                 "<div class='sub'>A cell is one (checkpoint, task, sample index). Byte identical means the same "
                 "answer text. Score agreement means the judge gave the same number.</div>"
                 "<div class='wrap'><table><tr><th>A</th><th>B</th><th class='num'>shared cells</th>"
                 "<th class='num'>byte identical</th><th class='num'>both scored</th><th class='num'>exact score agreement</th>"
                 "<th class='num'>within 1</th><th class='num'>mean A&minus;B</th><th class='num'>mean |A&minus;B|</th></tr>")
        for a, b, st in pair_stats:
            if not st["shared_cells"]:
                continue
            p.append(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td><td class='num'>{st['shared_cells']}</td>"
                     f"<td class='num'>{st['byte_identical']} / {st['shared_cells']}</td>"
                     f"<td class='num'>{st['both_scored']}</td>"
                     f"<td class='num'>{st['score_exact_agreement']} / {st['both_scored']}</td>"
                     f"<td class='num'>{st['score_within_1']} / {st['both_scored']}</td>"
                     f"<td class='num'>{f2(st['mean_score_diff_a_minus_b'])}</td>"
                     f"<td class='num'>{f2(st['mean_abs_score_diff'])}</td></tr>")
        p.append("</table></div>")
        for a, b, st in pair_stats:
            if st["both_scored"] and st["per_task_diff"]:
                p.append(f"<h3>{esc(a)} minus {esc(b)}, per task</h3><div class='wrap'><table><tr>")
                p += [f"<th class='num'>{SHORT.get(t, t)}</th>" for t in TASK_ORDER if t in st["per_task_diff"]]
                p.append("</tr><tr>")
                p += [f"<td class='num'>{st['per_task_diff'][t]:+.2f}</td>" for t in TASK_ORDER if t in st["per_task_diff"]]
                p.append("</tr></table></div>")

    p.append("</body></html>")
    return "\n".join(p)


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Summarise logged_eval runs: denominators, text facts, scores, agreement")
    ap.add_argument("jsonl", nargs="*", help="logged_eval JSONL files, judged or not. Each is one series.")
    ap.add_argument("--upstream-dir", action="append", default=[],
                    help="an upstream results directory (generations.json [+ results_judged.json]). Repeatable.")
    ap.add_argument("--out", default=None, help="JSON summary")
    ap.add_argument("--html", default=None, help="HTML page")
    ap.add_argument("--title", default="GPT-1900 eval report")
    args = ap.parse_args()

    loaded = []
    for path in args.jsonl:
        name = os.path.relpath(path)
        loaded.append((name, load_jsonl(path)))
    for d in args.upstream_dir:
        loaded.append((f"upstream:{os.path.basename(os.path.normpath(d))}", load_upstream(d)))
    if not loaded:
        ap.error("give at least one JSONL or --upstream-dir")

    series = [(name, summarize(recs)) for name, recs in loaded]
    pairs = []
    for (na, ra), (nb, rb) in combinations(loaded, 2):
        pairs.append((na, nb, pairwise(ra, rb)))

    # ---- terminal ----
    line = "=" * 62
    print(line)
    print("REPORT")
    print(line)
    for name, s in series:
        ci = (f"  95% CI {f2(s['score_ci95'][0])} to {f2(s['score_ci95'][1])}"
              if s["score_ci95"][0] is not None else "")
        print(f"{name}")
        print(f"  records {s['records']}  errors {s['errors']}  scored {s['scored']}"
              f"  stock opening {s['stock_opening']}/{s['records'] - s['errors']}"
              f"  hit max_tokens {s['hit_max_tokens']}")
        if s["scored"]:
            print(f"  MEAN SCORE {f2(s['score_mean'])} (n={s['scored']}){ci}   hist "
                  + " ".join(f"{k}:{s['score_hist'].get(k, 0)}" for k in "012345"))
        else:
            print("  not judged yet")
    for a, b, st in pairs:
        if st["shared_cells"]:
            print(f"{a}  vs  {b}")
            print(f"  shared {st['shared_cells']}  byte identical {st['byte_identical']}"
                  + (f"  score exact agreement {st['score_exact_agreement']}/{st['both_scored']}"
                     f"  mean diff {f2(st['mean_score_diff_a_minus_b'])}" if st["both_scored"] else ""))
    print(line)

    if args.out:
        with open(args.out, "w") as f:
            json.dump({"series": [{"name": n, **s} for n, s in series],
                       "pairs": [{"a": a, "b": b, **st} for a, b, st in pairs]}, f, indent=2)
        print(f"wrote {args.out}")
    if args.html:
        with open(args.html, "w") as f:
            f.write(render(series, pairs, args.title))
        print(f"wrote {args.html}")


if __name__ == "__main__":
    main()

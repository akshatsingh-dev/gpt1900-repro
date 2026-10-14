"""
Turn grades written by a reader into judged JSONL, through the packet key.

Why this exists
---------------
judge.py scores answers through the Claude API and records the model,
temperature and prompt. When there is no API access, the same rubric can be
applied by a reader working through the blinded batches that blind_packet.py
writes. The reader sees answer ids and nothing else. This script takes their
grades, looks each id up in the sealed key, and writes a judged JSONL beside
each source file so that report.py can treat it exactly like an API pass.

The judge fields say plainly what happened: judge_model is whatever the
grader was, judge_temperature is null (not controllable), judge_raw_response
is the grader's own JSON line. Nothing is dressed up as an API call.

Grades file: one JSON object per line, {"id": "A001", "score": 3, ...},
which is what the batch files ask for. Several grades files can be given.

    python tools/judge_import.py --key evidence/review-packet/key.json \
        --grades evidence/review-packet/grades/*.jsonl \
        --grader "claude-fable-5-1, interactive, blinded batches of 24" \
        --out-suffix .graded.jsonl
"""

import argparse
import glob
import hashlib
import json
import os
import sys
from datetime import datetime, timezone


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_jsonl(path):
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


def main():
    ap = argparse.ArgumentParser(description="Import reader grades through the packet key")
    ap.add_argument("--key", required=True, help="key.json from blind_packet.py")
    ap.add_argument("--grades", nargs="+", required=True, help="grades JSONL files (globs ok)")
    ap.add_argument("--grader", required=True, help="who or what graded, recorded as judge_model")
    ap.add_argument("--out-suffix", default=".graded.jsonl")
    args = ap.parse_args()

    key = json.load(open(args.key))
    by_id = {a["id"]: a for a in key["answers"]}

    grades = {}
    dupes = 0
    for pattern in args.grades:
        for path in sorted(glob.glob(pattern)) or [pattern]:
            for g in load_jsonl(path):
                if g.get("id") in grades:
                    dupes += 1
                grades[g["id"]] = {**g, "_file": os.path.basename(path)}
    if dupes:
        print(f"WARNING: {dupes} id(s) graded more than once, last one kept")

    unknown = sorted(set(grades) - set(by_id))
    if unknown:
        print(f"WARNING: {len(unknown)} graded id(s) not in the key: {unknown[:5]}")
    missing = sorted(set(by_id) - set(grades))

    # group by source file, so each gets one judged JSONL beside it
    by_source = {}
    for aid, a in by_id.items():
        by_source.setdefault(a["source"], {})[a["completion_sha256"]] = (aid, a)

    total_written = total_scored = 0
    for source, cells in by_source.items():
        if source.startswith("upstream:"):
            # their published answers, regraded: write them out in our record
            # shape so report.py can treat them as a series
            dirpath = source[len("upstream:"):]
            out_path = os.path.join(os.path.dirname(args.key), f"{os.path.basename(os.path.normpath(dirpath))}.regraded.jsonl")
            scored = written = 0
            with open(out_path, "w") as out:
                for sha, (aid, a) in cells.items():
                    g = grades.get(aid)
                    try:
                        score = int(g["score"]) if g else None
                    except (KeyError, TypeError, ValueError):
                        score = None
                    out.write(json.dumps({
                        "checkpoint_name": a["checkpoint"], "task_id": a["task_id"],
                        "sample_index": a["sample_index"], "prompt_condition": a["prompt_condition"],
                        "seed": None, "mode": None, "completion": None, "completion_sha256": sha,
                        "completion_tokens": None, "finish_reason": None, "error": None,
                        "temperature": None, "top_k": None, "num_samples": None, "max_tokens": None,
                        "model_repo": None, "model_revision": None, "eval_config_sha256": None,
                        "dtype": None, "gpu_name": None, "_upstream": True, "_source": source,
                        "judge_model": args.grader if g else None, "judge_model_version": None,
                        "judge_prompt_sha256": hashlib.sha256((args.key + "|" + aid).encode("utf-8")).hexdigest() if g else None,
                        "judge_temperature": None,
                        "judge_raw_response": json.dumps({k: v for k, v in g.items() if k != "_file"}) if g else None,
                        "score": score, "judged_at_utc": utc_now() if g else None,
                        "upstream_published_score": a.get("llm_judge_score"),
                    }) + "\n")
                    written += 1
                    scored += score is not None
            print(f"{source}: {scored} of {written} regraded -> {out_path}")
            total_written += written
            total_scored += scored
            continue
        if not os.path.exists(source):
            print(f"skip {source}: not found on this machine")
            continue
        records = load_jsonl(source)
        out_path = os.path.splitext(source)[0] + args.out_suffix
        scored = 0
        with open(out_path, "w") as out:
            for r in records:
                new = dict(r)
                hit = cells.get(r.get("completion_sha256"))
                if hit and hit[0] in grades:
                    aid, _ = hit
                    g = grades[aid]
                    try:
                        score = int(g["score"])
                    except (KeyError, TypeError, ValueError):
                        score = None
                    new.update({
                        "judge_model": args.grader,
                        "judge_model_version": None,
                        "judge_prompt_sha256": hashlib.sha256(
                            (args.key + "|" + aid).encode("utf-8")).hexdigest(),
                        "judge_temperature": None,
                        "judge_raw_response": json.dumps({k: v for k, v in g.items() if k != "_file"}),
                        "score": score,
                        "judged_at_utc": utc_now(),
                    })
                    scored += score is not None
                out.write(json.dumps(new) + "\n")
        print(f"{source}: {scored} of {len(records)} scored -> {out_path}")
        total_written += len(records)
        total_scored += scored

    print(f"\ngraded ids {len(grades)}   in key {len(by_id)}   ungraded {len(missing)}"
          + (f"   first ungraded {missing[:5]}" if missing else ""))
    print(f"records written {total_written}   scored {total_scored}   grader '{args.grader}'")


if __name__ == "__main__":
    main()

"""
Cut one task out of an eval config, leaving every other field byte-identical.

Why this exists
---------------
logged_eval.py has no task-id filter. --limit-tasks slices from the front and
the elevator task is index 6 of 8. A one-task config file is the clean way to
run a single task: eval_config_sha256 still identifies exactly what was asked,
and logged_eval.py needs no change.

Same pattern as make_leading_config.py: read the source as text, keep its
sha256, change only the tasks list, stamp _derived_from.

    python tools/make_task_config.py --source upstream/gpt1900/EVAL.json \
        --task gr_main_elevator_light --out tools/EVAL_elevator_scaffolded.json
"""

import argparse
import hashlib
import json
import os


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--task", required=True, help="task id to keep")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    raw = open(a.source).read()
    cfg = json.loads(raw)
    src_sha = hashlib.sha256(raw.encode("utf-8")).hexdigest()

    keep = [t for t in cfg["tasks"] if t["id"] == a.task]
    if len(keep) != 1:
        raise SystemExit(f"{a.task}: found {len(keep)} in {a.source}, expected 1. "
                         f"ids: {[t['id'] for t in cfg['tasks']]}")

    # everything except tasks must survive untouched
    before = {k: v for k, v in cfg.items() if k not in ("tasks", "_derived_from")}
    cfg["tasks"] = keep
    after = {k: v for k, v in cfg.items() if k not in ("tasks", "_derived_from")}
    assert json.dumps(before, sort_keys=True) == json.dumps(after, sort_keys=True)

    prior = cfg.get("_derived_from")
    cfg["_derived_from"] = {
        "file": os.path.relpath(a.source),
        "sha256": src_sha,
        "change": f"tasks filtered to id == {a.task}; all other fields unchanged",
        "prior_derivation": prior,
    }

    with open(a.out, "w") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    out_sha = hashlib.sha256(open(a.out).read().encode("utf-8")).hexdigest()
    print(f"wrote {os.path.relpath(a.out)}")
    print(f"  source {os.path.relpath(a.source)} sha256 {src_sha[:16]}")
    print(f"  output sha256 {out_sha[:16]}, 1 task: {keep[0]['id']}, "
          f"{len(keep[0]['prompt_lines'])} prompt lines")


if __name__ == "__main__":
    main()

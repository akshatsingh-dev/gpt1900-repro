"""
Merge blinded reader verdicts back through the shuffle key.

The reading files give each answer an R### id so the reader sees no
provenance. This maps the verdicts back to checkpoint|task|seed, the key
freefall_jump.py and open_report.py expect, and keeps the blinded file too.

    python tools/merge_blind_readings.py --key evidence/freefall/seed-read-key.json \
        --verdicts evidence/freefall/seed-verdicts-1.jsonl evidence/freefall/seed-verdicts-2.jsonl \
        --reader "blinded reader, fresh sessions, 1 Oct 2026" \
        --out evidence/freefall/readings.json --blind-out evidence/freefall/readings-blind.json
"""

import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", required=True)
    ap.add_argument("--verdicts", nargs="+", required=True)
    ap.add_argument("--reader", required=True)
    ap.add_argument("--allowed", default="geometry,not-a-force,equivalence,none,loops,incoherent")
    ap.add_argument("--out", required=True)
    ap.add_argument("--blind-out", default=None)
    a = ap.parse_args()

    ids = json.load(open(a.key))["ids"]
    allowed = set(a.allowed.split(","))
    blind, verdicts, notes, bad = {}, {}, {}, []
    for path in a.verdicts:
        for n, line in enumerate(open(path), 1):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError as exc:
                bad.append(f"{path}:{n} unparseable ({exc})"); continue
            rid, v = r.get("id"), r.get("verdict")
            if rid not in ids:
                bad.append(f"{path}:{n} unknown id {rid}"); continue
            if v not in allowed:
                bad.append(f"{path}:{n} {rid} verdict {v!r} not in {sorted(allowed)}"); continue
            if rid in blind:
                bad.append(f"{path}:{n} {rid} read twice, keeping first"); continue
            blind[rid] = v
            verdicts[ids[rid]] = v
            if r.get("note"):
                notes[ids[rid]] = r["note"]
    missing = sorted(set(ids) - set(blind))
    json.dump({"reader": a.reader, "verdicts": verdicts, "notes": notes}, open(a.out, "w"), indent=1)
    if a.blind_out:
        json.dump({"reader": a.reader, "verdicts": blind}, open(a.blind_out, "w"), indent=1)
    for b in bad:
        print("WARN", b, file=sys.stderr)
    print(f"read {len(blind)} of {len(ids)}; missing {len(missing)}" + (f": {missing[:6]}" if missing else "")
          + f"; wrote {a.out}" + (f" and {a.blind_out}" if a.blind_out else ""))
    return 1 if missing or bad else 0


if __name__ == "__main__":
    sys.exit(main())

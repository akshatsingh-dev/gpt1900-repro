"""
Third reader through the OpenAI Decisions API (POST /v1/decisions, model gpt-6-luna).
Typed answers with probabilities, no free text. The API sees only the prompt, the
expected answer and the model's text, never the checkpoint or seed, so it is blind
by construction.

Two modes:
  verdict   one choice question per answer, options = the verdict ladder in the
            eval config (verdicts + verdict_help). For the abduction and elevator runs.
  rubric    one score question per answer, levels = the 0-5 scoring_rubric in the
            eval config. For the sweep and sensitivity runs, to sit beside the
            Claude grades and the published ones.

    python tools/decide.py evidence/abduction/abduction.jsonl --config tools/EVAL_abduction.json \
        --mode verdict --out evidence/abduction/decisions.jsonl --dry-run
    export OPENAI_API_KEY=...   # then drop --dry-run

Output is one json line per answer, journal-appended, so a rerun skips answers
already decided. Nothing is sent in --dry-run; it prints the token and cost estimate.
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
import time

import requests

URL = "https://api.openai.com/v1/decisions"
MODEL = "gpt-6-luna"
PRICE_PER_M_INPUT = 0.10  # USD, input tokens only, no output charge (docs, Oct 2026)


def rung_descriptions(help_text):
    """'wrong: ... weightless: ... none: ...' -> {rung: description}"""
    out = {}
    for m in re.finditer(r"(?:^|\s)([a-z][a-z-]*):\s(.*?)(?=\s[a-z][a-z-]*:\s|$)", help_text, re.S):
        out[m.group(1)] = m.group(2).strip()
    return out


def build(r, tc, mode):
    answer = r.get("completion") or ""
    if mode == "verdict":
        desc = rung_descriptions(tc.get("verdict_help", ""))
        choices = [{"value": v, "description": desc.get(v, v)} for v in tc["verdicts"]]
        q = {"type": "choice", "name": "verdict",
             "instructions": ("Read the answer. Pick the highest rung the answer reaches on its own, "
                              "using the rung descriptions. An answer that only repeats the question's premise "
                              "does not reach a rung for it. Loops means the text repeats itself; incoherent means "
                              "it cannot be read as an answer."),
             "choices": choices}
        text = (f"QUESTION PUT TO THE MODEL:\n{r['prompt']}\n\n"
                f"A FULLY CORRECT ANSWER WOULD SAY:\n{tc.get('expected', '')}\n\n"
                f"THE MODEL'S ANSWER:\n{answer}")
    else:
        rub = tc["scoring_rubric"]
        levels = [{"label": str(k), "description": rub[str(k)]} for k in range(6)]
        q = {"type": "score", "name": "score",
             "instructions": (tc.get("judge_focus", "") + " Core concepts to look for: "
                              + " ".join(tc.get("expected_core_concepts", []))
                              + " Score the answer against the levels, 0 to 5."),
             "levels": levels}
        text = f"QUESTION PUT TO THE MODEL:\n{r['prompt']}\n\nTHE MODEL'S ANSWER:\n{answer}"
    return {"model": MODEL, "input": text, "questions": [q]}


def key(r):
    return f"{r['checkpoint_name']}|{r['task_id']}|{r.get('seed')}|{r.get('sample_index', 0)}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl")
    ap.add_argument("--config", required=True)
    ap.add_argument("--mode", choices=["verdict", "rubric"], required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.2)
    ap.add_argument("--limit", type=int, default=None, help="send only the first N undecided answers (cheap first test)")
    a = ap.parse_args()

    rs = [json.loads(l) for l in open(a.jsonl) if l.strip()]
    cfg = {t["id"]: t for t in json.load(open(a.config))["tasks"]}
    done = set()
    if os.path.exists(a.out):
        done = {key(json.loads(l)) for l in open(a.out) if l.strip()}
    todo = [r for r in rs if key(r) not in done and r["task_id"] in cfg]
    if a.limit:
        todo = todo[:a.limit]

    reqs = [(r, build(r, cfg[r["task_id"]], a.mode)) for r in todo]
    chars = sum(len(json.dumps(b)) for _, b in reqs)
    est_tokens = chars / 4
    print(f"{len(rs)} answers, {len(done)} already decided, {len(todo)} to send. "
          f"~{est_tokens:,.0f} input tokens, ~${est_tokens / 1e6 * PRICE_PER_M_INPUT:.3f} at ${PRICE_PER_M_INPUT}/M.")
    if a.dry_run:
        if reqs:
            print("sample request:"); print(json.dumps(reqs[0][1], indent=1)[:2500])
        return
    k = os.environ.get("OPENAI_API_KEY")
    if not k:
        sys.exit("OPENAI_API_KEY not set")
    H = {"Authorization": f"Bearer {k}", "Content-Type": "application/json"}
    n_ok = n_fail = 0
    with open(a.out, "a") as f:
        for i, (r, body) in enumerate(reqs, 1):
            rec = {"key": key(r), "checkpoint_name": r["checkpoint_name"], "task_id": r["task_id"],
                   "seed": r.get("seed"), "sample_index": r.get("sample_index", 0),
                   "completion_sha256": r.get("completion_sha256"), "mode": a.mode,
                   "decision_model": MODEL, "decided_at_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
            try:
                resp = requests.post(URL, headers=H, json=body, timeout=60)
                rec["request_id"] = resp.headers.get("x-request-id")
                rec["http_status"] = resp.status_code
                j = resp.json()
                rec["raw"] = j
                ans = (j.get("answers") or [{}])[0]
                rec["answer_type"] = ans.get("type")
                if ans.get("type") == "choice":
                    rec["verdict"] = ans.get("choice"); rec["confidence"] = ans.get("confidence")
                    rec["probabilities"] = {p["value"]: p["probability"] for p in ans.get("probabilities", [])}
                elif ans.get("type") == "score":
                    rec["score"] = ans.get("score"); rec["confidence"] = ans.get("confidence")
                    rec["probabilities"] = {str(p["value"]): p["probability"] for p in ans.get("probabilities", [])}
                else:
                    rec["error"] = j.get("error") or ans
                n_ok += 1 if "error" not in rec else 0; n_fail += 1 if "error" in rec else 0
            except Exception as e:  # network or parse; keep the failure, no silent zero
                rec["error"] = repr(e); n_fail += 1
            f.write(json.dumps(rec, ensure_ascii=False) + "\n"); f.flush()
            if i % 20 == 0 or i == len(reqs):
                print(f"{i}/{len(reqs)} sent, {n_ok} ok, {n_fail} failed")
            time.sleep(a.sleep)
    print(f"-> {a.out}")


if __name__ == "__main__":
    main()

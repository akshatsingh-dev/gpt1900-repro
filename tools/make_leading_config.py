"""
Build the "leading prompt" eval config from upstream's EVAL.json.

Why this exists
---------------
Prompt sensitivity needs three conditions. Upstream ships two: EVAL.json
(scaffolded: the classical assumptions are spelled out) and
EVAL_no_assumptions.json (minimal: they are not). The third, a prompt that
deliberately gives away part of the answer, did not exist. This makes it.

The file is generated rather than hand-edited so that every field except
prompt_lines is byte-identical to EVAL.json. The judge therefore sees exactly
the same rubric, focus and expected concepts in all three conditions, and any
score difference is caused by the prompt the model saw and nothing else.

Each task gets one extra paragraph appended after the original question. The
question wording itself is untouched.

    python tools/make_leading_config.py
    # writes tools/EVAL_leading.json and prints what changed
"""

import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "upstream", "gpt1900", "EVAL.json")
OUT = os.path.join(HERE, "EVAL_leading.json")

# One hint per task. Each one hands the model the core idea the rubric is
# looking for, on purpose. If scores jump under these prompts, the benchmark
# is partly measuring how much of the answer the prompt already contains.
HINTS = {
    "uv_catastrophe_main":
        "Hint: consider whether each mode can only take up energy in discrete "
        "lumps whose size grows with frequency, so that high-frequency modes are "
        "almost never excited at ordinary temperatures.",
    "photoelectric_effect_main":
        "Hint: consider whether light delivers its energy in individual packets, "
        "each carrying an energy set by the light's frequency, so that one packet "
        "either has enough energy to free an electron or it does not.",
    "sr_frozen_light":
        "Hint: if every observer measures light at the same speed c, then no "
        "observer can ever catch up with a light wave, and the ordinary rule for "
        "adding velocities cannot be right. Consider what that implies about "
        "measurements of distance and time.",
    "sr_approaching_c":
        "Hint: consider that the added energy might go into the object's momentum "
        "and energy of motion without a matching increase in speed, so that the "
        "speed approaches c but never reaches it.",
    "sr_train_lightning":
        "Hint: the train observer moves toward the light from the front strike and "
        "away from the light from the back strike, so the front flash reaches them "
        "first. Consider what that implies about whether the two strikes were "
        "simultaneous for the train observer.",
    "sr_michelson_morley":
        "Hint: consider dropping the aether entirely and taking the fixed speed of "
        "light as a law that holds for every observer, which would mean the "
        "ordinary rule for adding velocities, and the notion of absolute time, "
        "must be revised.",
    "gr_main_elevator_light":
        "Hint: consider that gravity might not be a force pulling on mass at all, "
        "but a change in the shape of space and time itself, which light follows "
        "like everything else.",
    "gr_free_fall_equivalence":
        "Hint: consider that free fall might be the natural, unforced state of "
        "motion, and that what we call gravity is an effect of the structure of "
        "space and time, which is why it can be removed locally by falling.",
}


def main():
    raw = open(SRC).read()
    cfg = json.loads(raw)

    ids = [t["id"] for t in cfg["tasks"]]
    missing = set(ids) - set(HINTS)
    extra = set(HINTS) - set(ids)
    if missing or extra:
        raise SystemExit(f"task list changed: missing hints {sorted(missing)}, "
                         f"unused hints {sorted(extra)}")

    for task in cfg["tasks"]:
        task["prompt_lines"] = list(task["prompt_lines"]) + ["", HINTS[task["id"]]]

    # provenance: which exact EVAL.json this was derived from
    cfg["_derived_from"] = {
        "file": "EVAL.json",
        "sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        "change": "one 'Hint:' paragraph appended to prompt_lines of every task; "
                  "all judge fields unchanged",
        "prompt_condition": "leading",
    }

    with open(OUT, "w") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"wrote {os.path.relpath(OUT)}")
    print(f"source EVAL.json sha256 {cfg['_derived_from']['sha256'][:16]}...")
    for task in cfg["tasks"]:
        print(f"  {task['id']:28} +{len(HINTS[task['id']])} chars")


if __name__ == "__main__":
    main()

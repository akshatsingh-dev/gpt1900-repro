"""
Build the abduction suite and the final elevator case from upstream's EVAL.json.

Three groups, every prompt in period-neutral English a pre-1900 reader would
follow. Each task carries, beside prompt_lines, the fields a blind reader
needs: the expected top answer and the ordered verdict list for that task.
Shared judge fields are copied from EVAL.json unchanged so logged_eval.py
accepts the file; the rubric grader is not used on these prompts.

  final    the elevator test case in the draft paper's own words: an elevator whose cable
           breaks, what would it feel like. Four phrasings.
  ladder   the 1907 observation with increasing amounts of help, to find the
           point on the ladder where the equivalence first appears.
  control  reasoning-type controls for the "LLMs can't jump" claim: deduction
           and induction inside the corpus, abduction inside the corpus
           (Neptune), abduction beyond it (Michelson-Morley, black body).

    python tools/make_abduction_config.py
    # writes tools/EVAL_abduction.json and tools/EVAL_elevator_final.json
"""

import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "upstream", "gpt1900", "EVAL.json")

OBS = ["A person falling freely from a roof does not feel their own weight during the fall.",
       "",
       "In a small cabin falling freely, nearby released objects float beside them.",
       ""]

GR = ["wrong", "none", "weightless", "equivalence", "not-a-force", "geometry", "loops", "incoherent"]
GR_HELP = ("wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. "
           "weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, "
           "but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel "
           "like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an "
           "ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, "
           "curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. "
           "loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.")

TASKS = [
    # ---- final: the draft paper's words -------------------------------------
    dict(id="elev_cable_feel", group="final", reasoning="abduction", in_corpus=False,
         prompt_lines=["You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.", "",
                       "What do you feel during the fall?"],
         expected="Weightlessness; the full answer goes on to say gravity and acceleration are the same thing felt from inside.",
         verdicts=GR, verdict_help=GR_HELP),
    dict(id="elev_cable_feel_why", group="final", reasoning="abduction", in_corpus=False,
         prompt_lines=["You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.", "",
                       "What do you feel during the fall? Explain why, and say what this tells us about gravity."],
         expected="Weightlessness, because everything falls together; so gravity felt as weight is indistinguishable from acceleration, and can be removed by falling.",
         verdicts=GR, verdict_help=GR_HELP),
    dict(id="elev_cable_stone", group="final", reasoning="abduction", in_corpus=False,
         prompt_lines=["A man stands in an elevator when the cable breaks and the elevator falls freely.",
                       "He holds a stone out at arm's length and lets go of it.", "",
                       "What does he see the stone do? What does this tell us about weight?"],
         expected="The stone stays beside his hand; weight is not a property of the stone but of being held back from falling; gravity and acceleration are the same from inside.",
         verdicts=GR, verdict_help=GR_HELP),
    dict(id="elev_cable_scale", group="final", reasoning="abduction", in_corpus=False,
         prompt_lines=["A man stands on a weighing scale inside an elevator. The cable breaks and the elevator falls freely.", "",
                       "What does the scale show during the fall, and what does that mean?"],
         expected="The scale shows nothing; weight is the floor pushing back, absent in free fall; gravity is locally the same as acceleration.",
         verdicts=GR, verdict_help=GR_HELP),
    # ---- ladder: the 1907 observation with increasing help ---------------
    dict(id="ladder_1_mistaken", group="ladder", reasoning="abduction", in_corpus=False,
         prompt_lines=OBS + ["Something in our ordinary understanding of gravity must be mistaken. What is it?"],
         expected="That gravity is a force one always feels; in fact it can be made to vanish by falling, so it is locally the same as acceleration.",
         verdicts=GR, verdict_help=GR_HELP),
    dict(id="ladder_2_carriage", group="ladder", reasoning="abduction", in_corpus=False,
         prompt_lines=OBS + ["Compare this with a man in a closed carriage that is pulled forward with ever increasing speed, who feels himself pressed back into his seat.", "",
                             "What do the two cases have in common?"],
         expected="In both, what is felt as weight is the vehicle pushing on the body; gravity and acceleration are the same from inside; falling removes one as the carriage creates the other.",
         verdicts=GR, verdict_help=GR_HELP),
    dict(id="ladder_3_undetectable", group="ladder", reasoning="abduction", in_corpus=False,
         prompt_lines=OBS + ["Suppose no experiment the falling man can perform inside the cabin will reveal gravity to him.", "",
                             "What follows about the nature of gravity?"],
         expected="Gravity is not an ordinary force but a feature of the frame of motion, locally removable, equivalent to acceleration; a strong answer reaches geometry.",
         verdicts=GR, verdict_help=GR_HELP),
    # ---- controls ---------------------------------------------------------
    dict(id="ded_ship_mast", group="control", reasoning="deduction", in_corpus=True,
         prompt_lines=["A ship sails steadily across a calm sea. A sailor at the top of the mast lets a stone fall.", "",
                       "Where does the stone land on the deck: at the foot of the mast, behind it, or ahead of it? Explain."],
         expected="At the foot of the mast, because the stone shares the ship's forward motion (Galileo's argument, well known before 1900).",
         verdicts=["correct", "partial", "wrong", "none", "loops", "incoherent"],
         verdict_help="correct: foot of the mast, with the shared-motion reason. partial: foot of the mast without a reason, or the right reason with a hedge. wrong: behind or ahead. none: no answer to the question."),
    dict(id="ded_two_stones", group="control", reasoning="deduction", in_corpus=True,
         prompt_lines=["Two stones, one ten times heavier than the other, are let fall at the same instant from the top of a tower.", "",
                       "Which strikes the ground first? Explain."],
         expected="They strike together (air aside); the heavier is pulled harder but is harder to move by the same factor.",
         verdicts=["correct", "partial", "wrong", "none", "loops", "incoherent"],
         verdict_help="correct: together, with a reason. partial: together without a reason, or 'nearly together, air resistance aside' hedged. wrong: the heavier first. none: no answer."),
    dict(id="ind_pendulum", group="control", reasoning="induction", in_corpus=True,
         prompt_lines=["A pendulum one foot long swings once in about one second; four feet long, in about two seconds; nine feet long, in about three seconds; sixteen feet long, in about four seconds.", "",
                       "What rule connects the length of a pendulum to the time of its swing?"],
         expected="The time goes as the square root of the length (four times the length, twice the time).",
         verdicts=["correct", "partial", "wrong", "none", "loops", "incoherent"],
         verdict_help="correct: square root, or 'length as the square of the time', or 'four times the length doubles the time' generalised. partial: 'longer swings slower' only, or the right numbers restated without the rule. wrong: time proportional to length or any other rule. none: no rule given."),
    dict(id="abd_uranus", group="control", reasoning="abduction", in_corpus=True,
         prompt_lines=["The planet Uranus is observed to wander slightly from the path that Newton's law predicts for it, as if some influence not yet accounted for were acting upon it.", "",
                       "What might explain this?"],
         expected="An unseen planet beyond Uranus pulling on it (the Neptune hypothesis of 1846, inside the corpus).",
         verdicts=["correct", "partial", "wrong", "none", "loops", "incoherent"],
         verdict_help="correct: an undiscovered planet or body beyond it. partial: 'some other attracting body' or 'another planet' without placing it, or several hypotheses including this one. wrong: Newton's law is wrong, a resisting medium, comets, divine action, with no unseen body. none: no explanation offered."),
    dict(id="abd_mm_bare", group="control", reasoning="abduction", in_corpus=False,
         prompt_lines=["Light is sent along the direction of the Earth's motion through space, and also at right angles to it, and the two speeds are compared with the greatest care.",
                       "No difference is found, however the apparatus is turned.", "",
                       "What must be true for this to be so?"],
         expected="The speed of light is the same for every observer whatever their motion, so there is no detectable medium at rest; ordinary addition of velocities fails for light.",
         verdicts=["correct", "partial", "wrong", "none", "loops", "incoherent"],
         verdict_help="correct: light's speed is the same for all observers, or motion through a medium cannot be detected in principle and the medium idea must go. partial: the medium is carried along with the Earth, or the apparatus shrinks in the direction of motion, or the Earth happens to be at rest in the medium (ad hoc rescues). wrong: the measurement must be in error, or light has no speed. none: no explanation."),
    dict(id="abd_bb_bare", group="control", reasoning="abduction", in_corpus=False,
         prompt_lines=["A heated body glows. As one looks to higher and higher frequencies of its light, the energy given out at each frequency rises to a peak and then falls away to nothing,",
                       "instead of growing without limit as the theory of equal sharing of energy among all vibrations would predict.", "",
                       "What must be wrong with that theory?"],
         expected="Energy cannot be shared continuously among all vibrations; the high-frequency vibrations are not excited because energy is exchanged in lumps that grow with frequency.",
         verdicts=["correct", "partial", "wrong", "none", "loops", "incoherent"],
         verdict_help="correct: energy is taken up in discrete amounts, larger at higher frequency, so high frequencies are starved. partial: equal sharing fails at high frequency, or the high vibrations are somehow restrained, without a mechanism. wrong: the measurement is at fault, or the body is not hot enough. none: no answer."),
]


def main():
    raw = open(SRC).read()
    base = json.loads(raw)
    shared = {k: v for k, v in base.items() if k != "tasks"}
    judge_fields = {k: base["tasks"][7][k] for k in ("category", "judge_focus", "expected_core_concepts",
                                                     "common_failure_modes", "scoring_rubric")}
    tasks = []
    for t in TASKS:
        tasks.append({**judge_fields, "title": t["id"], **t})
    derived = {"file": "EVAL.json", "sha256": hashlib.sha256(raw.encode()).hexdigest(),
               "change": "new prompts; judge fields copied from gr_free_fall_equivalence so the file validates; not for rubric grading, for blind reading with the per-task verdict list"}
    out = {**shared, "tasks": tasks, "_derived_from": {**derived, "prompt_condition": "abduction"}}
    with open(os.path.join(HERE, "EVAL_abduction.json"), "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False); f.write("\n")
    final = {**shared, "tasks": [x for x in tasks if x["id"] == "elev_cable_feel_why"],
             "_derived_from": {**derived, "prompt_condition": "final"}}
    with open(os.path.join(HERE, "EVAL_elevator_final.json"), "w") as f:
        json.dump(final, f, indent=2, ensure_ascii=False); f.write("\n")
    print(f"wrote EVAL_abduction.json ({len(tasks)} tasks) and EVAL_elevator_final.json (1 task)")
    for t in tasks:
        print(f"  {t['group']:8} {t['reasoning']:10} {'corpus' if t['in_corpus'] else 'beyond':7} {t['id']}")


if __name__ == "__main__":
    main()

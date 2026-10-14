# Lab notebook

Append-only. Newest entries at the bottom. Nothing is deleted, including
mistakes, dead ends and failed runs. If a run was wrong, the entry stays and a
later entry says why it was wrong.

Entries are numbered `E001`, `E002` and so on, so findings can be cited by
number in the weekly reports and in the final packet.

Raw terminal output for each command is saved under `logs/` and referenced by
filename.

**Fields**

- **Phase** which phase of `notes/plan.md` this belongs to
- **Goal** what question this step was meant to answer
- **Command** exactly what was run
- **Exit status** and duration
- **Upstream commit** the pinned GPT-1900 commit in effect
- **Raw log** path under `logs/`
- **Result** what actually came back, including failures, with denominators
- **Interpretation** what it means, stated no more strongly than the data allows
- **Next** what this unblocks

---

## E001 - 2026-08-25 00:59 PT - workspace created

- **Phase:** 0, workspace and provenance
- **Goal:** Set up a directory layout that separates upstream code, own code, raw logs and finished evidence, so the final packet can be assembled without guessing where anything came from.
- **Command:** `mkdir -p notes tools logs evidence upstream`
- **Exit status:** 0
- **Upstream commit:** not cloned yet
- **Raw log:** none
- **Result:** Workspace created. Initially at `Desktop/College/ResearchKeeting/einstein-sprint`, later moved and renamed, see E002.
- **Interpretation:** No scientific content. Setup only.
- **Next:** Move to final location, clone upstream.

## E002 - 2026-08-25 01:03 PT - workspace moved and renamed

- **Phase:** 0
- **Goal:** Put the sprint inside the existing `Projects` git repo so the work is versioned alongside everything else, without letting multi-gigabyte checkpoints into a repo that gets pushed.
- **Command:** `mv .../einstein-sprint .../Projects/gpt1900-repro`, then `rm -rf gpt1900-repro/.git`
- **Exit status:** 0
- **Upstream commit:** not cloned yet
- **Raw log:** none
- **Result:** Workspace now at `~/Desktop/Akshat/Projects/gpt1900-repro/`. The nested `.git` created during the first attempt was removed, since a repo inside a repo is recorded by git as a broken pointer rather than as files.
- **Interpretation:** Setup only. One real constraint recorded: `Projects` is pushed to a remote, so weights must never enter the working tree.
- **Next:** Write a gitignore before anything downloads.

## E003 - 2026-08-25 01:03 PT - gitignore written

- **Phase:** 0
- **Goal:** Prevent checkpoints, Hugging Face cache, API keys and the upstream clone from ever being committed.
- **Command:** wrote `.gitignore`
- **Exit status:** 0
- **Upstream commit:** not cloned yet
- **Raw log:** none
- **Result:** Ignores `upstream/`, `*.pt`, `*.bin`, `*.safetensors`, `*.gguf`, `*.ckpt`, `hf_cache/`, `.cache/`, `checkpoints/`, `.venv/`, `__pycache__/`, `.env`, `*.key`, `.DS_Store`. Verified with `git status --short`, which shows `gpt1900-repro/` untracked and nothing from `upstream/`.
- **Interpretation:** Two specific failure modes closed. GitHub rejects files over 100MB, and one checkpoint is roughly 6.6GB, so a single careless `git add -A` would have required history surgery. The eval calls the Claude API as judge, so an API key will exist locally and must not be committed.
- **Next:** Clone upstream.

## E004 - 2026-08-25 01:20 PT - record-keeping set up

- **Phase:** 0
- **Goal:** Have a place where every step is written down as it happens, so the weekly report and the end-of-sprint packet are compiled from a record rather than reconstructed from memory.
- **Command:** created `notes/lab-notebook.md`, `notes/decisions.md`, `reports/week-01.md`, `logs/`, `evidence/`
- **Exit status:** 0
- **Upstream commit:** not cloned yet
- **Raw log:** none
- **Result:** Notebook is append-only with numbered entries. Decisions log holds D001 to D003, each recording a choice and why, written before the result is known. Weekly report file created with the findings section deliberately empty.
- **Interpretation:** No scientific content. This is the machinery for workstream 4, archive everything and report denominators. It does not yet capture the per-generation fields that matter, seed, temperature, top_k, HF revision, because those live inside the eval script and get handled in phase 5.
- **Next:** Clone upstream.

## E005 - 2026-08-25 01:35 PT - upstream cloned and pinned

- **Phase:** 0, workspace and provenance
- **Goal:** Get the GPT-1900 code locally and fix it to one exact version, so every later result can be attributed to a known state of the codebase.
- **Command:** `git clone https://github.com/michaelhla/gpt1900.git upstream/gpt1900` then `git log -1`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c5378f6b1bf3e1ba782f56876f65cde7a`
- **Raw log:** `logs/20260825-clone-upstream.log`
- **Result:** 2369 objects, 21.70 MiB, no submodules, no LFS pointers pulled. HEAD is `5b489c8c` on branch `master`, committed 2026-04-09 00:55:36 -0700 by Michael Hla. Recorded in `notes/provenance.md` along with the restore command.
- **Interpretation:** Phase 0 is closed. Two things worth noting. First, 21.70 MiB confirms the repository carries code and results JSON only, no model weights, so weights are a separate download from Hugging Face and a separate provenance pin. Second, the most recent commit is 9 April 2026, four and a half months before this sprint started, so upstream is not moving underneath the work. That removes one source of drift: any difference between a run here and the published results cannot be explained by upstream changing mid-sprint.
- **Next:** Read the repository structure, then the eval script, and start the tool inventory.

## E006 - 2026-08-25 01:40 PT - repository structure surveyed

- **Phase:** 1, tool inventory
- **Goal:** Identify the audit surface before running anything. Which directories hold the eval harness, the task prompts, and the published results.
- **Command:** `ls`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-ls-repo-root.log`
- **Result:** Top level holds `CHECKPOINTS.md`, `EVAL.json`, `EVAL_no_assumptions.json`, `LICENSE`, `PROJECT_LOG.md`, `README.md`, `SERVER_SETUP.md`, `pyproject.toml`, `uv.lock`, and directories `deploy`, `dev`, `figures`, `mcp`, `nanochat`, `results`, `runs`, `scripts`, `tasks`, `tests`.
- **Interpretation:** The audit surface is four things: `scripts/` for the harness, the two `EVAL*.json` files for the task prompts in scaffolded and minimal conditions, `results/` for the published outputs to diff against, and `CHECKPOINTS.md` for which checkpoints exist and how they are addressed on Hugging Face. `nanochat/` is Karpathy's training framework and is out of scope, since this sprint audits the evaluation, not the training. `PROJECT_LOG.md` is upstream's own working notes and is worth reading for admissions of known problems. `tests/` matters for what it does not cover as much as what it does.
- **Next:** List `scripts`, `results` and `tasks` to find the harness filename and count the published result sets.

## E007 - 2026-08-25 01:50 PT - eval harness, tasks and published results located

- **Phase:** 1, tool inventory
- **Goal:** Find the eval script, find where the physics questions are defined, and count the published result sets.
- **Command:** `ls scripts results tasks`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-ls-scripts-results-tasks.log`
- **Result:**
  - `scripts/physics_eval.py` confirmed present. Also present and possibly relevant: `physics_clm.py`, `generate.py`, `base_eval.py`, `chat_eval.py`, `pre1900_sft.py`, `pre1900_scripts/`, `upload_to_hf.py`, `organize_hf.py`, `dashboard.py`, and an `archive/` directory.
  - `tasks/` holds 10 files. Nine are standard nanochat benchmarks (`arc`, `common`, `customjson`, `gsm8k`, `humaneval`, `math_task`, `mmlu`, `smoltalk`, `spellingbee`). One, `yale_physics.py`, is the physics task and is the only one in scope.
  - `results/` holds 15 entries: `physics_eval`, `physics_eval_clm`, `physics_eval_gen_phys`, `physics_eval_v5`, `v6`, `v7`, `v8`, `v8_det`, `v11`, `v11_no_assumptions`, `v11_rephrase`, `v11_replication`, `general_reasoning_eval`, `power_samp_pe`, `wandb_exports`, plus `gallery_of_funny_failures.md`.
- **Interpretation:** Two things change the plan. First, `results/physics_eval_v8_det` exists. If `det` stands for deterministic, then a determinism run may already have been attempted upstream, which contradicts the working assumption in `notes/plan.md` that phase 4 is unexplored ground. This has to be checked before any effort is spent designing that experiment. Second, there are 15 result sets, not one. The published headline comes from `v11`, but `v5` through `v8` exist alongside it with no stated relationship. A reviewer would ask which runs were discarded and on what basis. That question belongs in the inventory whether or not it has an answer.
- **Next:** Inspect `results/physics_eval_v8_det` to determine what `det` means.

## E008 - 2026-08-25 02:00 PT - physics_eval_v8_det contains generations only, no scores

- **Phase:** 1, tool inventory
- **Goal:** Determine whether `results/physics_eval_v8_det` is an existing determinism run, which would change the plan for phase 4.
- **Command:** `ls results/physics_eval_v8_det`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-ls-v8-det.log`
- **Result:** The directory contains exactly one file, `generations.json`. There is no judged or scored results file.
- **Interpretation:** Whatever `det` stands for, the run was generated and never scored. This is the second result directory found with that shape. `physics_eval_v11_replication` has the same problem: generations present, no judged results. So both attempts at re-running the evaluation stop before producing a number. The original `v11` run has 192 judged scores. Neither repeat does. Stated plainly, the published mean of 0.93 out of 5 has no scored counterpart from any repeat run, so no claim about reproducibility of the score itself has ever been computed upstream. That holds whether or not `det` turns out to mean deterministic. What `det` means is still open and depends on the contents of the file.
- **Next:** Read the file size and the first records of `generations.json` to see whether sampling settings, in particular temperature, were recorded.

## E009 - 2026-08-25 02:10 PT - v8_det generations.json structure and first task

- **Phase:** 1, tool inventory
- **Goal:** Establish whether `physics_eval_v8_det` is a real run and what its records contain.
- **Command:** `ls -lh results/physics_eval_v8_det && head -c 600 results/physics_eval_v8_det/generations.json`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-head-v8-det-generations.log`
- **Result:** `generations.json` is 370K, so a real run rather than an abandoned stub. Structure is nested three levels: checkpoint name, then task name, then a record. First checkpoint key is `discovery-rl-v8-s035`. First task key is `uv_catastrophe_main`. The record begins with a `prompt` field. The prompt is a scaffolded one: it states the physical setup and then lists five observed facts about the blackbody spectrum.
- **Interpretation:** Two things follow.
  First, the checkpoint name `discovery-rl-v8-s035` indicates a reinforcement-learning tuned checkpoint at step 35, not the plain pre-trained model. Which checkpoint produced the published `v11` numbers is therefore a substantive question, since the collection contains more than one kind of model.
  Second, `uv_catastrophe` is the ultraviolet catastrophe, whose resolution is Planck's law, published October and December 1900. The corpus is named `pre1900`. Planck's solution sits exactly on the stated boundary. This turns a vague contamination worry into a checkable one with a specific date: does the corpus contain any 1900-dated material, and if so, does it include Planck. That is a concrete query to run against `mhla/pre1900-corpus` in phase 7.
- **Next:** Print the key structure of the file to determine how many checkpoints and tasks it covers, and whether sampling settings such as temperature and seed are recorded per record.

## E010 - 2026-08-25 02:25 PT - v8_det covers 12 checkpoints, records only three fields

- **Phase:** 1, tool inventory
- **Goal:** Determine the size of the `v8_det` run and whether sampling settings, in particular temperature and seed, are recorded per record.
- **Command:** `python3 -c` printing top-level keys, task counts and record field names from `results/physics_eval_v8_det/generations.json`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-v8-det-structure.log`
- **Result:** 12 checkpoints, named `discovery-rl-v8-s035` through `discovery-rl-v8-s420` in increments of 35. Each has exactly 8 tasks, for 96 prompt-answer records total. Every record has exactly three fields: `prompt`, `mode`, `completions`. There is no `temperature`, no `seed`, no model revision, no timestamp and no code version.
- **Interpretation:** The directory name asserts something with the suffix `_det`, and the file it contains has no field capable of confirming or denying it. From the artifact alone, whether this run was deterministic is unknowable. Separately, all 12 checkpoints are reinforcement-learning tuned `discovery-rl-v8` models, so this run does not touch the plain pre-trained model at all.
  The more important point is scope. These are the same three fields previously reported for `results/physics_eval_v11`, which is the published run. The logging gap is therefore not confined to an experimental directory. It is uniform across runs including the headline one, which makes it a property of the pipeline rather than an oversight in one folder. This has now been verified directly rather than carried over from earlier desk research.
- **Next:** Count the entries in `completions` for one checkpoint, and inspect the `mode` field, which is so far unexplained. If `completions` holds more than one answer per task, a same-machine repeatability comparison already exists in the data.

## E011 - 2026-08-25 02:40 PT - one completion per task, mode is completion, all eight task names visible

- **Phase:** 1, tool inventory
- **Goal:** Determine whether `v8_det` stores repeated answers to the same prompt, which would provide a same-machine repeatability comparison without running anything, and identify what the unexplained `mode` field holds.
- **Command:** `python3 -c` printing task name, `mode` and `len(completions)` for checkpoint `discovery-rl-v8-s035`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-v8-det-completions.log`
- **Result:** All 8 tasks report `completions: 1` and `mode: completion`. Task names are `uv_catastrophe_main`, `photoelectric_effect_main`, `sr_frozen_light`, `sr_approaching_c`, `sr_train_lightning`, `sr_michelson_morley`, `gr_main_elevator_light`, `gr_free_fall_equivalence`.
- **Interpretation:** Negative result on the free-comparison hypothesis from E010. Each prompt was answered once, so this file alone contains no repeated generation to compare against. `mode: completion` indicates the model was run as raw text continuation rather than in a chat or instruction-following wrapper, which is the appropriate way to prompt a base model and is worth recording because a run in a different mode would not be comparable.
  Two further observations on the task set. Six of the eight target results published in 1905 or later, comfortably outside a pre-1900 corpus. `uv_catastrophe` targets Planck's law, published October and December 1900, which sits on the stated boundary. `sr_michelson_morley` refers to an 1887 experiment, so the experimental result is inside the training corpus and only its 1905 interpretation is outside. Those two tasks are testing something different from the other six and should not be pooled with them without comment.
  Remaining possibility for a no-cost comparison: `results/physics_eval_v8` exists alongside `results/physics_eval_v8_det`. If both cover the same 12 checkpoints and the same 8 tasks, the pair constitutes a repeat run split across two directories.
- **Next:** List `results/physics_eval_v8` to see whether it contains a comparable `generations.json`.

## E012 - 2026-08-25 02:50 PT - physics_eval_v8 is graded, v8_det is not

- **Phase:** 1, tool inventory
- **Goal:** Determine whether `results/physics_eval_v8` contains a comparable generations file, which would make the `v8` and `v8_det` pair a candidate repeat run.
- **Command:** `ls results/physics_eval_v8`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-ls-v8.log`
- **Result:** `physics_eval_v8` contains three files: `generations.json`, `results_judged.json`, `summary.txt`. `physics_eval_v8_det` contains only `generations.json`.
- **Interpretation:** The asymmetry is informative. Version 8 was run, judged and summarised. The run labelled `_det` was generated and abandoned before judging. This is the same abandonment pattern already recorded for `physics_eval_v11_replication` in E008, now seen a second time, which strengthens rather than weakens that finding.
  The opportunity is that both directories contain a `generations.json`. If they cover the same 12 checkpoints and the same 8 tasks, then together they constitute a repeat of the same evaluation stored across two directories, and a same-machine comparison of generated text becomes possible without downloading any weights. That has not been established yet. The directories may cover different checkpoints, different tasks, or `_det` may denote something unrelated to determinism. Checked next.
  Also noted: `summary.txt` in `v8` should contain scores for a run other than the published `v11`, which would give a second graded run to set beside the headline mean of 0.93.
- **Next:** Compute the checkpoint overlap between `physics_eval_v8` and `physics_eval_v8_det`.

## E013 - 2026-08-25 03:00 PT - v8 and v8_det cover an identical checkpoint set

- **Phase:** 1, tool inventory, and a possible short cut into phase 4
- **Goal:** Establish whether `physics_eval_v8` and `physics_eval_v8_det` cover the same checkpoints, which would make the pair a repeat of the same evaluation stored across two directories.
- **Command:** `python3 -c` computing the set intersection of top-level keys in both `generations.json` files
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-v8-overlap.log`
- **Result:** `v8` has 12 checkpoints, `v8_det` has 12 checkpoints, and the intersection is 12. Shared names begin `discovery-rl-v8-s035`, `discovery-rl-v8-s070`, `discovery-rl-v8-s105`.
- **Interpretation:** The two directories cover an identical checkpoint set. Combined with E011, which established 8 tasks per checkpoint in `v8_det`, this gives up to 96 paired records. If the prompts also match, the pair constitutes a same-machine repeat of the same evaluation and permits a byte-level comparison of generated text without downloading any weights.
  Two cautions before drawing conclusions. First, an identical checkpoint list does not prove the runs were independent. One file could be a copy of the other, or derived from it. If the answer texts come back 100 percent identical, that possibility has to be ruled out before claiming determinism. Second, whatever this pair shows concerns level 1 or 2 reproducibility as defined in the meeting notes, same machine, and says nothing about level 3, whether the run transfers to different hardware. A local run is still required for that.
- **Next:** Compare prompts and first completions across all 96 paired records, counting identical and differing pairs.

## E014 - 2026-08-25 03:10 PT - zero of 96 paired generations reproduce between v8 and v8_det

- **Phase:** 1, with a direct bearing on phase 4
- **Goal:** Determine how many of the 96 paired records in `physics_eval_v8` and `physics_eval_v8_det` produced identical generated text, having first confirmed the prompts are identical.
- **Command:** `python3 -c` comparing `prompt` and `completions[0]` across all paired records in both files
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-v8-vs-v8det-compare.log`
- **Result:** Prompts identical in 96 of 96 pairs, 0 differing. Generated answers identical in **0 of 96** pairs, differing in 96 of 96.
- **Interpretation:** The prompt check is what makes this result usable. Both runs were given byte-identical inputs across all 96 records, so the comparison is valid and the difference cannot be attributed to differing questions. Given identical inputs to an identical checkpoint set, not one of 96 outputs reproduced.
  This is consistent with the earlier desk figure for the other pair in the repository, `physics_eval_v11` against `physics_eval_v11_replication`, reported as 2 identical out of 24. Taken together the two independent pairs give **2 identical out of 120 paired generations, 1.7 percent**. One pair could be an artefact of how a single run was configured. Two pairs behaving the same way is a property of the pipeline.
  Limits that must be stated with the number. First, neither file records temperature, top_k, seed or any sampling parameter, so it is not possible to establish from these artefacts which run used sampling, or whether both did. The result establishes that the outputs do not reproduce, not why. Second, this concerns level 1 and 2 reproducibility as defined in `reports/meeting-2026-08-26.md`, same machine. It says nothing about level 3, portability to different hardware, which still requires a local run.
  Two things this does rule out. The 96 of 96 prompt match rules out the possibility that the directories cover different task definitions. The 0 of 96 answer match rules out the possibility raised in E013 that one file is a copy of the other.
  Bearing on the published result: the headline mean of 0.93 out of 5 rests on 192 judged answers produced by this same pipeline. If generations do not reproduce and the sampling settings were never recorded, that mean is a single unreplicated draw from an unrecorded distribution. This is a measurement problem rather than a claim about the model's physics ability, and it is fixable.
  Note on naming: the directory suffix `_det` conventionally denotes deterministic. Whatever was intended, this run does not match `v8` on any of 96 records.
- **Next:** Characterise how the pairs differ. Measure the shared leading character count for each pair to distinguish sampling divergence, which would show a long shared prefix followed by a split, from a structural difference, which would show divergence from the first character.

## E015 - 2026-08-25 03:20 PT - divergence pattern is consistent with sampling, not a structural difference

- **Phase:** 1, bearing on phase 4
- **Goal:** Characterise how the 96 differing pairs differ, in order to distinguish sampling divergence from a structural difference such as a different checkpoint, different code or different settings.
- **Command:** `python3 -c` computing the shared leading character count for each of the 96 pairs, then printing the pair with the longest shared prefix along with the first 100 characters of each continuation after the split
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-v8-divergence.log`
- **Result:** Shared leading characters across the 96 pairs: shortest 1, longest 86, mean 16. Longest-agreeing pair is checkpoint `discovery-rl-v8-s070` on task `sr_train_lightning`. Both runs produced `" Is it not clear that the train observer sees the two flashes arrive at the same time "`, after which `v8` continued `"in the same space? ..."` and `v8_det` continued `"because he sees them arrive at the same speed in the two inertia frames? ..."`.
- **Interpretation:** The diagnostic signal is the variability of the split point, not its average. A structural difference between the two runs, a different checkpoint, different code path, different precision or a different tokenizer, would be expected to produce divergence at or near the first character consistently across all 96 pairs. What is observed instead is a split point ranging from 1 to 86 characters with a mean of 16. That variability is what token-level sampling produces: the model is highly confident at some positions, so both runs pick the same token, and near-tied at others, so the runs separate. The divergence pattern is therefore consistent with sampling being enabled in at least one of the two runs, and does not indicate a structural difference.
  This should be stated as a lean rather than a conclusion. Neither file records temperature, top_k or a seed, so this is inference from output characteristics rather than from recorded settings. The claim that can be defended is that the pattern of divergence is consistent with sampling rather than a structural difference. Confirming it requires reading the eval source.
  If it holds, the implication is favourable: the reproducibility failure would be a recording problem with a small fix, setting and archiving a seed, rather than a structural failure requiring the pipeline to be rebuilt.
  Separate observation, not about reproducibility. The sampled text circles rather than advancing: "Is it not clear that ... Is not this the only way in which he can see them arrive at the same time?" Rhetorical questions substituting for inference. This is a single hand-picked example and no claim is made about the corpus of outputs, but it is consistent with the published mean of 0.93 out of 5 and is worth revisiting systematically when the judged results are examined.
- **Next:** Read `scripts/physics_eval.py` for `manual_seed`, and for the declared defaults of `temperature`, `top_k` and `top_p`, and establish whether any of them are written into the results file.

## E016 - 2026-08-25 03:30 PT - no seed exists in the eval source; sampling defaults confirmed; two further findings

- **Phase:** 1, tool inventory
- **Goal:** Confirm at the source whether `scripts/physics_eval.py` sets a random seed, and establish the declared defaults for the sampling parameters.
- **Command:** `grep -n "temperature\|top_k\|top_p\|seed\|manual_seed\|add_argument" scripts/physics_eval.py`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-grep-sampling-params.log`
- **Result:** Zero matches for `seed` or `manual_seed`. Neither string occurs anywhere in the file. `temperature` appears with default `0.7` at lines 220, 347 and in the argument parser at line 532. `top_k` appears with default `50` at lines 221, 348 and line 533. No `top_p` anywhere. The argument parser at lines 525 to 534 declares ten arguments including `--skip-judge` ("Skip the Claude judge phase"), `--num-samples` (default 3, "Number of samples per task"), `--max-tokens` (default 1024) and `--num-gpus` (default 1).
- **Interpretation:** Four findings.
  **First, and principal.** The eval source contains no seed. This is now confirmed at the source rather than inferred from output artefacts, and it establishes the mechanism behind E014: with sampling enabled at temperature 0.7 and no seed set, generations cannot be regenerated by anyone, including the authors. The 0 of 96 non-reproduction is the expected consequence of the code as written, not an anomaly.
  **Second.** Defaults of temperature 0.7 and top_k 50 confirm the sampling configuration independently of the divergence analysis in E015. Two separate lines of evidence, one from output characteristics and one from source, agree.
  **Third.** The `--skip-judge` flag explains the ungraded runs recorded in E008 and E012. `v8_det` and `v11_replication` lack judged files because the judging phase was deliberately skipped, not because a run crashed or was forgotten. This revises the earlier framing in E008 and E012, which used the word "abandoned". That word implies an accident and was not supported by evidence; the correct statement is that the repeat runs were generated with judging deliberately disabled.
  The most plausible explanation is cost. The judging phase sends every generation to a paid API, and disabling it on an exploratory run that is not intended for publication is ordinary practice. That explanation should be offered before any other. What the artefacts cannot supply is intent, so the question belongs to the authors. The finding itself is unchanged either way: no repeat run has been scored, therefore no reproducibility figure for the score exists.
  **Fourth.** `--num-samples` defaults to 3, yet every record examined in E011 contains exactly one completion. So the runs were executed with a non-default value, or samples were dropped downstream. Because no invocation parameters are archived with the results, which of these occurred cannot be determined from the artefacts. This is materially unfortunate: three samples per prompt is precisely the data needed to estimate output variance, the pipeline is built to collect it by default, and the archived runs do not contain it.
- **Next:** Locate the write path in `scripts/physics_eval.py` to establish which fields are serialised into `generations.json` and confirm from the source that the sampling parameters are in scope at that point and omitted.

## E017 - 2026-08-25 03:45 PT - the write path is line 609, with sampling parameters in scope and omitted

- **Phase:** 1, and this identifies the intervention point for phase 5
- **Goal:** Locate the serialisation points in `scripts/physics_eval.py` and establish from the source, rather than from the artefacts, that the sampling parameters are available at the point of writing and are not recorded.
- **Command:** `grep -n "json.dump\|generations.json\|results_judged\|summary.txt\|def save" scripts/physics_eval.py`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-grep-write-paths.log`
- **Result:** Three write points. Line 573 constructs the path for `generations.json` and line 609 writes it with `json.dump(all_generations, f, indent=2)`. Line 634 constructs the path for `results_judged.json` and line 636 writes it. Line 646 constructs the path for `summary.txt`. Line 396 is unrelated: it serialises the judge output schema into the judge prompt.
- **Interpretation:** From E016, `args.temperature` and `args.top_k` are referenced at lines 595 to 596 and 603 to 604. The generations file is written at line 609. The sampling parameters are therefore in scope in the same function, within fifteen lines of the write, and are not included in the serialised payload. This upgrades the claim from an observation about output files to a statement about a specific line: the omission is not a structural limitation of the pipeline, it is a field selection at line 609.
  This also explains the file-level asymmetry recorded in E008 and E012. Lines 634 to 646 execute only when the judging phase runs, so a run invoked with `--skip-judge` produces `generations.json` alone. `v8_det` and `v11_replication` match that signature exactly.
  The causal chain is now complete and traceable end to end: no seed in the source (E016), sampling enabled by default at temperature 0.7 (E016), sampling parameters omitted at the write in line 609 (this entry), judging optionally skipped (E016), and the measured consequence of 0 identical generations in 96 paired records with nothing in the artefacts able to explain why (E014).
  Phase 5 intervention point identified: the fix is an expansion of the record written at line 609, not a redesign of the pipeline.
- **Next:** Read lines 590 to 615 directly to confirm the structure of `all_generations` and enumerate every parameter in scope at the write that is currently discarded.

## E018 - 2026-08-25 03:55 PT - write path read directly; four parameters discarded; checkpoints are deleted after use

- **Phase:** 1, defining the phase 5 fix and revising a phase 2 constraint
- **Goal:** Read the generation write path directly and enumerate every parameter in scope at the point of serialisation that is not recorded.
- **Command:** `sed -n '590,615p' scripts/physics_eval.py`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-sed-590-615.log`
- **Result:** The generation call passes `num_samples`, `max_tokens`, `temperature` and `top_k` from `args`, in both the single-device and multi-GPU branches. Results are assigned with `all_generations[ckpt.name] = ckpt_results` and written three lines later with `json.dump(all_generations, f, indent=2)`. The file is rewritten after every checkpoint, commented "Save after each checkpoint for crash resilience". Immediately after the write, the checkpoint's cache directory is deleted with `shutil.rmtree(ckpt_cache)`, guarded against symlinks and local paths, under the comment "Free disk space by removing downloaded checkpoint".
- **Interpretation:** Three points.
  **The discard set is now enumerated from source.** Four sampling and generation parameters are in scope within three lines of the write and none is serialised: `temperature`, `top_k`, `num_samples`, `max_tokens`. `device` and `num_gpus` are also in scope in the surrounding block and are likewise discarded; these are the hardware fields required for any statement about portability. Separately, the record is keyed on `ckpt.name` alone. A Hugging Face model name is mutable, so a name without a revision does not identify which weights produced a generation. The phase 5 record therefore needs: temperature, top_k, num_samples, max_tokens, checkpoint name **and revision**, device, GPU count, and a seed, which does not currently exist and must be introduced.
  **A phase 2 constraint is materially relaxed.** The script deletes each checkpoint's cache immediately after evaluating it, so peak disk usage is one checkpoint rather than the full collection. The concern recorded in `notes/plan.md` and in the meeting notes, that 24 checkpoints at roughly 6.6GB cannot fit in 31GB of free space, does not apply to a sequential sweep as implemented. Disk is not the binding constraint. Generation speed on CPU or Apple Silicon, still untested, is.
  **Credit where due.** Saving after each checkpoint rather than at the end of the sweep is deliberate crash resilience, and deleting caches as it goes is deliberate resource management. Both are careful choices and should be stated as such. The reproducibility gap identified here is a field selection at the write, not general carelessness, and the audit should say so.
- **Next:** Establish how checkpoints are addressed on Hugging Face, in particular whether a `revision` is pinned or whether the script accepts whatever weights currently sit behind a mutable name.

## E019 - 2026-08-25 04:05 PT - checkpoint registry read; two open questions raised, one search invalidated by truncation

- **Phase:** 1, tool inventory
- **Goal:** Establish which Hugging Face repositories the weights come from and whether a revision is pinned at download.
- **Command:** `grep -n "hf_hub\|snapshot_download\|revision\|repo_id\|huggingface\|mhla" scripts/physics_eval.py | head -30`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-grep-hf-checkpoints.log`
- **Result:** Line 25 imports `snapshot_download` from `huggingface_hub`. Lines 46 onward declare a checkpoint registry of four-field records: short name, Hugging Face repository id, step number, and mode. Lines 46 to 50 declare `completion` mode; lines 51 to 56 and 97 to 114 declare `chat`. Lines 97 to 114 show eighteen distinct checkpoints all referencing the single repository `mhla/gpt1900-d34-contradiction-rl-v11`, differing only in step number.
- **Interpretation:** Three points, two of which are open questions rather than findings.
  **The search was truncated and cannot support a conclusion.** The `| head -30` limit was consumed entirely by the checkpoint registry, so the absence of `revision` in this output is not evidence of its absence in the file. No finding is recorded on version pinning until the search is re-run without truncation. Noting this explicitly because the conclusion would have been convenient and was not earned.
  **Disk cost per checkpoint is not yet established.** Multiple checkpoints share one repository and are distinguished only by step number, so a checkpoint is a save point within a repository rather than a separate repository. Whether `snapshot_download` is called with a filter restricting the transfer to one step's files, or fetches the entire repository, determines the actual per-checkpoint disk cost. The 6.6GB figure used so far assumes the former. Until this is checked, the disk conclusion in E018 holds only for the deletion behaviour, not for peak size during a single checkpoint's evaluation.
  **A possible mode mismatch.** The registry declares a mode per checkpoint, `completion` or `chat`, and every `discovery-rl-v11` entry is declared `chat`. E011 recorded `mode: completion` in the saved records of `results/physics_eval_v8_det` for checkpoints named `discovery-rl-v8-*`. If the v8 registry entries are also declared `chat`, then that run generated in a mode other than the one declared for those checkpoints, meaning the model was prompted in a format it was not tuned for. That would be a more serious defect than the missing seed and would bear directly on the low mean score. The v8 declarations have not yet been read and no claim is made until they are.
- **Next:** Re-run the `revision` search without truncation, read the `discovery-rl-v8` registry entries, and read the `snapshot_download` call site.

## E020 - 2026-08-25 04:20 PT - no revision pinning; mode-mismatch hypothesis disproved; 54 of 89 checkpoints unreleased; per-checkpoint download confirmed

- **Phase:** 1, tool inventory. Resolves the three questions left open in E019.
- **Goal:** Determine (a) whether a Hugging Face revision is pinned at download, (b) whether the `discovery-rl-v8` checkpoints are declared in a mode inconsistent with their saved records, (c) whether `snapshot_download` fetches one step or an entire repository.
- **Command:** `grep -n "revision"` without truncation; `grep -n "discovery-rl-v8"`; `grep -n -A8 "snapshot_download("`; plus a regex census of all `Checkpoint(...)` registry entries
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-three-open-questions.log`
- **Result:**
  (a) `revision` does not occur anywhere in `scripts/physics_eval.py`. Zero matches, search not truncated.
  (b) Lines 85 to 96 declare the twelve `discovery-rl-v8` checkpoints with repo `"local"` and mode `"completion"`.
  (c) Line 180 calls `snapshot_download` with `allow_patterns=[f"model_{step_str}.pt", f"meta_{step_str}.json", "tokenizer/*"]`. A second call at line 195 fetches the tokenizer alone.
  Registry census: 89 `Checkpoint` entries total. 54 have repo `"local"`, 35 are hosted. Modes: 55 `completion`, 34 `chat`. Local families are `discovery-rl-v5`, `v6`, `v7`, `v8`, `gen-physics-rl`, `physics-clm`. Twelve distinct Hugging Face repositories are referenced, of which `mhla/gpt1900-d34-contradiction-rl-v11` accounts for 24 entries and the remaining eleven have one each.
- **Interpretation:**
  **(a) A second reproducibility gap, confirmed at source and independent of the seed.** `snapshot_download` is called without a `revision` argument, so it resolves to whatever the repository's default branch points at when the command runs. Hugging Face repository names are mutable. Consequently, even with a seed set and every sampling parameter archived, two runs separated in time could silently use different weights and nothing in the code or the output would indicate it. This gap sits upstream of the sampling gap: the seed governs which sample is drawn, the revision governs which model draws it.
  **(b) The mode-mismatch hypothesis raised in E019 is disproved and is withdrawn.** The v8 checkpoints are declared `completion` and their saved records report `completion`. Declaration and execution agree. No defect. Recording this explicitly because the hypothesis was speculative when raised and would have been a serious allegation had it been carried into the meeting unchecked.
  **(c) The disk conclusion in E018 is confirmed and strengthened.** `allow_patterns` restricts the transfer to a single step's weight file, its metadata and the tokenizer, rather than the full repository. Combined with the post-evaluation cache deletion, peak disk usage is one checkpoint. 31GB is sufficient for a sequential sweep.
  **New finding, and it constrains the headline result.** 54 of 89 registry entries, 61 percent, reference repo `"local"`, meaning weights that exist only on the author's machine and were never published. Every `discovery-rl-v8` checkpoint is among them. The 0-of-96 non-reproduction recorded in E014 was therefore measured between two runs over unreleased weights. That result remains valid as evidence about the authors' own saved artefacts, but it is not independently re-derivable by anyone, including this project. It must be reported as a property of their files rather than as a reproduction attempt, and the distinction should be stated before a reviewer raises it.
  **Corresponding good news, and it sets the target for phase 3.** Of the 35 hosted entries, 24 belong to `mhla/gpt1900-d34-contradiction-rl-v11`. Twenty-four checkpoints across eight tasks is 192, exactly the number of judged scores in the published `physics_eval_v11` run. The published result therefore rests on downloadable weights, and the `v11` against `v11_replication` pair uses those same weights. That pair is independently re-derivable and is the correct target for local reproduction, in place of v8.
- **Next:** Verify the `v11` against `v11_replication` comparison directly, using the same paired method as E014, since that figure is currently carried from desk research rather than measured here. It requires no download.

## E021 - 2026-08-25 04:35 PT - v11 against v11_replication verified locally: 2 of 24

- **Phase:** 1, verifying a figure previously carried from desk research
- **Goal:** Measure the `physics_eval_v11` against `physics_eval_v11_replication` comparison directly rather than relying on the figure recorded in the project brief.
- **Command:** `python3 -c` comparing prompts and completions across shared checkpoints in both files
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-v11-compare.log`
- **Result:** `v11` covers 24 checkpoints, `v11_replication` covers 3: `discovery-rl-v11-s560`, `-s630`, `-s735`. 24 paired records. Prompts identical in 24 of 24. Answers identical in 2 of 24, differing in 22. Among the differing pairs, shared leading characters ranged from 80 to 1647 with a mean of 904. `v11_replication` also contains a `comparison.txt` of 53,156 bytes, written upstream.
- **Interpretation:** The figure of 2 of 24 is confirmed by direct measurement and no longer rests on desk research. Combined with E014, the measured total is 2 identical out of 120 paired generations, 1.7 percent, across two independent pairs.
  The replication covers 3 of 24 checkpoints, 12.5 percent, so it was never a full repeat of the published run.
  The mean shared prefix of 904 characters is far higher than the 16 measured for the v8 pair in E015. That gap initially suggested different sampling settings between the two pairs. E023 supplies a better explanation and this reading is superseded there.
- **Next:** Read upstream's own `comparison.txt`.

## E022 - 2026-08-25 04:45 PT - sample counts differ between each run and its repeat; headline re-checked and unchanged

- **Phase:** 1, correcting E016
- **Goal:** Establish how many completions each run stores per task, after `comparison.txt` was found to display three replication samples per task, and re-test the E014 headline allowing a match against any sample.
- **Command:** `python3 -c` counting `len(completions)` per task in all four files, and re-running the paired comparison against every sample rather than the first
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-sample-counts.log`
- **Result:** `physics_eval_v11` stores 1 completion per task. `physics_eval_v11_replication` stores 3. `physics_eval_v8` stores 3 per task, 288 outputs across 96 records. `physics_eval_v8_det` stores 1. Re-testing E014 allowing the `v8_det` answer to match any of the three `v8` samples: 0 of 96, unchanged from the first-sample comparison. Re-testing E021 the same way: 2 of 24, unchanged, and both matches occurred at sample index 0.
- **Interpretation:** **Correction to E016.** That entry stated that every record examined contained one completion and inferred that runs had been executed with a non-default `--num-samples`. That inference was drawn from `v8_det` alone and generalised without warrant. Two of the four files store three completions per task. The corrected statement is that sample count varies between files: `v11` and `v8_det` store one, `v11_replication` and `v8` store three.
  **This produces a finding rather than merely a correction.** In both pairs, the run and its repeat used different sample counts. `v11` used one and its replication used three; `v8` used three and `v8_det` used one. A replication should hold configuration fixed apart from the variable under test, so neither pair is strictly like-for-like. Because no invocation parameters are archived, this is detectable only by counting entries in the output files.
  **The headline is unaffected and was tested against the more generous reading.** Allowing a match against any of three samples rather than only the first leaves both figures unchanged, at 0 of 96 and 2 of 24. The comparison was re-run in the direction that could have weakened the finding, and it did not.
- **Next:** Characterise the generated text itself, given that `comparison.txt` shows a repeated opening formula across outputs.

## E023 - 2026-08-25 04:55 PT - 78 percent of published v11 outputs share a stereotyped opening; supersedes the E021 prefix reading

- **Phase:** 1, output characterisation
- **Goal:** Determine whether the high mean shared prefix measured in E021 reflects near-deterministic generation or a formulaic opening.
- **Command:** `python3 -c` tabulating leading 40-character strings across all v11 and v8 completions and counting outputs beginning "You have touched"
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-opening-formula.log`
- **Result:** Across the full published `physics_eval_v11` run, 150 of 192 outputs, 78 percent, begin with "You have touched". Restricted to the three checkpoints that were replicated, 95 of 96 outputs across both runs, 98 percent. In `physics_eval_v8`, 0 of 288 outputs begin with that phrase. The five most frequent 40-character openings across the v11 comparison set are all variants of "You have touched a matter/point/question of considerable...".
- **Interpretation:** **This supersedes the reading offered in E021.** The mean shared prefix of 904 characters between `v11` and its replication does not indicate near-deterministic generation. It reflects a stereotyped opening formula: the two runs agree on boilerplate before diverging on content. Prefix-agreement therefore overstates similarity for this run and should not be used as a proxy for reproducibility. The contrast with `v8`, where the phrase never occurs, is consistent with the mode difference recorded in E019 and E020, `chat` for v11 against `completion` for v8, and with the persona induced by supervised fine-tuning.
  **Second implication, which is a question rather than a finding.** The judge is a language model scoring free text. If 78 percent of scored outputs open in the same confident period register, it is legitimate to ask whether the score partly tracks stylistic fluency rather than physical reasoning. Nothing here establishes that it does. What can be said is that the question is open, that no human calibration or second rater exists to answer it, and that it is empirically checkable. It belongs in the design of the blinded physicist review.
  **Methodological note.** The formula was found by reading the outputs rather than by computing over them. E021's aggregate statistic was misleading on its own and the error would not have surfaced without inspecting the text.
- **Next:** Environment install and first local generation, phase 2, targeting a v11 checkpoint since those weights are published.

## E024 - 2026-08-25 06:10 PT - published mean verified at 0.932; 86 percent of scores are 0 or 1; four of eight tasks are effectively binary

- **Phase:** 1, extended to the judged results
- **Goal:** Establish whether physics performance was measured at all, given that judging was skipped on the repeat runs, and characterise the distribution behind the published mean.
- **Command:** `head -30 results/physics_eval_v11/summary.txt`, a `python3` parse of the score table, and an inventory of which result directories contain `results_judged.json`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-v11-score-distribution.log`
- **Result:** Seven result directories contain judged results: `physics_eval`, `physics_eval_clm`, `v5`, `v6`, `v8`, `v11`, `v11_no_assumptions`. Five contain generations without judged results: `gen_phys`, `v7`, `v8_det`, `v11_rephrase`, `v11_replication`.
  The `v11` summary holds 24 checkpoints across 8 tasks, 192 scores. Recomputed mean: **0.932**, matching the previously carried figure of 0.93.
  Distribution across the 0 to 5 rubric: 0 appears 44 times (22.9%), 1 appears 122 times (63.5%), 2 appears 22 times (11.5%), 3 appears 3 times (1.6%), 4 appears once (0.5%), 5 never. **86.4 percent of all scores are 0 or 1.**
  Range per task: `sr_frozen_light`, `sr_approaching_c`, `sr_train_lightning` and `gr_free_fall_equivalence` take only the values 0 and 1. `sr_michelson_morley` takes only 1 and 2, never 0. `uv_catastrophe` takes 0 to 2, `gr_main_elevator_light` 0 to 3, `photoelectric_effect_main` 0 to 4.
  Mean across the first 8 checkpoints: 0.62. Across the last 8: 1.11.
- **Interpretation:** Four points.
  **Physics performance was measured, once.** The judging skip established in E016 applies to repeat runs only. The distinction that matters is therefore not that performance went unmeasured, but that it was measured a single time with no second measurement against which to assess stability. The published mean is now verified locally rather than carried from earlier notes.
  **The instrument has little resolution over this model.** With 86.4 percent of scores on two adjacent values and the top of the scale never used, the rubric is operating in a narrow band. Four of the eight tasks are binary in practice. This does not imply the scoring is incorrect: if the model's answers are uniformly poor, uniformly low scores are the right measurement. What it does mean is that any comparison between checkpoints rests on the small subset of task-checkpoint cells that actually vary, and that a difference of a tenth of a point in an aggregate mean is not obviously meaningful. Uncertainty quantification, absent here, would settle that and cannot currently be computed because each cell is a single draw.
  **There is genuine signal, and it favours the work.** Mean rises from 0.62 over the first eight checkpoints to 1.11 over the last eight, close to a doubling across RL training. Whatever else is true of the measurement, it detects real improvement. This should be reported as prominently as the negative findings.
  **One observation held as a hypothesis, not a finding.** `sr_michelson_morley` is the only task that never scores 0, with a floor of 1 across all 24 checkpoints. It is also the only task whose underlying experiment, dated 1887, sits inside the pre-1900 training corpus. That is the pattern familiarity with source material would produce, but there are ordinary explanations, most plausibly that the rubric awards a point for describing an experimental setup the model has read about. n is 24, one task, one run. It is testable against `v5` through `v8` and against the no-assumptions condition, and it should not be presented as more than something noticed.
- **Next:** Compare judged means between `physics_eval_v11` and `physics_eval_v11_no_assumptions`. Both are graded, so a scaffolded-versus-minimal prompt-sensitivity comparison is available immediately with no download.

## E025 - 2026-08-25 06:30 PT - prompt condition shifts individual task scores by up to 1.33 points, with a sample-count confound

- **Phase:** 1, extending into phase 6 territory
- **Goal:** Test prompt sensitivity using the two judged conditions already present in the repository, `physics_eval_v11` (scaffolded, `EVAL.json`) and `physics_eval_v11_no_assumptions` (minimal), without downloading weights.
- **Command:** `head -6` on the no-assumptions summary, then a `python3` parse comparing per-task means across shared checkpoints
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Raw log:** `logs/20260825-prompt-condition-compare.log`
- **Result:** The minimal condition covers 3 checkpoints, `s560`, `s630`, `s735`, against 24 in the scaffolded condition. Restricted to the 3 shared checkpoints, 24 scores per condition: scaffolded mean 1.250, minimal mean 1.371, difference +0.121.
  Per task, scaffolded to minimal: `sr_michelson_morley` 1.00 to 2.10 (+1.10), `gr_free_fall_equivalence` 1.00 to 1.67 (+0.67), `sr_approaching_c` 0.33 to 0.80 (+0.47), `uv_catastrophe` 1.33 to 1.77 (+0.43), `sr_train_lightning` 0.67 to 1.10 (+0.43), `sr_frozen_light` 1.00 to 1.10 (+0.10), `gr_main_elevator_light` 2.33 to 1.43 (-0.90), `photoelectric_effect_main` 2.33 to 1.00 (-1.33).
  Scores in the minimal condition are fractional in thirds; scores in the scaffolded condition are integers.
- **Interpretation:** **A confound is present and constrains what can be claimed.** The fractional scores in the minimal condition indicate three samples averaged per cell, against one in the scaffolded condition. The two conditions therefore differ in sample count as well as in prompt, which is the same defect recorded in E022 for the reproduction pairs. Averaging should not bias a mean systematically, but it substantially reduces variance on one side of the comparison and not the other, so the aggregate difference of +0.121 should not be treated as an effect estimate. Coverage is also 3 of 24 checkpoints, 12.5 percent.
  **The per-task movement is nonetheless large relative to the measured signal.** The benchmark's overall mean is approximately 1.3 on a 0 to 5 rubric. Individual task means shift by up to 1.33 points between conditions, and in both directions: `michelson_morley` and `free_fall` rise substantially under the minimal prompt while `photoelectric` and `elevator` fall substantially. The magnitude of prompt-induced movement is comparable to the entire magnitude of the score being reported.
  **The bidirectionality is itself informative.** A scaffolded prompt supplying part of the answer would be expected to raise scores uniformly. It does not. Some tasks score better with less scaffolding. That is not consistent with a simple leakage story and suggests the scaffolded prompts help on some tasks and constrain the model on others, which is a more interesting result than uniform leakage and warrants a proper experiment.
  **Bearing on the draft.** This is direct evidence for the prompt-leakage threat in section 13.2, and it is currently the only quantitative handle on it. It is not yet strong enough to publish: it needs matched sample counts, full checkpoint coverage, and a third, deliberately leading condition, which does not exist upstream and must be written.
  Also noted: `sr_michelson_morley` shows the largest positive shift and is the task flagged in E024 as never scoring 0 and as the only task whose underlying experiment sits inside the training corpus. Two independent oddities on the same task. Neither is a finding alone. Together they justify making that task a specific target of the contamination work in phase 7.
- **Next:** Phase 2, environment install and first local generation. The prompt-sensitivity experiment is redesigned as a phase 6 task with matched sample counts and full coverage.

## E026 - 2026-09-01 - the seed is not missing, it is fixed at 42 and shared across the batch; num_samples changes the draw sequence

- **Phase:** 2, source reading ahead of first generation
- **Goal:** Before writing the logging wrapper, establish exactly where sampling randomness enters, so the wrapper sets the right thing rather than adding a seed that is already there.
- **Command:** `grep -n "temperature\|top_k\|multinomial\|argmax\|def generate" nanochat/engine.py`, then reading `nanochat/engine.py` lines 136 to 279
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Result:** `Engine.generate` is declared at line 171 as
  `def generate(self, tokens, num_samples=1, max_tokens=None, temperature=1.0, top_k=None, seed=42)`.
  Lines 182 to 183 build a dedicated generator, `rng = torch.Generator(device=device)` then `rng.manual_seed(seed)`, and line 234 draws with it: `next_ids = sample_next_token(logits, rng, temperature, top_k)`. Inside `sample_next_token`, line 146, the draw is `torch.multinomial(probs, num_samples=1, generator=rng)`.
  `generate_batch` at line 263 forwards `**kwargs` into `generate`. `scripts/physics_eval.py` calls `generate_batch` at line 245 and does not pass `seed`, so every upstream run has used `seed=42`.
  Line 206: after a batch-1 prefill the logits are expanded to `num_samples` rows, and one shared `rng` then serves every row of the batch for the whole decode loop.
  Line 139 to 140: `if temperature == 0.0: return torch.argmax(...)`, which bypasses `rng` entirely.
- **Interpretation:** Three points, and the first revises a claim carried since E011.
  **The seed was never absent.** The earlier statement, that `physics_eval.py` contains zero occurrences of `seed`, is literally true and remains so. The inference drawn from it, that generation was unseeded, is wrong. The seed is one layer down in the engine, it defaults to 42, and upstream never overrides it. So every published run was nominally seeded, identically. The logging gap stands unchanged: 42 was never written down, and a reader of the archive could not have known it.
  **That makes the reproduction failure worse, not better, and points somewhere specific.** A fixed seed with 118 of 120 paired generations differing means the divergence is not sampling randomness. It is structural. The strongest candidate is now visible in the code: one `rng` is shared across all rows of the batch, so the sequence of random numbers reaching row 0 depends on how many rows sit beside it. Sample 0 of a three-sample run and sample 0 of a one-sample run consume different draws from the same seed and cannot match. E022 established that both upstream run pairs used mismatched `--num-samples`. Those two facts together are sufficient on their own to explain the 0 of 96, with no appeal to hardware or library nondeterminism.
  **This is a mechanism, not yet a measurement.** It is read from source and has not been run. It predicts something falsifiable and cheap: at matched `num_samples` and `temperature 0.0`, which takes the `argmax` path and touches no generator at all, two runs on one machine should be byte-identical. If they are, the cause is confirmed as batch coupling plus an unrecorded seed, and the fix is small. If they are not, something below the sampler is nondeterministic and no seed will fix it. That is the phase 2 determinism test and it is now a sharper experiment than when it was written.
- **Next:** `tools/logged_eval.py` written against this. Install, then run the test.

## E027 - 2026-09-01 - generation wrapper written, 43 fields, one sample per engine call

- **Phase:** 2
- **Goal:** Implement `notes/logging-schema.md` as a runnable generation pass that leaves upstream untouched, per D003.
- **Command:** `python3 -m py_compile tools/logged_eval.py`, and a parse of `EVAL.json` to confirm the task field names used
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Result:** `tools/logged_eval.py` created. Imports `CHECKPOINTS`, `build_model_only`, `download_tokenizer` and `make_prompt_text` from upstream and calls `Engine` directly. Writes JSONL, append-only, flushed and fsynced per line. Compiles clean. `EVAL.json` confirmed to hold 8 tasks keyed `id` and `prompt_lines`, matching the field names used.
  Departures from upstream, each deliberate: `seed` passed explicitly and recorded per generation; `revision` resolved through `HfApi().repo_info().sha` and passed to `snapshot_download`; one sample per engine call rather than a batch, per D004; `temperature` defaults to 0.0 rather than 0.7; failures written as records with an `error` field and a null `completion`.
  Retained from upstream unchanged: the `allow_patterns` filter that pulls one step's weights, and deletion of each checkpoint cache after use. Both are what keep peak disk at one checkpoint.
  Judge fields are written as null. Judging is a separate pass and is not in this script.
- **Interpretation:** Not yet evidence of anything. Nothing has been run against a model. The script's own claims, that it captures 43 fields and that one-sample-per-call removes the batch coupling identified in E026, are untested until the determinism test executes.
- **Next:** `uv sync --extra cpu`, then one v11 checkpoint at temperature 0.0, twice, byte compare.

## E028 - 2026-09-03 - local environment verified, laptop disk exhausted, work moves to Expanse

- **Phase:** 2
- **Goal:** Establish whether anything can actually run on this machine before committing the determinism test to a cluster.
- **Command:** `.venv/bin/python tools/logged_eval.py --help`, `.venv/bin/python -m pip list`, `df -h /System/Volumes/Data`, `diskutil info /`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Result:** Three findings, two of which contradict what `notes/where-we-are.md` and `reports/progress-week-2.md` currently say.
  **The environment exists and works.** `.venv` holds Python 3.12.2 and 33 packages including torch 2.14.0. `logged_eval.py --help` returns cleanly, which means the import chain succeeded: `torch`, `huggingface_hub`, `nanochat.engine`, and `CHECKPOINTS`, `build_model_only`, `download_tokenizer`, `make_prompt_text` from `scripts.physics_eval`. The claim "nothing installed" is false as of today. It is not the upstream `uv sync` environment, it is a hand-built minimal one, sufficient for generation and not for judging: no `anthropic`, no `transformers`, no `datasets`.
  **Free disk is 3.3 GB.** `notes/where-we-are.md` records 31 GB at sprint start. One bf16 checkpoint is roughly 6.6 GB. The pull-use-delete strategy from E018 and E020 assumed headroom that no longer exists, so the determinism test cannot run on this laptop at all, at any checkpoint count.
  **The Expanse account is live.** An `rsync` to `asingh59@login.expanse.sdsc.edu:/expanse/lustre/projects/sdp197/asingh59/gpt1900` authenticated and transferred. `reports/progress-week-2.md` says the account is not active. That is now out of date.
- **Interpretation:** The blocker was never installation. It is storage, and it appeared between 26 Aug and today without being noticed, which is itself an argument for recording the environment on every run rather than at sprint start. Expanse stops being an optimisation and becomes the only route to the phase 2 experiment.
  Three unknowns now sit on the critical path and none can be answered from this machine: the Slurm account string, the module names, and whether the GPUs support bfloat16. Expanse GPU nodes are V100, a generation with no hardware bfloat16, while `environment_fields()` in `logged_eval.py` records `"bfloat16" if device.type == "cuda"`, inheriting upstream's assumption that any GPU is Ampere or later. If that goes unfixed the archive records a dtype that was never used, which is the exact failure class this sprint exists to expose, this time in my own tool.
  The Mac-versus-Expanse dtype comparison promised in week 2 is now conditional on freeing roughly 15 GB. If that does not happen it is dropped, and dropping it is a decision that belongs in `notes/decisions.md` rather than something that quietly stops being mentioned.
- **Next:** SSH shortcuts, then log in and read the three unknowns off the machine.

## E029 - 2026-09-03 - Expanse surveyed, V100 confirmed, GPU allocation not visible

- **Phase:** 2, environment
- **Goal:** Read the three unknowns blocking the job script off the machine rather than guessing them: Slurm account, module names, and whether the GPUs support bfloat16.
- **Command:** over a multiplexed SSH session, `whoami`, `groups`, `ls -la /expanse/lustre/projects/sdp197/`, `sacctmgr -nP show assoc user=$USER`, `expanse-client user -p`, `sinfo -s`, `module list`, `module avail`, `module load gpu/0.17.3b && module avail`, `scontrol show node exp-1-57`, `ls /cm/shared/apps/containers/singularity/pytorch/`
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Result:**
  **Layout.** Login node `login02`, user `asingh59`, group `sdp197`. `/expanse/lustre/projects/sdp197/` contains `asingh59/` and `bkeating/`. `asingh59/gpt1900/` holds one file, `requirments.txt`, 487 bytes, from 2 Sep. Scratch exists at `/expanse/lustre/scratch/asingh59/temp_project`. `~/.bash_profile` sources `~/.bashrc`.
  **Slurm.** Account `sdp197`. QOS list includes `gpu-shared-normal`, `gpu-debug-normal`, `gpu-normal`, `gpu-preempt-normal`. Partitions: `gpu-shared` and `gpu` at 2 day walltime, `gpu-debug` at 30 minutes.
  **Allocation.** `expanse-client user -p` returns exactly one resource row, `expanse`, project `sdp197`, TG project `TG-CIS261668`, 0 used, 4000 available. No GPU resource row appears.
  **Hardware.** `scontrol show node exp-1-57` reports `Gres=gpu:v100:4`, 40 cores, 385500 MB RAM, partitions `gpu,gpu-preempt,gpu-shared`.
  **Software.** Default tree is `cpu/0.17.3b`; `module load gpu/0.17.3b` switches to the GPU tree. Available in both: `anaconda3/2021.05`, `git/2.31.1`. CUDA toolkits 10.2, 11.7 and 12.2 only. System Python on the login node is 3.6.8, below upstream's `requires-python >=3.10`. A maintained container exists at `/cm/shared/apps/containers/singularity/pytorch/pytorch-latest.sif`, resolving to PyTorch 2.2.1, CUDA 12.1.1, Ubuntu 22.04.
- **Interpretation:** Two of the three unknowns are answered and the third is now confirmed rather than predicted.
  **The bfloat16 problem is real, not hypothetical.** The GPUs are V100, Volta, which has no hardware bfloat16. `environment_fields()` in `tools/logged_eval.py` writes `"dtype": "bfloat16" if device.type == "cuda"`, inherited from upstream's assumption that any GPU is Ampere or later. Run unmodified here, the archive would record a dtype that the hardware cannot produce. This must be read off the loaded model, not inferred from the device, before any run. It is the same class of defect as the one this sprint exists to document, and it is mine.
  **Torch version becomes a recorded variable, not a constant.** Upstream pins `torch==2.9.1`, the local venv holds 2.14.0, and the SDSC container ships 2.2.1. Three environments, three versions. `logged_eval.py` already records `torch_version` and `platform`, so this is captured rather than lost, but it means a Mac-versus-Expanse comparison is not a clean single-variable test and should not be reported as one.
  **The GPU allocation is not confirmed.** Slurm grants the GPU QOS, so permission exists at the scheduler level, but no GPU resource row appears in `expanse-client`. Those two facts can coexist if the GPU award has not been attached to the account. A GPU job submitted against an account with no GPU balance fails at submit rather than at run, so this is cheap to discover and worth settling before queueing anything.
  Nothing was modified on Expanse. This entry is a survey only.
- **Next:** confirm the GPU balance, then clone upstream at `5b489c8c` on Expanse and rsync `tools/` up.

## E030 - 2026-09-03 - correction: the GPU allocation exists, expanse-client was the wrong instrument

- **Phase:** 2, environment
- **Goal:** Cross-check the E029 claim that no GPU allocation was attached, before acting on it.
- **Command:** `expanse-client user --help`, then `module load accessusage && accessusage`
- **Exit status:** 0
- **Result:** `accessusage` reports four allocations under CIS261668, PI Keating, all valid 2026-08-27 to 2027-08-26 and all at zero usage:

  | Resource | Total | Remaining |
  |---|---|---|
  | `credits.allocations.access-ci.org` | 141,653 | 141,653 |
  | `expanse-gpu.sdsc.xsede.org` | 1,000 | 1,000 |
  | `expanse-ps.sdsc.xsede.org` | 500 | 500 |
  | `expanse.sdsc.xsede.org` | 4,000 | 4,000 |

  `asingh59` is listed on every one of them.
  The help text also corrected two readings of the earlier command. `-p` is `--plain`, meaning no graphics in the output, not "project". And `-a, --auth` exists and was never passed, so every `expanse-client` query in E029 ran unauthenticated.
- **Interpretation:** The E029 conclusion, that the GPU award was not attached, is withdrawn. The award is granted, is 1000 GPU hours, is unused, and runs to Aug 2027. `expanse-client` returning an empty table was an artefact of the instrument, most likely the missing `-a`, and possibly a resource-name mismatch between what that tool calls a resource and what ACCESS calls one.
  The error was drawing a conclusion about the world from a single tool without checking what its flags meant. One command is one source. The `--help` that settled it costs two seconds and was skipped.
  What remains genuinely unverified is whether Slurm will accept and start a GPU job. Award granted and scheduler willing are separate facts, and only `sbatch --test-only` settles the second.
- **Next:** `sbatch --test-only` against `gpu-debug` with `--gpus=1`. If accepted, the 24-checkpoint sweep in goal 2 is unblocked and the determinism test can run on GPU rather than CPU.

## E031 - 2026-09-03 - schema 1.1, dtype measured not guessed, comparison script written

- **Phase:** 2
- **Goal:** Make `logged_eval.py` correct before it is expensive to run, and build the script that turns two runs into the sprint's headline number.
- **Command:** `python -m py_compile` on both files, `logged_eval.py --smoke-test`, and `compare_runs.py` against three synthetic JSONL fixtures
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Result:** Six changes to `tools/logged_eval.py`, and one new file.
  **dtype is now measured.** `environment_fields` no longer writes `"bfloat16" if device.type == "cuda"`. `model_dtype_of(model)` reads `next(model.parameters()).dtype` after the checkpoint loads, and that value is threaded through `make_record`. Null when loading failed. `gpu_name`, `compute_capability` and `bf16_supported` are recorded alongside it, so the claimed dtype can be checked against what the hardware can do rather than assumed consistent with it. If weights arrive as bfloat16 on a card that does not support it, the run prints a warning rather than writing a quiet lie.
  **`slurm_job_id`** is captured from the environment, tying a record to its scheduler log.
  **`--deterministic`** added, default off. Sets `CUBLAS_WORKSPACE_CONFIG`, `torch.use_deterministic_algorithms(True)` and the cuDNN flags. Off by default deliberately: phase 2 measures whether the pipeline reproduces as it stands, and forcing determinism first would answer a different question. The setting is recorded per generation either way.
  **`--limit-tasks N`** added, so a first run on new hardware costs one generation rather than eight.
  **`--smoke-test`** added earlier today, now reporting the 1.1 fields. Downloads nothing, runs one 512x512 matmul to prove compute works rather than that imports resolved, prints `TEST RUN COMPLETE`.
  **Closing summary** added: records written, records carrying an error, elapsed minutes, and an explicit warning when the count does not match what was expected, because a wrong denominator invalidates any rate computed from the file.
  **Schema bumped to 1.1**, 43 fields to 48, documented in `notes/logging-schema.md` with a reason per field.
  **`tools/compare_runs.py` written.** Matches records on checkpoint, task, prompt condition, mode, seed and sample index. Compares `completion_sha256`, so a match is byte equality. Refuses to report a rate when `temperature`, `top_k`, `num_samples`, `max_tokens`, `model_repo`, `model_revision`, `eval_config_sha256`, `code_commit` or `schema_version` differ between the runs, overridable with `--force`. Reports environment differences without blocking, labelling such a comparison a portability test. Excludes unpaired records from the rate and says how many were excluded.
  Tested on fixtures: 2 of 3 identical returned `2 / 3 = 66.7%` with the mismatching record named and both hashes printed, exit 1. A pair differing only in temperature was refused, exit 2.
- **Interpretation:** The refusal behaviour is the point of the second script, not a nicety. E022 found upstream compared runs whose `--num-samples` differed, which alone guarantees mismatch, and nothing in their archive would have revealed it. A comparison tool that reports a number regardless of whether the number means anything reproduces exactly that failure.
  Both scripts are still unproven against a model. `logged_eval.py` has generated no tokens and `compare_runs.py` has only seen synthetic input. The fixtures prove the logic, not the pipeline.
- **Next:** clone upstream on Expanse, rsync `tools/`, run `--smoke-test` under Slurm on a GPU node. That single job settles `bf16_supported` on V100 and proves a job runs at all.

## E032 - 2026-09-08 - determinism test on Expanse: 8 of 8 byte-identical at temperature 0

- **Phase:** 2
- **Goal:** The experiment nobody had run. Same checkpoint, same 8 prompts, temperature 0 (argmax, no generator touched), run twice back to back on one GPU. If the bytes match, everything below the sampler is stable and the published divergence is bookkeeping. If not, no seed will fix it.
- **Command:** `sbatch tools/runeval.sh`, Slurm job 54222400, gpu-shared, one V100. Output in `logs/expanse/eval.o54222400.txt`, evidence in `evidence/determinism/`.
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Result:** Checkpoint `discovery-rl-v11-s560`, HF revision `71bf395f06dff39ad5ee9f8981b941b3c37daae9`, weights held as bfloat16 on a Tesla V100-SXM2-32GB that reports `bf16_supported False`, so bf16 is emulated. Run a: run_id `2026-09-08T08:02:54Z-b7bc6a`, 8 records, 1.7 min. Run b: `2026-09-08T08:04:42Z-076a4e`, 8 records, 1.7 min. `compare_runs.py`: 8 of 8 paired records identical, 100.0%. Token counts per task identical between runs (586, 586, 238, 325, 350, 301, 462, 433). Per-generation time 6.6s to 16.4s. All 8 answers open with "You have touched a matter of considerable importance", 100 percent at temperature 0 against 78 percent in the published sampled outputs (E023). Against upstream's published v11 answers for the same 8 cells: 0 of 8 byte-identical, expected, since theirs were sampled at 0.7.
  Entry written 15 Sep from the archived job output. The run happened 8 Sep and was reported in `reports/progress-week-3.md` but had not been entered here.
- **Interpretation:** Compute is deterministic on this machine at this setting. The published 118 of 120 divergence cannot be explained by hardware or library nondeterminism, and the E026 mechanism, one RNG shared across a batch plus unmatched `--num-samples`, stands as the explanation. This says nothing yet about sampled runs at 0.7, which do touch the generator; that is the next test. The `weights_sha256` field is null in every record because `--hash-weights` was not passed; the revision pin covers identity for now, the hash should be added on the sweep.
- **Next:** seeded sampling at upstream's exact settings (temperature 0.7, top_k 50, seed 42, one sample), twice, plus a byte comparison against their published v11 output for the same cells.

## E033 - 2026-09-15 - the remaining experiments scripted and dry-tested; nothing new run on a GPU

- **Phase:** 2 and 3
- **Goal:** Turn everything still open into scripts that run one at a time, each ending in an HTML page, so the remaining work is submission and reading rather than writing.
- **Command:** `python tools/make_leading_config.py`; `python -m py_compile` on every new tool; `tools/report.py` on `evidence/determinism/` plus the upstream v11 and no_assumptions results; `tools/judge.py --dry-run`; `tools/blind_packet.py` on determinism plus upstream; `tools/probe_report.py` on a synthetic file; `tools/corpus_search.py` against a stubbed parquet reader; `bash -n` on every Slurm script.
- **Exit status:** 0 for all
- **Upstream commit:** `5b489c8c`, still clean, `git diff` empty
- **Result:** New files. `tools/EVAL_leading.json`, generated from upstream `EVAL.json` (sha256 `3d2ee617836f...`) by appending one "Hint:" paragraph per task, every other field byte-identical, verified by a field-by-field assert. Slurm jobs `run_sampling.sh` (seeded 0.7 four ways), `run_sensitivity.sh` (3 checkpoints x 3 conditions x 3 samples = 216), `run_sweep.sh` (24 x 8 x 1 = 192 at upstream's settings), `run_knowledge_probe.sh` (16 stems x 2 checkpoints, base model and s560, greedy), `run_corpus_search.sh` (CPU, 56GB corpus, 15 terms). Mac-side tools `judge.py` (upstream's `build_judge_messages` imported unchanged, judge model defaults to their `claude-sonnet-4-20250514`, temperature 0, resumable, failures recorded as null), `report.py` (denominators, bootstrap CI, per task and checkpoint and condition, pairwise byte and score agreement, upstream loadable as a series), `blind_packet.py`, `probe_report.py`, `corpus_search.py`. `logged_eval.py` gained recognition of `leading` and `probe` config names. Ordered runbook in `notes/runbook.md`.
  Two things surfaced by running `report.py` over upstream's own files, both new. Upstream's minimal-prompt run (`physics_eval_v11_no_assumptions`, 3 checkpoints, 3 samples) has mean 1.38, n=72, bootstrap 95% CI 1.21 to 1.54, against 0.93, n=192, CI 0.84 to 1.03 for the scaffolded sweep; the two intervals do not overlap, though the checkpoint sets differ. And 72 of 72 minimal-prompt outputs open with the stock phrase, against 150 of 192 scaffolded.
  Upstream's judge call sets no temperature, so the API default applied and was not recorded. Their judge failure path writes `score: 0`; in the v11 judged file 0 of 192 rationales start "Judge error", so it did not fire there.
- **Interpretation:** The pipeline is complete on paper and every CPU-side piece has run on real files. Nothing in this entry is a result about the model. The GPU jobs are queued behind one command each, and the judged numbers are behind an API key.
- **Next:** `sbatch tools/run_sampling.sh`, in the order given in `notes/runbook.md`.

## E034 - 2026-09-15 - four Expanse jobs submitted

- **Phase:** 2 and 3
- **Goal:** Run the scripted experiments from E033.
- **Command:** `sbatch tools/run_sampling.sh` (job 54315364), `sbatch tools/run_sensitivity.sh` (54315386), `sbatch tools/run_knowledge_probe.sh` (54315391), from `/expanse/lustre/projects/sdp197/asingh59/gpt1900` on login01, after `rsync -av tools/ $EXPGPT/tools/`.
- **Exit status:** all three accepted. Sampling started on `exp-14-60` within a minute; the other two pending on priority.
- **Upstream commit:** `5b489c8c`
- **Result:** pending. Logs will land in `script_logs/<jobname>.o<jobid>.txt` on Expanse, to be copied to `logs/expanse/`.
- **Next:** `run_sweep.sh`, then pull `evidence/` down and read `evidence/sampling/compare-ab.html`.

## E035 - 2026-09-15 - seeded sampling reproduces: 8 of 8, three ways

- **Phase:** 2
- **Goal:** Does generation at upstream's actual settings (temperature 0.7, top_k 50, seed 42, one sample) reproduce on one machine? E032 only covered temperature 0.
- **Command:** `sbatch tools/run_sampling.sh`, job 54315364, node exp-14-60, V100, bf16 emulated. Log `script_logs/sampling.o54315364.txt`.
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Result:** a vs b (normal kernels): 8 / 8 identical. c vs d (`--deterministic`): 8 / 8. a vs c (normal vs deterministic): 8 / 8. Run a took 2.3 min; answers longer than at temperature 0 (photoelectric 948 tokens vs 586). Byte match against upstream's published v11 answers for the same cells: to be read off `compare-ab.html`, expected 0.
- **Interpretation:** With the seed recorded and one sample per call, sampled generation is exactly repeatable on this hardware, and forcing deterministic kernels changes nothing. The published 118 of 120 divergence is fully explained by bookkeeping: an unrecorded default seed and mismatched `--num-samples` between run and repeat (E022, E026). No hardware or library nondeterminism is needed to explain it, and none was observed.
- **Next:** read the upstream column on `compare-ab.html`; wait for sensitivity and probe jobs.

## E036 - 2026-09-15 - knowledge probe: no post-1900 recall, but no pre-1900 recall either

- **Phase:** 3
- **Goal:** Contamination from the model side. 16 sentence stems, 11 about post-1900 physics and people, 5 controls about pre-1900 physics, continued greedily by the base model `d34-22btok` (completion mode) and by `discovery-rl-v11-s560` (chat mode). 200 tokens each.
- **Command:** `sbatch tools/run_knowledge_probe.sh`, job 54315391. `tools/probe_report.py` for keyword flags. Evidence `evidence/contamination/probe.jsonl`, `probe.html`, log `script_logs/probe-knowledge.o54315391.txt`.
- **Exit status:** 0. 32 of 32 generations, 0 errors.
- **Upstream commit:** `5b489c8c`
- **Result:** Keyword flags: 4 of 11 post-1900 stems on each model, 0 of 5 controls on each. Every one of the 8 flags is the stem's own word echoed back (photon, relativity, Planck, Bohr, Nobel, Wright brothers) or, once, the base model counting years upward from the 1901 in the stem (1902 to 1909, "awarded to the University of Gottingen"). No flag came from a word the stem did not contain.
  Read by eye, post-1900 stems, base model: Planck's constant becomes a tautology loop; a photon is "a small piece of paper, or a piece of cloth" for receiving images; Einstein is an author of popular geology; relativity is about the mind; E = mc^2 is about coefficients; spacetime is transit timing; Bohr proposed covering the earth with water; the events of 1905 are the discovery of Neptune and Uranus "on the 1st of November, 1805"; the Wright brothers are rifle shots. RL model: every stem answered in the same period-letter voice, most opening "You have touched a matter of considerable importance", with content unrelated to the stem: Planck's constant is about plant growth, E = mc^2 about wages, spacetime about commerce, Bohr about "a universal language of the senses", the Wright brothers about an iron process.
  Controls, base model: the electron is "a thin plate of copper" in mercury; Michelson-Morley "showed that the best results were obtained by the use of a single wire", repeated to the token limit; Maxwell's equations describe motion on a parabola; Rontgen's rays degenerate into "the electric light of the electric light". Only the aether stem is roughly right ("the medium of the light of the sun"). RL model: the electron is "a living force" with iron filings; Michelson and Morley "showed that" a double-tube boiler is efficient; Maxwell is gases under pressure; Rontgen's rays "a new form of energy" that "pervade all matter", the one near-miss.
  Two side observations. The base model at temperature 0 falls into verbatim repetition loops within two sentences on 13 of 16 stems, the known greedy-decoding degeneration of small models. And on the Wright stem the RL model emitted the chat template tokens `<|user_end|><|assistant_start|>` mid-completion, wrote itself a user turn, and continued; the engine did not stop on it and the text carries the raw tokens.
- **Interpretation:** No evidence of post-1900 knowledge in either model. But the negative result is weaker than the flag count makes it look, because the controls failed too: neither model can state what Thomson's electron or the Michelson-Morley experiment was, and both are inside the corpus. So the probe shows absence of factual recall in this decoding mode, not specifically absence of post-1900 recall. Two confounds to remove before the memo leans on it: greedy decoding loops, fixable by sampling a few continuations per stem at 0.7; and the RL model's register, which overrides the prompt content entirely. The register finding is itself important and links to E023: the RL checkpoint produces the same letter-voice prose whether the stem is Planck's constant, wages, or a boiler, which sharpens the question of whether the published scores partly reward that voice. "Michelson and Morley showed that" answered with boiler design, on the one task that never scores 0, is the single line to show Keating.
- **Next:** rerun the probe at temperature 0.7 with 3 samples per stem (one flag change in the job script), corpus search, and the judge.

## E037 - 2026-09-15 - prompt sensitivity generations complete: 216 of 216, stock opening 216 of 216

- **Phase:** 3
- **Goal:** Generate the three-condition prompt sensitivity set with matched checkpoints and sample counts, so the judged comparison in the next step is fair (plan 3.1, E025).
- **Command:** `sbatch tools/run_sensitivity.sh`, job 54315386, node exp-5-60. Log `script_logs/sensitivity.o54315386.txt`. Evidence `evidence/prompt-sensitivity/{scaffolded,minimal,leading}.jsonl` plus HTML.
- **Exit status:** 0
- **Upstream commit:** `5b489c8c`
- **Result:** Checkpoints s560, s630, s735; 8 tasks; seeds 42, 43, 44; temperature 0.7, top_k 50. 72 records per condition, 0 errors, 0 hit max_tokens. Stock opening "You have touched" in 72 of 72 scaffolded, 72 of 72 minimal, 72 of 72 leading. Byte-identical answers across conditions: 0 of 72 for every pair, as expected since the prompts differ. Not yet judged.
- **Interpretation:** Denominators are clean and matched, which is the point of the run. The stock opening at 100 percent under all three wordings, including the leading one, is stronger than E023's 78 percent in the published sweep: at these three checkpoints the RL model opens every answer identically regardless of how the question is put. Whether the judge rewards that is the question the scores will answer. No claim about sensitivity until judged.
- **Next:** judge all three files (needs the API key), then `report.py` on the three judged files with upstream's no_assumptions run as a fourth series.

## E038 - 2026-09-22 - three Expanse jobs submitted: sweep, sampled probe, corpus search

- **Phase:** 3
- **Goal:** Run the three experiments still outstanding from `notes/runbook.md`. The 15 Sep sweep was never submitted; `script_logs/` has no sweep entry and `evidence/sweep/` did not exist.
- **Command:** `rsync tools/` up, `pip install pyarrow` in the GPT1900 conda env (pyarrow 25.0.1), then `sbatch tools/run_sweep.sh` (job 54390360), `sbatch tools/run_knowledge_probe_sampled.sh` (54390361), `sbatch tools/run_corpus_search.sh` (54390362). Transcript in `logs/20260922-expanse-status.log`.
- **Exit status:** all three accepted, all pending on priority at submission.
- **Upstream commit:** `5b489c8c`
- **Result:** Before submission: queue empty, `hf_cache/` 38 GB holding d26-8btok, d34-22btok, s560, s630, s735; `HF_HOME` already pointed at `$GPT/hf_cache` in `.bashrc`, and the corpus job now exports the same so the 56 GB download cannot land in `/home`. The corpus script no longer loads a compiler module; the conda Python does not need one. Sweep will add about 125 GB of checkpoints, corpus 56 GB, total under 220 GB of the 500 GB project allocation.
- **Next:** wait for the three logs, pull `evidence/` down, log each result.

## E039 - 2026-09-22 - prompt sensitivity graded, provisional grader: leading 1.64, scaffolded 1.36, minimal 1.22

- **Phase:** 3
- **Goal:** Score the 216 sensitivity generations from E037 and the 8 sampling answers from E035, with no API access, in a way that stays checkable (D008).
- **Command:** `tools/blind_packet.py` on the four JSONL files, seed 20260922, `--batches 24` (224 answers, 10 batches); each batch graded in a fresh Claude session that saw only id, prompt, rubric and answer; `tools/judge_import.py` back through the sealed key; `tools/report.py` with upstream's `physics_eval_v11_no_assumptions` as a fourth series. Logs `logs/20260922-judge-import-a.log`, `logs/20260922-report-sensitivity.log`. Grades in `evidence/review-packet-a/grades/`, judged files `evidence/prompt-sensitivity/*.graded.jsonl`.
- **Exit status:** 0. 224 of 224 scored, 0 unparseable.
- **Upstream commit:** `5b489c8c`
- **Result:** Means with 95% bootstrap intervals, n=72 each: scaffolded 1.36 (1.22 to 1.50), minimal 1.22 (1.12 to 1.32), leading 1.64 (1.46 to 1.83). Score histograms: scaffolded 0:1 1:49 2:17 3:5; minimal 0:0 1:56 2:16 3:0; leading 0:0 1:40 2:20 3:10 4:2. Leading minus scaffolded per task: elevator +0.89, frozen light +0.56, photoelectric +0.44, Michelson-Morley +0.44, free fall +0.11, approaching c +0.11, train 0.00, UV catastrophe -0.33. Per checkpoint the ordering leading > scaffolded > minimal holds on all three (s560 1.54 / 1.29 / 1.17; s630 1.54 / 1.38 / 1.12; s735 1.83 / 1.42 / 1.38). Upstream's own minimal run on the same three checkpoints, their judge: 1.38 (1.21 to 1.54); ours on the same wording, our grader, different samples: 1.22 (1.12 to 1.32).
  Sampling run a (s560, seed 42, their settings) graded: 1.00, n=8, interval 0.62 to 1.38; upstream's published s560 row is 1.25; exact score agreement 6 of 8 cells despite different text and a different grader.
  Grader reliability: batch 02 graded twice in independent sessions, 24 of 24 exact agreement, both means 1.08. Batch 01 repeat pending.
- **Interpretation:** With matched checkpoints, seeds and sample counts, the leading prompt scores highest and the intervals of leading and minimal do not overlap; leading and scaffolded overlap by 0.04. The hint moves the mean by +0.28 on a scale where the whole published signal is 0.93, and the largest gains land on the two tasks whose hint most nearly states the rubric's top answer (elevator, frozen light). UV catastrophe goes the other way: the hint about discrete lumps did not help and may have pulled answers toward restating it. Minimal below scaffolded is the opposite of upstream's unfair comparison (E025), which put minimal higher; with sample counts matched, removing the assumptions costs about 0.14. All of this under a provisional grader that is not the one the paper used; the comparison to upstream's minimal run (1.38 vs 1.22) is the first cross-grader number; the intervals overlap, their point estimate sits outside ours (corrected 7 Oct; an earlier wording said each was inside the other's interval, which 1.38 against 1.12 to 1.32 is not). 24 of 24 exact agreement on a re-graded batch says this grader is at least self-consistent.
- **Next:** repeat batch 01 for a second reliability figure; grade the sweep the same way when it lands; put both graders side by side when a key exists.

## E040 - 2026-09-22 - sampled knowledge probe: 66 of 66 post-1900 stems clean, controls still fail without the greedy loops

- **Phase:** 3
- **Goal:** Remove the greedy-decoding confound from E036 by sampling three continuations per stem at temperature 0.7.
- **Command:** `sbatch tools/run_knowledge_probe_sampled.sh`, job 54390361. 16 stems x 2 checkpoints x 3 samples (seeds 42, 43, 44), 200 tokens. Every continuation read blind against the expected outcome in `tools/probe_knowledge.json` and given a verdict in `evidence/contamination/probe-sampled-readings.json`; page rebuilt with `tools/probe_report.py`. Log `logs/expanse/probe-sampled.o54390361.txt`.
- **Exit status:** 0. 96 of 96 generations, 0 errors.
- **Upstream commit:** `5b489c8c`
- **Result:** Post-1900 stems: base model 33 of 33 clean, RL s560 33 of 33 clean, 0 leaks. Keyword flags from words the stem did not contain: 1 of 96 (the year-counting continuation again). Controls, base model: 2 knows (both the aether stem), 13 fails. Controls, RL s560: 6 partial, 9 fails, 0 knows. The repetition loops of E036 are gone; the base model now writes varied period prose, and it is still about the wrong thing: "the electron" is a hardened steel bar in copper sulphate, a rack-and-pinion apparatus, a glass instrument of 200 disks; "Michelson and Morley in 1887 showed that" is followed by membership statistics of a National Association, or water temperatures in a pneumatic trough. Echo (the stem's own term as the only link to the topic) on 22 of 96.
- **Interpretation:** The greedy loops were not hiding knowledge. With sampling, the base model produces fluent 1890s text and cannot state a single one of the five pre-1900 facts except, twice, that the aether is the medium of light. The clean post-1900 result therefore stands, and so does the caveat: this probe measures the absence of fact recall in general. A 3.29B model trained on 22B tokens of OCR'd books does not carry "Thomson, 1897, corpuscle" as a retrievable fact, so a stem-completion probe cannot separate "never saw Planck" from "saw it and did not retain it". The corpus search (E041) is the instrument that can. For the paper, the useful sentence is that the model's contamination risk is bounded above by its recall, which is near zero at the level of named facts.
- **Next:** corpus search result; sweep grading.

## E041 - 2026-09-22 - corpus search: 0 of 2,074,160 documents dated 1900 or later, and one that is anyway

- **Phase:** 7, contamination, corpus side
- **Goal:** Search the training corpus itself for text that a pre-1900 model should never have seen. The model-side probe (E036, E040) could not separate "never saw Planck" from "saw it and did not retain it"; only the corpus can.
- **Command:** `sbatch tools/run_corpus_search.sh` (job 54390362, `shared` partition, 16 workers), which runs `tools/corpus_search.py` over `mhla/pre1900-corpus` at revision `ff332ef64f896c8d44672b4d1d0c752029e32f29`, 42 parquet shards, 56.4 GB, 15 terms with a year histogram each and a count of documents dated 1900 or later.
- **Exit status:** 0, 49.6 minutes of scanning
- **Upstream commit:** `5b489c8c`
- **Result:** 2,074,160 documents, years 1547 to 1899, **0 dated 1900 or later** by metadata.

  | Term | Docs | Share | Latest year | Reading |
  |---|---|---|---|---|
  | Einstein | 0 | 0 | none | clean |
  | photon | 0 | 0 | none | clean |
  | photoelectric | 0 | 0 | none | clean |
  | spacetime | 0 | 0 | none | clean |
  | aether wind | 0 | 0 | none | clean |
  | Planck | 705 | 0.034% | 1899 | plausible, publishing from 1879 |
  | Lorentz | 330 | 0.016% | 1899 | plausible, publishing from 1875 |
  | Michelson | 277 | 0.013% | 1899 | plausible, 1881 and 1887 experiments |
  | Rayleigh | 702 | 0.034% | 1899 | plausible |
  | relativity | 1,391 | 0.067% | 1899 | philosophical sense, pre-Einstein |
  | quantum | 14,407 | 0.695% | 1899 | Latin "how much", common |
  | quanta | 2,614 | 0.126% | 1899 | same |
  | Morley | 14,235 | 0.686% | 1899 | surname |
  | FitzGerald | 19,216 | 0.926% | 1899 | surname |
  | Nobel Prize | 1 | 0.00005% | 1829 | **contamination, see below** |

  The one Nobel Prize hit is an annual report of the American Peace Society, metadata year 1829, source `institutional-books`. Its text reads: "The Nobel Prize was awarded in December last to two distinguished Scandinavian peace workers, one-half to Mr. Fredrik Bajer of Denmark, founder and president of the Society". Bajer received the Peace Prize in 1908. The document is a 1909 report carrying a wrong date.
- **Interpretation:** Two results, and they pull in different directions.
  **The physics is clean.** Every term that could only exist after 1900 returns zero across two million documents. The terms that do appear are all accounted for by pre-1900 usage: Planck, Lorentz, Michelson and Rayleigh were active before 1900; quantum and quanta are ordinary Latin; relativity is the philosophical word; Morley and FitzGerald are surnames. Nothing in the corpus names Einstein, the photon, the photoelectric effect or spacetime. Combined with E040, where the model showed no post-1900 recall, there is no evidence that the eight physics tasks are answerable from leaked text.
  **The date filter has at least one hole.** "0 documents dated 1900 or later" is a statement about metadata, and one document dated 1829 contains a 1908 fact. The corpus was assembled by date, so a misdated source passes the filter and its contents are in the training set. One document in two million is not a physics leak, and the physics-only terms say none happened. But it means the clean count is a lower bound on contamination, not a proof of zero, and the memo must say so. The mechanism is now demonstrated rather than hypothetical.
  What this does not cover: paraphrase without the keyword, and any post-1900 physics stated in period vocabulary. A term search cannot find those. The model-side probe is the check for that, and it found nothing either, with the caveat that it finds nothing pre-1900 as well.
- **Next:** memo 7.3, slide 8, talking points 8. The sweep is still running.

## E042 - 2026-09-22 - full sweep reproduced and graded: 1.27 (1.18 to 1.36) against the published 0.93 (0.84 to 1.03)

- **Phase:** 3, workstream 1
- **Goal:** Reproduce the published 24-checkpoint evaluation at its own settings, grade it, and set the result beside 0.932 with denominators and intervals.
- **Command:** `sbatch tools/run_sweep.sh`, job 54390360, one V100, 64.3 min. All 24 v11 checkpoints x 8 tasks x 1 sample, seed 42, temperature 0.7, top_k 50, scaffolded prompt, `--hash-weights`. Then `blind_packet.py` (seed 20260923, 8 batches of 24), eight fresh-session graders plus two regrades (D008), `judge_import.py`, `report.py --upstream-dir upstream/gpt1900/results/physics_eval_v11`. Logs `logs/expanse/sweep.o54390360.txt`, `logs/20260922-judge-import-b.log`, `logs/20260922-report-sweep.log`, `logs/20260922-sweep-reliability-and-rank.log`. Evidence `evidence/sweep/`, grades `evidence/review-packet-b/`.
- **Exit status:** 0. 192 of 192 generated, 0 errors, 4 hit max_tokens. 192 of 192 graded.
- **Upstream commit:** `5b489c8c`. HF revision `71bf395f...` for all 24, weight sha256 in every record.
- **Result:** Text level: stock opening 151 of 192 (published 150 of 192); 0 of 192 byte-identical to the published answers, as expected across hardware.
  Scores, provisional grader: mean **1.27**, n=192, 95% bootstrap 1.18 to 1.36, histogram 0:13 1:126 2:41 3:12 4:0 5:0. Published: 0.93, 0.84 to 1.03, histogram 0:44 1:122 2:22 3:3 4:1 5:0. Cell-by-cell against the published grades: exact 101 of 192, within one point 188 of 192, mean difference +0.34, mean absolute difference 0.49. Per task, ours / published: UV 1.25 / 0.83, photoelectric 2.17 / 1.54, frozen light 1.00 / 0.75, approaching c 0.88 / 0.38, train 0.96 / 0.54, Michelson-Morley 1.29 / 1.04, elevator 1.58 / 1.46, free fall 1.04 / 0.92. Every task higher under our grader on our text. Per checkpoint: first eight checkpoints average 0.97, last eight 1.52; published 0.62 and 1.11 (E024). Rank correlation of the 24 per-checkpoint means with the published ones: Spearman 0.71, Pearson 0.75. Our range 0.75 to 1.62; published 0.25 to 1.25.
  Grader reliability on this packet: 48 answers regraded in independent sessions, 45 of 48 exact (94%), 48 of 48 within one point. Combined with E039: 89 of 96 exact across both packets.
- **Interpretation:** The published sweep reproduces in shape and not in level. The training trend is there (+0.55 from first to last third against their +0.49), the per-checkpoint ordering correlates at 0.71, and the score histogram has the same mode at 1. The mean sits 0.34 higher and the intervals do not overlap. Two things differ at once: the answer text (sampled here, on a V100 with emulated bf16) and the grader (a different Claude, in a session rather than through the API, no temperature control). This entry cannot say which one carries the 0.34. The cross-grade in E044, our grader on their 192 published texts, is the experiment that separates them, and it is running as this is written. What can be said now: the grader gives far fewer zeros (13 against 44), so part of the gap is almost certainly the grader's floor, and the memo will say that whatever E044 shows.
- **Next:** E044, then memo sections 4 and 6, talking points 5, slide 6.

## E044 - 2026-09-22 - cross-grade: the 0.34 gap is the grader, not the model. Their text under our grader 1.26, ours 1.27, theirs under theirs 0.93

- **Phase:** 3, workstream 1
- **Goal:** E042 left two things confounded, the answer text and the grader. Separate them by grading the authors' own 192 published answers with the same blinded procedure used on ours.
- **Command:** `blind_packet.py --upstream-dir upstream/gpt1900/results/physics_eval_v11 --seed 20260924 --batches 24` (packet C), eight fresh-session graders, `judge_import.py` writing `evidence/review-packet-c/physics_eval_v11.regraded.jsonl`, `report.py` with three series. Logs `logs/20260922-judge-import-c.log`, `logs/20260922-report-sweep-crossgrade.log`. Page `evidence/sweep/report.html`.
- **Exit status:** 0. 192 of 192 regraded.
- **Upstream commit:** `5b489c8c`
- **Result:** Three series, n=192 each, 95% bootstrap intervals.

  | Text | Grader | Mean | Interval | Histogram 0/1/2/3/4 |
  |---|---|---|---|---|
  | our sweep (E042) | ours | 1.27 | 1.18 to 1.36 | 13 / 126 / 41 / 12 / 0 |
  | their published | ours | 1.26 | 1.17 to 1.35 | 13 / 125 / 45 / 9 / 0 |
  | their published | theirs (published) | 0.93 | 0.84 to 1.03 | 44 / 122 / 22 / 3 / 1 |

  Cell by cell: our text vs their text, both under our grader, 126 of 192 exact, mean difference +0.01. Their text under our grader vs their published grades, same bytes, 119 of 192 exact, 188 within one point, mean difference +0.33. Per task, their text under our grader / their grader: UV 1.33 / 0.83, photoelectric 1.92 / 1.54, frozen light 1.08 / 0.75, approaching c 0.75 / 0.38, train 0.96 / 0.54, Michelson-Morley 1.25 / 1.04, elevator 1.67 / 1.46, free fall 1.12 / 0.92. Training trend, first eight to last eight checkpoints: our text 0.97 to 1.52, their text under our grader 0.92 to 1.45, published 0.62 to 1.11.
- **Interpretation:** The generation step reproduces the published result at the level of the score, not just the trend: a fresh sweep on different hardware, graded by one grader alongside the authors' own answers, lands within 0.01 of them with two thirds of cells agreeing exactly. Every part of the 0.34 gap in E042 is the grader. Same rubric, same answers, a different Claude: +0.33, mostly from the zero row (44 zeros under their grader, 13 under ours) and the 2-and-3 rows. So the published 0.93 is a property of the grader as much as of the model, by about a third of a point on a five-point scale, which is larger than the whole prompt-sensitivity effect (E039, +0.28 for a leading hint) and comparable to the training gain across the sweep (+0.49). The memo's headline changes from "we got 1.27, they got 0.93" to "the model reproduces; the number does not survive a change of grader". This is the strongest single argument for pinning the judge model and version in the record (D006), and for a human-graded anchor (the packet).
  What this does not settle: which grader is closer to a physicist. The blinded packet is the instrument for that.
- **Next:** memo sections 4 and 6, talking points 5, slide 6, the presentation brief.

## E043 - 2026-09-22 - dtype control: V100 emulated bf16 against CPU float32, 0 of 8 identical

- **Phase:** 2, the caveat carried since E032
- **Goal:** Every generation so far ran on a V100 holding bf16 weights that the hardware cannot compute natively, so PyTorch emulates it. Does that change the answers? Upstream's own hardware is unrecorded, so this is also the question of whether any of their text could be reproduced on a different machine even with every setting matched.
- **Command:** First attempt, `sbatch tools/runfp32.sh` (job 54390458): `logged_eval.py --dtype float32` on the GPU, schema 1.2. Second, `sbatch tools/runfp32cpu.sh` (job 54390459): `--device cpu`, upstream's own CPU path, `shared` partition, 32 cores. Both against `evidence/determinism/run-a.jsonl`, the V100 run from E032. Same checkpoint s560, same `EVAL.json`, temperature 0, seed 1337, one sample.
- **Exit status:** 54390458 completed in 12 s with 8 of 8 generations failed; 54390459 completed in 39.4 min with 8 of 8 written, 0 errors.
- **Upstream commit:** `5b489c8c`
- **Result:**
  **The GPU float32 attempt cannot run.** `model.float()` recasts the rotary tables that `nanochat/gpt.py:258` keeps in bfloat16, and `gpt.py:396` asserts on it: `Rotary embeddings must be in bfloat16`. Eight error records with that traceback are in `evidence/dtype-control/fp32.jsonl`. Upstream's model does not support float32 on a GPU without patching their code, which D003 rules out.
  **The CPU float32 path runs and gives different answers on every task.** Byte identity with the V100 run: **0 of 8**. All 8 open with the stock phrase. Per task, tokens V100 / CPU and the length of the identical prefix before the first differing character:

  | Task | V100 tok | CPU tok | Shared prefix (chars / words) |
  |---|---|---|---|
  | uv_catastrophe_main | 586 | 498 | 792 / 136 |
  | photoelectric_effect_main | 586 | 518 | 201 / 34 |
  | sr_frozen_light | 238 | 333 | 600 / 108 |
  | sr_approaching_c | 325 | 305 | 479 / 89 |
  | sr_train_lightning | 350 | 377 | 205 / 35 |
  | sr_michelson_morley | 301 | 257 | 210 / 37 |
  | gr_main_elevator_light | 462 | 416 | 801 / 142 |
  | gr_free_fall_equivalence | 433 | 272 | 314 / 55 |

  Mean shared prefix 450 characters. The UV catastrophe pair agrees for 136 words, then the V100 writes "the total energy is not uniform throughout the frequency interval" and the CPU writes "the total energy thus produced is finite", and nothing after that point matches.
  Environment fields that differ, as `compare_runs.py` reports them: device cuda vs cpu, dtype bfloat16 vs float32, gpu V100 vs none, schema 1.1 vs 1.2. Every generation setting matches.
- **Interpretation:** This is the mechanism the caveat predicted, now measured. Two machines, same bytes of model, same prompt, the argmax path with no random draw anywhere, and every answer diverges: identical for tens to hundreds of words, then one near-tied token flips under different rounding and the rest cascades. Neither answer is the correct one. They are two computations.
  Three consequences. First, "reproducible" for this pipeline means reproducible on one machine at one dtype: the V100 gives the same 8 answers twice (E032), and the CPU run's own repeat is job 54390635, pending. Across machines, the text does not carry, even with everything recorded. Second, upstream's unrecorded evaluation hardware is therefore not a footnote. With their seed, sample count and settings all matched, their text still could not be reproduced on a V100 or a CPU, and probably not on an H100 without their exact torch build. The record needs the device, the dtype, and the library version, which schema 1.1 and 1.2 now carry and their three fields do not. Third, the scores may be more stable than the text. Two answers that differ from word 137 onward can both score 1. That is the comparison E042's grading makes possible and it is the one that matters for the paper's 0.93.
  What this does not show: whether emulated bf16 on a V100 is closer to native bf16 on an H100 than float32 is. There is no bf16-native hardware on this allocation. The honest statement is that three plausible hardware paths exist and this project has measured two of them disagreeing.
- **Next:** job 54390635, the CPU path run twice, expected 8 of 8. Then score both dtype runs through the same blinded grader and compare score agreement against byte agreement.

### E043, addendum - CPU float32 path run twice: 8 of 8 identical

Job 54390635, `tools/runfp32cpu-b.sh`, 25.4 min, 8 written, 0 errors.
`compare_runs.py evidence/dtype-control/fp32-cpu.jsonl fp32-cpu-b.jsonl`:
**8 of 8 identical**, both files 34,426 bytes. So the three comparisons stand
together: V100 twice, 8 of 8 [E032]; CPU twice, 8 of 8; V100 against CPU,
0 of 8. Each hardware path is exactly repeatable and the two paths disagree
on every answer. The cross-machine divergence is a property of the numerics,
not noise in either run.

## E045 - 2026-09-30 - elevator light task at n=72 per condition: hint effect +0.89, CI +0.69 to +1.08

- **Phase:** 6, prompt sensitivity, the elevator task deep
- **Goal:** Take `gr_main_elevator_light` from n=9 per condition (E039) to n=72, all 24 v11 checkpoints, so the +0.89 leading-minus-scaffolded gain has an interval and a training curve. Keating named the elevator the final benchmark on 23 Sep.
- **Command:** `sbatch tools/run_elevator.sh` (job 54507422, 77.5 min, gpu-shared). Three one-task configs from `tools/make_task_config.py`: `EVAL_elevator_{scaffolded,minimal,leading}.json`, every non-task field byte-identical to the source. Temperature 0.7, top_k 50, seeds 42 to 44, one sample per call. Graded per D008: `blind_packet.py --batches 24` into `evidence/review-packet-elevator/`, 9 batches in fresh sessions, batches 01 and 05 regraded, `judge_import.py`, `report.py`.
- **Exit status:** 0. 216 of 216 written, 0 errors, 4 hit max_tokens.
- **Upstream commit:** `5b489c8c`
- **Result:** n=72 per condition, 95% bootstrap intervals.

  | Condition | Mean | CI | 0 / 1 / 2 / 3 / 4 | Stock opener |
  |---|---|---|---|---|
  | minimal | 1.31 | 1.18 to 1.43 | 0 / 53 / 16 / 3 / 0 | 64 of 72 |
  | scaffolded | 1.57 | 1.44 to 1.69 | 2 / 27 / 43 / 0 / 0 | 62 of 72 |
  | leading | 2.46 | 2.26 to 2.65 | 0 / 11 / 22 / 34 / 5 | 58 of 72 |

  Paired by checkpoint and seed: leading minus scaffolded **+0.89** (+0.69 to +1.08); scaffolded minus minimal +0.26 (+0.08 to +0.44). Without the hint, no answer in 72 scores above 2. With it, 39 of 72 score 3 or 4. Training trend, first 8 to last 8 checkpoints: scaffolded 1.21 to 1.83, leading 1.71 to 2.79. Published Elev column mean 1.46 against our scaffolded 1.57. Regrade: batch 01 14 of 24 exact (second reader higher on 10, lower on 0), batch 05 21 of 24 exact; combined 35 of 48 exact, 48 of 48 within one.
- **Interpretation:** The n=9 estimate held to two decimals and the interval excludes anything below +0.69. The hint does not nudge the score, it moves the distribution up a rung: scaffolded never reaches 3, leading reaches 3 or 4 more than half the time. The hint paragraph restates rubric levels 4 and 5 ("gravity might not be a force pulling on mass at all, but a change in the shape of space and time"), so the benchmark is measuring whether the model can carry a stated idea into an answer, not whether it can produce the idea. The hint helps more as training proceeds, which is consistent with RL teaching the model to follow the prompt rather than to reason. Batch 01's regrade is the widest disagreement seen so far (mean 1.62 vs 2.04), all in one direction; it does not change the ordering but it is a reminder that the provisional grader has a floor that moves between sessions.
  **Correction to the task choice, recorded here.** This task is upstream's 1911 light-bending consequence, not Einstein's 1907 happiest thought. Keating's "elevator test" means the falling person who feels no weight, which is upstream's `gr_free_fall_equivalence`. That task has sweep n=24 mean 1.04, sensitivity n=9 scaffolded 1.11, minimal 1.22, leading 1.22 (hint +0.11), published 0.92. The n=72 run on it is job 54546826, E047.
- **Next:** E046 for the open-ended run; free-fall at n=72 with two new seed-only conditions.

## E046 - 2026-09-30 - the elevator setup with no question: 0 of 64 reach geometry, the trained model restates line 4 and stops

- **Phase:** 6, what the model does unprompted
- **Goal:** Keating's actual question is whether the model can reason toward general relativity from the thought experiment. Give it the seven numbered observations of `gr_main_elevator_light` and no puzzle, no question, no hint, and read what it produces.
- **Command:** `sbatch tools/run_elevator_open.sh` (job 54507423, 23 min). `tools/EVAL_elevator_open.json`: two prompts, `elevator_open_continue` (observations only) and `elevator_open_ask` (observations plus "What follows from this?"). Checkpoints `d34-22btok` (pre-RL base, completion mode per the registry), `discovery-rl-v11-s035`, `s560`, `s839` (chat mode). 8 samples each, seeds 42 to 49, temperature 0.7, max 1024 tokens. 64 continuations shuffled with seed 20260930, provenance stripped, read once by a blinded reader with one verdict per item from {geometry, not-a-force, bends-in-gravity, equivalence, none, loops, incoherent}, highest rung reached. `tools/open_report.py` renders all 64 with verdicts.
- **Exit status:** 0. 64 of 64 written, 0 errors.
- **Upstream commit:** `5b489c8c`
- **Result:**

  | Model | Mode | loops | none | equivalence | bends-in-gravity | not-a-force | geometry | Stock opener | Hit 1024 |
  |---|---|---|---|---|---|---|---|---|---|
  | d34-22btok (base) | completion | 16 | 0 | 0 | 0 | 0 | 0 | 0 of 16 | 16 of 16 |
  | s035 | chat | 0 | 8 | 5 | 2 | 1 | 0 | 1 of 16 | 1 of 16 |
  | s560 | chat | 0 | 1 | 14 | 1 | 0 | 0 | 16 of 16 | 0 |
  | s839 | chat | 0 | 0 | 16 | 0 | 0 | 0 | 16 of 16 | 0 |

  Geometry: 0 of 64. Reader's notes record three continuations that state light does not bend (s560 seeds 45 and 49, s035 seed 42) and one that says "we must revise our notion of space but never says gravity is its shape" (s560 seed 42). The two bends-in-gravity and one not-a-force verdicts all come from s035; the reader marks two of the three as marginal (Earth's rotation offered as the mechanism; garbled numerics).
- **Interpretation:** Three things. The base model cannot continue the thought experiment at all: every continuation degenerates into repetition, "2.2. 2.2. 2.2." or "If the planet be whirled around the sun" twenty times. The trained model converges on one sentence, "acceleration and gravity are equivalent", which is line 4 of the prompt, and stops there: 16 of 16 for s839, 14 of 16 for s560. It restates the given as a conclusion and, three times, denies the next step. The only verdicts above rung 1 come from the least-trained RL checkpoint, which is also the only one that has not yet acquired the stock opener. Set beside E045: with the hint, 39 of 72 reach rung 3 or 4; without a question, 0 of 64 reach rung 4 and 1 of 64 reaches rung 3. The hint is not eliciting what the model already thinks. It is supplying the thought.
  Two caveats. The base model runs in completion mode and the RL checkpoints in chat mode, as the registry defines them; a base-vs-RL comparison carries that confound. And the reading is one reader, one pass, no regrade.
- **Next:** the same design on the 1907 seed (E047).

## E047 - 2026-10-01 - free fall, the 1907 seed, at n=72: hint effect +0.00; 0 of 144 answers supply the equivalence unprompted

- **Phase:** 6, prompt sensitivity and the jump test on Einstein's happiest thought
- **Goal:** Do for `gr_free_fall_equivalence` what E045 did for the elevator: all 24 v11 checkpoints, three seeds, three wordings, graded. And add the test the benchmark lacks: give the model only the 1907 observation, the falling person who feels no weight, and count how often it brings in acceleration, equivalence or geometry on its own.
- **Command:** `sbatch tools/run_freefall.sh` (job 54546826, 30 Sep, gpu-shared, 360 generations, about 2 h). Configs from `tools/make_task_config.py`: `EVAL_freefall_{scaffolded,minimal,leading}.json`, one task each, every non-task field byte-identical to the source; `EVAL_freefall_seed.json` with two new prompts, `gr_freefall_seed` (the two observations plus "What does this tell us about gravity?") and `gr_freefall_bare` (the two observations, nothing appended). Temperature 0.7, top_k 50, seeds 42 to 44, one sample per call, max 1024 tokens. Graded per D008: `blind_packet.py --batches 24` into `evidence/review-packet-freefall/` (seed 20261001), 9 fresh-session graders, batches 01 and 05 regraded, `judge_import.py`, `report.py`. Seed and bare read blind: 144 answers shuffled (seed 20261001), R-ids, two fresh-session readers of 72 each with the six-verdict rule (geometry, not-a-force, equivalence, none, loops, incoherent; highest rung reached; restating the observations is none), merged through the key by `tools/merge_blind_readings.py`, rendered by `tools/freefall_jump.py`; every automatic keyword hit checked by eye against the verdict. Pages `evidence/freefall/summary.html`, `report.html`, `jump.html`. Logs `logs/expanse/freefall.o54546826.txt`, `logs/20261001-*.log`.
- **Exit status:** 0. 360 of 360 written, 0 errors, 8 hit max_tokens. 216 of 216 graded. 144 of 144 read.
- **Upstream commit:** `5b489c8c`
- **Result:** Rubric task, n=72 per condition, 95% bootstrap intervals.

  | Condition | Mean | CI | 0 / 1 / 2 / 3 / 4 | Stock opener |
  |---|---|---|---|---|
  | minimal | 0.92 | 0.81 to 1.03 | 12 / 54 / 6 / 0 / 0 | 60 of 72 |
  | scaffolded | 0.99 | 0.89 to 1.07 | 6 / 61 / 5 / 0 / 0 | 64 of 72 |
  | leading | 0.99 | 0.90 to 1.07 | 5 / 63 / 4 / 0 / 0 | 59 of 72 |

  Paired by checkpoint and seed: leading minus scaffolded **+0.00** (-0.12 to +0.12); scaffolded minus minimal +0.07 (-0.07 to +0.21). Highest score in 216 answers: 2. No answer reaches 3 under any wording. Training trend, first 8 to last 8 checkpoints: scaffolded 0.83 to 1.00, minimal 0.71 to 1.08, leading 0.92 to 1.08. Published Fall column mean 0.92 (their single answer per checkpoint, their judge); our scaffolded 0.99; exact score agreement on the 24 shared cells 17 of 24. Regrade: batch 01 16 of 24 exact, batch 05 22 of 24; combined 38 of 48 exact, 48 of 48 within one.
  The jump: seed form 0 of 72, bare form 0 of 72. All 144 verdicts none; 0 loops, 0 incoherent. Automatic keyword flags fired on 7 of 144; each is a false positive on reading ("equivalent to the sum of all the forces", "not a force that can be measured in pounds", "this is the geometry of gravity" followed by Newtonian pressing). Readers' near-misses, all none under the rule: the fall "neutralises" the force and weight "dissolves" (s490 seed 42); bodies "glide side by side" (shared motion, acceleration never named); weight felt only at the abrupt stop; universality of free fall stated several times without the step to equivalence. Stock opener 60 of 72 seed, 57 of 72 bare. Mean length 406 and 354 tokens.
- **Interpretation:** Set beside E045 the two general-relativity tasks give one result with two halves. On the 1911 consequence, light bending, the hint is worth +0.89 and lifts 39 of 72 answers to rung 3 or 4. On the 1907 seed, the same kind of hint, which states that free fall is the natural state and gravity is structure, is worth +0.00 with an interval of a quarter point either side, and no answer in 216 reaches 3 under any wording. The model can be led to the consequence and cannot be led to the seed, even when the seed is handed to it. And when the seed is all it has, it never supplies the idea: 0 of 144 bring in acceleration, equivalence or geometry. What it produces instead is period prose about air, muscles, inertia, Newton's attraction and the Divine order, in the stock voice 117 times out of 144.
  Why the two tasks differ is visible in the prompts. The elevator prompt already states the equivalence (line 4) and asks for its consequence; the hint supplies the rubric's top answer and the model carries it forward. The free-fall prompt asks for the equivalence itself. Restating a given idea the model can do; producing the idea, or using it once stated, it cannot. That is the benchmark's five-stage test failing at stage one, measured rather than argued. For the paper the cleanest line is the pair of hint effects, +0.89 and +0.00, with the jump count under them.
  Caveats as before: the provisional grader (D008), 38 of 48 exact on regrade, a touch lower than earlier packets; one reading pass on the jump, no regrade, though the keyword cross-check and the two readers' independent 72 of 72 agree; all 24 checkpoints are RL checkpoints in chat mode, the base model is not in this run.
- **Next:** paper draft section 4.4 and figure 4; the free-fall and elevator summaries are the two pages to show Keating.

## E048 - 2026-10-07 - abduction suite and the final elevator case submitted

- **Phase:** 6, the professor's final test and the "can't jump" controls
- **Goal:** Run the professor's elevator question in his own words across the whole training run, and add the controls that make the 0 of 144 jump result (E047) a statement about abduction specifically. Design in `notes/abduction-suite.md`, written before the results.
- **Command:** `python tools/make_abduction_config.py` (13 prompts in three groups, verdict ladders fixed per prompt), `sbatch tools/run_elevator_final.sh` (job 54719457: one prompt, 24 v11 checkpoints plus base, 3 seeds, 75 generations), `sbatch tools/run_abduction.sh` (job 54719458: 13 prompts x 4 checkpoints x 5 seeds, 260 generations). Temperature 0.7, top_k 50, max 768 tokens, all weights cached. Transcript `logs/20261007-expanse-status.log`.
- **Exit status:** both accepted, pending on priority at 22:40 PT.
- **Upstream commit:** `5b489c8c`
- **Result:** pending. Reading tooling ready: `tools/make_read_file.py`, `tools/merge_blind_readings.py`, `tools/abduction_report.py`.
- **Next:** pull, read blind, E049 (final) and E050 (suite).

## E049 - 2026-10-07 - the elevator test in the professor's words, 25 checkpoints: 0 of 75 reach weightlessness, 23 say weight is still felt

- **Phase:** 6, the final test case
- **Goal:** Put the professor's own phrasing to the whole training run: "You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft. What do you feel during the fall? Explain why, and say what this tells us about gravity." Read every answer blind against a ladder fixed in advance (D009): wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent.
- **Command:** `tools/debug/elevfin1.sh` (job 54719479, 21.6 min, base plus v11 s035 to s455) and `tools/debug/elevfin2.sh` (54719480, 17.0 min, s490 to s839) on gpu-debug after the gpu-shared queue stalled at 142 jobs ahead; stitched into `evidence/elevator-final/final.jsonl`. Temperature 0.7, top_k 50, seeds 42 to 44, max 768 tokens. Read in two fresh sessions through R-ids (`tools/make_read_file.py`, seed 20261008), merged by `tools/merge_blind_readings.py`, rendered by `tools/abduction_report.py`. Logs `logs/expanse/elevfin*.o*.txt`, `logs/20261007-elevator-final-readings.log`. Page `evidence/elevator-final/report.html`.
- **Exit status:** 0. 75 of 75 written, 0 errors, 9 hit max_tokens. 75 of 75 read.
- **Upstream commit:** `5b489c8c`
- **Result:** Verdicts, 75 answers: none 48, wrong 23, loops 4, weightless 0, equivalence 0, not-a-force 0, geometry 0. The base model (3 answers) loops every time. The 24 RL checkpoints (72 answers): none 48, wrong 23, loops 1. "Wrong" means the answer states that weight or pressure is still felt during the fall, or that a heavier passenger falls faster. Wrong answers rise with training: first eight checkpoints 3 of 24, last eight 12 of 24. "None" answers are period prose about cables, levers, pendulums, gravity acting on every particle, or the mechanics of the shaft, that never say what the rider feels. Readers' nearest misses, all held at none: one answer cut off mid-sentence after "does not feel the weight of the floor"; one says cage and passengers share a common motion but then says the heavier passenger falls faster; one says gravity differs from other forces and defines it as a persistent pull. Stock opener 55 of 75. Mean length 497 tokens.
- **Interpretation:** On the professor's test, asked in the professor's words, no checkpoint at any point in training states the observation that Einstein called his happiest thought, that a falling person feels no weight. The model does not reach the jump; it does not reach the step before the jump. Where it commits to an answer, it commits to the opposite one, and more so as training proceeds: the late checkpoints are the ones that say the rider still feels his weight. Set beside E047 (the observation handed to the model: 0 of 144 reach equivalence) and E045 (the hint handed to the model: 39 of 72 reach rungs 3 and 4 on the 1911 task), the pattern is complete. Handed the conclusion, it repeats it; handed the observation, it cannot take the step; asked to produce the observation, it produces the wrong one. The rising wrong count with training is the one new fact: the RL rewards taught the model to answer confidently, not to answer correctly, and on this prompt the confident answer is a Newtonian one.
  Caveats: one phrasing, three seeds; the four phrasings of the abduction suite (E050) test whether the wording matters. One reading pass each, two readers in agreement on the shape, no regrade.
- **Next:** E050, the abduction suite.

## E050 - 2026-10-07 - abduction suite: the elevator in four phrasings reaches the jump 0 of 140 times, and the reasoning controls fail too

- **Phase:** 6, the final test and the "can't jump" controls
- **Goal:** Three questions fixed in `notes/abduction-suite.md` before the run. Does the professor's elevator question, in four phrasings, ever draw the observation or the jump? At what rung of help on the 1907 observation does the equivalence first appear? And is the failure specific to abduction, or does the model also fail deduction and induction inside its own corpus?
- **Command:** four gpu-debug slices `tools/debug/abd-{base,s035,s560,s839}.sh` (jobs 54724264, 54724266, 54724525, 54724526, 13 to 29 min each), one checkpoint per slice, 13 prompts x 5 seeds (42 to 46), temperature 0.7, top_k 50, max 768 tokens; stitched to `evidence/abduction/abduction.jsonl`. Read blind in four fresh sessions of 65 through R-ids (seed 20261008) against the per-prompt verdict ladders in `tools/EVAL_abduction.json` (D009); merged by `tools/merge_blind_readings.py`; page `evidence/abduction/report.html`. Logs `logs/expanse/abd-*.o*.txt`, `logs/20261007-abduction-readings.log`.
- **Exit status:** 0. 260 of 260 written, 0 errors, 84 hit max_tokens (52 of those the base model). 260 of 260 read.
- **Upstream commit:** `5b489c8c`
- **Result:** Each cell below is 20 answers (base model plus v11 s035, s560, s839, five seeds each).

  | prompt | group | wrong | none | weightless | equivalence | not-a-force | geometry | loops | incoh. |
  |---|---|---|---|---|---|---|---|---|---|
  | elevator: what do you feel | final | 3 | 12 | 0 | 0 | 0 | 0 | 5 | 0 |
  | elevator: feel, why, gravity | final | 4 | 11 | 0 | 0 | 0 | 0 | 4 | 1 |
  | elevator: lets go of a stone | final | 14 | 1 | 0 | 0 | 0 | 0 | 5 | 0 |
  | elevator: standing on a scale | final | 5 | 10 | 0 | 0 | 0 | 0 | 4 | 1 |
  | 1907 observation + "something is mistaken, what" | ladder | 0 | 12 | 0 | 0 | 3 | 0 | 5 | 0 |
  | 1907 observation + accelerating carriage | ladder | 4 | 11 | 1 | 0 | 0 | 0 | 4 | 0 |
  | 1907 observation + "no experiment reveals gravity" | ladder | 0 | 15 | 0 | 0 | 0 | 0 | 5 | 0 |

  Gravity prompts together, 140 answers: none 72, loops 32 (every one from the base model), wrong 30, not-a-force 3, incoherent 2, weightless 1, equivalence 0, geometry 0. The three not-a-force verdicts are all on the prompt that tells the model something in its understanding is mistaken; they negate "gravity is a pull" ("not a pull, but a motion"; "the weight is borne by the floor and walls") and none brings in acceleration. The one weightless verdict (s560, carriage prompt) says a man in motion bears no weight and attributes it to motion in general, never to the carriage.

  Controls, 20 answers each (RL checkpoints only, 15, in brackets):

  | prompt | type | in corpus | correct | partial | wrong | none | loops | incoh. |
  |---|---|---|---|---|---|---|---|---|
  | stone dropped from a ship's mast | deduction | yes | 0 (0) | 2 (2) | 10 (10) | 3 (3) | 5 | 0 |
  | two stones of different weight | deduction | yes | 0 (0) | 6 (6) | 9 (9) | 0 | 3 | 2 |
  | pendulum rule from four data points | induction | yes | 1 (1) | 3 (3) | 10 (10) | 1 (1) | 5 | 0 |
  | Uranus wanders, what explains it | abduction | yes | 0 (0) | 5 (5) | 14 (10) | 0 | 0 | 1 |
  | Michelson-Morley null, bare | abduction | no | 0 (0) | 0 (0) | 7 (6) | 10 (9) | 3 | 0 |
  | black-body peak, bare | abduction | no | 0 (0) | 2 (2) | 5 (4) | 9 (9) | 4 | 0 |

  Base model, all 65 answers: loops 52, wrong 7, incoherent 5, none 1. Per RL checkpoint on the 35 gravity answers: s035 none 28 wrong 7; s560 none 22 wrong 10 not-a-force 2 weightless 1; s839 none 22 wrong 12 not-a-force 1. Stock opener 135 of 260.
- **Interpretation:** Three answers to the three questions. First, the professor's elevator, in any of four phrasings, never draws the observation that the rider feels no weight (0 of 80), and the most concrete phrasing draws the opposite 14 times out of 15: asked what a stone does when let go in the falling elevator, the trained model says it falls to the floor. With E049 (0 of 75 on the one phrasing across all 24 checkpoints) the wording is ruled out as the cause. Second, no rung of help on the 1907 observation produces the equivalence: 0 of 60 across the three ladder prompts, as 0 of 144 with no help (E047); the only movement is that a prompt saying "something is mistaken" makes the model deny that gravity is a pull, which is negation on cue, not the jump. Third, and this is the finding the suite was built for: the controls fail. On Galileo's ship and Galileo's two stones, both well inside the corpus and both pure deduction, the trained checkpoints are wrong 10 and 9 times out of 15 and correct 0. On the pendulum induction, 1 of 15. On the one abduction the corpus contains, the unseen planet behind Uranus, 0 of 15. So the "can't jump" framing does not fit this model: it is not a system that walks but cannot jump; it cannot walk. What it does, confidently, in the stock voice, is give the everyday answer: the heavier stone first, the stone behind the mast, the stone to the floor, weight still felt. The base model, before RL, mostly cannot answer at all (52 of 65 loop). RL taught the voice and the confidence; the answers underneath are a 19th-century layman's, not a 19th-century physicist's.
  What this means for the Einstein test as a benchmark: a prompt that scores 1 on the published rubric is one that restates the given; nothing in this suite suggests the model can be brought to stage one by any wording short of stating the answer. Caveats: four checkpoints on the suite (24 on E049's single phrasing); one reading pass, four readers whose counts agree in shape; the readers flagged a handful of near-misses in their notes, all held at none under the strict rule and all listed on the page; temperature 0.7, five seeds per cell.
- **Next:** fold E049 and E050 into the brief and the inserts; nothing further to run for the presentation.

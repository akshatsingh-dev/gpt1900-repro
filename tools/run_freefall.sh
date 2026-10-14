#!/bin/bash
#SBATCH --job-name=freefall
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# Einstein's happiest thought as the final benchmark, and the jump test.
#
# Upstream's gr_free_fall_equivalence is the 1907 seed: a person falling from
# a roof feels no weight. Five conditions, all 24 v11 checkpoints, 3 seeds:
#
#   scaffolded  upstream EVAL.json               falling person + accelerating cabin + "gravity can disappear"
#   minimal     upstream EVAL_no_assumptions     falling person + accelerating cabin
#   leading     tools/EVAL_leading.json          scaffolded + hint (free fall is the natural state, gravity is structure)
#   seed        tools/EVAL_freefall_seed.json    falling person ONLY + "What does this tell us about gravity?"
#   bare        same file, second task           falling person ONLY, no question
#
# The first three are the same design as run_elevator.sh. seed and bare are
# new: they give the model Einstein's observation and nothing else. If the
# accelerating-cabin idea or the word equivalence appears in a seed/bare
# answer, the model supplied it. That is the jump. If it only appears once
# the prompt states it, the model did not jump.
#
# 24 x 3 x 3 + 24 x 2 x 3 = 360 generations. About 2 hours.
# Submit from the project root:   sbatch tools/run_freefall.sh

set -euo pipefail
module purge
module load slurm
module load gpu
module load gcc/10.2.0
source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

OUTDIR=evidence/freefall
mkdir -p "$OUTDIR"
for F in scaffolded minimal leading seed; do
    if [ -e "$OUTDIR/$F.jsonl" ]; then echo "ERROR: $OUTDIR/$F.jsonl exists"; exit 1; fi
done

run_condition () {
    echo "################ CONDITION $1 ################"
    srun --unbuffered python tools/logged_eval.py \
        --eval-config "$2" --prompt-condition "$1" \
        --temperature 0.7 --top-k 50 --seed 42 --num-samples 3 --max-tokens 1024 \
        --keep-cache --cache-dir hf_cache \
        --out "$OUTDIR/$1.jsonl"
    python tools/render_html.py "$OUTDIR/$1.jsonl" -o "$OUTDIR/$1.html"
}

run_condition scaffolded tools/EVAL_freefall_scaffolded.json
run_condition minimal    tools/EVAL_freefall_minimal.json
run_condition leading    tools/EVAL_freefall_leading.json
run_condition seed       tools/EVAL_freefall_seed.json

echo "################ SUMMARY (text level) ################"
python tools/report.py "$OUTDIR"/scaffolded.jsonl "$OUTDIR"/minimal.jsonl "$OUTDIR"/leading.jsonl \
    --upstream-dir upstream/gpt1900/results/physics_eval_v11 \
    --out "$OUTDIR/report.json" --html "$OUTDIR/report.html"
echo "FREEFALL COMPLETE. Open $OUTDIR/report.html. Grade and read on the Mac next."

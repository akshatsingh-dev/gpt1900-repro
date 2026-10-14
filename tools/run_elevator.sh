#!/bin/bash
#SBATCH --job-name=elevator
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=03:00:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# The elevator task as the final benchmark, deep.
#
# gr_main_elevator_light only, all 24 v11 checkpoints, three prompt conditions,
# three seeds. 24 x 3 x 3 = 216 generations. Takes the elevator from n=9 per
# condition (E039) to n=72, so the +0.89 leading-minus-scaffolded gain gets an
# interval and a training curve.
#
#   scaffolded   tools/EVAL_elevator_scaffolded.json   from upstream EVAL.json
#   minimal      tools/EVAL_elevator_minimal.json      from EVAL_no_assumptions.json
#   leading      tools/EVAL_elevator_leading.json      from tools/EVAL_leading.json
#
# Same settings as run_sensitivity.sh: temperature 0.7, top_k 50, seeds 42-44,
# one sample per engine call (D004). All 24 checkpoints are already in
# hf_cache/, no download. Scores come later from the blinded grader on the Mac.
#
# Submit from the project root:   sbatch tools/run_elevator.sh
# Expected: about 75 minutes.

set -euo pipefail

module purge
module load slurm
module load gpu
module load gcc/10.2.0

source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

OUTDIR=evidence/elevator
mkdir -p "$OUTDIR"

for COND in scaffolded minimal leading; do
    if [ -e "$OUTDIR/$COND.jsonl" ]; then
        echo "ERROR: $OUTDIR/$COND.jsonl already exists. Move or delete the old"
        echo "       $OUTDIR directory first, then resubmit."
        exit 1
    fi
done

run_condition () {
    # $1 = condition name, $2 = config path. No --only: every v11 checkpoint.
    echo "################ CONDITION $1 ################"
    srun --unbuffered python tools/logged_eval.py \
        --eval-config "$2" --prompt-condition "$1" \
        --temperature 0.7 --top-k 50 --seed 42 --num-samples 3 \
        --keep-cache --cache-dir hf_cache \
        --out "$OUTDIR/$1.jsonl"
    python tools/render_html.py "$OUTDIR/$1.jsonl" -o "$OUTDIR/$1.html"
}

run_condition scaffolded tools/EVAL_elevator_scaffolded.json
run_condition minimal    tools/EVAL_elevator_minimal.json
run_condition leading    tools/EVAL_elevator_leading.json

echo "################ SUMMARY (text level, no scores yet) ################"
python tools/report.py "$OUTDIR"/scaffolded.jsonl "$OUTDIR"/minimal.jsonl "$OUTDIR"/leading.jsonl \
    --upstream-dir upstream/gpt1900/results/physics_eval_v11 \
    --out "$OUTDIR/report.json" --html "$OUTDIR/report.html"
echo "ELEVATOR COMPLETE. Open $OUTDIR/report.html. Grade on the Mac next."

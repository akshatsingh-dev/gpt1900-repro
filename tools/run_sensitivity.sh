#!/bin/bash
#SBATCH --job-name=sensitivity
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=02:30:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# STEP 2. Prompt sensitivity, done properly.
#
# Three prompt conditions on the SAME checkpoints with the SAME sample count,
# which upstream's own comparison did not do (E025):
#
#   scaffolded   upstream/gpt1900/EVAL.json                classical assumptions spelled out
#   minimal      upstream/gpt1900/EVAL_no_assumptions.json assumptions removed
#   leading      tools/EVAL_leading.json                   a hint that gives away the answer
#
# Checkpoints: s560, s630, s735. These are the three upstream used for their
# minimal-prompt run, so ours can be set beside theirs.
# 3 checkpoints x 8 tasks x 3 samples x 3 conditions = 216 generations.
# Seeds 42, 43, 44 (base seed + sample index), temperature 0.7, top_k 50.
#
# Scores come later, from tools/judge.py on the Mac. This job produces the
# generations and a readable page per condition. The 3-sample spread per cell
# is also the error bar material for the memo.
#
# Submit from the project root:   sbatch tools/run_sensitivity.sh
# Expected wall time: about 50 minutes. Downloads s630 and s735 (~13GB) into
# hf_cache/ and keeps them.

set -euo pipefail

module purge
module load slurm
module load gpu
module load gcc/10.2.0

source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

CKPTS=discovery-rl-v11-s560,discovery-rl-v11-s630,discovery-rl-v11-s735
OUTDIR=evidence/prompt-sensitivity
mkdir -p "$OUTDIR"

for COND in scaffolded minimal leading; do
    if [ -e "$OUTDIR/$COND.jsonl" ]; then
        echo "ERROR: $OUTDIR/$COND.jsonl already exists. Move or delete the old"
        echo "       $OUTDIR directory first, then resubmit."
        exit 1
    fi
done

run_condition () {
    # $1 = condition name, $2 = config path
    echo "################ CONDITION $1 ################"
    srun --unbuffered python tools/logged_eval.py \
        --only "$CKPTS" \
        --eval-config "$2" --prompt-condition "$1" \
        --temperature 0.7 --top-k 50 --seed 42 --num-samples 3 \
        --keep-cache --cache-dir hf_cache \
        --out "$OUTDIR/$1.jsonl"
    python tools/render_html.py "$OUTDIR/$1.jsonl" -o "$OUTDIR/$1.html"
}

run_condition scaffolded upstream/gpt1900/EVAL.json
run_condition minimal    upstream/gpt1900/EVAL_no_assumptions.json
run_condition leading    tools/EVAL_leading.json

echo "################ SUMMARY (text level, no scores yet) ################"
python tools/report.py "$OUTDIR"/scaffolded.jsonl "$OUTDIR"/minimal.jsonl "$OUTDIR"/leading.jsonl \
    --out "$OUTDIR/report.json" --html "$OUTDIR/report.html"
echo "STEP 2 COMPLETE. Open $OUTDIR/report.html. Judge on the Mac next."

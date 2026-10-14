#!/bin/bash
#SBATCH --job-name=probe-sampled
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=00:45:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# STEP 4b. Knowledge probe again, with sampling.
#
# The greedy (temperature 0) probe fell into repetition loops on 13 of 16
# stems for the base model, which makes the control failures hard to read.
# This reruns the same 16 stems on the same two checkpoints at temperature
# 0.7 with 3 samples each (seeds 42, 43, 44). 96 generations. If the controls
# now come back sensible, the loops were the problem. If they still fail,
# the model does not know its own corpus at the level of a single fact.
#
# Submit from the project root:   sbatch tools/run_knowledge_probe_sampled.sh
# Weights are cached from the first probe. About 15 minutes.

set -euo pipefail

module purge
module load slurm
module load gpu
module load gcc/10.2.0

source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

OUTDIR=evidence/contamination
OUT="$OUTDIR/probe-sampled.jsonl"
mkdir -p "$OUTDIR"

if [ -e "$OUT" ]; then
    echo "ERROR: $OUT already exists. Move it aside first, then resubmit."
    exit 1
fi

srun --unbuffered python tools/logged_eval.py \
    --only d34-22btok,discovery-rl-v11-s560 \
    --eval-config tools/probe_knowledge.json --prompt-condition probe \
    --temperature 0.7 --top-k 50 --seed 42 --num-samples 3 --max-tokens 200 \
    --keep-cache --cache-dir hf_cache \
    --out "$OUT"

python tools/render_html.py "$OUT" -o "$OUTDIR/probe-sampled-generations.html"
python tools/probe_report.py "$OUT" --config tools/probe_knowledge.json \
    --out "$OUTDIR/probe-sampled.json" --html "$OUTDIR/probe-sampled.html"
echo "STEP 4b COMPLETE. Open $OUTDIR/probe-sampled.html."

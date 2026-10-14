#!/bin/bash
#SBATCH --job-name=eval
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=00:30:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# The determinism test. One checkpoint, all 8 tasks, temperature 0, run twice
# back to back on the same node into two files. Then compare_runs.py on the pair.
# Submit from the project root:  cd $GPT && sbatch tools/runeval.sh
# Weights are already in hf_cache/ from the probe, so no download.

set -euo pipefail

module purge
module load slurm
module load gpu
module load gcc/10.2.0

source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

CKPT=discovery-rl-v11-s560
OUTDIR=evidence/determinism
mkdir -p "$OUTDIR"

for RUN in a b; do
    echo "################ RUN $RUN ################"
    srun --unbuffered python tools/logged_eval.py \
        --only "$CKPT" \
        --temperature 0.0 \
        --num-samples 1 \
        --keep-cache \
        --cache-dir hf_cache \
        --out "$OUTDIR/run-$RUN.jsonl"
done

echo "################ COMPARE ################"
python tools/compare_runs.py "$OUTDIR/run-a.jsonl" "$OUTDIR/run-b.jsonl" \
    --out "$OUTDIR/compare.json" --html "$OUTDIR/compare.html" \
    --upstream upstream/gpt1900/results/physics_eval_v11/generations.json \
    --eval-config upstream/gpt1900/EVAL.json || true
python tools/render_html.py "$OUTDIR/run-a.jsonl" "$OUTDIR/run-b.jsonl" \
    -o "$OUTDIR/generations.html"

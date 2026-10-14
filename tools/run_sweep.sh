#!/bin/bash
#SBATCH --job-name=sweep
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

# STEP 3. The full published sweep, reproduced.
#
# All 24 v11 checkpoints x 8 tasks x 1 sample = 192 generations, which is
# exactly the cell count behind the published mean of 0.932. Settings match
# upstream's physics_eval_v11 run: temperature 0.7, top_k 50, seed 42, one
# sample, scaffolded prompt. The only things that differ are the ones we
# cannot control and DO record: the GPU (V100, bf16 emulated) and the torch
# build.
#
# Each checkpoint is downloaded (~6.6GB, ~50s), run, and kept in hf_cache/.
# All 24 come to ~158GB, inside the 500GB project allocation.
#
# Output is one JSONL with 192 records. Scores come from tools/judge.py on
# the Mac afterwards; then tools/report.py sets our mean beside 0.932.
#
# Submit from the project root:   sbatch tools/run_sweep.sh
# Expected wall time: 60 to 90 minutes.
# If it dies part way, DO NOT resubmit as is: the file is append-only and the
# denominator would be wrong. Move the partial file aside first.

set -euo pipefail

module purge
module load slurm
module load gpu
module load gcc/10.2.0

source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

OUTDIR=evidence/sweep
OUT="$OUTDIR/v11-scaffolded.jsonl"
mkdir -p "$OUTDIR"

if [ -e "$OUT" ]; then
    echo "ERROR: $OUT already exists. Move it aside first, then resubmit."
    exit 1
fi

# no --only: logged_eval.py defaults to every discovery-rl-v11-* checkpoint
# --hash-weights: sha256 of every checkpoint file goes into the record, so the
# weights are identified even if the HF revision is later deleted. About 30s
# per checkpoint extra.
srun --unbuffered python tools/logged_eval.py \
    --temperature 0.7 --top-k 50 --seed 42 --num-samples 1 \
    --hash-weights \
    --keep-cache --cache-dir hf_cache \
    --out "$OUT"

python tools/render_html.py "$OUT" -o "$OUTDIR/v11-scaffolded.html"

echo "################ SUMMARY (text level, no scores yet) ################"
python tools/report.py "$OUT" \
    --upstream-dir upstream/gpt1900/results/physics_eval_v11 \
    --out "$OUTDIR/report.json" --html "$OUTDIR/report.html"
echo "STEP 3 COMPLETE. Open $OUTDIR/report.html. Judge on the Mac next."

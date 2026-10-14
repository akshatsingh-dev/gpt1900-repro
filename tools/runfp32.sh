#!/bin/bash
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu
#SBATCH --job-name=fp32
#SBATCH --time=00:30:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt

# dtype control. Same checkpoint and prompt as evidence/determinism/run-a.jsonl,
# but weights and KV cache forced to float32, which the V100 does natively.
# If 8/8 still match run-a, emulated bf16 changed nothing here.

set -euo pipefail
module purge
module load slurm
module load gpu
module load gcc/10.2.0
source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900
OUTDIR=evidence/dtype-control
mkdir -p "$OUTDIR"
srun --unbuffered python tools/logged_eval.py --only discovery-rl-v11-s560 \
    --dtype float32 --temperature 0.0 --num-samples 1 --keep-cache --cache-dir hf_cache \
    --out "$OUTDIR/fp32.jsonl"
echo "################ COMPARE vs bf16-emulated run-a ################"
python tools/compare_runs.py evidence/determinism/run-a.jsonl "$OUTDIR/fp32.jsonl" \
    --out "$OUTDIR/compare.json" --html "$OUTDIR/compare.html" \
    --upstream upstream/gpt1900/results/physics_eval_v11/generations.json --eval-config upstream/gpt1900/EVAL.json || true
python tools/render_html.py "$OUTDIR/fp32.jsonl" -o "$OUTDIR/generations.html"

#!/bin/bash
#SBATCH --job-name=fp32cpu
#SBATCH --account=sdp197
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=04:00:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# dtype control, take two. The GPU float32 attempt (job 54390458) hit upstream's
# own assert: rotary tables are kept in bfloat16 and gpt.py:396 insists on it.
# Upstream's supported CPU path casts the weights to float32 and leaves those
# tables alone, so this runs that path, unpatched, on a CPU node. Same
# checkpoint and prompt as evidence/determinism/run-a.jsonl (V100, emulated
# bf16). 8 of 8 matching means dtype and device did not move the argmax here.

set -euo pipefail
module purge
module load slurm
module load cpu
source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900
export OMP_NUM_THREADS=32

OUTDIR=evidence/dtype-control
mkdir -p "$OUTDIR"
srun --unbuffered python tools/logged_eval.py --only discovery-rl-v11-s560 \
    --device cpu --temperature 0.0 --num-samples 1 --keep-cache --cache-dir hf_cache \
    --out "$OUTDIR/fp32-cpu.jsonl"
echo "################ COMPARE vs V100 bf16-emulated run-a ################"
python tools/compare_runs.py evidence/determinism/run-a.jsonl "$OUTDIR/fp32-cpu.jsonl" \
    --out "$OUTDIR/compare-cpu.json" --html "$OUTDIR/compare-cpu.html" \
    --upstream upstream/gpt1900/results/physics_eval_v11/generations.json \
    --eval-config upstream/gpt1900/EVAL.json || true
python tools/render_html.py "$OUTDIR/fp32-cpu.jsonl" -o "$OUTDIR/generations-cpu.html"

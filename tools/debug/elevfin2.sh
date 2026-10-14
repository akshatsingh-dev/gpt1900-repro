#!/bin/bash
#SBATCH --job-name=elevfin2
#SBATCH --account=sdp197
#SBATCH --partition=gpu-debug
#SBATCH --qos=gpu-debug-normal
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=00:30:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt

# Final elevator case, professor's wording, part 2 of 2.
# Debug-partition slice of run_elevator_final.sh; the full-size job stays queued on
# gpu-shared as a fallback. Parts are concatenated on the Mac.

set -euo pipefail
module purge
module load slurm
module load gpu
module load gcc/10.2.0
source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900
OUTDIR=evidence/elevator-final/parts
mkdir -p "$OUTDIR"
if [ -e "$OUTDIR/final-2.jsonl" ]; then echo "ERROR: $OUTDIR/final-2.jsonl exists"; exit 1; fi
srun --unbuffered python tools/logged_eval.py \
    --only discovery-rl-v11-s455,discovery-rl-v11-s490,discovery-rl-v11-s525,discovery-rl-v11-s560,discovery-rl-v11-s595,discovery-rl-v11-s630,discovery-rl-v11-s665,discovery-rl-v11-s700,discovery-rl-v11-s735,discovery-rl-v11-s770,discovery-rl-v11-s805,discovery-rl-v11-s839 \
    --eval-config tools/EVAL_elevator_final.json --prompt-condition final \
    --temperature 0.7 --top-k 50 --seed 42 --num-samples 3 --max-tokens 768 \
    --keep-cache --cache-dir hf_cache \
    --out "$OUTDIR/final-2.jsonl"
echo "elevfin2 COMPLETE"

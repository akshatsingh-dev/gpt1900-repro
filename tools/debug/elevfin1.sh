#!/bin/bash
#SBATCH --job-name=elevfin1
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

# Final elevator case, professor's wording, part 1 of 2.
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
if [ -e "$OUTDIR/final-1.jsonl" ]; then echo "ERROR: $OUTDIR/final-1.jsonl exists"; exit 1; fi
srun --unbuffered python tools/logged_eval.py \
    --only d34-22btok,discovery-rl-v11-s035,discovery-rl-v11-s070,discovery-rl-v11-s105,discovery-rl-v11-s140,discovery-rl-v11-s175,discovery-rl-v11-s210,discovery-rl-v11-s245,discovery-rl-v11-s280,discovery-rl-v11-s315,discovery-rl-v11-s350,discovery-rl-v11-s385,discovery-rl-v11-s420 \
    --eval-config tools/EVAL_elevator_final.json --prompt-condition final \
    --temperature 0.7 --top-k 50 --seed 42 --num-samples 3 --max-tokens 768 \
    --keep-cache --cache-dir hf_cache \
    --out "$OUTDIR/final-1.jsonl"
echo "elevfin1 COMPLETE"

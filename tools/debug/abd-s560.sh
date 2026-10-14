#!/bin/bash
#SBATCH --job-name=abd-s560
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

# Abduction suite, checkpoint discovery-rl-v11-s560.
# Debug-partition slice of run_abduction.sh; the full-size job stays queued on
# gpu-shared as a fallback. Parts are concatenated on the Mac.

set -euo pipefail
module purge
module load slurm
module load gpu
module load gcc/10.2.0
source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900
OUTDIR=evidence/abduction/parts
mkdir -p "$OUTDIR"
if [ -e "$OUTDIR/abduction-s560.jsonl" ]; then echo "ERROR: $OUTDIR/abduction-s560.jsonl exists"; exit 1; fi
srun --unbuffered python tools/logged_eval.py \
    --only discovery-rl-v11-s560 \
    --eval-config tools/EVAL_abduction.json --prompt-condition abduction \
    --temperature 0.7 --top-k 50 --seed 42 --num-samples 5 --max-tokens 768 \
    --keep-cache --cache-dir hf_cache \
    --out "$OUTDIR/abduction-s560.jsonl"
echo "abd-s560 COMPLETE"

#!/bin/bash
#SBATCH --job-name=probe
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

# First real generation. One checkpoint, one task, full record.
# Submit from the project root:  cd $GPT && sbatch tools/runprobe.sh
# Downloads ~6.6GB into hf_cache/ and keeps it, so later runs skip the download.

set -euo pipefail

module purge
module load slurm
module load gpu
module load gcc/10.2.0

source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

srun --unbuffered python tools/logged_eval.py \
    --only discovery-rl-v11-s560 \
    --limit-tasks 1 \
    --temperature 0.0 \
    --num-samples 1 \
    --keep-cache \
    --cache-dir hf_cache \
    --out evidence/probe.jsonl

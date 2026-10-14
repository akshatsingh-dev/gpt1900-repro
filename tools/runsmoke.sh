#!/bin/bash
#SBATCH --job-name=smoke
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=00:30:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=BEGIN,END,FAIL,REQUEUE,TIME_LIMIT_90
#SBATCH --mail-user=aks022@ucsd.edu

set -euo pipefail

module purge
module load slurm
module load gpu
module load gcc/10.2.0


echo "Activating virtual environment..."
source /home/asingh59/miniconda3/etc/profile.d/conda.sh || { echo "Failed to source conda shell"; exit 1; }
conda activate GPT1900 || { echo "Failed to activate virtual environment"; exit 1; }

echo "Starting script"
srun --unbuffered python tools/smoke.py || { echo "smoke.py failed"; exit 1; }

echo "Fit completed."
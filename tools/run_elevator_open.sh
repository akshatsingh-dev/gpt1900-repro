#!/bin/bash
#SBATCH --job-name=elevopen
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=01:00:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# The elevator thought experiment with no rubric-shaped question.
#
# tools/EVAL_elevator_open.json holds two prompts built from the seven numbered
# observations of gr_main_elevator_light, nothing else:
#   elevator_open_continue   the observations, no question at all
#   elevator_open_ask        the observations plus "What follows from this?"
#
# Four checkpoints. d34-22btok is the pre-RL base and runs in completion mode
# (registry, physics_eval.py:49); the three v11 checkpoints run in chat mode.
# That mode difference is a confound and is recorded, not hidden. 8 samples
# per prompt per checkpoint, seeds 42-49, temperature 0.7, max 1024 tokens.
# 4 x 2 x 8 = 64 generations. Downloads d34-22btok (~6.6 GB) once.
#
# Not graded on the rubric. Read blind on the Mac, verdict per answer,
# tools/open_report.py.
#
# Submit from the project root:   sbatch tools/run_elevator_open.sh
# Expected: about 25 minutes.

set -euo pipefail

module purge
module load slurm
module load gpu
module load gcc/10.2.0

source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

OUTDIR=evidence/elevator-open
mkdir -p "$OUTDIR"
if [ -e "$OUTDIR/open.jsonl" ]; then
    echo "ERROR: $OUTDIR/open.jsonl already exists. Move or delete it first."
    exit 1
fi

srun --unbuffered python tools/logged_eval.py \
    --only d34-22btok,discovery-rl-v11-s035,discovery-rl-v11-s560,discovery-rl-v11-s839 \
    --eval-config tools/EVAL_elevator_open.json --prompt-condition open \
    --temperature 0.7 --top-k 50 --seed 42 --num-samples 8 --max-tokens 1024 \
    --keep-cache --cache-dir hf_cache \
    --out "$OUTDIR/open.jsonl"
python tools/render_html.py "$OUTDIR/open.jsonl" -o "$OUTDIR/open.html"
echo "ELEVATOR-OPEN COMPLETE. Open $OUTDIR/open.html. Read blind on the Mac next."

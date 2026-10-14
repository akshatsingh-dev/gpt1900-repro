#!/bin/bash
#SBATCH --job-name=abduction
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# The abduction suite. tools/EVAL_abduction.json, 13 prompts in three groups:
#   final    the professor's broken-cable elevator, four phrasings
#   ladder   the 1907 observation with increasing help
#   control  deduction, induction and abduction inside and beyond the corpus
# Four checkpoints as in the open elevator run: the pre-RL base d34-22btok
# (completion mode) and v11 s035, s560, s839 (chat mode). 5 samples each,
# seeds 42 to 46, temperature 0.7, max 768 tokens. 13 x 4 x 5 = 260.
# All weights cached. Not graded on the rubric; read blind on the Mac.
#
# Submit from the project root:   sbatch tools/run_abduction.sh
# Expected: about 50 minutes.

set -euo pipefail
module purge
module load slurm
module load gpu
module load gcc/10.2.0
source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

OUTDIR=evidence/abduction
mkdir -p "$OUTDIR"
if [ -e "$OUTDIR/abduction.jsonl" ]; then
    echo "ERROR: $OUTDIR/abduction.jsonl already exists. Move it aside first."
    exit 1
fi

srun --unbuffered python tools/logged_eval.py \
    --only d34-22btok,discovery-rl-v11-s035,discovery-rl-v11-s560,discovery-rl-v11-s839 \
    --eval-config tools/EVAL_abduction.json --prompt-condition abduction \
    --temperature 0.7 --top-k 50 --seed 42 --num-samples 5 --max-tokens 768 \
    --keep-cache --cache-dir hf_cache \
    --out "$OUTDIR/abduction.jsonl"
python tools/render_html.py "$OUTDIR/abduction.jsonl" -o "$OUTDIR/abduction.html"
echo "ABDUCTION COMPLETE. Open $OUTDIR/abduction.html. Read blind on the Mac next."

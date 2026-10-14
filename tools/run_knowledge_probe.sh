#!/bin/bash
#SBATCH --job-name=probe-knowledge
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

# STEP 4. Contamination probe, model side.
#
# Asks the model to continue 16 sentence stems (tools/probe_knowledge.json):
# 11 about post-1900 physics it should not know (Planck's constant, photon,
# Einstein, relativity, 1905, spacetime, ...) and 5 controls about pre-1900
# physics it should know (Thomson's electron, Michelson-Morley, Maxwell, ...).
#
# Two checkpoints:
#   d34-22btok              the BASE model, completion mode. Cleanest test of
#                           what the corpus taught it. Never RL-tuned.
#   discovery-rl-v11-s560   the RL checkpoint the rest of the sprint uses.
#
# Temperature 0 (greedy), so this is the model's single most likely
# continuation, not a lucky draw. 32 generations, 200 tokens each.
#
# Read the result in evidence/contamination/probe.html. Keyword flags mark any
# continuation that uses a post-1900 term. A flag is a lead, not a verdict;
# read the text.
#
# Submit from the project root:   sbatch tools/run_knowledge_probe.sh
# Expected wall time: about 8 minutes. Downloads the base model (~6.6GB).

set -euo pipefail

module purge
module load slurm
module load gpu
module load gcc/10.2.0

source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

OUTDIR=evidence/contamination
OUT="$OUTDIR/probe.jsonl"
mkdir -p "$OUTDIR"

if [ -e "$OUT" ]; then
    echo "ERROR: $OUT already exists. Move it aside first, then resubmit."
    exit 1
fi

srun --unbuffered python tools/logged_eval.py \
    --only d34-22btok,discovery-rl-v11-s560 \
    --eval-config tools/probe_knowledge.json --prompt-condition probe \
    --temperature 0.0 --num-samples 1 --max-tokens 200 \
    --keep-cache --cache-dir hf_cache \
    --out "$OUT"

python tools/render_html.py "$OUT" -o "$OUTDIR/probe-generations.html"
READINGS=""
[ -e "$OUTDIR/probe-readings.json" ] && READINGS="--readings $OUTDIR/probe-readings.json"
python tools/probe_report.py "$OUT" --config tools/probe_knowledge.json $READINGS \
    --out "$OUTDIR/probe.json" --html "$OUTDIR/probe.html"
echo "STEP 4 COMPLETE. Open $OUTDIR/probe.html."

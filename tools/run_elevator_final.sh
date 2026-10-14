#!/bin/bash
#SBATCH --job-name=elevfinal
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=01:30:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# The final test case in the professor's own words, across the whole
# training run: "an elevator whose cable breaks; what would it feel like,
# and what does it tell us about gravity." One prompt (elev_cable_feel_why),
# all 24 v11 checkpoints plus the pre-RL base, 3 samples each, seeds 42 to
# 44, temperature 0.7, max 768 tokens. 25 x 3 = 75 generations. All cached.
#
# Submit from the project root:   sbatch tools/run_elevator_final.sh
# Expected: about 20 minutes.

set -euo pipefail
module purge
module load slurm
module load gpu
module load gcc/10.2.0
source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

OUTDIR=evidence/elevator-final
mkdir -p "$OUTDIR"
if [ -e "$OUTDIR/final.jsonl" ]; then
    echo "ERROR: $OUTDIR/final.jsonl already exists. Move it aside first."
    exit 1
fi

V11=$(python - <<'PY'
import sys; sys.path.insert(0, "upstream/gpt1900")
from scripts.physics_eval import CHECKPOINTS
print(",".join(c.name for c in CHECKPOINTS if c.name.startswith("discovery-rl-v11-")))
PY
)

srun --unbuffered python tools/logged_eval.py \
    --only "d34-22btok,$V11" \
    --eval-config tools/EVAL_elevator_final.json --prompt-condition final \
    --temperature 0.7 --top-k 50 --seed 42 --num-samples 3 --max-tokens 768 \
    --keep-cache --cache-dir hf_cache \
    --out "$OUTDIR/final.jsonl"
python tools/render_html.py "$OUTDIR/final.jsonl" -o "$OUTDIR/final.html"
echo "ELEVATOR-FINAL COMPLETE. Open $OUTDIR/final.html. Read blind on the Mac next."

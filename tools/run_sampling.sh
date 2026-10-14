#!/bin/bash
#SBATCH --job-name=sampling
#SBATCH --account=sdp197
#SBATCH --partition=gpu-shared
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=00:40:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# STEP 1. Does seeded sampling reproduce?
#
# The determinism test (8 Sep) used temperature 0, which never touches the
# random number generator. Upstream's published runs used temperature 0.7 with
# the engine's default seed 42. This runs at THEIR settings, on one checkpoint:
#
#   run a, run b   temperature 0.7, seed 42, normal kernels
#   run c, run d   same, plus --deterministic (forces deterministic GPU kernels)
#
# Then three comparisons:
#   a vs b   do two seeded 0.7 runs match on this machine?      (the test)
#   c vs d   same question with deterministic kernels forced
#   a vs c   does forcing deterministic kernels change the bytes?
#
# compare.html also shows upstream's published answer for each cell, and
# whether ours is byte-identical to it.
#
# Submit from the project root:   sbatch tools/run_sampling.sh
# Weights for s560 are already in hf_cache/ so there is no download.
# Expected wall time: about 8 minutes.

set -euo pipefail

module purge
module load slurm
module load gpu
module load gcc/10.2.0

source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

CKPT=discovery-rl-v11-s560
OUTDIR=evidence/sampling
UPSTREAM_GEN=upstream/gpt1900/results/physics_eval_v11/generations.json
mkdir -p "$OUTDIR"

# refuse to append to files from an earlier attempt: the denominator would lie
for RUN in a b c d; do
    if [ -e "$OUTDIR/run-$RUN.jsonl" ]; then
        echo "ERROR: $OUTDIR/run-$RUN.jsonl already exists. Move or delete the"
        echo "       old $OUTDIR directory first, then resubmit."
        exit 1
    fi
done

for RUN in a b; do
    echo "################ RUN $RUN  (temperature 0.7, seed 42) ################"
    srun --unbuffered python tools/logged_eval.py \
        --only "$CKPT" \
        --temperature 0.7 --top-k 50 --seed 42 --num-samples 1 \
        --keep-cache --cache-dir hf_cache \
        --out "$OUTDIR/run-$RUN.jsonl"
done

# Deterministic kernels can refuse an op that has no deterministic version.
# If that happens the run fails; a and b are still compared, and the failure
# is itself worth reporting.
for RUN in c d; do
    echo "################ RUN $RUN  (same, --deterministic) ################"
    srun --unbuffered python tools/logged_eval.py \
        --only "$CKPT" \
        --temperature 0.7 --top-k 50 --seed 42 --num-samples 1 \
        --deterministic \
        --keep-cache --cache-dir hf_cache \
        --out "$OUTDIR/run-$RUN.jsonl" \
        || echo "WARNING: deterministic run $RUN failed, see the error log. Continuing."
done

echo "################ COMPARE a vs b ################"
python tools/compare_runs.py "$OUTDIR/run-a.jsonl" "$OUTDIR/run-b.jsonl" \
    --out "$OUTDIR/compare-ab.json" --html "$OUTDIR/compare-ab.html" \
    --upstream "$UPSTREAM_GEN" --eval-config upstream/gpt1900/EVAL.json || true

echo "################ COMPARE c vs d ################"
python tools/compare_runs.py "$OUTDIR/run-c.jsonl" "$OUTDIR/run-d.jsonl" \
    --out "$OUTDIR/compare-cd.json" --html "$OUTDIR/compare-cd.html" \
    --upstream "$UPSTREAM_GEN" --eval-config upstream/gpt1900/EVAL.json || true

echo "################ COMPARE a vs c ################"
python tools/compare_runs.py "$OUTDIR/run-a.jsonl" "$OUTDIR/run-c.jsonl" \
    --out "$OUTDIR/compare-ac.json" --html "$OUTDIR/compare-ac.html" \
    --upstream "$UPSTREAM_GEN" --eval-config upstream/gpt1900/EVAL.json || true

python tools/render_html.py "$OUTDIR"/run-*.jsonl -o "$OUTDIR/generations.html"

echo "################ SUMMARY ################"
python tools/report.py "$OUTDIR"/run-*.jsonl \
    --upstream-dir upstream/gpt1900/results/physics_eval_v11 \
    --out "$OUTDIR/report.json" --html "$OUTDIR/report.html"
echo "STEP 1 COMPLETE. Open $OUTDIR/compare-ab.html first."

#!/bin/bash
#SBATCH --job-name=corpus-search
#SBATCH --account=sdp197
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=03:00:00
#SBATCH --output=script_logs/%x.o%j.txt
#SBATCH --error=script_logs/%x.e%j.txt
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aks022@ucsd.edu

# STEP 5. Contamination probe, corpus side. CPU only, no GPU.
#
# Downloads the training corpus (mhla/pre1900-corpus, 44 parquet shards,
# 56GB) into corpus_cache/ and scans every document for 15 terms: Planck,
# Michelson, Morley, aether wind, quantum, photon, Einstein, spacetime, ...
# Reports documents per term, year histogram, snippets, and the count of any
# document dated 1900 or later.
#
# Needs pyarrow in the conda env. Before the first submit, once:
#     conda activate GPT1900 && pip install pyarrow
#
# Submit from the project root:   sbatch tools/run_corpus_search.sh
# Expected wall time: 15 to 40 minutes download, then 15 to 30 minutes scan.
# Result: evidence/contamination/corpus-search.html

set -euo pipefail

module purge
module load slurm
module load cpu

source /home/asingh59/miniconda3/etc/profile.d/conda.sh
conda activate GPT1900

python -c "import pyarrow" || { echo "pyarrow missing: conda activate GPT1900 && pip install pyarrow"; exit 1; }

# 56 GB must land on project storage. /home is 100 GB and would fill.
export HF_HOME="$PWD/hf_cache"

OUTDIR=evidence/contamination
mkdir -p "$OUTDIR" corpus_cache

srun --unbuffered python tools/corpus_search.py \
    --local-dir corpus_cache --workers 16 \
    --out "$OUTDIR/corpus-search.json" --html "$OUTDIR/corpus-search.html"
echo "STEP 5 COMPLETE. Open $OUTDIR/corpus-search.html."

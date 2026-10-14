#!/bin/bash
# Mac-side driver. The gpu-debug QOS allows two queued jobs per account, so the
# six slices go in pairs: the two elevator halves (already running), then the
# four abduction slices two at a time. Pulls each finished part down as it lands.
set -u
R=/expanse/lustre/projects/sdp197/asingh59/gpt1900
L=logs/20261007-chain.log
log(){ echo "$(date '+%H:%M:%S') $*" | tee -a "$L"; }
waitfor(){ # wait until none of the named jobs are in the queue
  while ssh expanse "squeue -h -u asingh59 -o '%j'" 2>/dev/null | grep -q -E "$1"; do sleep 60; done
}
pull(){ rsync -aq "expanse:$R/evidence/" evidence/ && rsync -aq "expanse:$R/script_logs/" logs/expanse/; }
log "waiting for elevfin1 elevfin2"
waitfor '^elevfin[12]$'; pull; log "elevator halves done: $(wc -l evidence/elevator-final/parts/*.jsonl 2>/dev/null | tail -1)"
for pair in "abd-base abd-s035" "abd-s560 abd-s839"; do
  for j in $pair; do
    out=$(ssh expanse "cd $R && sbatch tools/debug/$j.sh" 2>&1); log "submit $j: $out"
  done
  waitfor "^($(echo $pair | tr ' ' '|'))$"; pull
  log "pair done: $pair"
done
log "ALL SLICES DONE $(wc -l evidence/abduction/parts/*.jsonl 2>/dev/null | tail -1)"

"""
Search the pre-1900 training corpus for terms that should not be there.

Why this exists
---------------
Two eval tasks sit on the training boundary (E023, plan 3.2). uv_catastrophe
targets Planck's law, published in late 1900, on the stated cut-off line.
sr_michelson_morley refers to an 1887 experiment that is inside the corpus and
is the only task that never scores 0. Whether the corpus contains material
about these is a fact that can be counted rather than argued.

The corpus is mhla/pre1900-corpus on Hugging Face: 44 parquet shards, 56GB,
columns text, year, title, source. This streams every shard, counts documents
matching each term, keeps a year histogram and a few snippets per term, and
counts any document whose year is 1900 or later (the README says there are
none, which is worth checking).

Whole-word, case-insensitive matching. A count is documents, not occurrences.

Usage (on Expanse, CPU only; see tools/run_corpus_search.sh)
-----
    python tools/corpus_search.py --local-dir corpus_cache --workers 16 \
        --out evidence/contamination/corpus-search.json \
        --html evidence/contamination/corpus-search.html
    # smoke test on two shards first:  add  --max-shards 2
"""

import argparse
import glob
import html
import json
import os
import re
import sys
import time
from collections import Counter
from multiprocessing import Pool

DATASET = "mhla/pre1900-corpus"

# term -> why it is here. Whole-word regex is built from the key.
DEFAULT_TERMS = {
    "Planck":            "author of the 1900 radiation law behind uv_catastrophe",
    "Michelson":         "the 1887 experiment behind sr_michelson_morley",
    "Morley":            "same",
    "aether wind":       "the concept the M-M task asks about",
    "Rayleigh":          "Rayleigh-Jeans law, also 1900",
    "quantum":           "ordinary word pre-1900; the physics sense is post-1900",
    "quanta":            "same",
    "photoelectric":     "term in use from the 1890s; checks the task's vocabulary",
    "Einstein":          "should be absent, or a different Einstein",
    "relativity":        "ordinary word pre-1900; checks the physics sense",
    "Lorentz":           "1892-1899 contraction hypothesis, legitimately pre-1900",
    "FitzGerald":        "1889 contraction hypothesis, legitimately pre-1900",
    "photon":            "coined 1926; any hit is contamination",
    "spacetime":         "post-1908; any hit is contamination",
    "Nobel Prize":       "first awarded 1901; any hit is contamination",
}
SNIPPETS_PER_TERM = 6
SNIPPET_RADIUS = 160


def build_patterns(terms):
    return {t: re.compile(r"(?<![A-Za-z])" + re.escape(t) + r"(?![A-Za-z])", re.IGNORECASE) for t in terms}


def scan_shard(args):
    """One worker, one parquet file. Returns plain dicts so they pickle."""
    path, terms = args
    import pyarrow.parquet as pq
    pats = build_patterns(terms)
    docs = 0
    post1900 = 0
    post1900_samples = []
    years = Counter()
    hits = {t: 0 for t in terms}
    hit_years = {t: Counter() for t in terms}
    snippets = {t: [] for t in terms}
    pf = pq.ParquetFile(path)
    for batch in pf.iter_batches(batch_size=512, columns=["text", "year", "title", "source"]):
        cols = batch.to_pydict()
        for text, year, title, source in zip(cols["text"], cols["year"], cols["title"], cols["source"]):
            docs += 1
            years[year] += 1
            if year is not None and year >= 1900:
                post1900 += 1
                if len(post1900_samples) < 5:
                    post1900_samples.append({"year": year, "title": title, "source": source,
                                             "head": (text or "")[:200]})
            if not text:
                continue
            for t, pat in pats.items():
                m = pat.search(text)
                if m:
                    hits[t] += 1
                    hit_years[t][year] += 1
                    if len(snippets[t]) < SNIPPETS_PER_TERM:
                        a, b = max(0, m.start() - SNIPPET_RADIUS), min(len(text), m.end() + SNIPPET_RADIUS)
                        snippets[t].append({"year": year, "title": title, "source": source,
                                            "text": text[a:b].replace("\n", " ")})
    return {"shard": os.path.basename(path), "docs": docs, "post1900": post1900,
            "post1900_samples": post1900_samples, "years": dict(years), "hits": hits,
            "hit_years": {t: dict(c) for t, c in hit_years.items()}, "snippets": snippets}


def esc(v):
    return html.escape(str(v)) if v is not None else ""


def main():
    ap = argparse.ArgumentParser(description="Term search over mhla/pre1900-corpus")
    ap.add_argument("--local-dir", default="corpus_cache", help="where the parquet shards live or get downloaded")
    ap.add_argument("--no-download", action="store_true", help="use what is in --local-dir, download nothing")
    ap.add_argument("--terms", default=None, help="comma-separated override of the default term list")
    ap.add_argument("--max-shards", type=int, default=None, help="scan only the first N shards (smoke test)")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", required=True)
    ap.add_argument("--html", required=True)
    args = ap.parse_args()

    terms = dict(DEFAULT_TERMS)
    if args.terms:
        terms = {t.strip(): "user supplied" for t in args.terms.split(",") if t.strip()}

    revision = None
    if not args.no_download:
        from huggingface_hub import HfApi, snapshot_download
        revision = HfApi().dataset_info(DATASET).sha          # pin what we scanned
        print(f"dataset {DATASET} revision {revision}")
        patterns = None
        if args.max_shards is not None:
            patterns = [f"shard_{i:05d}.parquet" for i in range(args.max_shards)]
        print(f"downloading to {args.local_dir} ...", flush=True)
        snapshot_download(repo_id=DATASET, repo_type="dataset", revision=revision,
                          local_dir=args.local_dir, allow_patterns=patterns)

    shards = sorted(glob.glob(os.path.join(args.local_dir, "shard_*.parquet")))
    if args.max_shards is not None:
        shards = shards[:args.max_shards]
    if not shards:
        raise SystemExit(f"no shard_*.parquet under {args.local_dir}")
    total_bytes = sum(os.path.getsize(s) for s in shards)
    print(f"scanning {len(shards)} shards, {total_bytes / 1e9:.1f} GB, {len(terms)} terms, {args.workers} workers", flush=True)

    started = time.time()
    results = []
    with Pool(args.workers) as pool:
        for i, res in enumerate(pool.imap_unordered(scan_shard, [(s, list(terms)) for s in shards]), 1):
            results.append(res)
            print(f"  {i}/{len(shards)} {res['shard']}: {res['docs']:,} docs, "
                  + ", ".join(f"{t} {res['hits'][t]}" for t in list(terms)[:4]) + " ...", flush=True)
    elapsed = time.time() - started

    # ---- merge ----
    docs = sum(r["docs"] for r in results)
    post1900 = sum(r["post1900"] for r in results)
    post1900_samples = [s for r in results for s in r["post1900_samples"]][:10]
    years = Counter()
    for r in results:
        years.update({int(k) if k is not None else -1: v for k, v in r["years"].items()})
    merged = {}
    for t in terms:
        hy = Counter()
        snips = []
        for r in results:
            hy.update({int(k) if k is not None else -1: v for k, v in r["hit_years"][t].items()})
            snips.extend(r["snippets"][t])
        n = sum(r["hits"][t] for r in results)
        merged[t] = {"why": terms[t], "docs": n, "share": n / docs if docs else None,
                     "by_decade": {str(d): c for d, c in sorted(Counter((y // 10) * 10 for y in hy.elements()).items())},
                     "latest_year": max(hy) if hy else None,
                     "snippets": snips[:SNIPPETS_PER_TERM]}

    summary = {"dataset": DATASET, "revision": revision, "shards_scanned": len(shards),
               "shards_total_bytes": total_bytes, "documents": docs, "documents_year_ge_1900": post1900,
               "year_ge_1900_samples": post1900_samples,
               "year_min": min((y for y in years if y >= 0), default=None),
               "year_max": max((y for y in years if y >= 0), default=None),
               "elapsed_minutes": elapsed / 60, "terms": merged}
    with open(args.out, "w") as f:
        json.dump(summary, f, indent=2)

    # ---- terminal ----
    print("=" * 62)
    print(f"documents {docs:,}   with year >= 1900: {post1900}   years {summary['year_min']}..{summary['year_max']}   {elapsed / 60:.1f} min")
    for t, m in merged.items():
        print(f"  {t:16} {m['docs']:>9,} docs  {100 * (m['share'] or 0):6.3f}%   latest year {m['latest_year']}")
    print("=" * 62)

    # ---- html ----
    p = ["<!doctype html><html><head><meta charset='utf-8'><title>Corpus search</title><style>",
         "body{margin:0 auto;padding:2rem;max-width:1100px;font:14px/1.5 -apple-system,Helvetica,Arial,sans-serif;color:#1a1a1a;background:#fafafa}",
         "table{border-collapse:collapse;width:100%;background:#fff;font-size:13px}th,td{text-align:left;padding:.4rem .6rem;border-bottom:1px solid #e2e2e2;vertical-align:top}th{background:#f0f0f0}td.num{text-align:right}",
         ".card{background:#fff;border:1px solid #e2e2e2;border-radius:8px;padding:1rem 1.25rem;margin:1rem 0}",
         ".snip{font-size:13px;background:#f6f6f6;border:1px solid #e2e2e2;border-radius:6px;padding:.5rem .8rem;margin:.4rem 0}",
         ".muted{color:#6b6b6b}mark{background:#fff2a8}",
         "</style></head><body><h1>Corpus search: mhla/pre1900-corpus</h1>",
         f"<p class='muted'>revision {esc(revision)} &middot; {len(shards)} shards, {total_bytes / 1e9:.1f} GB &middot; "
         f"{docs:,} documents, years {summary['year_min']} to {summary['year_max']} &middot; {elapsed / 60:.1f} min</p>",
         f"<div class='card'><b>Documents with year &ge; 1900: {post1900}</b>"
         + ("" if not post1900 else "<ul>" + "".join(f"<li>{s['year']} &middot; {esc(s['title'])} &middot; {esc(s['source'])}: {esc(s['head'])}</li>" for s in post1900_samples) + "</ul>")
         + "</div>",
         "<h2>Terms</h2><table><tr><th>term</th><th>why it is here</th><th class='num'>documents</th><th class='num'>share</th><th class='num'>latest year</th><th>by decade</th></tr>"]
    for t, m in merged.items():
        dec = " ".join(f"{d}s:{c}" for d, c in m["by_decade"].items())
        p.append(f"<tr><td><b>{esc(t)}</b></td><td class='muted'>{esc(m['why'])}</td><td class='num'>{m['docs']:,}</td>"
                 f"<td class='num'>{100 * (m['share'] or 0):.3f}%</td><td class='num'>{esc(m['latest_year'])}</td><td class='muted'>{esc(dec)}</td></tr>")
    p.append("</table><h2>Snippets</h2><p class='muted'>Up to six per term, first found. Whole-word, case-insensitive.</p>")
    for t, m in merged.items():
        p.append(f"<div class='card'><h3>{esc(t)} <span class='muted'>({m['docs']:,} documents)</span></h3>")
        pat = build_patterns([t])[t]
        for s in m["snippets"]:
            marked = pat.sub(lambda mo: f"<mark>{esc(mo.group(0))}</mark>", esc(s["text"]))
            p.append(f"<div class='snip'><span class='muted'>{esc(s['year'])} &middot; {esc(s['title'])} &middot; {esc(s['source'])}</span><br>&hellip;{marked}&hellip;</div>")
        if not m["snippets"]:
            p.append("<p class='muted'>no matches</p>")
        p.append("</div>")
    p.append("</body></html>")
    with open(args.html, "w") as f:
        f.write("\n".join(p))
    print(f"wrote {args.out}\nwrote {args.html}")


if __name__ == "__main__":
    main()

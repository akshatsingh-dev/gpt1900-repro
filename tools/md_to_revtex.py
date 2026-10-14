"""
Convert reports/paper-full-draft.md into a REVTeX 4.2 project for Overleaf.

Handles exactly the constructs that file uses: numbered headings, paragraphs,
"**Table N.** caption" followed by a pipe table, "> **Figure N (placeholder).**"
quotes, bracketed citations [N] with a "## References" list, inline code,
bold, italic, bullet and numbered lists, [CHECK] marks, and the HTML comments
that carry each number's notebook entry (kept as LaTeX comments after the
paragraph, invisible in the PDF).

    python tools/md_to_revtex.py reports/paper-full-draft.md reports/overleaf/gpt1900-paper
"""

import os
import re
import sys
import zipfile

SPECIAL = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
           "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
UNICODE = {"\u2264": r"$\leq$", "\u2265": r"$\geq$", "\u00d7": r"$\times$", "\u2248": r"$\approx$",
           "\u2212": "-", "\u2019": "'", "\u2018": "'", "\u201c": "``", "\u201d": "''", "\u00a0": "~",
           "\u2026": r"\ldots{}", "\u00b0": r"$^{\circ}$"}


def esc(s):
    out = []
    for ch in s:
        if ch in SPECIAL:
            out.append(SPECIAL[ch])
        elif ch in UNICODE:
            out.append(UNICODE[ch])
        else:
            out.append(ch)
    return "".join(out)


def inline(s, comments):
    """Escape text and convert inline markdown. Pulls HTML comments out into `comments`."""
    for m in re.finditer(r"<!--\s*(.*?)\s*-->", s):
        comments.append(m.group(1))
    s = re.sub(r"\s*<!--.*?-->", "", s)
    parts = re.split(r"(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|\[CHECK[^\]]*\]|\[\d+(?:,\s*\d+)*\])", s)
    out = []
    for p in parts:
        if not p:
            continue
        if p.startswith("`") and p.endswith("`"):
            out.append(r"\texttt{" + esc(p[1:-1]) + "}")
        elif p.startswith("**") and p.endswith("**"):
            out.append(r"\textbf{" + esc(p[2:-2]) + "}")
        elif p.startswith("*") and p.endswith("*") and len(p) > 2:
            out.append(r"\emph{" + esc(p[1:-1]) + "}")
        elif p.startswith("[CHECK"):
            out.append(r"\textbf{\textcolor{red}{" + esc(p) + "}}")
        elif re.fullmatch(r"\[\d+(?:,\s*\d+)*\]", p):
            keys = ",".join("ref" + k.strip() for k in p[1:-1].split(","))
            out.append(r"\cite{" + keys + "}")
        else:
            out.append(esc(p))
    return "".join(out)


def table_block(caption, rows, comments):
    header = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    body = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows[2:]]
    ncol = len(header)
    env = "table*" if ncol > 2 or max(len(" ".join(r)) for r in [header] + body) > 70 else "table"
    spec = "l" * ncol
    out = [f"\\begin{{{env}}}[t]", f"\\caption{{{inline(caption, comments)}}}",
           "\\begin{ruledtabular}", f"\\begin{{tabular}}{{{spec}}}",
           " & ".join(inline(c, comments) for c in header) + r" \\", r"\hline"]
    for r in body:
        r = (r + [""] * ncol)[:ncol]
        out.append(" & ".join(inline(c, comments) for c in r) + r" \\")
    out += ["\\end{tabular}", "\\end{ruledtabular}", f"\\end{{{env}}}", ""]
    return out


def figure_block(text, comments):
    m = re.match(r"\*\*Figure (\d+) \(placeholder\)\.\*\*\s*(.*)", text)
    n, cap = (m.group(1), m.group(2)) if m else ("?", text)
    return ["\\begin{figure}[t]", "\\centering",
            "\\fbox{\\parbox{0.92\\columnwidth}{\\centering\\vspace{2.2cm}Figure " + n + " placeholder\\vspace{2.2cm}}}",
            f"\\caption{{{inline(cap, comments)}}}", f"\\label{{fig:{n}}}", "\\end{figure}", ""]


def convert(md):
    lines = md.splitlines()
    title = None; authors = None; abstract = []; body = []; refs = []
    mode = "front"; para = []; comments = []; list_env = None; pending_table_caption = None; table_rows = []

    def flush_para():
        nonlocal para, comments
        if para:
            text = " ".join(x.strip() for x in para)
            target = abstract if mode == "abstract" else body
            target.append(inline(text, comments))
            if comments and mode != "abstract":
                target.append("% sources: " + "; ".join(comments))
            target.append("")
        para = []; comments = []

    def close_list():
        nonlocal list_env
        if list_env:
            body.append(f"\\end{{{list_env}}}"); body.append(""); list_env = None

    def flush_table():
        nonlocal table_rows, pending_table_caption
        if table_rows:
            body.extend(table_block(pending_table_caption or "", table_rows, comments))
            table_rows = []; pending_table_caption = None

    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("# ") and title is None:
            title = ln[2:].strip(); i += 1; continue
        if mode == "front" and ln.startswith("**") and authors is None:
            authors = ln.strip("* ").strip(); i += 1; continue
        if mode == "front" and ln.strip() and not ln.startswith("#"):
            i += 1; continue                      # the draft's own preamble note
        if ln.startswith("## References"):
            flush_para(); close_list(); flush_table(); mode = "refs"; i += 1; continue
        if mode == "refs":
            m = re.match(r"\[(\d+)\]\s*(.*)", ln.strip())
            if m:
                refs.append((m.group(1), m.group(2)))
            elif ln.strip() and refs:
                refs[-1] = (refs[-1][0], refs[-1][1] + " " + ln.strip())
            i += 1; continue
        if ln.startswith("## Abstract"):
            flush_para(); mode = "abstract"; i += 1; continue
        if ln.startswith("## "):
            flush_para(); close_list(); flush_table(); mode = "body"
            body.append("\\section{" + inline(re.sub(r"^\d+\.\s*", "", ln[3:].strip()), []) + "}"); body.append(""); i += 1; continue
        if ln.startswith("### "):
            flush_para(); close_list(); flush_table()
            body.append("\\subsection{" + inline(re.sub(r"^\d+\.\d+\s*", "", ln[4:].strip()), []) + "}"); body.append(""); i += 1; continue
        if ln.startswith("#### "):
            flush_para(); close_list(); flush_table()
            body.append("\\subsubsection{" + inline(ln[5:].strip(), []) + "}"); body.append(""); i += 1; continue
        if re.match(r"\*\*Table \d+\.\*\*", ln.strip()):
            flush_para(); close_list()
            pending_table_caption = re.sub(r"^\*\*Table \d+\.\*\*\s*", "", ln.strip()); i += 1; continue
        if ln.startswith("|"):
            flush_para(); close_list(); table_rows.append(ln); i += 1; continue
        if table_rows and not ln.startswith("|"):
            flush_table()
        if ln.startswith("> "):
            flush_para(); close_list(); body.extend(figure_block(ln[2:].strip(), comments)); comments = []; i += 1; continue
        m_b = re.match(r"^[-*]\s+(.*)", ln); m_n = re.match(r"^\d+\.\s+(.*)", ln)
        if m_b or m_n:
            flush_para()
            env = "itemize" if m_b else "enumerate"
            if list_env != env:
                close_list(); body.append(f"\\begin{{{env}}}"); list_env = env
            c = []; body.append("\\item " + inline((m_b or m_n).group(1), c))
            if c: body.append("% sources: " + "; ".join(c))
            i += 1; continue
        if ln.strip() == "":
            flush_para(); close_list(); flush_table(); i += 1; continue
        para.append(ln); i += 1
    flush_para(); close_list(); flush_table()

    tex = []
    tex.append(r"""\documentclass[reprint,prx,amsmath,amssymb,aps,superscriptaddress]{revtex4-2}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\usepackage{url}
\begin{document}
""")
    tex.append("\\title{" + inline(title or "", []) + "}")
    tex.append("\\author{Akshat Singh}\n\\affiliation{University of California San Diego}")
    tex.append("\\author{Brian Keating}\n\\affiliation{University of California San Diego}")
    tex.append("\\date{\\today}\n")
    tex.append("\\begin{abstract}")
    tex.extend(abstract)
    tex.append("\\end{abstract}\n\n\\maketitle\n")
    tex.extend(body)
    tex.append("\\begin{thebibliography}{99}")
    for n, text in refs:
        tex.append(f"\\bibitem{{ref{n}}} " + inline(text, []))
    tex.append("\\end{thebibliography}\n\\end{document}")
    return "\n".join(tex), len(refs)


def main():
    src, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    tex, nref = convert(open(src).read())
    open(os.path.join(outdir, "main.tex"), "w").write(tex)
    open(os.path.join(outdir, "README.txt"), "w").write(
        "GPT-1900 reproducibility paper, REVTeX 4.2 project.\n\n"
        "Upload to Overleaf: New Project > Upload Project > choose the zip. Then Recompile.\n"
        "main.tex is the whole paper. Red [CHECK] marks are sentences that need an author's word.\n"
        "Figures are placeholder boxes; drop PNGs into a figures/ folder and replace the \\fbox lines with \\includegraphics.\n"
        "Lines beginning '% sources:' name the lab notebook entry behind each paragraph's numbers; they do not print.\n"
        f"Generated from {os.path.basename(src)} by tools/md_to_revtex.py.\n")
    zpath = outdir.rstrip("/") + ".zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(outdir, "main.tex"), "main.tex")
        z.write(os.path.join(outdir, "README.txt"), "README.txt")
    print(f"wrote {outdir}/main.tex ({tex.count(chr(10))} lines, {nref} references) and {zpath}")


if __name__ == "__main__":
    main()

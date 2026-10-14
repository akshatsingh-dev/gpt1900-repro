# PRX Intelligence briefing

Akshat Singh, 7 Oct 2026. A working guide to the journal Keating named as the target, what a submission there needs, how the GPT-1900 reproducibility work fits, the fallbacks, and what a first paper feels like. Every factual claim carries a source number that points to the Sources section at the end. Where a page could not be checked today, the line says "unverified". Pages were read on 7 Oct 2026 unless the entry says otherwise. This note extends `reports/journal-recon.md` (28 Sep) and does not repeat the per-paper structure survey there.

The one-paragraph version. PRX Intelligence is the American Physical Society's newest journal, announced 19 Nov 2025, open for submissions since Feb 2026, first papers out 28 Jul 2026. It is fully open access and the publication charge is zero for anything submitted before 1 Jan 2027. It has no impact factor and cannot have one for years, so its standing rests entirely on the PRX name and the editor list. A PDF is all that is needed to be reviewed. The paper needs a Data Availability Statement, an AI-use disclosure, a cover letter, and ideally a CRediT contribution paragraph. Our work is a good match for the journal's "exceptional insight" criterion and for its own editorial, which names benchmark leaderboards and Goodhart's law as a problem. The weak points a referee will go for first are the provisional grader and the absence of human grading, and both are fixable before December.

---

## 1. What PRX Intelligence is

### 1.1 The facts

| Item | What the APS pages say | Source |
|---|---|---|
| Publisher | American Physical Society (APS) | [1] |
| Announced | 19 Nov 2025, APS press release | [5], [6] |
| Call for papers | 18 Feb 2026; submissions began Feb 2026 | [6], [5] |
| First papers | 28 Jul 2026, six research papers plus an editorial | [7], [6] |
| Mission | "a highly selective, fully open access journal for impactful research in artificial intelligence and machine learning (AI/ML) that advances the physical sciences and related fields" | [1] |
| Access | Fully open access, CC BY 4.0, authors keep copyright | [1], [3] |
| Publication charge | "$0 - Introductory promotion, no APCs through the end of 2026". Home page: "APC waived for all submissions and transfers received before 01 Jan 2027". After that, standard APS rates apply (PRX is $4,685 in 2026, PRX Quantum $3,590, PRX Energy and PRX Life $3,105). Authors in lower-income countries are always waived. | [21], [8], [3], [7] |
| Metrics | "Some metrics are not yet available for PRX Intelligence... due to their recent launch". No impact factor, no CiteScore. | [12], [8] |
| ISSN | 3070-0329 (online), recorded in journal-recon on 28 Sep; not re-checked today | [recon] |

### 1.2 Scope, quoted

The scope page opens: "PRX Intelligence welcomes manuscripts on AI/ML methods as well as their use across the physical sciences and related fields." It then lists five groups. [2]

AI/ML methods for science: "physics-informed learning, surrogate and hybrid models, generative models for scientific data, probabilistic modeling, uncertainty quantification, interpretability and reliability, causal and mechanistic machine learning, reinforcement learning for design and control, scientific agents and automation, AI based optimization, statistical learning applied to experimental planning and system engineering."

Data, simulation, and modeling: "multimodal experimental, simulated, or synthetic datasets, meta data assimilation and curation from literature, scientific workload, cost and timing data."

Domain applications: "condensed-matter and materials, discovery and synthesis, soft matter and fluids, plasma and fusion, atomic/molecular/optical physics, high-energy and nuclear physics, astrophysics and cosmology, geophysics and climate, energy systems and devices, imaging and sensing (including microscopy and tomography)."

Systems, tools, and instrumentation: "ML-enabled experimental design and control, robotics for laboratories, adaptive/streaming analyses at facilities, edge/embedded ML for instruments, ML pipelines integrated with experimental or observational platforms, high-performance computing."

Emerging areas: "quantum-aware/quantum-enhanced ML and ML for quantum systems, ML-guided theorem proving and scientific reasoning, trustworthy and robust and safety-aware ML for scientific deployment, agentic and robotic AI."

Our paper sits in the last group under "scientific reasoning" and "trustworthy and robust and safety-aware ML", and in the first group under "interpretability and reliability". It is not a domain application paper and should not be framed as one.

### 1.3 Acceptance criteria, quoted

The About page says manuscripts "should address relevant questions, report sufficient or state-of-the-art validation, and demonstrate exceptional achievement in at least one of the following dimensions" and then lists four. [1]

- "Exceptional advance: Introducing AI/ML concepts, results, or systems that open new and consequential directions for scientific discovery or understanding."
- "Exceptional connection: Bridging AI/ML with disparate areas of science or engineering, or unifying previously separate approaches to enable new capabilities."
- "Exceptional capabilities: Delivering tools, techniques, datasets, software, or platforms that unlock progress on major challenges (e.g., scale, interpretability, reliability, efficiency)."
- "Exceptional insight: Providing clear, generalizable understanding of AI/ML behavior or scientific phenomena with high relevance across multiple communities."

The same four headings appear on the PRX Quantum, PRX Energy and PRX Life About pages, each defined relative to that journal's field. [14], [15], [16]

### 1.4 The editorial team

From the journal's staff page. [4]

| Role | Name, affiliation |
|---|---|
| Chief Editor | Anatole von Lilienfeld, University of Toronto and Vector Institute, Canada |
| Deputy Editors | Ann B. Lee, Carnegie Mellon; Nicola Marzari, EPFL and Paul Scherrer Institut; Benjamin Nachman, Stanford and SLAC |
| Associate Editors | Michele Ceriotti, EPFL; Mario Krenn, University of Tübingen; Mariel Pettee, University of Wisconsin-Madison |
| APS staff | Kyle Welch, Managing Editor; Marie Rupolo, Assistant Editor |
| Editorial Board | Viviana Acquaviva (CUNY), Xavier Bresson (NUS), Giuseppe Carleo (EPFL), Luca M. Ghiringhelli (KIT), Sebastian Goldt (SISSA), Ganna Gryn'ova (Birmingham), Eun-Ah Kim (Cornell), Klaus-Robert Müller (TU Berlin and Korea University), William Ratcliff II (NIST), Jesse Thaler (MIT), Alexandre Tkatchenko (Luxembourg), Risa Wechsler (Stanford) |

The press release of Nov 2025 listed Marzari at Cambridge and Nachman as associate professor at Stanford; the staff page is the current list. [5], [4]

Two things in the editorial matter for us. The Chief Editor, interviewed in APS News, said the goal is to "identify studies that truly represent a major new insight or advancement in the field, and to relate those advances to physics", and that "the focus will be on improving the quality of the content, rather than fighting to get published". [9] The editors' own editorial (received 17 Jul 2026, published 28 Jul 2026) says research papers should include "rigorous validation against strong baselines and null models, a clear discussion of limitations and out-of-distribution behavior, and, wherever feasible, open availability of data and code", and it invokes Goodhart's law against "incremental gains on benchmark leaderboards". Those sentences were checked against the PDF on 28 Sep (journal-recon section 1); today only the abstract page could be opened, which confirms the title, authors and dates. [10], [11]

### 1.5 How it relates to the rest of the Physical Review family

| Journal | First issue | Model | 2025 impact factor | 2026 APC | What it is for |
|---|---|---|---|---|---|
| Physical Review Letters (PRL) | 1958 | Hybrid, subscription or paid OA | 9.4 | $4,140 for OA | Short Letters, 3,750 words, "of unusual intrinsic interest to PRL's broad audience" | 
| Physical Review X (PRX) | 2011 | Fully OA | 16.8 | $4,685 | "the world's leading open access journal for cutting-edge research across physics and adjacent fields" |
| Physical Review Research (PRR) | 2019 | Fully OA | 4.0 | $2,910 | Broad, sound work; papers should "Add to the existing knowledge related to a particular field of research with a connection to physics" |
| PRX Quantum | 2020 | Fully OA | 12.3 | $3,590 | Quantum information science and technology |
| PRX Energy | 2022 | Fully OA | none yet; CiteScore 7.5 | $3,105 | Energy science and technology |
| PRX Life | 2023 | Fully OA | none yet; CiteScore 3.1 | $3,105 | Biological physics |
| PRX Intelligence | 2026 | Fully OA | none yet | $0 through 31 Dec 2026 | AI/ML that advances the physical sciences |

Sources: first issues [20]; metrics [12], [13]; APCs [21]; descriptions [17], [18], [19], [14], [15], [16], [1]; PRL word limit [25].

The pattern: APS launched PRX in 2011 as its selective open access flagship, then used the PRX name for a set of field-specific selective journals (Quantum 2020, Energy 2022, Life 2023, Intelligence 2026). Each carries the same four "exceptional" criteria and the same "highly selective" language. PRR, launched 2019, is the broad, lower-bar open access title and is the natural place a rejected PRX-family paper gets offered a transfer to. APS editorial policy lists "Rejection with Offer to Transfer to Another APS Journal" as a standard decision. [23]

### 1.6 Prestige, honestly

What is verified:

- PRX itself is strong by every number APS publishes. 2025 impact factor 16.8, CiteScore 23.2, and APS says it "again leads all open access titles as ranked by total citations (40,187), impact factor (16.8), journal citation indicator (4.01), immediacy index (4.1), and article influence score (5.968)". [12], [13]
- PRX Quantum reached 12.3 in its fifth year. PRX Energy and PRX Life, three and four years in, have no impact factor yet. [12]
- PRL, the journal most physicists think of as the prestige venue, has a 2025 impact factor of 9.4, lower than PRX. Impact factor and prestige are not the same thing; PRL's standing comes from sixty-plus years of history and a much larger volume. [12], [20]
- PRX Intelligence has no metrics at all. [12], [8]

What is not verified, and what is my reading:

- APS does not publish acceptance rates for PRX or PRX Intelligence. A search of aps.org found none. An old arXiv paper on PRL seasonal bias puts PRL at roughly a quarter of submissions; that is a secondary source and is not an APS figure. Treat all acceptance-rate numbers as unverified. [31]
- An impact factor for a given year counts citations in that year to papers from the two years before. A journal whose first papers appeared in mid-2026 cannot have a meaningful figure before the 2028 reports, released in 2029. This is arithmetic from the standard definition, not a statement from any APS page; unverified against Clarivate.
- How physicists read "PRX Intelligence" on a CV today: the name buys the reader's assumption that it was selected by PRX-grade editors, and the editor list (Marzari, Thaler, Carleo, Müller, Wechsler, Tkatchenko) is one that physicists in ML-adjacent fields recognise. For someone outside that overlap the title is unfamiliar and will be read as "a new APS journal". For an undergraduate, any first-author APS paper is a real line; the specific journal's weight will be settled by its first few years of papers, not by anything we can control. This paragraph is interpretation.
- Because the journal is new and the first volume is thin (24 items as of late Sep), a paper there will be more visible inside the journal than it would be in PRX or PRL, and the editors have a direct interest in publishing work that defines what the journal is for. That cuts in our favour if the paper is rigorous and against us if it is not, because an early flawed paper is a reputational problem for them.

---

## 2. What a submission requires

### 2.1 Article types

From the journal's Information for Authors page. [3]

| Type | Length limit | Note |
|---|---|---|
| Research Articles (called "Regular Articles" in the description) | none | "original research articles that meet PRX Intelligence's editorial criteria and scope" |
| Data/Code papers | none | Data papers: Motivation, Description, Analysis, Conclusion. Code papers must report "a substantial technical advance within the topical scope" |
| Perspectives | 7,500 words | generally invited |
| Reviews | 30,000 words | generally invited, developments of the past 2 to 5 years |
| Tutorials | none | generally invited |
| Roadmaps | none | generally invited |
| Comments and Replies | 3,500 words | on papers already in the journal |
| Erratum | not stated | corrections |

The general APS length guide does not list PRX Intelligence, so the Authors page is the only authority. [25] Our paper is a Research Article. A separate Data/Code paper for the record schema is possible (recon section 8) but is a decision for after the main paper is accepted, not before.

### 2.2 Manuscript format

- For review: "A PDF version of your paper is all that's needed for it to be sent for peer review." The general APS guideline: "We only require a PDF file for a new submission and resubmissions. For PDF submissions, all textual material and figures should be in a single file." Source files are requested at acceptance. [3], [22]
- At acceptance: "Text files should be formatted in REVTeX (preferred) or LaTeX." Word "is also acceptable; although their use is extremely limited in the production process." [22]
- REVTeX version: 4.2f, released 30 May 2023. The journal substyle options listed on the REVTeX page are prl, pra, prb, prc, prd, pre, prx, prab, prapplied, prfluids, prmaterials, prper and a generic physrev, plus AIP options. There is no prxintelligence, prxquantum, prxenergy or prxlife option and the page gives no instruction for those journals. [26]
- Practical choice: write in `revtex4-2` with the `prx` option, two-column `reprint` mode for the submitted PDF, for example `\documentclass[prx,reprint,amsmath,amssymb,superscriptaddress]{revtex4-2}`. That `prx` is the right choice for PRX Intelligence is my inference from the option list, not an instruction on any APS page; unverified. The journal's Authors page says LaTeX source "simplifies peer-review", so a REVTeX PDF from the start costs nothing. [3]
- Supplemental Material goes in as a separate PDF, cited as a reference in the main text, and "A paper must stand on its own and be understandable and convincing without Supplemental Material." [22], [3]
- Audience: "Your manuscript should be written for a broad scientific readership" and should "avoid unnecessary field-specific jargon and unexplained acronyms." No Popular Summary is required, unlike PRX. [3], [17]

### 2.3 Title, abstract, sections

From the APS Style Basics page. [27]

- Title: "self-contained, concise, and informative, clearly stating the main findings." No new terminology, no brand names, no quality words.
- Abstract: one paragraph, "completely self-contained", "about 5% of the article and less than 500 words", no reference numbers, no displayed equations or tables. For a 12 to 16 page paper that means roughly 200 to 300 words.
- Sections: APS uses numbered sections. The published PRX Intelligence papers run Introduction, Results (one or several topical sections), Discussion or Conclusion, Methods, Acknowledgments, Data Availability (recon section 6).

### 2.4 Figures and tables

- Number figures with Arabic numerals and tables with Roman numerals, each with a caption that summarises its contents. [27]
- Smallest capital letters and numerals at least 2 mm high at final size; data points at least 1 mm across. [27]
- File formats and resolution: older APS "information for contributors" pages give .ps, .eps, .jpg and .png as the preferred formats, 600 dpi or higher for line art, and figures sized to one column (8.5 cm) or two. These came from a search of journals.aps.org and were not re-read in full today; partially verified. [28]
- Colour online is free. Also from the older contributor pages; partially verified. [28]
- AI-generated or AI-modified images are not allowed; plots drawn by code the authors verified are fine (section 2.8).

### 2.5 References

Numbered consecutively in order of first citation, cited in the text as numerals in square brackets. [27] Shared data and software must appear in the reference list with a DOI and that citation must be repeated inside the Data Availability Statement. [24] The full APS Style Guide for Authors (Nov 2024) is a PDF linked from the Style Basics page; it did not render in the tool used today, so its reference examples are not quoted here. [27]

### 2.6 Data Availability Statement

Required. "All published articles must include a Data Availability Statement (DAS)." The requirement applies to everything submitted on or after 11 Dec 2024. The statement "should describe clearly and concisely how the data and/or software used in your research can be accessed, including references." Software and code count as data. If data cannot be made public, "authors must agree to share data privately with editors, reviewers, and readers upon reasonable request" and the reason is published. Stock wording APS offers includes "The data that support the findings of this article are publicly available [1,2]." [24], [23]

For us: deposit the JSONL records, the schema, the graded files and the blinded packets in a DOI-issuing repository (Zenodo or figshare match what published PRX Intelligence authors used), put the tools on GitHub, cite both in the reference list, and write the statement around those citations. "Available on request" would be self-undermining in a reproducibility paper.

### 2.7 Authorship, contributions, competing interests

- Who is an author: "All individuals who contributed significantly to at least one of the following aspects of the reported results should be listed as authors: Concept, Design, Execution, Interpretation, Write-up." Others go in Acknowledgments. "All authors are accountable for the work presented in the paper." [23]
- The corresponding author certifies that the work is original, that all listed authors contributed meaningfully, that everyone who qualified was offered authorship, and that all authors agreed to submit. [23]
- Contribution statement: "APS strongly encourages authors to outline their contributor roles using the CRediT taxonomy." It goes in "a separate paragraph after the Acknowledgment section", for example "A.Z. and B.Y. conceptualized the work; C.X. conducted the experiments." Encouraged, not mandatory. [23], [27], [32]
- Competing interests: "Authors should alert editors to any potential conflict of interest such as sources of funding, condition of employment, and any limitations on disclosure of data, code, or experimental details." Authors "are encouraged to declare any conflict of interest within the paper itself using a Conflict of Interest statement." [23]
- Reproducibility policy, which is also our subject: "A scientific article should include all relevant details a fellow researcher of reasonable skill would need to reproduce the work and verify the results." [23]

### 2.8 APS policy on AI tools

APS released an updated policy on 17 Jun 2026. [30] The policy page and its FAQ say: [29], [30]

- "An AI program cannot be held accountable and cannot be listed as an author."
- "Authors are fully responsible for accuracy and must review and refine all AI-generated content."
- "Authors must keep a record of any AI use and disclose any substantive uses in the submitted paper." A disclosure states the "AI tool name and version", "How the AI assisted", and "How the authors directed and verified the AI output."
- Substantive use "includes, but is not limited to, assistance with: Scientific reasoning or interpretation / Drafting or revising scientific claims, conclusions, or explanations / Literature synthesis beyond routine organization / Figure generation or image analysis / Derivations or calculations / Code generation or debugging that materially affects results / Simulations or numerical analysis / Data analysis or statistical analysis".
- Placement: "Any AI use for figure generation should be mentioned in the figure caption. Any AI use in conducting research should be described where other methods are listed. All other uses worth disclosing should be in the Acknowledgment statement."
- Exempt: "Authors are not required to disclose the use of AI to polish, condense, or otherwise lightly edit the text."
- Peer review: the policy "prohibits authors and reviewers from sharing peer review materials with unrestricted AI tools". [30]

What this means for the paper. The LLM grader is a research instrument, so it is disclosed in Methods with model name and version, the exact prompt and rubric, the temperature, the blinding procedure and the regrade and human checks used to verify it. The provisional grader (D008) is disclosed the same way, with its version string. Any substantive drafting or analysis help goes in the Acknowledgments in the form the editors used in their own editorial, which names the tools and ends with a sentence taking full responsibility (recon section 1). The Style Basics page explicitly lists "use of AI in the writing" as something the Acknowledgments may record. [27]

### 2.9 Cover letter and suggested referees

- The journal's Authors page says the cover letter should include "Context of the results, Summary of key findings, Relevant submission history at Physical Review" and "Any recommended or excluded referees". Joint submissions and transfers are also flagged there. [3]
- PRX's own guide adds: "Prepare a letter of submission (i.e. cover letter), including any confidential remarks to the editors." [33]
- Referees: "Authors are encouraged to suggest suitable reviewers. They may also inform editors of experts who have a potential conflict of interest and who might provide a biased recommendation. However, the editors are not bound by these suggestions". The tips page: include "a list of possible referees who are experts on the subject matter and not your close colleagues" and "consider including younger individuals who, while possibly less well known, are sufficiently knowledgeable to be effective referees." [23], [34]

For us, the natural referee pool is people who have published on LLM-as-judge reliability, benchmark contamination, or physics reasoning benchmarks, and who are not Keating's collaborators. Three to five names, with one line each on why.

### 2.10 Where and how to submit

- Portal: all submissions go through the APS submission server at https://authors.aps.org/Submissions/login/new. One account; the corresponding author creates it. [22], [35]
- Upload: one PDF marked "Main text incl. Figures", a separate Supplemental Material PDF, the cover letter, the Data Availability Statement typed into a form field, and the referee suggestions. [22], [24]
- Preprints: APS allows posting to "free-access e-print servers (repositories, including institutional and subject specific such as the arXiv)" and asks authors to disclose "the e-print number of a manuscript deposited on a preprint server" at submission. [23]
- Deadline that matters: submit before 1 Jan 2027 for the zero APC. [8], [3]

### 2.11 Timeline and what a desk reject looks like

- Editors screen first. APS policy: "The editors may conclude that a submitted, resubmitted, or transferred manuscript is unlikely to move further in the review process on the basis of the journal's criteria and can issue a rejection without external review". PRX Intelligence says "We make timely, transparent decisions on which papers proceed to review." [23], [1]
- If sent to referees: "the editors select a number of experts in the research area and ask for an advisory opinion". "Editors generally offer up to two rounds of review". Decisions are "Offer to Resubmit", "Rejection with Offer to Transfer to Another APS Journal", or "Rejection without an Offer to Transfer". An appeal "is not an additional round of peer review". [23]
- PRX Intelligence's measured turnaround so far, from the two published papers checked today: received 26 Mar 2026, accepted 15 Jul, published 13 Aug; received 25 Mar 2026, accepted 15 Jul, published 20 Aug. That is about 16 weeks to acceptance and 4 to 5 weeks more to publication. Two data points. [36]
- PRL's published statistics give a sense of APS norms: first decision before review 7 days, first decision after review 54 days, submission to acceptance 179 days, submission to publication 212 days. [19]
- A desk reject at an APS journal is a short letter from the handling editor, usually within one to two weeks, saying the manuscript does not meet the journal's criteria for importance or breadth, often with one or two sentences of reasoning and frequently with an offer to transfer the files to PRR or another APS journal without resubmitting. The two-week figure and the tone are from experience reports and the PRL statistic, not from a PRX Intelligence page; unverified for this journal specifically. The transfer offer is a documented decision type. [23]

---

## 3. How this project fits

### 3.1 What is strong

Read from `reports/reproducibility-memo.md` (22 Sep) and `reports/paper-draft.md` (28 Sep).

1. A measured reproducibility result with denominators. The published archive records three fields per answer and no seed, which is why the authors' own repeats agreed on 2 of 120 answers. With seed and sample count recorded, generation is 8 of 8 identical on one machine at both temperature 0 and the authors' sampled settings, and 0 of 8 across machines, with each machine self-consistent. A fresh 192-answer sweep lands within 0.01 of the published answers under one grader (1.27 vs 1.26). This is the kind of "what a record must contain" finding the APS reproducibility policy describes in the abstract and almost nobody measures.
2. A grader-sensitivity finding. The same 192 published answers under two graders: 0.93 published, 1.26 under ours, 119 of 192 exact, 188 within one point. The +0.33 shift is larger than the prompt effect and comparable to the whole training gain. That is a direct instance of the editorial's Goodhart sentence and is the headline.
3. A prompt-sensitivity finding with a clean design. Three wordings, three seeds, matched judge fields, n=72 per condition: a one-paragraph hint moves the mean +0.28, with non-overlapping intervals, and the authors' own comparison is shown to be unmatched.
4. The two general-relativity tasks as a worked example. On the 1911 consequence the hint is worth +0.89 (n=72, CI +0.69 to +1.08); on the 1907 seed it is worth +0.00 (CI -0.12 to +0.12); given only the observation, 0 of 144 answers supply the equivalence. This is the part a physicist referee will read first and it is the part that connects the paper to physics rather than to ML evaluation in general.
5. A corpus audit with a real finding. 2,074,160 documents, 0 dated after 1899, every post-1900 term at zero, and one misdated 1909 document found by its content. The honest framing that the zero is a lower bound is already in the memo.
6. A full record-keeping pipeline. 50 fields per generation, one sample per call, a comparison tool that refuses to compare mismatched settings, null for judge failures, every number traceable to a notebook entry and a log. This supports the "exceptional capabilities" criterion as a secondary claim.

### 3.2 What reviewers will attack

In the order I expect them to raise it.

1. The provisional grader is not the paper's judge. Every score in the memo comes from a blinded reader that is not the upstream judge model, labelled provisional. A referee will say the grader comparison is confounded: a different model, a different session structure, no temperature pinned. The memo already says the API pass is 20 minutes and under $3. Until it is done the headline number is provisional and the paper cannot be submitted.
2. No human grading. The paper's claim is that the LLM grader is the largest source of variance, but which grader is closer to a physicist is untested (memo section 9, draft section 6). Without human scores on a blinded sample the referee can say both graders are wrong and the comparison is noise against noise.
3. One model. GPT-1900 is a single 3.29B artefact from one group. Any claim about "LLM-judged benchmarks" in general rests on one benchmark and one model family as judge.
4. Eight tasks. Per-task effects (elevator +0.89, UV catastrophe -0.33) are from n=9 per cell in the sensitivity run and n=72 only for the two GR tasks. A referee will ask why the other six were not run at n=72 and will treat the per-task ranking as suggestive.
5. Small n per cell in the sweep. The 192-answer sweep is one sample per checkpoint per task. Per-checkpoint means and the 0.71 rank correlation are from eight answers per checkpoint.
6. Lexical corpus search only. Fifteen terms and a date field. The memo says so. A referee from the contamination literature will ask for n-gram overlap against the prompts and rubrics at minimum.
7. Pipeline written and run by one undergraduate. The question will be whether anyone else has run it. Right now the answer is no.
8. Mode confound in the base-vs-RL comparisons (draft 4.5). Already flagged; keep it flagged.
9. Framing risk. If the paper reads as a critique of a named group's unpublished-checkpoint practice, referees may read it as adversarial. The memo's tone (their pipeline was fine, the record was thin, same-machine reproduction works) is the right one and must survive into the draft.

### 3.3 What has to be added before submission, in order

Ordered by how much review risk each removes per hour of work. The first five are the minimum. The APC waiver ends 31 Dec 2026, which is twelve weeks from today.

1. Run the upstream judge. `claude-sonnet-4-20250514` at temperature 0 on all 192 sweep answers, the 216 sensitivity answers, and the two 216-answer GR sets. Report both graders side by side. If the deprecated model is unreachable, run the nearest current model and say so. One API key, one afternoon. This turns "provisional" into a two-grader comparison and is the single biggest change.
2. Human grading on a blinded subsample. Two or three physicists, the existing packets, at least 96 answers covering all eight tasks and all three wordings, each answer graded by two humans. Report human-human agreement and human-vs-each-grader agreement as exact, within-one, and a chance-corrected statistic. This answers attack 2 and is the item that needs lead time, so it starts this week. Keating recruits the graders.
3. Null models, because the editorial asks for them by name. A random grader, a majority-class grader (score 1 for everything), and a length-based grader on the same answers, with their agreement to the published scores. Half a day of code.
4. Deposit and release. Zenodo DOI for records, schema, graded files and packets; GitHub for tools; both cited in the reference list and in the Data Availability Statement. Add the test suite for `logged_eval.py` and `compare_runs.py` that the upstream lacked.
5. AI disclosures written. Methods paragraph for both graders (name, version, prompt hash, temperature, blinding, verification). Acknowledgments sentence for any drafting or literature help, in the editors' own form.
6. Independent re-run. Someone other than me, from the public repo and a fresh environment, reproduces one table. One line in the paper, one name in the Acknowledgments, and attack 7 goes away.
7. Widen the sensitivity run. Three seeds on all 24 checkpoints for all eight tasks under all three wordings is 1,728 generations, about ten hours on one V100 at the measured rate. If Expanse time allows, it moves every per-task number to n=72 and removes attack 4. If not, say plainly that six tasks are at n=9 and treat them as exploratory.
8. Strengthen the contamination check. n-gram overlap (say 8-grams) between every prompt, rubric line and hint and the corpus, plus a search for the exact phrasing of the eight thought experiments. Report hits with context. This is a scan over 56 GB and a week of elapsed time on shared nodes.
9. A second judge family. One non-Claude grader (any open-weights instruct model that fits on the V100) on the 192 sweep answers. It costs little and lets the Discussion say the grader effect is not a quirk of one vendor. If it cannot be done, drop the generality claim and state the limit.
10. The writing. Introduction against the evidence table, Discussion with limitations and out-of-distribution behaviour named in those words, Methods with the field table, abstract under 300 words leading with the grader finding. Cover letter, three to five referees, CRediT paragraph, Conflict of Interest line.

Items 1 to 5 fit in six weeks if the API key and two graders exist by mid-October. Items 6 to 10 fill the remaining time. A submission in the second week of December is realistic; a submission with items 7 to 9 undone is still defensible if the limitations section says what was not done and why.

### 3.4 How to frame it for the criteria

Lead with "exceptional insight": a clear, generalizable understanding of how an LLM-judged scientific benchmark behaves under re-grading, re-prompting and re-running, measured with denominators. Second, "exceptional capabilities": the record schema and the comparison tool as reusable instruments. Do not claim "exceptional advance"; the paper does not introduce a new AI method. Quote the editorial's own sentences on benchmarks and null models back to the editors in the cover letter, briefly.

---

## 4. If PRX Intelligence declines

| Venue | Fit | Timeline and cost | Source |
|---|---|---|---|
| Physical Review Research (APS) | Good. Criteria are soundness and a connection to physics, not exceptional impact. Regular Articles have no length limit; Letters are 4,500 words. A transfer from PRX Intelligence keeps the files and usually the reports. | APS timescales, months. 2026 APC $2,910, 2025 impact factor 4.0. | [18], [21], [12], [23] |
| Physical Review Letters (APS) | Unlikely. 3,750-word cap with figures and tables counted as words; the evidence tables will not fit; the claim is methodological and must clear "unusual intrinsic interest to PRL's broad audience". | 179 days median to acceptance. Hybrid; $4,140 only if you want open access. Impact factor 9.4. | [19], [25], [21], [12] |
| Nature Machine Intelligence | Plausible on topic (ML and its impact on other disciplines) and very competitive. The paper would need to be reframed as a general finding about LLM judges, with the physics as the case. | Months; timeline unverified. Hybrid: subscription route costs nothing, gold OA APC is $12,850. | [37], [38] |
| Patterns (Cell Press) | Strong fit on values: "dedicated to promoting open, reproducible science" and papers "selected, in part, based on the openness and FAIRness of underlying data, code, and models". Data science across all fields. | Months; timeline unverified. Fully OA, APC $4,900. | [39], [40] |
| TMLR | Strong fit on content. Acceptance asks only "Are the claims made in the submission supported by accurate and convincing evidence?" and whether some of the audience would be interested; "novelty of the studied method is not a necessary criterion". There is a Reproducibility Certification "awarded to papers whose primary purpose is reproduction of other published work". No fees to publish or read. Low recognition among physicists. | Action editor assigned within a week; reviewers submit recommendations after at least two weeks of discussion once all three reviews are in; total typically two to three months (the total is unverified). | [41], [42], [43] |
| A NeurIPS or ICLR workshop | A fast, low-stakes first outing for the grader finding. NeurIPS 2026 workshop paper deadlines have passed (suggested 29 Aug 2026, notifications 29 Sep). ICLR 2027 workshops: suggested paper deadline 1 Feb 2027, notification by 26 Feb 2027, conference 26 to 30 Apr 2027 in California. Workshop papers are usually non-archival, so a journal version can follow; check the specific workshop's call. | Four to eight page paper; free or registration fee; no APC. | [44], [45], [46] |
| arXiv first | Compatible with every venue above. APS allows preprints and asks for the e-print number at submission. A first-time submitter needs endorsement; an institutional email and claimed co-authored papers can make it automatic, otherwise an established author in the category endorses. Keating can. Categories to consider: cs.CL or cs.LG with physics.hist-ph as a cross-list (my suggestion). | Same day as the journal submission is the usual practice. Free. | [23], [47] |

PRX Quantum was named as an alternative in September; recon section 7 explains why the fit is poor (the paper is not a quantum information result) and nothing found today changes that. [14]

---

## 5. Your first paper

### 5.1 What the process feels like

A paper is written three times: once as a draft you think is done, once after the professor has rewritten the framing, and once after the referees. Each pass is shorter than the one before. The stages, with the numbers that are verified and the ones that are typical ranges:

| Stage | Who | How long | Verified? |
|---|---|---|---|
| Full draft from the skeleton, figures, methods, supplement | You, with Keating on framing | 4 to 8 weeks | typical range, unverified |
| Internal review and rewrite | Keating edits, you revise | 1 to 3 weeks, often two passes | typical range, unverified |
| Deposit data and code, write the DAS, cover letter, referee list, CRediT | You draft, Keating approves | 1 week | typical range |
| Submission | Corresponding author, one sitting | 1 to 2 hours | [22] |
| Editor screening | Editor | PRL median 7 days to a first decision before review; expect one to two weeks | [19] |
| Referee reports | Two or three referees | PRL median 54 days to first decision after review; PRX Intelligence has taken about 16 weeks from receipt to acceptance including revision | [19], [36] |
| Your response and revision | You and Keating | 2 to 4 weeks; the response letter is a document in its own right | typical range |
| Second round, acceptance | Editor, sometimes referees again | "up to two rounds" | [23] |
| Proofs and publication | APS production, you check proofs | 4 to 5 weeks after acceptance at PRX Intelligence so far | [36] |

End to end, a December 2026 submission accepted on the first revision would publish around April or May 2027. A rejection with transfer to PRR restarts the referee clock but not the writing.

Things nobody tells you the first time. Referee reports are blunt and sometimes wrong; the response letter answers every point, quotes the referee, says what changed and where, and never argues tone. "Offer to Resubmit" is good news. An editor's letter that says the work "does not meet the criteria" within two weeks is a desk reject and is not a judgement on the quality of the work, only on fit. Keep the lab notebook going through review, because referees ask for numbers and the ones you can produce in a day are the ones that get the paper accepted.

### 5.2 What you do and what the professor does

Yours: every number, every figure, the Methods section, the supplement, the data deposit, the reproducibility of your own pipeline, the first full draft of Results, and the response-letter drafts. Keating's: the question the paper answers and why a physicist should care, the Introduction and Discussion framing, the title and abstract in their final form, the cover letter, the referee list, the correspondence with the editor, and the judgement calls about what to claim. In practice both of you edit everything; the division is about who holds the pen first.

Corresponding author: usually the senior author on a first student paper, because the editor's questions and the referee correspondence land there and because the corresponding author signs the certifications APS requires. [23] It can be the student if both agree; it is worth asking rather than assuming.

### 5.3 Authorship norms in physics for work like this

- The rule APS states: authorship for significant contribution to concept, design, execution, interpretation or write-up; everyone else in Acknowledgments; all authors accountable. [23]
- The convention in small physics collaborations: first author is the person who did most of the work, which here is you; last author is the senior person who directed it; anyone in between contributed specific pieces (for example, physicists who graded the packets may become authors or may be acknowledged, depending on how much they did; decide that with them before they start). Alphabetical order is used in large collaborations and some theory communities and would not apply here. These ordering conventions are community practice, not written on any APS page; unverified in that sense.
- CRediT makes the conversation easier: write the contribution paragraph early, agree it, and the order follows. [32]
- People who gave compute (SDSC Expanse under the ACCESS allocation), onboarding help, or code review go in Acknowledgments with the grant number. The draft already has this.
- The GPT-1900 authors are not authors on this paper. Their artefact is the subject, their code is cited at the pinned commit under its MIT licence, and basic courtesy is a short email before the arXiv posting telling them it exists, with the record-keeping framing stated plainly. Keating decides whether and when.

---

## Sources

Read 7 Oct 2026 unless stated. Numbers in brackets in the text refer to this list.

1. PRX Intelligence, About: https://journals.aps.org/prxintelligence/about
2. PRX Intelligence, Scope: https://journals.aps.org/prxintelligence/scope
3. PRX Intelligence, Information for Authors: https://journals.aps.org/prxintelligence/authors
4. PRX Intelligence, Editors: https://journals.aps.org/prxintelligence/staff
5. APS press release, 19 Nov 2025: https://www.aps.org/about/news/2025/11/scientific-journal-ai-machine-learning
6. PRX Intelligence announcements page (launch 19 Nov 2025, call for papers and APC waiver 18 Feb 2026, first papers 28 Jul 2026): https://journals.aps.org/prxintelligence/edannounce
7. APS news, 28 Jul 2026, first papers: https://www.aps.org/about/news/2026/07/prx-intelligence-publishes-first-papers
8. PRX Intelligence home page (metrics not yet available; APC waived before 01 Jan 2027): https://journals.aps.org/prxintelligence/
9. APS News interview with the Chief Editor, Dec 2025: https://www.aps.org/apsnews/2025/12/von-lilienfeld-editor-newest-journal
10. Editorial abstract page, PRX Intelligence 1, 010001 (2026): https://journals.aps.org/prxintelligence/abstract/10.1103/PRXINTELL.1.010001
11. Editorial PDF (quotes checked 28 Sep 2026 in journal-recon.md; the PDF did not render today): https://journals.aps.org/prxintelligence/pdf/10.1103/PRXINTELL.1.010001
12. APS journal metrics page, 2025 figures: https://journals.aps.org/metrics
13. APS news, 29 Jun 2026, Journal Citation Reports: https://www.aps.org/about/news/2026/06/journals-performance-metrics-citation-reports
14. PRX Quantum, About: https://journals.aps.org/prxquantum/about
15. PRX Energy, About: https://journals.aps.org/prxenergy/about
16. PRX Life, About: https://journals.aps.org/prxlife/about
17. Physical Review X, About: https://journals.aps.org/prx/about
18. Physical Review Research, About and Authors: https://journals.aps.org/prresearch/about and https://journals.aps.org/prresearch/authors
19. Physical Review Letters, About (criteria, impact factor, turnaround statistics): https://journals.aps.org/prl/about
20. First issues: PRX https://journals.aps.org/prx/issues/1/1 (2011); PRX Quantum https://journals.aps.org/prxquantum/issues/1/1 (2020); PRX Energy https://journals.aps.org/prxenergy/issues/1/1 (2022); PRX Life https://journals.aps.org/prxlife/issues/1/1 (2023); PRR https://journals.aps.org/prresearch/issues/1/1 (2019). PRL's 1958 start: https://journals.aps.org/prl/issues/1/1 (not opened today; unverified)
21. APS open access and 2026 APC table: https://journals.aps.org/prresearch/openaccess
22. APS web submission guidelines: https://journals.aps.org/authors/web-submission-guidelines-physical-review
23. APS editorial policies and practices (peer review, decisions, referees, CRediT, conflicts, preprints, DAS date): https://journals.aps.org/authors/editorial-policies and ethics page https://journals.aps.org/authors/editorial-policies-ethics
24. APS Data Availability Statements: https://journals.aps.org/authors/data-availability-statements
25. APS length guide (PRL 3,750 words; figure and table word equivalents; PRX Intelligence not listed): https://journals.aps.org/authors/length-guide
26. REVTeX 4.2f and class options: https://journals.aps.org/revtex
27. APS Style Basics (title, abstract, references, figures, author contributions, acknowledgments): https://journals.aps.org/authors/style-basics
28. Figure formats and resolution, older APS contributor pages found by search and not re-read in full: https://journals.aps.org/prmaterials/authors/information-for-contributors and https://journals.aps.org/rmp/info/figures.html (partially verified)
29. APS policy on appropriate use of AI tools, and FAQ: https://journals.aps.org/authors/appropriate-use-ai-tools and https://journals.aps.org/authors/ai-based-writing-tools
30. APS news, 17 Jun 2026, updated AI policy: https://www.aps.org/about/news/2026/06/releases-updated-ai-policy-journals
31. PRL acceptance rate, secondary source, not an APS figure: https://arxiv.org/pdf/1308.1552 (unverified against APS)
32. CRediT taxonomy: https://credit.niso.org/
33. PRX submission guide (cover letter, referee list): https://journals.aps.org/prx/authors/submissionguide-prx
34. APS tips for authors (referee suggestions, no reference numbers in abstract): https://journals.aps.org/authors/tips-authors-physical-review-physical-review-letters
35. APS submission portal: https://authors.aps.org/Submissions/login/new
36. Turnaround data points: https://journals.aps.org/prxintelligence/abstract/10.1103/wv8r-7zr1 (received 26 Mar, accepted 15 Jul, published 13 Aug 2026) and https://journals.aps.org/prxintelligence/abstract/10.1103/cnsd-p8nc (received 25 Mar, accepted 15 Jul, published 20 Aug 2026)
37. Nature Machine Intelligence, aims and scope (seen via search excerpt; the page redirected when fetched directly): https://www.nature.com/natmachintell/aims
38. Nature Machine Intelligence publishing options and APC: https://www.nature.com/natmachintell/submission-guidelines/publishing-options and https://www.nature.com/natmachintell/open-access-funding
39. Patterns, aims and scope (seen via search excerpt; direct fetch returned 403): https://www.cell.com/patterns/aims
40. Patterns, information for authors (APC): https://www.cell.com/patterns/information-for-authors
41. TMLR home: https://jmlr.org/tmlr/
42. TMLR acceptance criteria: https://jmlr.org/tmlr/acceptance-criteria.html
43. TMLR editorial policies (no fees, certifications, review timing): https://jmlr.org/tmlr/editorial-policies.html
44. NeurIPS 2026 dates: https://neurips.cc/Conferences/2026/Dates
45. ICLR 2027 call for workshops: https://iclr.cc/Conferences/2027/CallForWorkshops
46. ICLR 2027 main page (26 to 30 Apr 2027, California): https://iclr.cc/Conferences/2027
47. arXiv endorsement: https://info.arxiv.org/help/endorsement.html

Internal: `reports/journal-recon.md` (28 Sep 2026), `reports/reproducibility-memo.md` (22 Sep 2026), `reports/paper-draft.md` (28 Sep 2026).

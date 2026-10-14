# Journal reconnaissance for the GPT-1900 reproducibility paper

28 Sep 2026

Target named by Keating: PRX Intelligence. Alternative: PRX Quantum. Comparison point: PRL. This note collects what the journal pages actually say so the draft can be shaped to the venue before it is written. Everything below was checked against journals.aps.org today unless a line says otherwise.

## 1. PRX Intelligence at a glance

| Item | What the journal says |
|---|---|
| Publisher | American Physical Society, ISSN 3070-0329 (online) |
| Mission | "a highly selective, fully open access journal for impactful research in artificial intelligence and machine learning (AI/ML) that advances the physical sciences and related fields" |
| First papers | 28 Jul 2026, six papers plus the editorial |
| Papers published so far | 24 items in Vol. 1, Iss. 1 as of 24 Sep 2026: one editorial and 23 research papers |
| Editorial | Ceriotti, Krenn, Lee, Marzari, Nachman, Pettee, von Lilienfeld, "Editorial: Publishing Physical Sciences in the Era of AI", PRX Intelligence 1, 010001 (2026), received 17 Jul, published 28 Jul 2026, 4 pages |
| Editorial team | O. A. von Lilienfeld, Chief Editor; A. B. Lee, N. Marzari, B. Nachman, Deputy Editors; M. Ceriotti, M. Krenn, M. Pettee, Associate Editors (named in the editorial's Acknowledgments; the About page does not name individuals) |
| Open access | CC BY 4.0, authors keep copyright |
| APC | Waived for any article submitted through 31 Dec 2026. After that, APS rates apply. Waivers continue for authors from lower income countries |

Sources: https://journals.aps.org/prxintelligence/about, https://journals.aps.org/prxintelligence/authors, https://journals.aps.org/prxintelligence/issues/1/1, https://journals.aps.org/prxintelligence/abstract/10.1103/PRXINTELL.1.010001, https://www.aps.org/about/news/2026/07/prx-intelligence-publishes-first-papers

### Scope

Confirmed earlier today on the About page: the scope list includes "ML-guided theorem proving and scientific reasoning" and "trustworthy and robust and safety-aware ML for scientific deployment". The About page also frames the scope as AI/ML methods and their applications across the physical sciences, spanning physics, computer science and mathematics, materials science and engineering, chemistry and biology, and earth and environmental sciences.
Source: https://journals.aps.org/prxintelligence/about

### Acceptance criteria, verbatim

"Submitted manuscripts should address relevant questions, report sufficient or state-of-the-art validation, and demonstrate exceptional achievement in at least one of the following dimensions:"

- "Exceptional advance: Introducing AI/ML concepts, results, or systems that open new and consequential directions for scientific discovery or understanding."
- "Exceptional connection: Bridging AI/ML with disparate areas of science or engineering, or unifying previously separate approaches to enable new capabilities."
- "Exceptional capabilities: Delivering tools, techniques, datasets, software, or platforms that unlock progress on major challenges (e.g., scale, interpretability, reliability, efficiency)."
- "Exceptional insight: Providing clear, generalizable understanding of AI/ML behavior or scientific phenomena with high relevance across multiple communities."

Source: https://journals.aps.org/prxintelligence/about

The reproducibility paper lands most naturally on "exceptional insight" (generalizable understanding of AI/ML behavior: how stable an LLM-judged physics benchmark is under re-grading) with a secondary claim on "exceptional capabilities" if the record schema and the blinded packet builder are released as reusable tools.

### What the editorial asks for

These are the sentences in the editorial that bear directly on this paper.

"To meet the standards of the Physical Review journals, research papers should include rigorous validation against strong baselines and null models, a clear discussion of limitations and out-of-distribution behavior, and, wherever feasible, open availability of data and code to facilitate reproducibility. We require transparent disclosure of any use of generative AI tools in manuscript preparation or figure creation, consistent with APS policy."

"Goodhart's law, that a measure that becomes a target ceases to be a good measure [18], applies here as well: when progress is reduced to incremental gains on benchmark leaderboards, the result is optimization of metrics rather than advancement of understanding."

"we encourage authors and reviewers to consider null models (e.g., k-nearest neighbors), training and data scaling laws, characterization of underfitting and overfitting regimes, performance in the limit of minimal model complexity, and the use of explainable AI."

"Papers are accepted when authors resolve criticism and address suggestions meaningfully, under the condition that the work is novel and free of substantive flaws."

The editorial's own Acknowledgments is a usable model for the AI disclosure: "The authors acknowledge the use of Claude (Anthropic) and Gemini (Google) for assistance with editing, and literature search. The authors take full responsibility for all scientific arguments, editorial positions, and final content."
Source: https://journals.aps.org/prxintelligence/pdf/10.1103/PRXINTELL.1.010001

The Goodhart sentence is the hook. A paper that measures how much a benchmark score moves under re-grading is exactly a paper about whether the leaderboard number means anything.

## 2. Article types and length

| Type | Length | Invited? | Description on the Authors page |
|---|---|---|---|
| Research Articles | no length limit | no | "Regular Articles are original research articles that meet PRX Intelligence's editorial criteria and scope." The heading says Research Articles, the sentence under it says Regular Articles. Same thing. |
| Data/Code | no length limit | no | "Data/Code papers provide a peer-reviewed venue to present data sets and/or code that will be of high interest to researchers." Details below. |
| Perspectives | 7,500 words | generally invited, proposals considered | "forward-looking, brief and focused articles, with an emphasis on future outlook and implications for research" |
| Reviews | 30,000 words | generally invited | "balanced and high-quality surveys of relatively recent developments (past 2-5 years) in a particular field" |
| Tutorials | no length limit | generally invited | "hands-on guides" that "aim to train newcomers" |
| Roadmaps | no length limit | generally invited | "the viewpoint of a group of experts on future prospects and a potential path to tackling the main challenges" |
| Comments and Replies | 3,500 words | no | "critique or correct papers by other authors that were previously published in PRX Intelligence" |
| Erratum | not stated | no | "notifies readers about errors or omissions in previously published papers" |

Source: https://journals.aps.org/prxintelligence/authors

The general APS Length Guide does not list PRX Intelligence at all; the only limits are the ones on the journal's own Authors page.
Source: https://journals.aps.org/authors/length-guide

### Data/Code papers in full

Data papers: "Data papers describe and document novel data sets that enable important new research or substantially improve the community's ability to test, compare, or reproduce results within the topical scope of PRX Intelligence." They are expected to have four parts: (i) Motivation, with context and a brief literature review; (ii) Description, "dataset genesis and structure, including an overview table of entries, format specifications, and key distributions/summaries"; (iii) Analysis, "quality testing, curation and validation, including tests of convergence, consistency, applicability, and other appropriate checks"; (iv) Conclusion, with shortcomings and future efforts. "Authors must provide links/citations to appropriate data repositories."

Code papers: "Code papers report code and algorithms that represent a substantial technical advance within the topical scope of PRX Intelligence." Same four-part shape: (i) Motivation against the state of the art; (ii) Description with "essential technical specifications for operation of the code such as libraries, parallelism, compilers, etc."; (iii) Analysis, "benchmark performance in terms of predictive accuracy, precision, and speed (ideally measured in FLOPS)"; (iv) Conclusions. "Links and citations to code repositories are strongly encouraged."
Source: https://journals.aps.org/prxintelligence/authors

The editorial adds that datasets "must be novel and valuable" and gives extraction from literature, autonomous experimentation, and high-performance computing as the kinds of provenance it has in mind.
Source: https://journals.aps.org/prxintelligence/pdf/10.1103/PRXINTELL.1.010001

## 3. Template and what gets submitted

A PDF is enough for review. The Authors page: "A PDF version of your paper is all that's needed for it to be sent for peer review." The APS web submission guidelines: "We only require a PDF file for a new submission and resubmissions. For PDF submissions, all textual material and figures should be in a single file." Source files "will not be requested until acceptance."
Sources: https://journals.aps.org/prxintelligence/authors, https://journals.aps.org/authors/web-submission-guidelines-physical-review

At acceptance: "Text files should be formatted in REVTeX (preferred) or LaTeX." Word is accepted but "their use is extremely limited in the production process." The template is apstemplate.tex from the REVTeX package; a Word template is also downloadable. The guidelines page does not state a REVTeX version number. REVTeX 4.2 is the current release as far as I know, but that was not verified today.
Sources: https://journals.aps.org/authors/web-submission-guidelines-physical-review, https://journals.aps.org/prxintelligence/authors, https://journals.aps.org/revtex

Supplemental Material goes in as a separate PDF, and "A paper must stand on its own and be understandable and convincing without Supplemental Material."
Sources: https://journals.aps.org/authors/web-submission-guidelines-physical-review, https://journals.aps.org/prxintelligence/authors

Audience instruction: "Your manuscript should be written for a broad scientific readership, it should be understandable to researchers across disciplines and should avoid unnecessary field-specific jargon."
Source: https://journals.aps.org/prxintelligence/authors

No extra materials: "PRX Intelligence does not require additional materials beyond what is mentioned above." So no Popular Summary, unlike PRX. None of the three published papers I opened has one.
Source: https://journals.aps.org/prxintelligence/authors

Joint submissions are welcome: "Authors are welcome to submit two or more related or complementary papers", coordinated by the editors. This matters for the Data/Code option in section 7.
Source: https://journals.aps.org/prxintelligence/authors

## 4. APS policy on the appropriate use of AI tools

APS refreshed this policy on 17 Jun 2026. AI may assist with research, manuscript preparation, and review, but "An AI program cannot be held accountable and cannot be listed as an author" and "Authors are fully responsible for accuracy and must review and refine all AI-generated content." Two disclosure rules apply. First, "Any AI used to conduct the actual research (e.g., data analysis) must, like any tool, be disclosed within the paper's methods section." Second, "Authors must keep a record of any AI use and disclose any substantive uses in the submitted paper", stating the "AI tool name and version", "How the AI assisted", and "How the authors directed and verified the AI output." The FAQ counts as substantive: scientific reasoning or interpretation, drafting or revising scientific claims, literature synthesis beyond routine organization, figure generation or image analysis, derivations or calculations, and code generation that affects results. Placement: figure-related use in the caption, research use in Methods, and "All other uses worth disclosing should be in the Acknowledgment statement." Light editing is exempt: "Authors are not required to disclose the use of AI to polish, condense, or otherwise lightly edit the text." AI may produce data visualizations if the authors verify them, but images generated or modified by generative AI are not allowed. For this paper that means two disclosures: the LLM grader is a research instrument and belongs in Methods with model name, version, prompt, and the verification procedure (the blinded re-grading and human spot checks); drafting help belongs in the Acknowledgments in the form the editors themselves used.
Sources: https://journals.aps.org/authors/appropriate-use-ai-tools, https://journals.aps.org/authors/ai-based-writing-tools, https://www.aps.org/about/news/2026/06/releases-updated-ai-policy-journals, https://journals.aps.org/prxintelligence/authors

## 5. Data Availability policy

"All published articles must include a Data Availability Statement (DAS)." The requirement applies to everything submitted to a Physical Review journal on or after 11 Dec 2024 (4 Sep 2024 for PRD and PRX Energy). Authors enter the statement during submission and it is printed in the article. It should "describe clearly and concisely how the data and/or software used in your research can be accessed, including references"; software and code count as research data. Sharing is "strongly encouraged" and should follow FAIR principles, and "Publicly shared data and software must be cited in the reference list" with that citation repeated inside the statement. If data will not be shared, the authors must give the reason, which is published, and must "agree to make any data required to support or replicate claims made in their article available privately to the journal's editors, reviewers, and readers upon reasonable request." Embargoes are allowed if stated. Stock wording offered: "The data that support the findings of this article are publicly available [1,2]." / "The data are available upon reasonable request from the authors." / "No data were created or analyzed in this study." / "The data that support the findings of this article will be publicly available after embargo from [date]." The three published papers I checked each deposited in a DOI-issuing repository (figshare, Materials Cloud Archive, Cornell eCommons) with code on GitHub, which is the pattern to match.
Sources: https://journals.aps.org/authors/data-availability-statements, https://journals.aps.org/edannounce/APS-Releases-Data-Availability-Policy-for-the-Journals, https://journals.aps.org/authors/editorial-policies

Related APS reproducibility policy, relevant because it is the subject of the paper: "A scientific article should include all relevant details a fellow researcher of reasonable skill would need to reproduce the work and verify the results", and "Deliberately concealing details necessary for reproducibility studies runs counter to the APS core value of adherence to the scientific method, as well as the values of truth and integrity."
Source: https://journals.aps.org/authors/editorial-policies-ethics

## 6. Published PRX Intelligence papers closest in spirit

Nothing in the journal yet is about an LLM benchmark, LLM grading, or the reproducibility of an evaluation. The 23 research papers published so far are mostly ML for materials, quantum many-body, plasma, and detector physics. The three below are the closest published ones: two measure how ML models behave (scaling, symmetry) and one runs AI agents in a loop with humans. Two accepted but unpublished papers are closer still because they are LLM-agent systems with evaluation sections.
Source: https://journals.aps.org/prxintelligence/issues/1/1

| Paper | Citation | Structure and length |
|---|---|---|
| M. Großmann, M. Grunert, E. Runge, "Broken Neural Scaling Laws in Learning the Optical Properties of Solids" | PRX Intelligence 1, 013011 (2026). Received 26 Mar, accepted 15 Jul, published 13 Aug 2026. arXiv:2602.05702 | Introduction, Results, Discussion, Methods, Acknowledgments, Data Availability. 15 typeset pages, 3 figures, 2 tables, separate Supplemental Material. Data on figshare (three DOIs), code on GitHub. A measurement-of-ML paper: how error scales with data and parameters. |
| M. Domina, J. W. Abbott, P. Pegolo, F. Bigi, M. Ceriotti, "How Unconstrained Machine-Learning Models Learn Physical Symmetries" | PRX Intelligence 1, 013013 (2026). Received 25 Mar, accepted 15 Jul, published 20 Aug 2026. arXiv:2603.24638 (15 pages, 9 figures) | Introduction, Quantifying Symmetry in ML Models, Unconstrained Models for Atomistic Simulations, Beyond Atomistic Simulations, Conclusions, Acknowledgments, Data Availability. 14 typeset pages, 9 figures, Supplemental Material. Data on Materials Cloud Archive. Introduces metrics to quantify a property of trained models; last author is an Associate Editor, so this is house style. |
| M.-C. Chang et al. (12 authors), "Autonomous Materials Exploration Integrates Automated Phase Identification and AI Agents Enhanced by Human Guidance" | PRX Intelligence 1, 013019 (2026). Received 17 Apr, accepted 22 Jul, published 10 Sep 2026. arXiv:2601.08185 (21 pages plus 12 pages SI) | Introduction, Results and Discussion, Conclusion, Methods, Acknowledgments, Data Availability. 20 typeset pages, 6 figures, Supplemental Material. Data at Cornell eCommons DOI. AI agents with a human in the loop; the title was rewritten between arXiv and publication. |
| F. Villaescusa-Navarro et al. (36 authors), "The Denario project: Deep knowledge AI agents for scientific discovery" | Accepted 4 Aug 2026, DOI 10.1103/kk55-gc95, not yet published. arXiv:2510.26887 (272 pages including 11 AI-generated paper drafts) | LLM multi-agent research assistant. Domain experts scored its AI-generated papers with "numerical scores and review-like feedback." The nearest thing in the journal to LLM output being graded by humans. Shows the no-length-limit rule is real in practice. |
| W. Dawson, L. Beal, Y. Curé, G. Fisicaro, D. Rolland, L. Genovese, "LARA-HPC: Validation-driven agentic supercomputer workflows for atomistic modeling" | Accepted 15 Sep 2026, DOI 10.1103/cp6v-t93q, not yet published. arXiv:2604.22571 (12 pages, 2 figures) | LLM agents for HPC workflows; abstract names "correctness, reproducibility, and safe interaction" as the gap and argues for "a shift from generation-first to validation-first paradigms". Short, and accepted. |

Sources: https://journals.aps.org/prxintelligence/abstract/10.1103/wv8r-7zr1, https://journals.aps.org/prxintelligence/abstract/10.1103/cnsd-p8nc, https://journals.aps.org/prxintelligence/abstract/10.1103/c362-349b, https://journals.aps.org/prxintelligence/accepted/10.1103/kk55-gc95, https://journals.aps.org/prxintelligence/accepted/10.1103/cp6v-t93q, https://arxiv.org/abs/2602.05702, https://arxiv.org/abs/2603.24638, https://arxiv.org/abs/2601.08185, https://arxiv.org/abs/2510.26887, https://arxiv.org/abs/2604.22571. Page, figure, and table counts for the three published papers come from the APS PDFs at https://journals.aps.org/prxintelligence/pdf/10.1103/wv8r-7zr1, https://journals.aps.org/prxintelligence/pdf/10.1103/cnsd-p8nc, https://journals.aps.org/prxintelligence/pdf/10.1103/c362-349b.

Turnaround from the three published papers: 3.5 to 4 months from receipt to acceptance, then 2 to 7 weeks to publication. A submission in Nov 2026 would plausibly be decided by Mar 2027.
Source: received, accepted, and published dates on the three abstract pages listed above

None of the three published papers discloses AI use in its Acknowledgments. The editorial does. The updated APS policy dates from Jun 2026 and these papers were received in Mar and Apr 2026, so their silence is not a precedent.
Sources: the three PDFs listed above, https://www.aps.org/about/news/2026/06/releases-updated-ai-policy-journals

## 7. Comparison points

### PRX Quantum

Scope: "all topics relevant to the diverse multidisciplinary quantum information science and technology research communities spanning physics, computer science, mathematics, chemistry, materials, engineering, and technology." Its four acceptance criteria are the same exceptional advance, connection, capabilities, insight template, but each is defined relative to "quantum science and technology". Research Articles have no length limit, Perspectives 7,500 words, Tutorials 37,500 words, and a PDF is enough for review. It is funded by APCs that are "due once an article is accepted for publication", with no waiver comparable to the PRX Intelligence promotion. Fit for this paper is poor. GPT-1900 is a physics reasoning benchmark and the paper is about grading stability; neither is a quantum information result. The only way in would be to reframe around a quantum-only subset of the problems and argue the grading findings matter for evaluating quantum reasoning specifically, which narrows the claim and drops the parts of the data that carry the most statistical weight. It also costs an APC that PRX Intelligence waives this year.
Sources: https://journals.aps.org/prxquantum/about, https://journals.aps.org/prxquantum/authors

### PRL

Letters are capped at 3,750 words. The Length Guide converts displayed math at 16 words per row (32 for two-column), single-column figures at (150 / aspect ratio) + 20 words, and single-column tables at 13 words plus 6.5 words per line; title, abstract, references, author list, and acknowledgments do not count. Letters are "brief accounts of highly important original research, which are complete and accessible for the general reader", and acceptance requires one of: open a new research area, solve or make essential steps toward solving a critical problem, introduce techniques or methods with highly significant impact, or "Be of unusual intrinsic interest to PRL's broad audience." PRL is hybrid: an APC buys open access, and a traditional publication carries an optional page charge of $830. Fit is weak for two reasons. The paper needs its tables: per-field agreement, grader variance across runs, and the record schema will not fit in 3,750 word equivalents without pushing nearly all evidence into Supplemental Material, and a PRL referee then asks what the Letter itself demonstrates. And a study of how reproducible an AI-judged benchmark is has to clear the "unusual intrinsic interest" bar for a general physics audience, which is a harder argument than the one PRX Intelligence's editors have already made for us in their own editorial.
Sources: https://journals.aps.org/prl/authors, https://journals.aps.org/authors/length-guide, https://journals.aps.org/prl/about

### Why PRX Intelligence is the better fit

The scope names scientific reasoning and trustworthy ML for scientific deployment. The criteria ask for "sufficient or state-of-the-art validation" and reward "generalizable understanding of AI/ML behavior". The editorial names benchmark leaderboards and Goodhart's law as a problem the journal exists to address, asks for null models and out-of-distribution discussion, and wants data and code open. There is no length limit, the APC is zero for anything submitted by 31 Dec 2026, and a PDF is all that is needed for review. The one thing the journal cannot offer is a precedent: nobody has published an LLM benchmark reproducibility paper there yet, which cuts both ways. It means the paper is novel for the venue and it means the referees will be drawn from the ML-for-physics community rather than from LLM evaluation.
Sources: https://journals.aps.org/prxintelligence/about, https://journals.aps.org/prxintelligence/authors, https://journals.aps.org/prxintelligence/pdf/10.1103/PRXINTELL.1.010001

## 8. What this means for the draft

### Article type

Research Article (the Authors page calls it Regular Article in the description) for the findings. A separate Data/Code paper for the 50-field record schema and the blinded packet builder is a real option. The Data paper template maps almost one to one onto the schema: Motivation, then Description with "an overview table of entries, format specifications, and key distributions/summaries", then Analysis with consistency and applicability checks, then Conclusion with shortcomings. The packet builder fits the Code paper template less cleanly because the Analysis section wants "benchmark performance in terms of predictive accuracy, precision, and speed", which is not how a packet builder is judged. The cleaner split is a Data paper for the schema plus the graded records, with the builder released as code inside it, and the journal explicitly welcomes joint submissions of complementary papers. The risk is that a thin main paper plus a Data paper reads as one paper cut in two; the split only makes sense if the schema is worth citing on its own by people who never read the reproducibility result.
Sources: https://journals.aps.org/prxintelligence/authors

### Target length

There is no limit. The published papers run 14 to 20 typeset two-column pages with 3 to 9 figures, and accepted papers range from 12 arXiv pages (LARA-HPC) to 272 (Denario). Aim for 12 to 16 typeset pages of main text, which is under the current median, and push the per-field tables and full grader-variance runs into Supplemental Material with the record schema in the repository. The main text still has to stand alone without the supplement.
Sources: the three PDFs and arXiv pages listed in section 6, https://journals.aps.org/prxintelligence/authors

### Required statements

- Data Availability Statement, entered at submission, printed in the paper. Deposit the records, the schema, and the packet builder in a DOI-issuing repository (Zenodo or figshare match what published authors used) and cite that DOI in the reference list as well as in the statement. "Available on request" is allowed but the reason is published, and for a reproducibility paper it would be self-undermining.
- AI disclosure in Methods for the LLM grader: tool name and version, how it assisted (what it graded, under what prompt), how the authors directed and verified its output (the blinded packet, re-grading runs, human checks). This is research use, so the Methods section is the mandated place.
- AI disclosure in Acknowledgments for drafting and literature help, in the form the editors used: tool and vendor, what it did, and a sentence taking full responsibility.
- No AI-generated or AI-modified images. Plots produced with AI-written code are fine if the authors verified them.
- Abstract written for a broad scientific readership, no field jargon, no Popular Summary needed.
- Supplemental Material as a separate single PDF.
- Submit before 31 Dec 2026 to take the APC waiver.
Sources: https://journals.aps.org/authors/data-availability-statements, https://journals.aps.org/authors/appropriate-use-ai-tools, https://journals.aps.org/prxintelligence/authors

### Three structural conventions the recent papers share

1. APS numbered sections in a fixed order: I. Introduction, then Results (either one Results section or two or three topical sections), then Discussion or Conclusion, then Methods at the end, then Acknowledgments, then Data Availability, then references. Two of the three published papers put Methods after the conclusions; the third folds methods into topical sections. For this paper: Introduction, Results (grader agreement, variance under re-grading, per-field breakdown), Discussion with limitations and out-of-distribution behavior called out by name because the editorial asks for it, Methods (benchmark, grader, blinding, statistics), Data Availability.
2. A Data Availability section pointing at a persistent DOI repository for data and a GitHub repository for code, both cited in the reference list. Every one of the three published papers does this.
3. Supplemental Material as a separate PDF carrying the long tables and extra figures, with 3 to 9 figures in a main text of 14 to 20 pages, and an abstract that ends on a one-sentence claim of general significance rather than a list of results.
Sources: https://journals.aps.org/prxintelligence/abstract/10.1103/wv8r-7zr1, https://journals.aps.org/prxintelligence/abstract/10.1103/cnsd-p8nc, https://journals.aps.org/prxintelligence/abstract/10.1103/c362-349b, https://journals.aps.org/prxintelligence/pdf/10.1103/PRXINTELL.1.010001

One more convention that is not structural: the editorial asks for "rigorous validation against strong baselines and null models". For a grading-stability paper the null model is cheap and should be in the paper: what agreement would a random grader, a majority-class grader, or a length-based grader achieve on the same packets. Reporting that alongside the LLM grader is the single easiest way to match what the editors say they want.
Source: https://journals.aps.org/prxintelligence/pdf/10.1103/PRXINTELL.1.010001

## 9. Checked and not found

- https://journals.aps.org/authors/data-availability-policy-and-guidelines and https://journals.aps.org/authors/data-availability-policy both return 404. The live guidelines page is https://journals.aps.org/authors/data-availability-statements.
- https://journals.aps.org/prl/authors/length-guide returns 404. The live page is https://journals.aps.org/authors/length-guide, which also carries the PRL limit.
- The PRX Intelligence About page does not name the Chief Editor; the editorial does.
- The issue page does not label article types, so I could not tell whether any of the 23 published research papers was submitted as a Data/Code paper. None of the titles reads like one.
- The REVTeX version was not verified today.

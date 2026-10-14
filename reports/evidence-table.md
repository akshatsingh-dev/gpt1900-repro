# Evidence table: AI-discovery benchmarks and their limits

Workstream 5. Every row below was read at the source on 22 Sep 2026; the
claim column quotes or closely paraphrases the paper's own abstract. The
"limit" column is what the benchmark itself says it cannot do, plus what it
does not measure that the Artificial Einstein Test needs.

The point of the table: no existing benchmark tests what GPT-1900 claims to
test, reconstruction of a breakthrough from pre-breakthrough knowledge. The
closest relatives split into two families that each cover half of it.

## Family 1. Can an AI do the work of science?

| Benchmark | What it measures | Headline result | Stated limits | What it does not test |
|---|---|---|---|---|
| DiscoveryBench (Majumder et al., 2024, arXiv:2407.01725) | 264 real tasks from 6 domains plus 903 synthetic: given a dataset and a goal, derive the hypothesis a paper derived | Best system scores 25% | Authors: "illustrates the challenges in autonomous data-driven discovery" | Discovery from data the model is handed, not from a knowledge state. The answer exists in a published paper the model may have read |
| ScienceAgentBench (Chen et al., 2024, arXiv:2410.05080) | 102 tasks from 44 peer-reviewed papers in 4 disciplines, validated by 9 subject experts; output is a runnable Python program | Best agent 32.4% alone, 34.3% with expert knowledge, 42.2% for o1-preview at over 10x the cost | Authors call for "rigorous assessment of agents on individual tasks... before making bold claims on end-to-end automation"; two explicit contamination-mitigation strategies | Code generation for data analysis, not conceptual reasoning. Contamination handled by design, which GPT-1900 handles by corpus cutoff instead |
| MLE-bench (Chan et al., 2024, arXiv:2410.07095) | 75 Kaggle competitions, human baselines per competition | Best setup, o1-preview with AIDE, reaches bronze-medal level in 16.9% of competitions | Engineering skill, not discovery; medals measure leaderboard position | Nothing about knowledge cutoff or reasoning from first principles |
| The AI Scientist (Lu et al., 2024, arXiv:2408.06292) | End-to-end: idea, code, experiment, paper, automated review, in three ML subfields | Papers at under $15 each; automated reviewer "near-human" on paper scores | System, not benchmark; the reviewer is itself an LLM, so the score is LLM-judged LLM output | No ground truth. Same structural issue as GPT-1900's Claude-as-judge, at larger scale |
| LAB-Bench (Laurent et al., 2024, arXiv:2407.10362) | 2,400+ multiple-choice questions on practical biology research tasks, compared to human expert researchers | Frontier models compared against human biologists (numbers in paper) | Multiple choice, biology only, "a step toward" agent benchmarks | Recall and tool use within current knowledge, not reconstruction of missing knowledge |

## Family 2. Can an AI reproduce what was already done?

| Benchmark | What it measures | Headline result | Stated limits | Relevance here |
|---|---|---|---|---|
| CORE-Bench (Siegel et al., 2024, arXiv:2409.11363) | 270 tasks from 90 papers in CS, social science, medicine: reproduce a paper's result from its code and data, three difficulty levels | Best agent 21% on the hardest level (19% in the published version) | "vast scope for improvement in automating routine scientific tasks" | The task this sprint did by hand. An agent that cannot reproduce a paper from its code cannot be trusted to judge one |
| PaperBench (Starace et al., 2025, arXiv:2504.01848) | Replicate 20 ICML 2024 papers from scratch; 8,316 individually gradable sub-tasks with hierarchical rubrics | Best agent, Claude 3.5 Sonnet with open scaffolding, 21.0%; top ML PhDs still beat the models | Rubric graded by an LLM judge, validated against human grading | Shows what a defensible LLM-judged rubric looks like: decomposed, validated, with a human baseline. GPT-1900's rubric has none of the three |

## Family 3. Models with a knowledge cutoff in the past

| Model | What it is | What it shows | Limits |
|---|---|---|---|
| GPT-1900 (Hla, 2026, github.com/michaelhla/gpt1900, HF mhla/gpt1900-d34-22btok) | 3.29B parameters, about 22B tokens of pre-1900 English from HathiTrust, Internet Archive, British Library, American newspapers; anachronism filter on the corpus; RL checkpoints trained with physics reasoning rewards | The subject of this sprint. Published physics score 0.93 of 5, judged by Claude, one draw per cell, no seed or revision recorded | Every finding in this repository. Also: the README says the RL checkpoints "should only be expected to perform well on physics prompts" and that temperature needs tuning |
| TypewriterLM (Luo et al., 2026, arXiv:2606.02991) | 7.24B parameters, 54B tokens of pre-1913 English, with explicit leakage mitigation and a History-Event benchmark for "competence, temporal grounding and data leakage" | The first of these models with a published leakage evaluation. Their table reports GPT-1900 base at ARC-Easy 36.7%, ARC-Challenge 23.8%, HellaSwag 32.3% | Evaluates knowledge and grounding, not breakthrough reconstruction. But its leakage benchmark is the missing piece for GPT-1900's contamination question |
| TimeCapsuleLLM (Grigorian, 2025 to 2026, github.com/haykgrigo3/TimeCapsuleLLM) | 1.22B model on 1800 to 1875 London text | Surfaced a real 1834 London event from period sources alone, per the awesome-vintage-llms listing | Anecdotal; no published evaluation found |
| Ranke-4B (per awesome-vintage-llms) | Family of 4B Qwen3-architecture models, 80B tokens, cutoffs 1913, 1929, 1933, 1939, 1946 | Multiple cutoffs allow before/after comparisons on one architecture | Listing only; primary paper not read for this table |

## What this means for the Artificial Einstein Test

1. **No benchmark tests reconstruction.** Family 1 hands the model the data or
   the current literature. Family 3 restricts knowledge but evaluates recall.
   The Einstein Test wants both: restricted knowledge and a reasoning task
   whose answer lies outside it. GPT-1900 is the only attempt found, and its
   evaluation has the gaps this repository documents.
2. **LLM-as-judge is standard and is the weak point everywhere.** The AI
   Scientist and PaperBench both use it. PaperBench validates the judge against
   humans and decomposes the rubric into thousands of gradable pieces; GPT-1900
   has a 0 to 5 rubric per task, one draw per cell, and no human check. The
   blinded packet in this repository is the first step toward the PaperBench
   standard.
3. **Reproduction is hard even for agents.** CORE-Bench's best agent manages
   21% on the hardest tasks. That is the level of difficulty this sprint was
   about, done by hand, on one repository.
4. **Leakage evaluation exists now.** TypewriterLM ships a leakage benchmark.
   GPT-1900 has a corpus filter and, as of this sprint, a 16-stem probe and a
   corpus term search. Adopting History-Event, or something like it, is the
   obvious next step.

## Sources

- arXiv:2407.01725, DiscoveryBench, Majumder et al., 1 Jul 2024
- arXiv:2410.05080, ScienceAgentBench, Chen et al., 7 Oct 2024, v3 31 Mar 2025
- arXiv:2410.07095, MLE-bench, Chan et al., 2024
- arXiv:2408.06292, The AI Scientist, Lu et al., 2024
- arXiv:2407.10362, LAB-Bench, Laurent et al., 14 Jul 2024
- arXiv:2409.11363, CORE-Bench, Siegel et al., 2024, v2 22 Jun 2026
- arXiv:2504.01848, PaperBench, Starace et al., 2 Apr 2025
- arXiv:2606.02991, Pretraining Language Models on Historical Text (TypewriterLM), Luo et al., 2 Jun 2026
- github.com/michaelhla/gpt1900 and huggingface.co/mhla/gpt1900-d34-22btok, read 22 Sep 2026
- github.com/entanglr/awesome-vintage-llms, read 22 Sep 2026

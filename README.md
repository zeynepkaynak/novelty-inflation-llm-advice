# Novelty Inflation in LLM Research Advice

Data and code for a project submitted to the Apart Research **AI x Epistemics Research Sprint** (13–15 November 2026).

We asked ChatGPT, Claude and Gemini for 10 "standout" project ideas for the sprint, with a 1–10 novelty score per idea and a win probability. We matched the 120 ideas against 97 existing projects and labelled overlap blind to model and score.

## Files

| File | Contents |
| --- | --- |
| `prompts.md` | Both prompts (neutral and novice) |
| `brief.txt` | Sprint brief text pasted into every prompt (from the public sprint page) |
| `responses/` | 14 raw model replies: 12 analysed, 2 marked `EXCLUDED` (see report, Appendix A.2). Author's first name redacted as `[NAME]` |
| `ideas.csv` | 120 ideas: model, framing, run, title, one-line summary, novelty score, top pick |
| `pool.csv` | 97 comparison projects: 18 sprint-brief examples (`S`), 70 AI Manipulation Hackathon entries (`M`), 9 AI for Epistemics hackathon projects (`E`) |
| `matches.csv` | Top-3 TF-IDF candidates per idea |
| `labels.csv` | Blind ID, first-pass and final labels |
| `similarity.py` | Rebuilds `matches.csv` |
| `analysis.py` | Reproduces the correlations and counts in Section 4.1 |
| `fig1.py` | Draws `figure1.png` / `figure1.pdf` |

Summaries in `ideas.csv` are one-line paraphrases written for retrieval; the raw replies in `responses/` are the reference.

## Reproduce

```
pip install pandas scikit-learn scipy matplotlib
python similarity.py
python analysis.py
python fig1.py
```

## AI use

Claude (Anthropic) assisted with study design, the comparison pool, code and drafting. All overlap labels were made by the author. See the report's Appendix A.3.

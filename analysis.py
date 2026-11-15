"""Reproduces Section 4.1 statistics from labels.csv."""
import pandas as pd
from scipy.stats import spearmanr
d = pd.read_csv("labels.csv")
order = {"Same": 0, "Similar": 1, "Different": 2}
for col in ["label_pass1", "label_final"]:
    k = d[d[col].isin(order)]
    s = k[col].map(order)
    print(col, "all: rho=%.3f n=%d" % (spearmanr(k.novelty_score, s).correlation, len(k)))
    for m, g in k.groupby("model"):
        r = spearmanr(g.novelty_score, g[col].map(order))
        print("  %-8s rho=%.2f p=%.3f n=%d" % (m, r.correlation, r.pvalue, len(g)))
print(pd.crosstab(d.model, d.label_final))
print(d.groupby(["model", "framing"]).novelty_score.mean().round(2))

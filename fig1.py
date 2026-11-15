"""Figure 1: mean self-assigned novelty score by blind overlap label (final labels)."""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

d = pd.read_csv("labels.csv")
order = ["Same", "Similar", "Different"]
d = d[d.label_final.isin(order)]
m = d.groupby(["model", "label_final"]).novelty_score.agg(["mean", "size"]).reset_index()
names = {"chatgpt": "ChatGPT", "gemini": "Gemini", "claude": "Claude"}

fig, ax = plt.subplots(figsize=(7, 3.6), dpi=300)
for key in ["chatgpt", "gemini", "claude"]:
    g = m[m.model == key].set_index("label_final").reindex(order)
    xs = range(len(order))
    ax.plot(xs, g["mean"], color="#9aa0a6", lw=1.8, zorder=1)
    ax.scatter(xs, g["mean"], color="#1a73e8", s=36, zorder=2)
    for x, (mean, n) in zip(xs, zip(g["mean"], g["size"])):
        ax.annotate(f"{mean:.1f}\n(n={n})", (x, mean), textcoords="offset points",
                    xytext=(0, 7), ha="center", fontsize=7, color="#444")
    ax.annotate(names[key], (len(order) - 1, g["mean"].iloc[-1]), textcoords="offset points",
                xytext=(10, -3), fontsize=9)
ax.set_xticks(range(len(order)), order)
ax.set_xlim(-0.4, len(order) - 0.4)
ax.set_ylim(5, 10.6)
ax.set_ylabel("Mean novelty score (1–10)")
ax.set_xlabel("Overlap label (blind)")
ax.grid(axis="y", color="#e5e5e5", lw=0.8)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("figure1.png")
fig.savefig("figure1.pdf")

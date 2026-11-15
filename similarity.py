"""Top-3 TF-IDF candidates from pool.csv for each idea in ideas.csv -> matches.csv"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
pool, ideas = pd.read_csv("pool.csv"), pd.read_csv("ideas.csv")
p_txt = (pool.title + ". " + pool.summary).tolist()
i_txt = (ideas.title + ". " + ideas.summary).tolist()
vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), sublinear_tf=True).fit(p_txt + i_txt)
sim = cosine_similarity(vec.transform(i_txt), vec.transform(p_txt))
rows = []
for i, r in ideas.iterrows():
    for rank, j in enumerate(sim[i].argsort()[::-1][:3], 1):
        rows.append({"model": r.model, "framing": r.framing, "run": r.run, "idea_no": r.idea_no, "title": r.title,
                     "rank": rank, "pool_id": pool.id[j], "pool_title": pool.title[j], "tfidf_similarity": round(sim[i, j], 3)})
pd.DataFrame(rows).to_csv("matches.csv", index=False)

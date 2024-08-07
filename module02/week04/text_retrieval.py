import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf_search(question, tfidi_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question])
    cosine_scores = cosine_similarity(
        query_embedded, context_embedded).flatten()

    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)
    return results


def corr_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question])
    corr_scores = np.corrcoef(query_embedded.toarray()[0],
                              context_embedded.toarray())
    corr_scores = corr_scores[0][1:]

    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc)
    return results


vi_data_df = pd.read_csv(
    "./AIO2024/AIO-Exercise/module02/week04/vi_text_retrieval.csv")
context = vi_data_df['text']
context = [doc.lower() for doc in context]

tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
print(context_embedded.toarray()[7][0])

question = vi_data_df.iloc[0]['question']
results = corr_search(question, tfidf_vectorizer, top_d=5)
print(results[1]['corr_score'])

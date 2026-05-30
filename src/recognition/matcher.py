from sklearn.metrics.pairwise import cosine_similarity

def compare_embeddings(
    emb1,
    emb2
):

    score = cosine_similarity(
        emb1.reshape(1,-1),
        emb2.reshape(1,-1)
    )[0][0]

    return float(score)
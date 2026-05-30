import numpy as np

from src.recognition.embeddings import get_embedding
from src.recognition.matcher import compare_embeddings

from src.config import SIMILARITY_THRESHOLD

def verify(
    image,
    embedding_path
):

    current_embedding = get_embedding(
        image
    )

    if current_embedding is None:
        return {
            "score": 0.0,
            "match": False,
            "message": "No face detected"
        }

    stored_embedding = np.load(
        embedding_path
    )

    score = compare_embeddings(
        current_embedding,
        stored_embedding
    )

    return {
        "score": float(score),
        "match": score >= SIMILARITY_THRESHOLD
    }
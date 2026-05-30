import numpy as np

from src.recognition.embeddings import get_embedding

def enroll(image, save_path):

    embedding = get_embedding(image)

    if embedding is None:
        return False

    np.save(save_path, embedding)

    return True
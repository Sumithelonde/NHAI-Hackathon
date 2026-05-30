import cv2

from src.config import SAMPLE_IMAGE
from src.recognition.embeddings import get_embedding

img = cv2.imread(SAMPLE_IMAGE)

embedding = get_embedding(img)

if embedding is None:
    print("No face detected")
else:
    print("Embedding Shape:", embedding.shape)
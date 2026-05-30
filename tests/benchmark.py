import cv2
import time
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.recognition.embeddings import get_embedding
from src.config import SAMPLE_IMAGE

sample_image_path = PROJECT_ROOT / SAMPLE_IMAGE
img = cv2.imread(str(sample_image_path))

if img is None:
    raise Exception(
        f"Could not load image: {sample_image_path}"
    )

times = []

for _ in range(20):

    start = time.perf_counter()

    embedding = get_embedding(img)

    end = time.perf_counter()

    times.append(end - start)

avg = sum(times) / len(times)

print(
    f"Average Inference Time: {avg:.4f} sec"
)

print(
    f"Average FPS: {1/avg:.2f}"
)
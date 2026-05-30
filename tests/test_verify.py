import cv2

from src.api.verify import verify
from src.config import EMBEDDING_DIR

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    result = verify(
        frame,
        f"{EMBEDDING_DIR}/sumit.npy"
    )

    print(result)

    cv2.imshow(
        "Verification",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
import cv2

from src.api.authenticate import authenticate
from src.config import EMBEDDING_DIR

cap = cv2.VideoCapture(0)

print("Authentication Test")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Replace with actual challenge result later
    liveness_passed = True

    result = authenticate(
        frame,
        f"{EMBEDDING_DIR}/sumit.npy",
        liveness_passed
    )

    print(result)

    cv2.imshow(
        "Authentication",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
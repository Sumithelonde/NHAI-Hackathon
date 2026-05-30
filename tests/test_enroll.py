import cv2

from src.api.enroll import enroll
from src.config import EMBEDDING_DIR

cap = cv2.VideoCapture(0)

print("Press S to enroll")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow(
        "Enrollment",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('s'):

        success = enroll(
            frame,
            f"{EMBEDDING_DIR}/sumit.npy"
        )

        print("Enrollment:", success)

        break

cap.release()
cv2.destroyAllWindows()
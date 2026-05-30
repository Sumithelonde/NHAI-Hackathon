from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import cv2

from insightface.app import FaceAnalysis

from src.liveness.challenge import (
    ChallengeEngine
)

app = FaceAnalysis(
    providers=['CPUExecutionProvider']
)

app.prepare(ctx_id=0)

engine = ChallengeEngine()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    faces = app.get(frame)

    if len(faces):

        face = faces[0]

        bbox = face.bbox

        kps = face.kps

        x1,y1,x2,y2 = bbox

        face_width = x2 - x1
        face_height = y2 - y1

        face_area = (
            face_width *
            face_height
        )

        nose = kps[2]

        nose_x_ratio = (
            nose[0] - x1
        ) / face_width

        live = engine.update(
            nose_x_ratio,
            face_area
        )

        instruction = (
            engine.get_instruction()
        )

        cv2.putText(
            frame,
            instruction,
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            f"Live: {live}",
            (20,90),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

    cv2.imshow(
        "Challenge Liveness",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
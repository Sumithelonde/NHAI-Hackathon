# API Contract

## 1. Enrollment API

Description:

Creates and stores a face embedding for a user.

Function:

enroll(
image,
save_path
)

Parameters:

image:
OpenCV image frame

save_path:
Path to store embedding

Example:

enroll(
frame,
"data/embeddings/sumit.npy"
)

Return:

True
or
False

---

## 2. Verification API

Description:

Verifies whether the current face matches the enrolled face.

Function:

verify(
image,
embedding_path
)

Parameters:

image:
Current camera frame

embedding_path:
Path to stored embedding

Example:

verify(
frame,
"data/embeddings/sumit.npy"
)

Response:

{
"score": 0.84,
"match": true
}

---

## 3. Authentication API

Description:

Combines liveness verification and face verification.

Function:

authenticate(
image,
embedding_path,
liveness_passed
)

Parameters:

image:
Current camera frame

embedding_path:
Stored face embedding

liveness_passed:
Boolean result from challenge engine

Example:

authenticate(
frame,
"data/embeddings/sumit.npy",
True
)

Response:

{
"success": true,
"score": 0.84,
"message": "Authentication Success"
}

---

## 4. Challenge Engine

Description:

Offline challenge-response liveness verification.

Class:

ChallengeEngine()

Methods:

get_instruction()

Returns:

* Turn Head Left
* Turn Head Right
* Move Closer To Camera

update(
nose_x_ratio,
face_area
)

Returns:

True if all challenges are completed.

reset()

Resets challenge sequence.

get_progress()

Returns:

{
"step": 1,
"total_steps": 3,
"completed": false,
"current_instruction": "Turn Head Left"
}

---

## Embedding Specification

Model:

InsightFace Buffalo_L

Embedding Dimension:

512

Data Type:

float32

Format:

numpy.ndarray

Example:

[
0.183,
-0.447,
0.092,
...
]

Similarity Metric:

Cosine Similarity

Matching Threshold:

0.72

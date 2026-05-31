# Face Detection Model

File:
det_10g.onnx

Purpose:
Detect faces from camera frames.

Input:
RGB Image

Output:
Face Bounding Boxes
Face Keypoints

---

# Face Landmark Model

File:
2d106det.onnx

Purpose:
Extract 106 facial landmarks.

Used For:
Head pose estimation
Challenge verification
Face alignment

Output:
106 Facial Landmark Points

---

# Face Recognition Model

File:
w600k_r50.onnx

Purpose:
Generate face embeddings.

Input:
Aligned Face

Input Size:
112 x 112 RGB

Output:
512-dimensional embedding

Type:
float32[512]

Example:

[0.12, -0.45, 0.33, ...]

---

# Face Matching

Metric:
Cosine Similarity

Threshold:
0.72

score >= 0.72
→ Match

score < 0.72
→ No Match
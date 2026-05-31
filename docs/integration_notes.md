# Enrollment Flow

Camera
→ Face Detection
→ Face Alignment
→ Face Recognition
→ 512-D Embedding
→ SQLite Storage

---

# Authentication Flow

Camera
→ Face Detection
→ Face Alignment
→ Face Recognition
→ Current Embedding

Stored Embedding
+
Current Embedding

→ Cosine Similarity

Threshold = 0.72

If score >= 0.72:
Authentication Success

Else:
Authentication Failed

---

# Liveness Flow

Challenge-Based

Challenges:

1. Turn Head Left
2. Turn Head Right
3. Move Closer

Challenge order is randomized.

All challenges must pass before authentication begins.
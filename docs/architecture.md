# Face Authentication System Architecture

## Overview

This project implements an offline facial authentication system with challenge-based liveness detection. The system is designed for Android and iOS integration through React Native and performs all recognition operations locally without requiring continuous internet connectivity.

## System Architecture

Camera Input
→ Face Detection
→ Face Embedding Generation
→ Challenge-Based Liveness Verification
→ Face Matching
→ Authentication Decision

## Components

### 1. Face Detection & Recognition

Model: InsightFace Buffalo_L

Responsibilities:

* Detect faces from camera frames
* Generate 512-dimensional face embeddings
* Extract facial keypoints required for liveness detection

Output:

* Face Bounding Box
* Facial Keypoints
* 512-D Face Embedding

### 2. Enrollment Module

File:

src/api/enroll.py

Responsibilities:

* Capture user's face
* Generate embedding
* Store embedding locally as .npy file

Output:

Stored face embedding

### 3. Verification Module

File:

src/api/verify.py

Responsibilities:

* Generate embedding from current frame
* Load enrolled embedding
* Compute cosine similarity
* Return match result

Threshold:

0.72

Output:

{
"score": similarity_score,
"match": true/false
}

### 4. Liveness Detection Module

File:

src/liveness/challenge.py

Method:

Challenge-Response Verification

Supported Challenges:

* Turn Head Left
* Turn Head Right
* Move Closer To Camera

Features:

* Random challenge order
* Offline operation
* No server dependency

Output:

True / False

### 5. Authentication Module

File:

src/api/authenticate.py

Responsibilities:

* Validate liveness result
* Perform face verification
* Return final authentication decision

Output:

{
"success": true,
"score": 0.84,
"message": "Authentication Success"
}

## Security Design

* Raw images are not stored.
* Only face embeddings are stored locally.
* Authentication is performed using cosine similarity.
* Liveness verification reduces spoofing attempts.

## Performance

Model: InsightFace Buffalo_L

Embedding Size: 512

Average Inference Time: 1.31 seconds

Average FPS: 0.76

Runtime: ONNX Runtime

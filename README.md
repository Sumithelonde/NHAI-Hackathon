# Offline Face Authentication System

## Overview

This project implements an offline facial authentication system with challenge-based liveness detection using InsightFace and ONNX Runtime.

The system is designed for Android and iOS integration through React Native and performs all face recognition operations locally without requiring continuous internet connectivity.

## Features

* Offline face enrollment
* Offline face verification
* Challenge-response liveness detection
* Face embedding generation
* Cosine similarity matching
* Local embedding storage
* React Native integration ready
* ONNX Runtime based inference

## Technology Stack

### AI & Computer Vision

* InsightFace Buffalo_L
* ONNX Runtime
* OpenCV
* NumPy
* Scikit-Learn

### Mobile Integration

* React Native
* Android
* iOS

## Project Structure

```text
face-auth-ai/
├─ data/
│  ├─ embeddings/
│  └─ samples/
├─ docs/
│  ├─ api_contract.md
│  ├─ architecture.md
│  └─ benchmark.md
├─ src/
│  ├─ api/
│  ├─ liveness/
│  ├─ recognition/
│  ├─ config.py
│  └─ version.py
├─ tests/
├─ README.md
└─ requirements.txt
```

## System Architecture

```text
Camera Input
      ↓
Face Detection
      ↓
Face Embedding Generation
      ↓
Challenge-Based Liveness Detection
      ↓
Face Verification
      ↓
Authentication Decision
```

## Recognition Pipeline

### Face Detection

Model:

* InsightFace Buffalo_L

Output:

* Face Bounding Box
* Facial Keypoints
* Face Embedding

### Face Embedding

Embedding Size:

```text
512 Dimensions
```

Example:

```python
[
  0.183,
 -0.447,
  0.092,
  ...
]
```

### Face Matching

Similarity Metric:

```text
Cosine Similarity
```

Threshold:

```text
0.72
```

## Liveness Detection

The system uses challenge-response verification.

Supported Challenges:

1. Turn Head Left
2. Turn Head Right
3. Move Closer To Camera

Features:

* Random challenge order
* Fully offline
* No cloud dependency
* Resistant to simple photo attacks

## Enrollment Workflow

```text
User Face
    ↓
Capture Image
    ↓
Generate Embedding
    ↓
Store Embedding
```

API:

```python
enroll(
    image,
    save_path
)
```

## Verification Workflow

```text
Current Face
      ↓
Generate Embedding
      ↓
Load Stored Embedding
      ↓
Cosine Similarity
      ↓
Match / No Match
```

API:

```python
verify(
    image,
    embedding_path
)
```

Response:

```python
{
    "score": 0.84,
    "match": True
}
```

## Authentication Workflow

```text
Face Capture
      ↓
Liveness Verification
      ↓
Face Verification
      ↓
Authentication Result
```

API:

```python
authenticate(
    image,
    embedding_path,
    liveness_passed
)
```

Response:

```python
{
    "success": True,
    "score": 0.84,
    "message": "Authentication Success"
}
```

## Installation

### Clone Repository

```bash
git clone <repository_url>
cd face-auth-ai
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running Tests

### Enrollment

```bash
python tests/test_enroll.py
```

### Verification

```bash
python tests/test_verify.py
```

### Authentication

```bash
python tests/test_authentication.py
```

### Liveness Detection

```bash
python tests/test_challenge.py
```

### Benchmark

```bash
python tests/benchmark.py
```

## Performance Benchmark

### Hardware

* Windows 11
* NVIDIA RTX 4050 Laptop GPU
* ONNX Runtime (CPU Execution Provider)

### Model

* InsightFace Buffalo_L
* Embedding Dimension: 512

### Results

Average Inference Time:

```text
1.31 seconds
```

Average FPS:

```text
0.76 FPS
```

## Security Considerations

* Raw face images are not stored.
* Authentication uses face embeddings.
* Liveness verification reduces spoofing attempts.
* Offline processing minimizes data exposure.

## Mobile Integration

The mobile application can integrate with the AI module using:

### Enrollment

```python
enroll(image, save_path)
```

### Verification

```python
verify(image, embedding_path)
```

### Authentication

```python
authenticate(
    image,
    embedding_path,
    liveness_passed
)
```

### Challenge Engine

```python
engine = ChallengeEngine()
```

Methods:

```python
engine.get_instruction()

engine.update(
    nose_x_ratio,
    face_area
)

engine.reset()
```

## Future Improvements

* GPU acceleration using CUDA
* MobileFaceNet deployment
* TensorFlow Lite conversion
* Secure embedding encryption
* AWS synchronization
* Multi-user enrollment support

## Version

Version:

```text
1.0.0
```

Model:

```text
InsightFace Buffalo_L
```

## Authors

AI Development:
Sumit

Mobile Development:
Team Member

Hackathon Project – Offline Face Authentication System

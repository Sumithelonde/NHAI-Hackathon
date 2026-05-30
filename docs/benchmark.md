# Benchmark Results

## Hardware

* Windows 11
* NVIDIA RTX 4050 Laptop GPU
* CPU Execution Provider (ONNX Runtime)

## Model

* InsightFace Buffalo_L
* Embedding Size: 512

## Performance

Average Inference Time: 1.31 seconds

Average FPS: 0.76

## Notes

The benchmark was executed using ONNX Runtime on CPU.

GPU acceleration was not enabled due to missing CUDA runtime dependencies.

The current performance is sufficient for enrollment and authentication workflows where real-time frame processing is not required.

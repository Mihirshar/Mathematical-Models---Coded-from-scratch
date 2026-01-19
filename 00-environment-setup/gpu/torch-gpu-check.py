#!/usr/bin/env python3
"""
Script to check if PyTorch can detect and use GPU.
"""

import torch


def check_gpu():
    """Check GPU availability and print information."""
    print("PyTorch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("CUDA version:", torch.version.cuda)
        print("Number of GPUs:", torch.cuda.device_count())
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("No GPU detected. Using CPU.")


if __name__ == "__main__":
    check_gpu()

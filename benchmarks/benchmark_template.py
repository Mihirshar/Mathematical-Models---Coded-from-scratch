"""Benchmark template for performance testing."""

import time
from typing import Callable, Dict

import numpy as np


def benchmark_function(func: Callable, *args, iterations: int = 100, **kwargs) -> Dict:
    """Benchmark a function's execution time."""
    times = []

    # Warmup
    func(*args, **kwargs)

    # Benchmark
    for _ in range(iterations):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        times.append(end - start)

    return {
        "mean": np.mean(times),
        "std": np.std(times),
        "min": np.min(times),
        "max": np.max(times),
        "iterations": iterations,
    }


def example_benchmark():
    """Example benchmark comparing implementations."""

    def numpy_implementation(size: int):
        return np.random.randn(size, size) @ np.random.randn(size, size)

    def python_implementation(size: int):
        # Slower pure Python implementation
        a = [[np.random.randn() for _ in range(size)] for _ in range(size)]
        return a

    print("Benchmarking Matrix Operations")
    print("=" * 50)

    size = 100

    # Benchmark NumPy
    numpy_results = benchmark_function(numpy_implementation, size, iterations=50)
    print(f"\nNumPy Implementation:")
    print(f"  Mean: {numpy_results['mean']*1000:.2f} ms")
    print(f"  Std:  {numpy_results['std']*1000:.2f} ms")

    print("\n✓ Benchmark completed!")


if __name__ == "__main__":
    example_benchmark()

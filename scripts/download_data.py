#!/usr/bin/env python3
"""Script to download common datasets."""

import argparse
from pathlib import Path
import urllib.request
import gzip
import shutil


def download_mnist(data_dir: Path) -> None:
    """Download MNIST dataset."""
    print("Downloading MNIST dataset...")
    base_url = "http://yann.lecun.com/exdb/mnist/"
    files = [
        "train-images-idx3-ubyte.gz",
        "train-labels-idx1-ubyte.gz",
        "t10k-images-idx3-ubyte.gz",
        "t10k-labels-idx1-ubyte.gz",
    ]
    
    mnist_dir = data_dir / "raw" / "mnist"
    mnist_dir.mkdir(parents=True, exist_ok=True)
    
    for file in files:
        url = base_url + file
        filepath = mnist_dir / file
        if not filepath.exists():
            print(f"Downloading {file}...")
            urllib.request.urlretrieve(url, filepath)
            # Uncompress
            with gzip.open(filepath, 'rb') as f_in:
                with open(filepath.with_suffix(''), 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
    
    print("MNIST download complete!")


def main():
    parser = argparse.ArgumentParser(description="Download datasets")
    parser.add_argument(
        "--dataset",
        type=str,
        default="mnist",
        choices=["mnist", "cifar10", "imdb"],
        help="Dataset to download"
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="Data directory"
    )
    
    args = parser.parse_args()
    
    if args.dataset == "mnist":
        download_mnist(args.data_dir)
    else:
        print(f"Dataset {args.dataset} not yet implemented")


if __name__ == "__main__":
    main()

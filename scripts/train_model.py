#!/usr/bin/env python3
"""Template script for training models."""

import argparse
import json
from pathlib import Path


def train_model(config_path: Path, output_dir: Path) -> None:
    """Train a model with given configuration."""
    print(f"Loading configuration from {config_path}")

    # Load config
    with open(config_path) as f:
        config = json.load(f)

    print(f"Training model: {config.get('model_name', 'unknown')}")

    # TODO: Implement training logic

    print(f"Model saved to {output_dir}")


def main():
    parser = argparse.ArgumentParser(description="Train ML model")
    parser.add_argument(
        "--config", type=Path, required=True, help="Path to configuration file"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("models/checkpoints"),
        help="Output directory for model",
    )

    args = parser.parse_args()
    train_model(args.config, args.output_dir)


if __name__ == "__main__":
    main()

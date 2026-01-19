# Data Directory

This directory contains datasets used in the repository.

## Structure

- `raw/` - Original, immutable data
- `processed/` - Cleaned and transformed data ready for modeling
- `external/` - Data from third-party sources
- `interim/` - Intermediate data transformations

## Data Sources

### Common Datasets
- MNIST - Handwritten digits
- CIFAR-10 - Image classification
- IMDB - Sentiment analysis
- WikiText - Language modeling

## Usage

```python
from pathlib import Path

# Load raw data
raw_data_path = Path("data/raw/dataset.csv")

# Save processed data
processed_data_path = Path("data/processed/dataset_clean.csv")
```

## Data Versioning

Consider using DVC (Data Version Control) for large datasets:

```bash
dvc init
dvc add data/raw/large_dataset.csv
git add data/raw/large_dataset.csv.dvc
```

## .gitignore

Large data files are excluded from git. See `.gitignore` for details.

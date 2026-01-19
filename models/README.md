# Models Directory

Storage for trained models, checkpoints, and pre-trained weights.

## Structure

- `pretrained/` - Pre-trained model weights (e.g., from Hugging Face)
- `checkpoints/` - Training checkpoints and intermediate models
- `exports/` - Exported models for deployment (ONNX, TorchScript, etc.)

## Usage

### Saving Models

```python
import torch

# Save PyTorch model
torch.save(model.state_dict(), 'models/checkpoints/model_epoch_10.pth')

# Save entire model
torch.save(model, 'models/checkpoints/model_complete.pth')
```

### Loading Models

```python
# Load state dict
model.load_state_dict(torch.load('models/checkpoints/model_epoch_10.pth'))

# Load entire model
model = torch.load('models/checkpoints/model_complete.pth')
```

## Model Versioning

Consider using MLflow or DVC for model versioning:

```python
import mlflow

# Log model with MLflow
mlflow.pytorch.log_model(model, "model")
```

## .gitignore

Model files are excluded from git due to size. Use Git LFS or model registries for sharing.

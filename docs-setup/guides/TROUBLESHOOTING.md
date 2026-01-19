# Troubleshooting Guide

## Installation Issues

### pip install fails
**Problem**: Dependencies fail to install

**Solutions**:
1. Upgrade pip: `pip install --upgrade pip`
2. Use virtual environment: `python -m venv venv`
3. Install build tools if needed

### CUDA not detected
**Problem**: PyTorch can't find GPU

**Solutions**:
1. Check CUDA installation: `nvidia-smi`
2. Install correct PyTorch version for your CUDA
3. Run: `python 00-environment-setup/gpu/torch-gpu-check.py`

## Runtime Issues

### Out of Memory errors
**Problem**: GPU/RAM runs out of memory

**Solutions**:
1. Reduce batch size
2. Use gradient accumulation
3. Enable mixed precision training
4. Use smaller model

### Import errors
**Problem**: Module not found

**Solutions**:
1. Ensure virtual environment is activated
2. Install missing package: `pip install <package>`
3. Check PYTHONPATH

## Common Errors

### ModuleNotFoundError
```python
# Add project root to path
import sys
sys.path.append('path/to/project')
```

### CUDA out of memory
```python
# Clear cache
import torch
torch.cuda.empty_cache()
```

## Getting Help

1. Check this troubleshooting guide
2. Search existing GitHub issues
3. Open a new issue with:
   - Error message
   - Steps to reproduce
   - Environment details

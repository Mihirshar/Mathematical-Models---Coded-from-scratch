# Regularization Techniques

Techniques to prevent overfitting and improve generalization in deep neural networks.

## Contents

- **dropout/** - Randomly disabling neurons during training
- **batch-normalization/** - Normalizing inputs to each layer
- **early-stopping/** - Stopping training when validation performance stops improving
- **weight-decay/** - Adding penalty to large weights (L2 regularization)

## Overfitting Problem

Deep networks can memorize training data:
- High training accuracy
- Poor test accuracy
- Model doesn't generalize
- Needs regularization

## Dropout

Randomly sets some neurons to zero:
- Prevents co-adaptation
- Forces network to be robust
- Reduces overfitting
- Commonly used (0.2-0.5 dropout rate)

## Batch Normalization

Normalizes layer inputs:
- Stabilizes training
- Allows higher learning rates
- Reduces internal covariate shift
- Often improves performance

## Early Stopping

Monitor validation loss:
- Stop when validation loss stops decreasing
- Prevents overfitting to training data
- Simple and effective
- Saves training time

## Weight Decay

Penalizes large weights:
- L2 regularization
- Prevents weights from growing too large
- Encourages simpler models
- Reduces overfitting

## Best Practices

- Use dropout in hidden layers
- Apply batch normalization
- Monitor validation metrics
- Use early stopping
- Combine multiple techniques

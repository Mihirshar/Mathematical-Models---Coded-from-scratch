# Convolutional Neural Networks (CNNs)

Specialized neural networks for processing grid-like data such as images.

## Contents

- **convolution-basics/** - Understanding convolution operations
- **architectures/** - Popular CNN architectures (LeNet, AlexNet, VGG, ResNet)
- **image-classification/** - Applying CNNs to image classification tasks
- **transfer-learning/** - Using pre-trained models for your tasks

## Why CNNs for Images?

- **Translation Invariance**: Recognizes objects regardless of position
- **Parameter Sharing**: Same filters used across image
- **Spatial Hierarchy**: Learns from local to global patterns
- **Efficiency**: Fewer parameters than fully connected networks

## Key Components

### Convolutional Layers
- Apply filters to detect features
- Learn edge detectors, textures, patterns
- Preserve spatial relationships

### Pooling Layers
- Reduce spatial dimensions
- Max pooling, average pooling
- Reduces computation
- Provides translation invariance

### Fully Connected Layers
- Final classification layers
- Process high-level features
- Output predictions

## Popular Architectures

- **LeNet**: Early CNN for digit recognition
- **AlexNet**: Breakthrough in ImageNet 2012
- **VGG**: Deep networks with small filters
- **ResNet**: Residual connections for very deep networks
- **EfficientNet**: Efficient and accurate models

## Transfer Learning

Using pre-trained models:
- Train on large dataset (ImageNet)
- Fine-tune on your dataset
- Saves time and resources
- Often better than training from scratch

## Applications

- Image classification
- Object detection
- Image segmentation
- Medical imaging
- Autonomous vehicles

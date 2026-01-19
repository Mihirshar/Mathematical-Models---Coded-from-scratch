# Neural Network Basics

Understanding the fundamental building blocks of neural networks.

## Contents

- **perceptron/** - The simplest neural unit, foundation of neural networks
- **activation-functions/** - Non-linear functions that enable learning complex patterns
- **loss-functions/** - Measuring how wrong predictions are
- **gradient-descent/** - Optimization algorithm for training
- **backpropagation/** - Algorithm for computing gradients efficiently

## Perceptron

The basic building block:
- Takes weighted sum of inputs
- Applies activation function
- Produces output
- Can learn simple patterns

## Activation Functions

Introduce non-linearity:
- **Sigmoid**: S-shaped curve, outputs 0-1
- **Tanh**: Similar to sigmoid, outputs -1 to 1
- **ReLU**: Rectified Linear Unit, most common
- **Softmax**: For multi-class classification

## Loss Functions

Measure prediction error:
- **MSE**: Mean Squared Error for regression
- **Cross-Entropy**: For classification
- **Hinge Loss**: For SVM-like models

## Gradient Descent

Optimization algorithm:
- Starts with random weights
- Computes gradient of loss
- Updates weights in direction that reduces loss
- Repeats until convergence

## Backpropagation

Efficient gradient computation:
- Forward pass: compute predictions
- Backward pass: compute gradients
- Chain rule: propagate errors backward
- Update weights using gradients

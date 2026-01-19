# Ensemble Learning

Ensemble methods combine multiple models to achieve better performance than individual models.

## Contents

- **bagging/** - Bootstrap Aggregating: training multiple models on different data subsets
- **random-forest/** - Ensemble of decision trees using bagging
- **boosting/** - Sequential training where each model corrects previous errors
- **gradient-boosting/** - Boosting using gradient descent optimization
- **xgboost-lightgbm/** - Advanced gradient boosting implementations
- **ensemble-comparisons/** - Comparing different ensemble techniques

## Key Concepts

### Bagging (Bootstrap Aggregating)
- Train multiple models on different subsets
- Average predictions (regression) or vote (classification)
- Reduces variance

### Boosting
- Train models sequentially
- Each model focuses on errors of previous models
- Reduces bias

### Random Forest
- Ensemble of decision trees
- Uses bagging + random feature selection
- Robust and handles overfitting well

### Gradient Boosting
- Sequential ensemble using gradient descent
- Each model fits residuals of previous models
- Very powerful but can overfit

## Advantages

- Better accuracy than single models
- More robust to overfitting
- Handles complex patterns better
- Reduces variance and bias

## Use Cases

- Winning Kaggle competitions
- Production ML systems
- When single models aren't accurate enough

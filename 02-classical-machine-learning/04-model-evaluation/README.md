# Model Evaluation

Proper evaluation is crucial for selecting the best model and understanding its performance.

## Contents

- **regression-metrics/** - Metrics for regression models (MSE, RMSE, MAE, R²)
- **classification-metrics/** - Metrics for classification (accuracy, precision, recall, F1, ROC-AUC)
- **cross-validation/** - Techniques for robust model evaluation
- **hyperparameter-tuning/** - Finding optimal model parameters
- **model-selection/** - Comparing and selecting best models

## Key Concepts

### Cross-Validation
- K-fold cross-validation
- Stratified cross-validation
- Time series cross-validation
- Prevents overfitting to a single train/test split

### Hyperparameter Tuning
- Grid search
- Random search
- Bayesian optimization
- Finding best model configuration

### Model Selection
- Comparing multiple models
- Bias-variance tradeoff
- Occam's razor principle
- Balancing complexity and performance

## Best Practices

- Always use cross-validation
- Separate validation set for hyperparameter tuning
- Keep test set completely unseen until final evaluation
- Consider multiple metrics, not just accuracy
- Understand your problem domain

## Common Pitfalls

- Data leakage
- Overfitting to validation set
- Using test set for model selection
- Ignoring class imbalance
- Not considering business metrics

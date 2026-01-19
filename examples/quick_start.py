"""Quick start example for the repository."""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def main():
    """Run a simple linear regression example."""
    print("AI/ML Generative Foundations - Quick Start Example")
    print("=" * 50)
    
    # Generate sample data
    np.random.seed(42)
    X = np.random.randn(100, 1)
    y = 2 * X + 1 + np.random.randn(100, 1) * 0.1
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\nModel Coefficients: {model.coef_[0][0]:.4f}")
    print(f"Model Intercept: {model.intercept_[0]:.4f}")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R² Score: {r2:.4f}")
    
    print("\n✓ Quick start example completed successfully!")


if __name__ == "__main__":
    main()

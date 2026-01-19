"""Linear Regression from Scratch - Placeholder."""

import numpy as np
from typing import Tuple, Optional


class LinearRegressionScratch:
    """
    Linear Regression implemented from scratch using NumPy.
    
    Parameters:
    -----------
    learning_rate : float, default=0.01
        Learning rate for gradient descent
    n_iterations : int, default=1000
        Number of iterations for gradient descent
    
    Attributes:
    -----------
    weights : np.ndarray
        Model weights
    bias : float
        Model bias term
    
    TODO: Implement the full class
    """
    
    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        """Initialize the model."""
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.cost_history = []
    
    def fit(self, X: np.ndarray, y: np.ndarray) -> 'LinearRegressionScratch':
        """
        Fit the model using gradient descent.
        
        Args:
            X: Training features, shape (n_samples, n_features)
            y: Target values, shape (n_samples,)
        
        Returns:
            self: Fitted model
        
        TODO: Implement gradient descent training
        """
        pass
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions.
        
        Args:
            X: Features, shape (n_samples, n_features)
        
        Returns:
            np.ndarray: Predictions
        
        TODO: Implement prediction
        """
        pass
    
    def _compute_cost(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Compute MSE cost.
        
        Args:
            X: Features
            y: True values
        
        Returns:
            float: Cost value
        
        TODO: Implement cost computation
        """
        pass


def normal_equation(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Solve linear regression using normal equation.
    
    Args:
        X: Features
        y: Target values
    
    Returns:
        np.ndarray: Optimal weights
    
    TODO: Implement normal equation solution
    """
    pass


if __name__ == "__main__":
    print("Linear Regression from Scratch - Placeholder")
    print("TODO: Add actual implementation")

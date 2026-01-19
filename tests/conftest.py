"""Pytest configuration and fixtures."""
import pytest
import numpy as np


@pytest.fixture
def sample_data():
    """Fixture providing sample data for tests."""
    return np.random.randn(100, 10)


@pytest.fixture
def sample_labels():
    """Fixture providing sample labels for tests."""
    return np.random.randint(0, 2, 100)

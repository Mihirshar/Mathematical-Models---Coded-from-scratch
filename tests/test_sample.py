"""Sample test file to verify testing infrastructure."""
import pytest


def test_sample():
    """Sample test that always passes."""
    assert True


@pytest.mark.slow
def test_slow_operation():
    """Example of a slow test."""
    import time
    time.sleep(0.1)
    assert True


class TestSampleClass:
    """Sample test class."""
    
    def test_method(self):
        """Sample test method."""
        assert 1 + 1 == 2

#!/bin/bash
# Setup script for development environment

echo "Setting up AI/ML Generative Foundations environment..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements/base.txt
pip install -r requirements/dev.txt

# Install pre-commit hooks
echo "Installing pre-commit hooks..."
pre-commit install

# Setup directories
echo "Creating necessary directories..."
python setup_enhanced_structure.py

echo "Setup complete! Activate the environment with: source venv/bin/activate"

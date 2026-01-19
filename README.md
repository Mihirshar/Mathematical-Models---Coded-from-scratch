# AI/ML Generative Foundations

<div align="center">

**A comprehensive, structured repository for learning AI, Machine Learning, and Generative AI foundations from scratch**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

## 📚 Overview

This repository provides a complete, structured learning path covering everything from Python fundamentals and mathematical foundations to advanced topics in Generative AI, Large Language Models, and MLOps. Whether you're a beginner starting your journey in AI/ML or an experienced practitioner looking to deepen your understanding, this repository offers comprehensive resources, implementations, and projects.

### What You'll Learn

- **Mathematical Foundations**: Linear algebra, calculus, probability, and statistics with ML applications
- **Classical Machine Learning**: Supervised and unsupervised learning algorithms implemented from scratch
- **Deep Learning**: Neural networks, CNNs, RNNs, and optimization techniques
- **Natural Language Processing**: Text preprocessing, vectorization, and sequence modeling
- **Generative AI**: Transformers, LLMs, prompt engineering, fine-tuning, and GenAI applications
- **Reinforcement Learning**: RL basics, classical RL, and deep RL
- **MLOps & Production**: Experiment tracking, model deployment, monitoring, and cloud integrations

---

## 🏗️ Repository Infrastructure

This repository includes a complete development infrastructure:

### Testing & Quality Assurance
- **pytest** - Comprehensive testing framework
- **Coverage reporting** - Track test coverage
- **Unit tests** - Test individual components
- **Integration tests** - Test component interactions
- **Test fixtures** - Reusable test data

### CI/CD Pipeline
- **GitHub Actions** - Automated workflows
- **Continuous Integration** - Run tests on every push
- **Code Quality Checks** - Automated linting and formatting
- **Pre-commit Hooks** - Local quality checks before commit

### Development Tools
- **Makefile** - Common development commands
- **Black** - Automatic code formatting
- **Flake8** - Code linting
- **isort** - Import sorting
- **mypy** - Static type checking
- **Bandit** - Security scanning

### Documentation
- **MkDocs** - Documentation site generator
- **Setup Guides** - Comprehensive setup instructions in `docs-setup/`
- **API Documentation** - Auto-generated from docstrings
- **Examples** - Ready-to-run code samples

### Project Organization
- **Modular Requirements** - Separate dependencies for different use cases
- **Configuration Management** - Centralized configs in `configs/`
- **Data Management** - Organized data directories
- **Model Storage** - Structured model versioning
- **Deployment Templates** - FastAPI, Kubernetes, serverless

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip or conda package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mihirshar/Mathematical-Models---Coded-from-scratch.git
   cd Mathematical-Models---Coded-from-scratch
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Install base dependencies
   pip install -r requirements/base.txt
   
   # Or install all dependencies including dev tools
   pip install -r requirements/dev.txt
   ```

4. **Verify setup** (optional)
   ```bash
   # Run tests
   pytest tests/
   
   # Check GPU availability
   python 00-environment-setup/gpu/torch-gpu-check.py
   ```

### 📚 Documentation & Setup Guides

This repository includes comprehensive setup documentation:

- **Quick Start**: See `docs-setup/guides/QUICK_START.md` for a 5-minute setup guide
- **Detailed Setup**: See `docs-setup/guides/SETUP_GUIDE.md` for comprehensive instructions
- **Setup Checklist**: See `docs-setup/guides/SETUP_CHECKLIST.md` to verify your setup
- **Troubleshooting**: See `docs-setup/guides/TROUBLESHOOTING.md` for common issues
- **All Documentation**: Browse `docs-setup/` for complete setup documentation

---

## 📁 Repository Structure

```
Mathematical-Models---Coded-from-scratch/
│
├── 📖 README.md                    # This file
├── 🗺️  ROADMAP.md                  # Learning roadmap (in README-guides/)
├── 🤝 CONTRIBUTING.md              # Contribution guidelines
├── � CODE_OF_CONDUCT.md           # Community standards
├── 🔐 LICENSE                      # MIT License
│
├── � docs-setup/                  # Setup documentation
│   ├── guides/                     # Setup guides and tutorials
│   ├── analysis/                   # Enhancement analysis documents
│   ├── scripts/                    # Script documentation
│   └── README.md                   # Setup documentation index
│
├── � docs-project-setup/          # Additional project documentation
│
├── 🧪 tests/                       # Testing infrastructure
│   ├── unit/                       # Unit tests
│   ├── integration/                # Integration tests
│   ├── fixtures/                   # Test fixtures
│   └── conftest.py                 # Pytest configuration
│
├── 📦 requirements/                # Dependency management
│   ├── base.txt                    # Core dependencies
│   ├── dev.txt                     # Development tools
│   ├── test.txt                    # Testing dependencies
│   ├── docs.txt                    # Documentation tools
│   ├── deep_learning.txt           # Deep learning frameworks
│   ├── nlp.txt                     # NLP/GenAI packages
│   ├── mlops.txt                   # MLOps tools
│   └── gpu.txt                     # GPU-specific packages
│
├── 🔧 scripts/                     # Utility scripts
│   ├── download_data.py            # Data acquisition
│   ├── setup_environment.sh        # Environment setup
│   └── train_model.py              # Training template
│
├── 💡 examples/                    # Quick-start examples
│   ├── quick_start.py              # Basic example
│   └── neural_network_example.py  # Neural network demo
│
├── 📓 notebooks/                   # Jupyter notebooks
│   ├── 01-foundations/             # Foundation notebooks
│   ├── 02-classical-ml/            # Classical ML notebooks
│   ├── 03-deep-learning/           # Deep learning notebooks
│   ├── 04-nlp/                     # NLP notebooks
│   ├── 05-genai/                   # GenAI notebooks
│   ├── 06-rl/                      # RL notebooks
│   ├── 07-mlops/                   # MLOps notebooks
│   └── exploratory/                # Experimental notebooks
│
├── 🎨 assets/                      # Images and diagrams
│   ├── images/                     # Screenshots and photos
│   ├── diagrams/                   # Architecture diagrams
│   └── presentations/              # Slide decks
│
├── ⚙️  configs/                    # Configuration files
│   ├── model/                      # Model configurations
│   ├── training/                   # Training hyperparameters
│   ├── data/                       # Data processing configs
│   └── logging_config.py           # Logging setup
│
├── 💾 data/                        # Data management
│   ├── raw/                        # Original datasets
│   ├── processed/                  # Cleaned datasets
│   ├── external/                   # Third-party data
│   └── interim/                    # Intermediate data
│
├── 🤖 models/                      # Model storage
│   ├── pretrained/                 # Pre-trained models
│   ├── checkpoints/                # Training checkpoints
│   └── exports/                    # Exported models
│
├── ⚡ benchmarks/                  # Performance tests
│   └── benchmark_template.py       # Benchmark utilities
│
├── 🚀 deployment/                  # Deployment templates
│   ├── api/                        # FastAPI templates
│   ├── kubernetes/                 # K8s manifests
│   └── serverless/                 # Serverless configs
│
├── 📚 resources/                   # Learning resources
│   ├── books.md                    # Recommended books
│   ├── courses.md                  # Online courses
│   └── papers/                     # Research papers
│
├── 📦 src/ml_foundations/          # Python package
│   ├── classical_ml/               # Classical ML modules
│   ├── deep_learning/              # Deep learning modules
│   ├── nlp/                        # NLP modules
│   ├── genai/                      # GenAI modules
│   └── utils/                      # Utility functions
│
├── 🛠️  00-environment-setup/       # Environment configuration
│   ├── local/                      # Local Python setup
│   ├── gpu/                        # GPU/CUDA setup
│   ├── docker/                     # Docker containers
│   └── cloud/                      # Cloud platform setup
│
├── 🐍 01-python-and-math-foundations/
│   ├── python/                     # Python fundamentals
│   ├── numpy-pandas/               # Data manipulation
│   ├── linear-algebra/             # Vectors, matrices, SVD
│   ├── calculus/                   # Derivatives, gradients
│   ├── probability/                # Distributions, Bayesian
│   └── statistics/                 # Descriptive, inferential
│
├── 🤖 02-classical-machine-learning/
│   ├── 01-supervised-learning/     # Regression, classification
│   ├── 02-ensemble-learning/       # Bagging, boosting
│   ├── 03-unsupervised-learning/   # Clustering, PCA
│   └── 04-model-evaluation/        # Metrics, validation
│
├── 🧠 03-deep-learning/
│   ├── 01-neural-network-basics/   # Perceptron, backprop
│   ├── 02-feedforward-networks/    # From scratch, PyTorch
│   ├── 03-regularization-techniques/ # Dropout, batch norm
│   ├── 04-cnn/                     # Convolution, architectures
│   ├── 05-rnn/                     # LSTM, GRU, sequences
│   ├── 06-optimization/            # Optimizers, schedulers
│   ├── 07-autoencoders/            # Autoencoders, VAEs
│   └── 08-gans/                    # Generative adversarial networks
│
├── 💬 04-natural-language-processing/
│   ├── 01-text-preprocessing/      # Tokenization, cleaning
│   ├── 02-vectorization/           # TF-IDF, embeddings
│   ├── 03-sequence-models/         # RNN, LSTM for NLP
│   ├── 04-nlp-tasks/               # Classification, NER
│   └── 05-word-embeddings/         # Word2Vec, GloVe
│
├── ✨ 05-generative-ai/
│   ├── 01-foundations/             # Generative vs discriminative
│   ├── 02-transformers/            # Attention, multi-head
│   ├── 03-large-language-models/   # GPT, BERT, LLaMA
│   ├── 04-prompt-engineering/      # Zero-shot, few-shot
│   ├── 05-fine-tuning/             # PEFT, LoRA, instruction
│   ├── 06-genai-applications/      # RAG, agents, chatbots
│   ├── 07-diffusion-models/        # Stable Diffusion
│   └── 08-multimodal/              # Vision-language models
│
├── 🎮 06-reinforcement-learning/
│   ├── 01-rl-basics/               # MDP, value functions
│   ├── 02-classical-rl/            # Q-learning, SARSA
│   ├── 03-deep-rl/                 # DQN, policy gradients
│   └── 04-rl-applications/         # Game playing, robotics
│
├── 🏭 07-mlops-and-production/
│   ├── experiment-tracking/        # MLflow, W&B
│   ├── model-versioning/           # Model registry
│   ├── deployment/                 # Serving, APIs
│   ├── monitoring/                 # Model monitoring
│   ├── cloud-integrations/         # AWS, GCP, Azure
│   ├── ab-testing/                 # A/B testing
│   └── data-pipelines/             # ETL pipelines
│
├── 🎯 08-projects/
│   ├── beginner/                   # Starter projects
│   ├── intermediate/               # Intermediate projects
│   ├── advanced/                   # Advanced projects
│   └── genai-capstone/             # GenAI capstone
│
└── 🛠️  utils/                      # Utility modules
    ├── data/                       # Data utilities
    ├── math/                       # Math utilities
    ├── visualization/              # Plotting tools
    ├── training/                   # Training helpers
    ├── evaluation/                 # Evaluation metrics
    └── logging/                    # Logging utilities
```

---

## 🎓 Learning Path

### Phase 1: Foundations (Weeks 1-4)
1. **Environment Setup** - Set up your development environment
2. **Python Fundamentals** - Master Python basics, OOP, and functional programming
3. **Mathematical Foundations** - Linear algebra, calculus, probability, and statistics
4. **Data Manipulation** - NumPy and Pandas for data processing

### Phase 2: Classical Machine Learning (Weeks 5-10)
1. **Supervised Learning** - Regression and classification algorithms
2. **Ensemble Methods** - Random forests, gradient boosting, XGBoost
3. **Unsupervised Learning** - Clustering and dimensionality reduction
4. **Model Evaluation** - Metrics, cross-validation, and hyperparameter tuning

### Phase 3: Deep Learning (Weeks 11-16)
1. **Neural Network Basics** - Perceptrons, activations, backpropagation
2. **Feedforward Networks** - Building networks from scratch and with frameworks
3. **CNNs & RNNs** - Convolutional and recurrent architectures
4. **Optimization** - Advanced optimizers and training techniques

### Phase 4: NLP & Generative AI (Weeks 17-22)
1. **Natural Language Processing** - Text preprocessing and vectorization
2. **Transformers** - Attention mechanisms and transformer architecture
3. **Large Language Models** - GPT, BERT, LLaMA
4. **Prompt Engineering & Fine-tuning** - Techniques for working with LLMs
5. **GenAI Applications** - RAG, agents, and chatbots

### Phase 5: Advanced Topics (Weeks 23-26)
1. **Reinforcement Learning** - RL basics, classical RL, and deep RL
2. **MLOps & Production** - Deployment, monitoring, and cloud integration
3. **Capstone Projects** - Real-world applications

For a detailed roadmap, see [ROADMAP.md](ROADMAP.md) and [README-guides/learning-roadmap.md](README-guides/learning-roadmap.md).

---

## 💻 Key Features

- **📖 Comprehensive Coverage**: From basics to advanced topics
- **🔬 From Scratch Implementations**: Understand algorithms by building them yourself
- **📚 Theory + Practice**: Mathematical foundations with practical implementations
- **🎯 Project-Based Learning**: Hands-on projects at each level
- **🤖 Modern Frameworks**: PyTorch, TensorFlow, Transformers, and more
- **☁️ Production Ready**: MLOps, deployment, and cloud integration guides
- **📊 Well-Documented**: Extensive documentation and code comments
- **🔄 Regular Updates**: Continuously updated with latest techniques
- **🧪 Testing Infrastructure**: Complete pytest setup with coverage reporting
- **🚀 CI/CD Pipeline**: Automated testing and code quality checks
- **📦 Modular Dependencies**: Organized requirements for different use cases
- **💡 Ready-to-Run Examples**: Quick-start code in `examples/` directory

---

## 🛠️ Technologies & Tools

### Core Libraries
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Classical machine learning
- **Matplotlib/Seaborn** - Data visualization

### Deep Learning
- **PyTorch** - Deep learning framework
- **TensorFlow** - Alternative deep learning framework

### NLP & Generative AI
- **Transformers (Hugging Face)** - Pre-trained models and tokenizers
- **Datasets** - Dataset loading and processing
- **Accelerate** - Distributed training

### MLOps
- **MLflow** - Experiment tracking and model registry
- **Weights & Biases (wandb)** - Experiment tracking and visualization

### Development Tools
- **Jupyter Notebooks** - Interactive development
- **Docker** - Containerization
- **Git** - Version control
- **pytest** - Testing framework
- **black** - Code formatting
- **flake8** - Linting
- **mypy** - Type checking
- **pre-commit** - Git hooks

### Available Commands

After setup, use these commands for development:

```bash
make help          # Show all available commands
make install       # Install base dependencies
make install-dev   # Install development dependencies
make test          # Run all tests
make test-fast     # Run fast tests only
make lint          # Check code quality
make format        # Format code with black and isort
make clean         # Clean build artifacts
make docs          # Build documentation
make docs-serve    # Serve documentation locally
```

---

## 📖 Usage Examples

### Example 1: Quick Start
```python
# Run the quick start example
python examples/quick_start.py
```

### Example 2: Neural Network Example
```python
# Run the neural network demo
python examples/neural_network_example.py
```

### Example 3: Linear Regression from Scratch
```python
# Navigate to: 02-classical-machine-learning/01-supervised-learning/regression/linear-regression/from-scratch/
# See implementation details and examples
```

### Example 4: Transformer from Scratch
```python
# Navigate to: 05-generative-ai/02-transformers/transformer-from-scratch/
# Understand transformer architecture by building it yourself
```

### Example 5: Using Jupyter Notebooks
```bash
# Launch Jupyter Lab
jupyter lab

# Navigate to notebooks/ directory and explore tutorials
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by various online courses and educational resources
- Built with the open-source community in mind
- Special thanks to all contributors

---

## 📞 Contact & Support

- **Issues**: If you encounter any problems, please open an issue on GitHub
- **Discussions**: Join discussions for questions and community support
- **Documentation**: 
  - Setup guides: `docs-setup/guides/`
  - Analysis documents: `docs-setup/analysis/`
  - Project documentation: `docs-project-setup/`
- **Troubleshooting**: See `docs-setup/guides/TROUBLESHOOTING.md`
- **FAQ**: See `docs-setup/guides/FAQ.md` (if available)

---

## 🌟 Star History

If you find this repository helpful, please consider giving it a ⭐ star!

---

## 📊 Repository Statistics

- **Total Directories**: 240+
- **Topics Covered**: 50+
- **Learning Path**: 26+ weeks
- **Projects**: Multiple levels (beginner to advanced)
- **Test Coverage**: Comprehensive pytest setup
- **CI/CD**: Automated workflows with GitHub Actions
- **Documentation**: 100+ documentation files

---

## 🔄 Updates & Roadmap

This repository is actively maintained and updated. Check [ROADMAP.md](ROADMAP.md) for planned features and improvements.

### Recent Updates
- ✅ Complete directory structure established
- ✅ Comprehensive documentation added
- ✅ Environment setup guides created
- ✅ Foundation modules structured
- ✅ Testing infrastructure implemented
- ✅ CI/CD pipeline configured
- ✅ Code quality tools integrated
- ✅ Development workflows automated
- ✅ Example implementations added
- ✅ Deployment templates created

### Upcoming Features
- 🔄 Content additions for each module
- 🔄 Interactive notebooks and examples
- 🔄 Video tutorials and walkthroughs
- 🔄 Community contributions and projects
- 🔄 Advanced GenAI implementations
- 🔄 Production MLOps examples

---

<div align="center">

**Happy Learning! 🚀**

*Start your journey into AI/ML and Generative AI today*

</div>

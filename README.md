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
   pip install -r requirements.txt
   ```

4. **Verify GPU setup** (optional, for GPU acceleration)
   ```bash
   python 00-environment-setup/gpu/torch-gpu-check.py
   ```

### Getting Started Guide

For detailed instructions on how to navigate and use this repository, see [README-guides/how-to-use-this-repo.md](README-guides/how-to-use-this-repo.md).

---

## 📁 Repository Structure

```
Mathematical-Models---Coded-from-scratch/
│
├── 📖 README.md                    # This file
├── 🗺️  ROADMAP.md                  # Learning roadmap
├── 🤝 CONTRIBUTING.md              # Contribution guidelines
├── 📦 requirements.txt             # Python dependencies
├── ⚙️  pyproject.toml              # Project configuration
├── 🚫 .gitignore                  # Git ignore rules
├── 🔐 .env.example                # Environment variables template
│
├── 📚 README-guides/               # Comprehensive guides
│   ├── learning-roadmap.md
│   ├── how-to-use-this-repo.md
│   ├── genai-course-alignment.md
│   ├── interview-prep-mapping.md
│   └── naming-conventions.md
│
├── 🛠️  00-environment-setup/       # Environment configuration
│   ├── local/                      # Local Python setup
│   ├── gpu/                        # GPU/CUDA setup
│   ├── docker/                     # Docker containers
│   └── cloud/                      # Cloud platform setup (GCP, AWS, Azure)
│
├── 🐍 01-python-and-math-foundations/
│   ├── python/                     # Python fundamentals
│   ├── numpy-pandas/               # Data manipulation
│   ├── linear-algebra/             # Vectors, matrices, SVD, eigen decomposition
│   ├── calculus/                   # Derivatives, gradients, backpropagation math
│   ├── probability/                # Random variables, distributions, Bayesian thinking
│   └── statistics/                 # Descriptive, inferential, hypothesis testing
│
├── 🤖 02-classical-machine-learning/
│   ├── 01-supervised-learning/     # Regression and classification
│   ├── 02-ensemble-learning/       # Bagging, Random Forest, Boosting, XGBoost
│   ├── 03-unsupervised-learning/   # Clustering, dimensionality reduction, anomaly detection
│   └── 04-model-evaluation/       # Metrics, cross-validation, hyperparameter tuning
│
├── 🧠 03-deep-learning/
│   ├── 01-neural-network-basics/  # Perceptron, activations, loss functions, backprop
│   ├── 02-feedforward-networks/   # From scratch, PyTorch, TensorFlow
│   ├── 03-regularization-techniques/ # Dropout, batch norm, early stopping
│   ├── 04-cnn/                     # Convolution basics, architectures, transfer learning
│   ├── 05-rnn/                     # Vanilla RNN, LSTM, GRU, sequence modeling
│   └── 06-optimization/            # Optimizers, learning rate schedulers, weight init
│
├── 💬 04-natural-language-processing/
│   ├── 01-text-preprocessing/
│   ├── 02-vectorization/
│   ├── 03-sequence-models/
│   └── 04-nlp-tasks/
│
├── ✨ 05-generative-ai/
│   ├── 01-foundations/             # Generative vs discriminative, likelihood, autoregressive
│   ├── 02-transformers/             # Attention, multi-head attention, positional encoding
│   ├── 03-large-language-models/   # GPT, BERT, LLaMA, inference pipelines
│   ├── 04-prompt-engineering/     # Zero-shot, few-shot, chain-of-thought
│   ├── 05-fine-tuning/             # Full fine-tuning, PEFT/LoRA, instruction tuning
│   └── 06-genai-applications/      # RAG, agents, chatbots, embeddings search
│
├── 🎮 06-reinforcement-learning/
│   ├── 01-rl-basics/
│   ├── 02-classical-rl/
│   ├── 03-deep-rl/
│   └── 04-rl-applications/
│
├── 🏭 07-mlops-and-production/
│   ├── experiment-tracking/
│   ├── model-versioning/
│   ├── deployment/
│   ├── monitoring/
│   └── cloud-integrations/
│
├── 🎯 08-projects/
│   ├── beginner/                   # Starter projects
│   ├── intermediate/               # Intermediate projects
│   ├── advanced/                   # Advanced projects
│   └── genai-capstone/             # Generative AI capstone project
│
└── 🛠️  utils/                      # Utility modules
    ├── data/                       # Data processing utilities
    ├── math/                       # Mathematical utilities
    ├── visualization/              # Visualization tools
    ├── training/                   # Training utilities
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

---

## 📖 Usage Examples

### Example 1: Linear Regression from Scratch
```python
# Navigate to: 02-classical-machine-learning/01-supervised-learning/regression/linear-regression/from-scratch/
# See implementation details and examples
```

### Example 2: Neural Network with PyTorch
```python
# Navigate to: 03-deep-learning/02-feedforward-networks/pytorch/
# See PyTorch implementation examples
```

### Example 3: Transformer from Scratch
```python
# Navigate to: 05-generative-ai/02-transformers/transformer-from-scratch/
# Understand transformer architecture by building it yourself
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
- **Documentation**: Check the [README-guides](README-guides/) directory for detailed guides

---

## 🌟 Star History

If you find this repository helpful, please consider giving it a ⭐ star!

---

## 📊 Repository Statistics

- **Total Directories**: 175+
- **Topics Covered**: 50+
- **Learning Path**: 26+ weeks
- **Projects**: Multiple levels (beginner to advanced)

---

## 🔄 Updates & Roadmap

This repository is actively maintained and updated. Check [ROADMAP.md](ROADMAP.md) for planned features and improvements.

### Recent Updates
- ✅ Complete directory structure established
- ✅ Comprehensive documentation added
- ✅ Environment setup guides created
- ✅ Foundation modules structured

### Upcoming Features
- 🔄 Content additions for each module
- 🔄 Interactive notebooks and examples
- 🔄 Video tutorials and walkthroughs
- 🔄 Community contributions and projects

---

<div align="center">

**Happy Learning! 🚀**

*Start your journey into AI/ML and Generative AI today*

</div>

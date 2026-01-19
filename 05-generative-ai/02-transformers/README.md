# Transformers

The transformer architecture revolutionized NLP and enabled modern large language models.

## Contents

- **attention/** - Self-attention mechanism
- **multi-head-attention/** - Multiple attention heads for richer representations
- **positional-encoding/** - Encoding position information
- **transformer-from-scratch/** - Building transformers from scratch

## Key Innovation: Attention

- Allows model to focus on relevant parts of input
- Parallel processing (unlike RNNs)
- Captures long-range dependencies
- Foundation of modern LLMs

## Architecture Components

### Encoder-Decoder
- **Encoder**: Processes input sequence
- **Decoder**: Generates output sequence
- Used in translation, summarization

### Encoder-Only (BERT)
- Bidirectional understanding
- Good for classification, NER
- Pre-training + fine-tuning

### Decoder-Only (GPT)
- Autoregressive generation
- Good for text generation
- Causal attention mask

## Multi-Head Attention

- Multiple attention mechanisms in parallel
- Captures different types of relationships
- Richer representations
- Standard in transformer models

## Positional Encoding

- Adds position information
- Since transformers have no inherent order
- Learned or fixed sinusoidal
- Critical for sequence understanding

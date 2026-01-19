# Recurrent Neural Networks (RNNs)

Neural networks designed for processing sequential data with temporal dependencies.

## Contents

- **vanilla-rnn/** - Basic RNN architecture
- **lstm/** - Long Short-Term Memory networks
- **gru/** - Gated Recurrent Units
- **sequence-modeling/** - Applications in sequence modeling tasks

## Why RNNs?

- Process sequences of variable length
- Maintain memory of previous inputs
- Share parameters across time steps
- Handle temporal dependencies

## Vanilla RNN

Basic recurrent architecture:
- Hidden state carries information forward
- Simple but limited memory
- Suffers from vanishing gradients
- Rarely used in practice

## LSTM (Long Short-Term Memory)

Solves vanishing gradient problem:
- **Cell State**: Long-term memory
- **Hidden State**: Short-term memory
- **Gates**: Control information flow
  - Forget gate: what to forget
  - Input gate: what to remember
  - Output gate: what to output

## GRU (Gated Recurrent Unit)

Simplified version of LSTM:
- Fewer parameters than LSTM
- Similar performance in many cases
- Faster to train
- Combines forget and input gates

## Applications

- **Natural Language Processing**: Language modeling, translation
- **Time Series**: Stock prediction, weather forecasting
- **Speech Recognition**: Audio sequence processing
- **Music Generation**: Sequential pattern learning
- **Video Analysis**: Temporal video understanding

## Key Concepts

- Sequence-to-sequence models
- Bidirectional RNNs
- Attention mechanisms
- Encoder-decoder architecture

# Vectorization

Converting text into numerical representations that ML models can process.

## Methods

- **Bag of Words (BoW)**: Count-based representation
- **TF-IDF**: Term Frequency-Inverse Document Frequency
- **Word Embeddings**: Dense vector representations (Word2Vec, GloVe)
- **Contextual Embeddings**: Context-aware representations (BERT, ELMO)

## Bag of Words

- Simple count-based approach
- Creates sparse vectors
- Loses word order
- Fast and interpretable

## TF-IDF

- Weights words by importance
- Reduces impact of common words
- Better than simple counts
- Still loses word order

## Word Embeddings

- Dense vector representations
- Captures semantic relationships
- Pre-trained models available
- Words with similar meanings are close in vector space

## Contextual Embeddings

- Same word has different embeddings in different contexts
- Captures context and meaning
- State-of-the-art performance
- Requires pre-trained models (BERT, GPT)

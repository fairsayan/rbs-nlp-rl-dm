# NLP, Reinforcement Learning and Decision Making – Course Examples

This repository contains a collection of exercises and examples used in the **[Rome Business School] Natural Language Processing (NLP), Reinforcement Learning and Decision Making** module.

## Purpose
The goal of this repository is to provide students with a simple and accessible reference for all the code discussed during the course. It serves as a learning companion to:

- Review and reuse code from class exercises.
- Better understand core concepts through hands-on examples.
- Experiment and build upon the material provided.

Feel free to explore, modify, and test the code. All examples are meant to support your understanding and practical application of the course topics.

## Quick Start

### Prerequisites
- Python 3.9 or higher
- At least 8GB of free disk space
- 16GB+ RAM recommended
- CUDA-compatible GPU (optional but recommended for deep learning labs)

### One-Time Setup
1. Clone this repository
2. Run the unified setup script:
   ```bash
   ./setup.sh
   ```
3. Activate the environment:
   ```bash
   source .venv/bin/activate
   ```

### Using the Laboratories
Navigate to any lab directory and start Jupyter:
```bash
cd [lab-directory]/
jupyter notebook [notebook-name].ipynb
```

**Note**: The same `.venv` environment works for all laboratories - no need for separate setups!

## Content

### 📚 Available Laboratories

#### 1. **Amazon Reviews Analysis** (`amazon-reviews/`)
- **Focus**: Sentiment analysis and text processing
- **Technologies**: NLTK, scikit-learn, pandas, wordcloud
- **Notebook**: `amazon_reviews_analysis.ipynb`
- **Skills**: Text preprocessing, feature extraction, sentiment classification

#### 2. **Text Classification with Transformers** (`text-classification/`)
- **Focus**: Modern deep learning for text classification
- **Technologies**: Transformers, PyTorch, Hugging Face
- **Notebook**: `transformer_text_classification_lab.ipynb`
- **Skills**: Fine-tuning pre-trained models, advanced NLP techniques

#### 3. **LLM Tool Calling Laboratory** (`llm-tool-calling/`)
- **Focus**: Local LLM deployment and function calling
- **Technologies**: Mistral, Ollama, custom tool integration
- **Notebook**: `mistral_tool_calling_lab.ipynb`
- **Skills**: Tool calling, local LLM deployment, function integration

#### 4. **Explore Embeddings** (`explore-embeddings/`)
- **Focus**: Word embeddings and semantic analysis
- **Technologies**: Gensim, word2vec, semantic similarity
- **Notebook**: `explore_embeddings_lab.ipynb`
- **Skills**: Vector representations, semantic analysis, similarity metrics

### 🛠️ Unified Environment
All laboratories share a single Python virtual environment (`.venv`) with all necessary dependencies pre-installed. This approach:
- ✅ Simplifies setup and maintenance
- ✅ Ensures version compatibility across labs
- ✅ Reduces disk space usage
- ✅ Provides consistent development experience

### 📋 Dependencies Included
- **Core**: numpy, pandas, matplotlib, seaborn
- **ML/NLP**: scikit-learn, nltk, gensim
- **Deep Learning**: torch, transformers, datasets
- **Visualization**: plotly, wordcloud
- **Development**: jupyter, notebook, ipywidgets
- **Specialized**: ollama (for local LLM), requests (for APIs)

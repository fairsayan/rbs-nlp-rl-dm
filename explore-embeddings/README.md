# NLP Embeddings Lab

This lab explores word embeddings using pretrained Word2Vec models.

## Setup Instructions

### Unified Environment Setup (Recommended)
This lab is part of a unified course environment. From the repository root:
```bash
# One-time setup for all laboratories
./setup.sh

# Activate the shared environment  
source .venv/bin/activate

# Navigate to this lab and start
cd explore-embeddings/
jupyter notebook explore_embeddings_lab.ipynb
```

### Alternative: Local Setup (if needed)
If you prefer to set up only this lab:

#### 1. Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Launch Jupyter Notebook
```bash
jupyter notebook explore_embeddings_lab.ipynb
```

## Lab Objectives

- Load and work with pretrained Word2Vec embeddings
- Find nearest neighbors in vector space
- Visualize word similarities using 2D plots
- Analyze business-relevant vocabulary through embeddings

## Requirements

- Python 3.7+
- See `requirements.txt` for package dependencies

## Lab Structure

The notebook contains:
1. Import required libraries
2. Load pretrained Word2Vec model
3. Define business-relevant words
4. Explore word similarity and nearest neighbors
5. Visualize embeddings in 2D space
6. Calculate similarity matrices
7. Word arithmetic and analogies
8. Hands-on exercises

## Notes

- The lab will automatically download a pretrained model if not found locally
- All visualizations and analysis are included in the notebook
- Exercise sections allow for hands-on practice

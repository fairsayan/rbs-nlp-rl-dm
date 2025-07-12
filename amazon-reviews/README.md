# Amazon Reviews Analysis Laboratory

## Project Overview
This project demonstrates natural language processing techniques for analyzing Amazon customer reviews. The laboratory covers text preprocessing, tokenization, stopword removal, and visualization of text data.

## Prerequisites
- Python 3.8 or higher
- Jupyter Notebook
- Required packages (see requirements.txt)

## Installation
1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download NLTK data (run this once):
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```

## Files Description
- `amazon_reviews_analysis.ipynb`: Main Jupyter notebook with the complete analysis
- `requirements.txt`: Python dependencies
- `data/`: Directory for dataset files
- `README.md`: This file

## Dataset
The project uses Amazon product reviews dataset. You can use any CSV file with review text, or download sample data from:
- [Amazon Product Reviews Dataset](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- [Amazon Reviews for Sentiment Analysis](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews)

## Laboratory Steps
1. **Data Loading**: Load the dataset using pandas
2. **Text Preprocessing**: Clean and preprocess review text
3. **Tokenization**: Split text into tokens
4. **Stopword Removal**: Remove common English stopwords
5. **Visualization**: Create word clouds and frequency plots
6. **Vectorization Preparation**: Prepare text for machine learning

## Learning Objectives
- Understand text preprocessing techniques
- Learn tokenization and stopword removal
- Visualize text data patterns
- Prepare text for machine learning models

## Usage
1. Open `amazon_reviews_analysis.ipynb` in Jupyter Notebook
2. Run cells sequentially
3. Follow the instructions and explanations in each cell

## Author
Domenico Pontari <fairsayan@gmail.com>

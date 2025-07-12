# Amazon Reviews Analysis Laboratory

## Project Overview
This project demonstrates natural language processing techniques for analyzing Amazon customer reviews. The laboratory covers text preprocessing, tokenization, stopword removal, and visualization of text data.

## Prerequisites
- Python 3.8 or higher
- Jupyter Notebook
- Required packages (see requirements.txt)

## Installation

### Unified Environment Setup (Recommended)
This lab is part of a unified course environment. From the repository root:
```bash
# One-time setup for all laboratories
./setup.sh

# Activate the shared environment  
source .venv/bin/activate

# Navigate to this lab and start
cd amazon-reviews/
jupyter notebook amazon_reviews_analysis.ipynb
```

### Alternative: Local Setup (if needed)
If you prefer to set up only this lab:
1. Clone or download this project
2. Create local environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

**Note**: NLTK data is automatically downloaded to a local `nltk_data/` directory within this project. The notebook handles all data downloads and configurations automatically on first run.

## Files Description
- `amazon_reviews_analysis.ipynb`: Main Jupyter notebook with the complete analysis
- `requirements.txt`: Python dependencies specific to this laboratory
- `data/`: Directory containing processed datasets and analysis results
  - `processed_amazon_reviews.csv`: Pre-processed Amazon reviews dataset (20 reviews)
  - `analysis_summary.txt`: Summary of analysis results and statistics
  - `count_vectorizer.pkl`: Saved CountVectorizer model
  - `tfidf_vectorizer.pkl`: Saved TF-IDF vectorizer model
- `nltk_data/`: Local NLTK data directory (automatically created/downloaded)
- `README.md`: This file

## Dataset
The project includes a pre-processed Amazon product reviews dataset (`data/processed_amazon_reviews.csv`) with 20 sample reviews for educational purposes. The analysis has already been performed and results are available in `data/analysis_summary.txt`.

### Sample Data Statistics
- **Dataset size**: 20 reviews
- **Average rating**: 3.30
- **Unique vocabulary**: 100 words  
- **Most frequent word**: "product" (16 occurrences)

For additional datasets, you can download from:
- [Amazon Product Reviews Dataset](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- [Amazon Reviews for Sentiment Analysis](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews)

## Laboratory Steps
1. **Environment Setup**: Import libraries and configure NLTK data path
2. **NLTK Data Download**: Download required NLTK resources to local directory
3. **Data Loading**: Load the pre-processed Amazon reviews dataset
4. **Data Exploration**: Examine dataset structure and basic statistics
5. **Text Preprocessing**: Clean and normalize review text
6. **Tokenization**: Split text into individual tokens
7. **Stopword Removal**: Filter out common English stopwords
8. **Lemmatization**: Reduce words to their root forms
9. **Visualization**: 
   - Create word clouds for visual text representation
   - Generate frequency plots and distributions
   - Plot rating distributions and statistics
10. **Feature Engineering**: 
    - Create TF-IDF and Count vectorizers
    - Prepare text features for machine learning
11. **Analysis Summary**: Generate comprehensive analysis report

## Learning Objectives
- Understand text preprocessing techniques and pipelines
- Learn tokenization, stopword removal, and lemmatization
- Master text visualization with word clouds and frequency analysis
- Explore feature engineering with TF-IDF and Count vectorization
- Practice data analysis and summary generation
- Understand local NLTK data management and configuration
- Prepare text data for machine learning applications

## Usage
1. Open `amazon_reviews_analysis.ipynb` in Jupyter Notebook or VS Code
2. Run cells sequentially from top to bottom
3. Follow the instructions and explanations in each cell
4. Examine the pre-processed data and generated visualizations
5. Review the analysis summary in `data/analysis_summary.txt`
6. Experiment with the saved vectorizer models (.pkl files) for further analysis

## Generated Outputs
The laboratory generates several outputs:
- **Word clouds**: Visual representations of text frequency
- **Frequency plots**: Bar charts and distributions of word usage
- **Analysis summary**: Statistical summary saved to `data/analysis_summary.txt`
- **Vectorizer models**: Saved TF-IDF and Count vectorizers for reuse
- **Processed dataset**: Clean, tokenized text ready for ML applications

## Author
Domenico Pontari <fairsayan@gmail.com>

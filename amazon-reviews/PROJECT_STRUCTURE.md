# Project Structure

```
amazon-reviews/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── setup.sh                          # Setup script for Unix/macOS
├── amazon_reviews_analysis.ipynb     # Main Jupyter notebook
├── quick_demo.py                     # Standalone Python demo
└── data/
    ├── sample_reviews.csv            # Sample dataset
    └── (processed files will be saved here)
```

# Quick Start

## Option 1: Using Jupyter Notebook (Recommended)
```bash
# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook

# Open amazon_reviews_analysis.ipynb
```

## Option 2: Using Setup Script
```bash
# Run the setup script
./setup.sh

# Start Jupyter
jupyter notebook
```

## Option 3: Quick Demo
```bash
# Install dependencies
pip install -r requirements.txt

# Run the demo
python quick_demo.py
```

# Learning Path

1. **Start with the Jupyter notebook** - `amazon_reviews_analysis.ipynb`
2. **Follow the step-by-step guide** - Each cell explains the concepts
3. **Run cells sequentially** - Build understanding progressively
4. **Experiment with the code** - Modify parameters and see results
5. **Try with your own data** - Replace sample data with real reviews

# Key Concepts Covered

- **Text Preprocessing**: Cleaning and normalizing text data
- **Tokenization**: Breaking text into individual words
- **Stopword Removal**: Filtering out common words
- **Lemmatization**: Reducing words to their base forms
- **Word Frequency Analysis**: Understanding word usage patterns
- **Text Visualization**: Word clouds and frequency plots
- **Vectorization**: Converting text to numerical representations
- **Data Preparation**: Getting ready for machine learning

# Next Steps

After completing this laboratory, you can:
- Apply these techniques to real Amazon review datasets
- Implement sentiment analysis models
- Build recommendation systems
- Explore advanced NLP techniques
- Create text classification models

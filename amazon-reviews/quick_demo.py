"""
Amazon Reviews Analysis - Quick Demo Script
This script demonstrates the main concepts from the Jupyter notebook
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

def setup_nltk():
    """Download required NLTK data"""
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
    except LookupError:
        print("Downloading NLTK data...")
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('omw-1.4')

def preprocess_text(text):
    """Complete preprocessing pipeline"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Remove short tokens
    tokens = [token for token in tokens if len(token) > 2]
    
    return tokens

def analyze_reviews():
    """Main analysis function"""
    print("Amazon Reviews Analysis Demo")
    print("=" * 40)
    
    # Setup NLTK
    setup_nltk()
    
    # Load data
    try:
        df = pd.read_csv('data/sample_reviews.csv')
        print(f"✅ Loaded {len(df)} reviews from dataset")
    except FileNotFoundError:
        print("❌ Sample dataset not found. Using built-in sample data.")
        # Create sample data
        sample_reviews = [
            "This product is absolutely amazing! I love it so much.",
            "Poor quality product. Disappointed with the purchase.",
            "The item arrived on time and works perfectly.",
            "Terrible experience. The product broke after one day.",
            "Good value for money. The product meets expectations."
        ]
        df = pd.DataFrame({
            'review_text': sample_reviews,
            'rating': [5, 1, 4, 1, 3]
        })
    
    # Preprocessing
    print("\n📝 Preprocessing reviews...")
    df['processed_tokens'] = df['review_text'].apply(preprocess_text)
    df['processed_text'] = df['processed_tokens'].apply(lambda x: ' '.join(x))
    
    # Collect all tokens
    all_tokens = []
    for tokens in df['processed_tokens']:
        all_tokens.extend(tokens)
    
    # Word frequency analysis
    word_freq = Counter(all_tokens)
    most_common = word_freq.most_common(10)
    
    print(f"✅ Processed {len(df)} reviews")
    print(f"📊 Total unique words: {len(set(all_tokens))}")
    print(f"📈 Most common words: {most_common[:5]}")
    
    # Create visualizations
    print("\n🎨 Creating visualizations...")
    
    # Word frequency plot
    if len(most_common) > 0:
        words, freqs = zip(*most_common)
        plt.figure(figsize=(10, 5))
        plt.bar(words, freqs, color='skyblue', edgecolor='navy')
        plt.title('Most Frequent Words in Amazon Reviews')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('word_frequency.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✅ Word frequency plot created")
    
    # Word cloud
    all_text = ' '.join(df['processed_text'])
    if len(all_text) > 0:
        wordcloud = WordCloud(width=800, height=400, 
                             background_color='white').generate(all_text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Amazon Reviews Word Cloud')
        plt.tight_layout()
        plt.savefig('wordcloud.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✅ Word cloud created")
    
    # Summary statistics
    print("\n📈 Summary Statistics:")
    print(f"• Average review length: {df['review_text'].apply(len).mean():.1f} characters")
    print(f"• Average word count: {df['review_text'].apply(lambda x: len(x.split())).mean():.1f} words")
    print(f"• Average processed tokens: {df['processed_tokens'].apply(len).mean():.1f}")
    
    if 'rating' in df.columns:
        print(f"• Average rating: {df['rating'].mean():.2f}")
        print(f"• Rating distribution: {dict(df['rating'].value_counts().sort_index())}")
    
    print("\n🎉 Analysis complete!")
    print("Check the generated plots: word_frequency.png and wordcloud.png")

if __name__ == "__main__":
    analyze_reviews()

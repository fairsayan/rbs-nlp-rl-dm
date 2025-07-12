#!/bin/bash

echo "Setting up Amazon Reviews Analysis Laboratory..."
echo "============================================="

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Download NLTK data
python3 -c "
import nltk
print('Downloading NLTK data...')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')
print('NLTK data downloaded successfully!')
"

echo ""
echo "Setup complete! 🎉"
echo ""
echo "To start the laboratory:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Start Jupyter: jupyter notebook"
echo "3. Open amazon_reviews_analysis.ipynb"
echo ""
echo "Happy analyzing! 📊"

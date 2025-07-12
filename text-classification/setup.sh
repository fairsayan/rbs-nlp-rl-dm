#!/bin/bash

# Transformers Text Classification Lab Setup Script
# This script sets up the environment for the Transformers text classification lab

echo "🚀 Setting up Transformers Text Classification Lab Environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ to continue."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "✅ Python version: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found. Please ensure requirements.txt exists in the current directory."
    exit 1
fi

# Install packages from requirements.txt
echo "📚 Installing packages from requirements.txt..."
pip install -r requirements.txt

# Final instructions
echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Start Jupyter Lab: jupyter lab"
echo "3. Open the lab notebook: transformer_text_classification_lab.ipynb"
echo ""
echo "Happy learning! 🚀"

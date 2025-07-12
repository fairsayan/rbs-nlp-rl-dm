#!/bin/bash

# NLP Embeddings Lab Setup Script
# This script sets up the environment for the lab

echo "🚀 Setting up NLP Embeddings Lab..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

# Create virtual environment
echo "🔧 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "📋 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📦 Installing requirements..."
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "To start the lab:"
echo "1. Activate the environment: source venv/bin/activate"
echo "2. Launch Jupyter: jupyter notebook explore_embeddings_lab.ipynb"

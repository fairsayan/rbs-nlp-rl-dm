#!/bin/bash

# NLP, RL and Decision Making - Unified Setup Script
# Sets up a single virtual environment for all course laboratories

echo "🎓 Setting up NLP, RL and Decision Making Course Environment..."
echo "=============================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9+ to continue."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "✅ Python version: $python_version"

if [[ $(echo "$python_version < 3.9" | bc -l) ]]; then
    echo "⚠️  Python 3.9+ is recommended for all laboratories"
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating unified virtual environment (.venv)..."
    python3 -m venv .venv
else
    echo "📁 Virtual environment (.venv) already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install all requirements
echo "📚 Installing unified requirements for all laboratories..."
if pip install -r requirements.txt; then
    echo "✅ All packages installed successfully!"
else
    echo "❌ Some packages failed to install. Please check the error messages above."
    exit 1
fi

# Check if Ollama is available (for Mistral lab)
echo ""
echo "🔍 Checking for Ollama (needed for LLM Tool Calling lab)..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama is installed"
    echo "🚀 Pulling Mistral model for tool calling lab..."
    ollama pull mistral:7b-instruct
else
    echo "⚠️ Ollama not found. Install from https://ollama.ai/ for the LLM Tool Calling lab"
    echo "   (The lab can still work with Hugging Face Transformers)"
fi

echo ""
echo "🎉 Setup complete! All laboratories are ready to use."
echo ""
echo "📚 Available laboratories:"
echo "  • amazon-reviews/         - Amazon reviews sentiment analysis"
echo "  • text-classification/    - Transformer-based text classification"
echo "  • llm-tool-calling/      - Mistral tool calling with local LLM"
echo "  • explore-embeddings/    - Word embeddings and semantic analysis"
echo ""
echo "🚀 Next steps:"
echo "1. Activate the environment: source .venv/bin/activate"
echo "2. Navigate to any lab directory: cd [lab-name]/"
echo "3. Start Jupyter: jupyter notebook [notebook-name].ipynb"
echo ""
echo "💡 The same .venv environment works for all laboratories!"
echo "   No need to create separate environments anymore."

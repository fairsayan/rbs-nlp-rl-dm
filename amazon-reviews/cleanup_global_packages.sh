#!/bin/bash

echo "🧹 Python Global Packages Cleanup Script"
echo "========================================"
echo ""

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if pip is available
if ! command_exists pip; then
    echo "❌ pip not found. Please install pip first."
    exit 1
fi

echo "📋 Current global packages:"
pip list

echo ""
echo "🔍 Finding potentially unnecessary packages..."
echo ""

# Common packages that can be safely removed (not system packages)
COMMON_UNNECESSARY_PACKAGES=(
    "boto3"
    "botocore"
    "beautifulsoup4"
    "requests-oauthlib"
    "tweepy"
    "facebook-sdk"
    "django"
    "flask"
    "fastapi"
    "tensorflow"
    "torch"
    "pytorch"
    "keras"
    "opencv-python"
    "opencv-contrib-python"
    "selenium"
    "scrapy"
    "jupyter-lab"
    "jupyterlab"
    "notebook"
    "ipython"
    "ipykernel"
    "ipywidgets"
    "matplotlib"
    "seaborn"
    "plotly"
    "bokeh"
    "altair"
    "pandas"
    "numpy"
    "scipy"
    "scikit-learn"
    "statsmodels"
    "nltk"
    "spacy"
    "gensim"
    "transformers"
    "wordcloud"
    "pillow"
    "pyqt5"
    "tkinter"
    "pygame"
    "kivy"
)

echo "🔎 Checking for these potentially unnecessary packages in your global installation:"
PACKAGES_TO_REMOVE=()

for package in "${COMMON_UNNECESSARY_PACKAGES[@]}"; do
    if pip show "$package" >/dev/null 2>&1; then
        echo "  ✓ Found: $package"
        PACKAGES_TO_REMOVE+=("$package")
    fi
done

echo ""
if [ ${#PACKAGES_TO_REMOVE[@]} -eq 0 ]; then
    echo "✅ No common unnecessary packages found in global installation."
else
    echo "📦 Found ${#PACKAGES_TO_REMOVE[@]} packages that could be removed:"
    for package in "${PACKAGES_TO_REMOVE[@]}"; do
        echo "  • $package"
    done
    
    echo ""
    echo "⚠️  WARNING: This will remove packages from your GLOBAL Python installation!"
    echo "   Make sure you have these packages in virtual environments if you need them."
    echo ""
    read -p "Do you want to proceed with removal? (y/N): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🗑️  Removing packages..."
        for package in "${PACKAGES_TO_REMOVE[@]}"; do
            echo "  Removing $package..."
            pip uninstall -y "$package"
        done
        echo "✅ Cleanup completed!"
    else
        echo "❌ Cleanup cancelled."
    fi
fi

echo ""
echo "💡 RECOMMENDATIONS:"
echo "  1. Use virtual environments for projects: python -m venv myenv"
echo "  2. Keep global Python installation minimal"
echo "  3. Install project-specific packages in virtual environments"
echo "  4. Use requirements.txt files for reproducible environments"
echo ""
echo "📝 To create a virtual environment for this project:"
echo "  python -m venv venv"
echo "  source venv/bin/activate  # On macOS/Linux"
echo "  pip install -r requirements.txt"
echo ""
echo "🏁 Script completed!"

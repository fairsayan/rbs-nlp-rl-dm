# Mistral Small 3.1 Tool Calling Laboratory

## Project Overview
This project demonstrates how to install and use Mistral Small 3.1 locally with tool calling capabilities. The laboratory covers model installation, setup, and practical examples of function calling with the Mistral language model.

## Prerequisites
- Python 3.9 or higher
- At least 8GB of free disk space
- 16GB+ RAM recommended
- CUDA-compatible GPU (optional but recommended)
- Jupyter Notebook

## Installation

### Unified Environment Setup (Recommended)
This lab is part of a unified course environment. From the repository root:
```bash
# One-time setup for all laboratories
./setup.sh

# Activate the shared environment  
source .venv/bin/activate

# Navigate to this lab and start
cd llm-tool-calling/
jupyter notebook mistral_tool_calling_lab.ipynb
```

### Alternative: Local Setup (if needed)
If you prefer to set up only this lab:

#### Option 1: Using Ollama (Recommended)
1. Install Ollama from [https://ollama.ai/](https://ollama.ai/)
2. Pull the Mistral model:
   ```bash
   ollama pull mistral:7b-instruct
   ```

#### Option 2: Using Transformers
1. Create local environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. The model will be downloaded automatically on first use

### Setup NLTK Data (if needed)
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Files Description
- `mistral_tool_calling_lab.ipynb`: Main Jupyter notebook with complete examples
- `requirements.txt`: Python dependencies
- `tools/`: Directory containing custom tool definitions
- `examples/`: Example tool calling scenarios
- `README.md`: This file

## Laboratory Features
1. **Model Installation**: Step-by-step guide to install Mistral Small 3.1 locally
2. **Tool Definition**: How to define custom tools/functions
3. **Function Calling**: Practical examples of tool calling
4. **Advanced Usage**: Complex scenarios with multiple tools
5. **Performance Optimization**: Tips for better performance

## Tool Categories Covered
- **Mathematical Operations**: Calculator functions
- **Data Retrieval**: API calls and data fetching
- **Text Processing**: Text analysis and manipulation
- **File Operations**: File reading/writing operations
- **Web Search**: Search functionality examples

## Learning Objectives
- Understand local LLM deployment
- Learn tool/function calling concepts
- Implement custom tools for specific use cases
- Optimize model performance for tool calling
- Handle tool calling errors and edge cases

## Usage
1. Open `mistral_tool_calling_lab.ipynb` in Jupyter
2. Follow the step-by-step instructions
3. Run cells sequentially to learn tool calling concepts
4. Experiment with custom tools in the provided examples

## Performance Notes
- First model load may take several minutes
- Tool calling adds latency compared to simple text generation
- GPU acceleration significantly improves performance
- Consider using quantized models for lower memory usage

## Troubleshooting
- **Memory Issues**: Use smaller batch sizes or quantized models
- **Installation Problems**: Check Python version and dependencies
- **Tool Errors**: Validate tool definitions and parameters
- **Performance**: Enable GPU acceleration if available

## Examples Included
- Basic calculator tool
- Weather information retrieval
- File system operations
- Web search and summarization
- Data analysis tools

## Further Reading
- [Mistral AI Documentation](https://docs.mistral.ai/)
- [Tool Calling Best Practices](https://docs.mistral.ai/capabilities/function_calling/)
- [Local LLM Deployment Guide](https://ollama.ai/docs)

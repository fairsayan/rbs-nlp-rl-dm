# Project Structure Documentation

## Overview
This laboratory demonstrates how to install and use Mistral Small 3.1 locally with tool calling capabilities.

## Directory Structure

```
llm-tool-calling/
├── README.md                           # Main project documentation
├── requirements.txt                    # Python dependencies
├── setup.sh                           # Setup script for easy installation
├── mistral_tool_calling_lab.ipynb     # Main Jupyter notebook
├── PROJECT_STRUCTURE.md               # This file
├── tools/                             # Custom tool definitions
│   ├── custom_tools.py                # Core tool implementations
│   └── ollama_client.py               # Ollama API client helper
└── examples/                          # Example usage scripts
    ├── calculator_example.py          # Mathematical operations demo
    └── text_analysis_example.py       # Text processing demo
```

## Key Components

### 1. Main Notebook (`mistral_tool_calling_lab.ipynb`)
The primary learning resource containing:
- Step-by-step installation guide
- Model setup (Ollama vs Hugging Face)
- Tool definition examples
- Interactive tool calling demonstrations
- Performance optimization tips
- Error handling examples

### 2. Custom Tools (`tools/custom_tools.py`)
Defines several tool categories:
- **CalculatorTool**: Basic mathematical operations
- **WeatherTool**: Mock weather data retrieval
- **FileOperationsTool**: File system operations
- **TextAnalysisTool**: Text processing and analysis

### 3. Ollama Client (`tools/ollama_client.py`)
Helper class for:
- Connecting to local Ollama instance
- Formatting tool calling prompts
- Extracting tool calls from responses
- Managing model interactions

### 4. Example Scripts
- **calculator_example.py**: Demonstrates mathematical tool usage
- **text_analysis_example.py**: Shows text processing capabilities

## Installation Methods

### Method 1: Ollama (Recommended)
1. Install Ollama from https://ollama.ai/
2. Run: `ollama pull mistral:7b-instruct`
3. Install Python dependencies: `pip install -r requirements.txt`

### Method 2: Hugging Face Transformers
1. Install dependencies: `pip install -r requirements.txt`
2. Model downloads automatically on first use
3. Requires ~8GB disk space for model

## Usage Patterns

### Basic Tool Calling Flow
1. User provides input
2. Model determines if tools are needed
3. Tool calls are extracted and executed
4. Results are incorporated into final response

### Tool Schema Format
```python
{
    "type": "function",
    "function": {
        "name": "tool_name",
        "description": "Tool description",
        "parameters": {
            "type": "object",
            "properties": {
                "param1": {"type": "string", "description": "Parameter description"}
            },
            "required": ["param1"]
        }
    }
}
```

## Supported Tool Categories

1. **Mathematical**: Addition, multiplication, power, square root
2. **Data Analysis**: Text analysis, keyword extraction, statistics
3. **External Data**: Weather information (mock), API calls
4. **File Operations**: Read/write files, directory listing
5. **Text Processing**: Word counts, character analysis, keyword extraction

## Performance Considerations

- **Memory**: 8GB+ RAM recommended
- **GPU**: CUDA acceleration significantly improves performance
- **Storage**: ~8GB for model files
- **Latency**: Tool calling adds ~200-500ms overhead

## Error Handling

The system handles:
- Invalid tool parameters
- Missing required parameters
- Tool execution failures
- Model connection issues
- File system errors

## Extension Points

### Adding New Tools
1. Define tool class in `custom_tools.py`
2. Add tool schema to `TOOL_SCHEMAS`
3. Update `execute_tool()` function
4. Test tool functionality

### Custom Model Integration
1. Implement model interface in new client
2. Update prompt formatting for your model
3. Modify tool call extraction logic
4. Test with various tool scenarios

## Best Practices

1. **Tool Design**: Keep tools simple and focused
2. **Error Handling**: Validate all inputs thoroughly
3. **Performance**: Cache results when possible
4. **Security**: Sanitize file operations and external calls
5. **Testing**: Implement comprehensive test coverage

## Troubleshooting

### Common Issues
- **Memory errors**: Use quantized models or reduce batch size
- **Slow performance**: Enable GPU acceleration
- **Connection failures**: Check Ollama service status
- **Import errors**: Verify all dependencies are installed

### Debug Mode
Enable verbose logging by setting environment variables:
```bash
export MISTRAL_DEBUG=1
export OLLAMA_VERBOSE=1
```

## Learning Objectives

After completing this laboratory, users will understand:
- Local LLM deployment strategies
- Tool calling implementation patterns
- Function schema design
- Error handling best practices
- Performance optimization techniques
- Custom tool development

## Further Development

Potential enhancements:
- Real API integrations (OpenWeatherMap, etc.)
- Database connectivity tools
- Advanced text processing with NLP libraries
- Multi-modal capabilities (image, audio)
- Production deployment with caching and monitoring

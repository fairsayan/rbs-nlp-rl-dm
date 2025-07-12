"""
Custom tools for Mistral Tool Calling Laboratory
This module contains various tool definitions that can be used with Mistral's function calling capability.
"""

import json
import math
import requests
from typing import Dict, Any, List
from datetime import datetime
import os

class CalculatorTool:
    """Basic calculator operations"""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract b from a"""
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def power(base: float, exponent: float) -> float:
        """Raise base to the power of exponent"""
        return math.pow(base, exponent)
    
    @staticmethod
    def square_root(number: float) -> float:
        """Calculate square root of a number"""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(number)

class WeatherTool:
    """Weather information retrieval (mock implementation)"""
    
    @staticmethod
    def get_current_weather(city: str, country: str = "US") -> Dict[str, Any]:
        """
        Get current weather for a city
        Note: This is a mock implementation. In real use, you'd use an actual weather API.
        """
        # Mock weather data
        mock_data = {
            "city": city,
            "country": country,
            "temperature": 22,
            "condition": "Sunny",
            "humidity": 60,
            "wind_speed": 10,
            "timestamp": datetime.now().isoformat()
        }
        return mock_data
    
    @staticmethod
    def get_weather_forecast(city: str, days: int = 5) -> List[Dict[str, Any]]:
        """
        Get weather forecast for specified number of days
        Note: This is a mock implementation.
        """
        forecast = []
        for i in range(days):
            day_data = {
                "day": i + 1,
                "city": city,
                "temperature_high": 25 + i,
                "temperature_low": 15 + i,
                "condition": ["Sunny", "Cloudy", "Rainy", "Partly Cloudy"][i % 4],
                "precipitation_chance": (i * 20) % 100
            }
            forecast.append(day_data)
        return forecast

class FileOperationsTool:
    """File system operations"""
    
    @staticmethod
    def read_file(file_path: str) -> str:
        """Read content from a file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return f"File not found: {file_path}"
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    @staticmethod
    def write_file(file_path: str, content: str) -> str:
        """Write content to a file"""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return f"Successfully wrote to {file_path}"
        except Exception as e:
            return f"Error writing file: {str(e)}"
    
    @staticmethod
    def list_directory(directory_path: str) -> List[str]:
        """List contents of a directory"""
        try:
            return os.listdir(directory_path)
        except FileNotFoundError:
            return [f"Directory not found: {directory_path}"]
        except Exception as e:
            return [f"Error listing directory: {str(e)}"]

class TextAnalysisTool:
    """Text analysis and processing tools"""
    
    @staticmethod
    def count_words(text: str) -> int:
        """Count words in text"""
        return len(text.split())
    
    @staticmethod
    def count_characters(text: str, include_spaces: bool = True) -> int:
        """Count characters in text"""
        if include_spaces:
            return len(text)
        else:
            return len(text.replace(' ', ''))
    
    @staticmethod
    def extract_keywords(text: str, max_keywords: int = 10) -> List[str]:
        """Extract keywords from text (simple implementation)"""
        # Simple keyword extraction - remove common words
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should'}
        
        words = text.lower().split()
        keywords = [word.strip('.,!?;:"()[]') for word in words if word.lower() not in common_words and len(word) > 2]
        
        # Count frequency and return top keywords
        word_freq = {}
        for word in keywords:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in sorted_words[:max_keywords]]

# Tool schema definitions for Mistral
TOOL_SCHEMAS = {
    "calculator_add": {
        "type": "function",
        "function": {
            "name": "calculator_add",
            "description": "Add two numbers together",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    "calculator_multiply": {
        "type": "function",
        "function": {
            "name": "calculator_multiply", 
            "description": "Multiply two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    "get_weather": {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather information for a city",
            "parameters": {
                "type": "object", 
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                    "country": {"type": "string", "description": "Country code (optional)", "default": "US"}
                },
                "required": ["city"]
            }
        }
    },
    "analyze_text": {
        "type": "function",
        "function": {
            "name": "analyze_text",
            "description": "Analyze text and extract keywords and statistics",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "Text to analyze"},
                    "max_keywords": {"type": "integer", "description": "Maximum number of keywords to extract", "default": 10}
                },
                "required": ["text"]
            }
        }
    }
}

def execute_tool(tool_name: str, parameters: Dict[str, Any]) -> Any:
    """Execute a tool with given parameters"""
    
    if tool_name == "calculator_add":
        return CalculatorTool.add(parameters["a"], parameters["b"])
    
    elif tool_name == "calculator_multiply":
        return CalculatorTool.multiply(parameters["a"], parameters["b"])
    
    elif tool_name == "get_weather":
        city = parameters["city"]
        country = parameters.get("country", "US")
        return WeatherTool.get_current_weather(city, country)
    
    elif tool_name == "analyze_text":
        text = parameters["text"]
        max_keywords = parameters.get("max_keywords", 10)
        
        word_count = TextAnalysisTool.count_words(text)
        char_count = TextAnalysisTool.count_characters(text)
        keywords = TextAnalysisTool.extract_keywords(text, max_keywords)
        
        return {
            "word_count": word_count,
            "character_count": char_count,
            "keywords": keywords,
            "text_length": len(text)
        }
    
    else:
        raise ValueError(f"Unknown tool: {tool_name}")

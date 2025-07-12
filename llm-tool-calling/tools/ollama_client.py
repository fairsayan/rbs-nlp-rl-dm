"""
Ollama client helper for Mistral Tool Calling
This module provides a simple interface to interact with Ollama-hosted Mistral models
"""

import json
import requests
from typing import Dict, Any, List, Optional

class OllamaClient:
    """Simple client for Ollama API"""
    
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url
        self.model_name = "mistral:7b-instruct"
    
    def is_available(self) -> bool:
        """Check if Ollama is running and accessible"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def list_models(self) -> List[str]:
        """List available models"""
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            if response.status_code == 200:
                data = response.json()
                return [model["name"] for model in data.get("models", [])]
            return []
        except:
            return []
    
    def generate(self, prompt: str, system_prompt: str = None, tools: List[Dict] = None) -> str:
        """Generate response from Mistral model"""
        
        # Prepare the request
        data = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9
            }
        }
        
        if system_prompt:
            data["system"] = system_prompt
        
        try:
            response = requests.post(f"{self.base_url}/api/generate", json=data)
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "")
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Connection error: {str(e)}"
    
    def chat(self, messages: List[Dict[str, str]], tools: List[Dict] = None) -> str:
        """Chat with Mistral model using conversation format"""
        
        data = {
            "model": self.model_name,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9
            }
        }
        
        if tools:
            # Format tools for Ollama (simplified)
            data["tools"] = tools
        
        try:
            response = requests.post(f"{self.base_url}/api/chat", json=data)
            if response.status_code == 200:
                result = response.json()
                return result.get("message", {}).get("content", "")
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Connection error: {str(e)}"

def format_tool_call_prompt(user_message: str, available_tools: List[Dict]) -> str:
    """Format a prompt for tool calling with Mistral"""
    
    tools_description = "\n".join([
        f"- {tool['function']['name']}: {tool['function']['description']}"
        for tool in available_tools
    ])
    
    prompt = f"""You are an AI assistant with access to the following tools:

{tools_description}

When you need to use a tool, respond with a JSON object in this format:
{{
    "tool_call": {{
        "name": "tool_name",
        "parameters": {{
            "param1": "value1",
            "param2": "value2"
        }}
    }}
}}

If you don't need to use any tools, respond normally.

User message: {user_message}"""
    
    return prompt

def extract_tool_call(response: str) -> Optional[Dict[str, Any]]:
    """Extract tool call from model response"""
    try:
        # Look for JSON in the response
        start_idx = response.find("{")
        end_idx = response.rfind("}") + 1
        
        if start_idx != -1 and end_idx != 0:
            json_str = response[start_idx:end_idx]
            parsed = json.loads(json_str)
            
            if "tool_call" in parsed:
                return parsed["tool_call"]
    except:
        pass
    
    return None

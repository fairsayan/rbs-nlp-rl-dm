"""
Example: Basic Calculator Tool Usage
This example demonstrates basic mathematical operations using tool calling.
"""

import sys
import os
sys.path.append('../tools')

from custom_tools import CalculatorTool, execute_tool

def calculator_examples():
    """Run various calculator examples"""
    
    print("🔢 Calculator Tool Examples")
    print("=" * 30)
    
    examples = [
        ("Addition", "calculator_add", {"a": 125, "b": 67}),
        ("Multiplication", "calculator_multiply", {"a": 15, "b": 8}),
        ("Power", "calculator_power", {"base": 2, "exponent": 10}),
        ("Square Root", "calculator_square_root", {"number": 144})
    ]
    
    for name, tool_name, params in examples:
        try:
            if hasattr(CalculatorTool, tool_name.split('_')[-1]):
                if tool_name == "calculator_power":
                    result = CalculatorTool.power(params["base"], params["exponent"])
                elif tool_name == "calculator_square_root":
                    result = CalculatorTool.square_root(params["number"])
                else:
                    result = execute_tool(tool_name, params)
                
                print(f"{name}: {params} = {result}")
            else:
                result = execute_tool(tool_name, params)
                print(f"{name}: {params} = {result}")
                
        except Exception as e:
            print(f"{name}: Error - {e}")
    
    # Advanced calculations
    print("\n🧮 Advanced Examples:")
    
    # Calculate area of a circle (π * r²)
    import math
    radius = 5
    area = CalculatorTool.multiply(math.pi, CalculatorTool.power(radius, 2))
    print(f"Circle area (r={radius}): {area:.2f}")
    
    # Compound interest calculation
    principal = 1000
    rate = 0.05  # 5%
    time = 10
    compound = CalculatorTool.multiply(principal, CalculatorTool.power(1 + rate, time))
    print(f"Compound interest: ${principal} at {rate*100}% for {time} years = ${compound:.2f}")

if __name__ == "__main__":
    calculator_examples()

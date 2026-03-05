#!/usr/bin/env python3
\"\"\"Debug helper utility for common debugging tasks.

Provides functions for:
- Error analysis
- Stack trace parsing
- Variable inspection
- Logging setup
- Quick diagnostics
\"\"\"

import sys
import traceback
import inspect
from typing import Any, Dict, List, Optional
from functools import wraps

def analyze_error(error: Exception) -> Dict[str, Any]:
    \"\"\"
    Analyze an exception and return detailed information.
    
    Args:
        error: The exception to analyze
        
    Returns:
        Dictionary with error details
    \"\"\"
    tb = traceback.extract_tb(error.__traceback__)
    
    return {
        "type": type(error).__name__,
        "message": str(error),
        "file": tb[-1].filename if tb else "unknown",
        "line": tb[-1].lineno if tb else 0,
        "function": tb[-1].name if tb else "unknown",
        "traceback": "".join(traceback.format_exception(type(error), error, error.__traceback__))
    }

def get_stack_info() -> Dict[str, Any]:
    \"\"\"
    Get current stack information.
    
    Returns:
        Dictionary with stack details
    \"\"\"
    frame = inspect.currentframe()
    caller = frame.f_back
    
    return {
        "file": caller.f_code.co_filename,
        "line": caller.f_lineno,
        "function": caller.f_code.co_name,
        "locals": dict(caller.f_locals)
    }

def inspect_variable(var: Any, name: str = "variable") -> Dict[str, Any]:
    \"\"\"
    Inspect a variable and return its details.
    
    Args:
        var: The variable to inspect
        name: Variable name for display
        
    Returns:
        Dictionary with variable details
    \"\"\"
    return {
        "name": name,
        "type": type(var).__name__,
        "value": repr(var),
        "size": sys.getsizeof(var),
        "is_none": var is None,
        "is_callable": callable(var),
        "has_len": hasattr(var, "__len__"),
        "length": len(var) if hasattr(var, "__len__") else None,
    }

def safe_call(func, *args, **kwargs) -> Dict[str, Any]:
    \"\"\"
    Safely call a function and return result or error.
    
    Args:
        func: Function to call
        *args: Positional arguments
        **kwargs: Keyword arguments
        
    Returns:
        Dictionary with success status and result/error
    \"\"\"
    try:
        result = func(*args, **kwargs)
        return {
            "success": True,
            "result": result,
            "error": None
        }
    except Exception as e:
        return {
            "success": False,
            "result": None,
            "error": analyze_error(e)
        }

def setup_logging(level: str = "DEBUG", file: str = None):
    \"\"\"
    Setup logging with debug format.
    
    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR)
        file: Optional file path for log output
    \"\"\"
    import logging
    
    format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    handlers = [logging.StreamHandler()]
    if file:
        handlers.append(logging.FileHandler(file))
    
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format=format_str,
        handlers=handlers
    )

def trace_calls(func):
    \"\"\"
    Decorator to trace function calls.
    
    Usage:
        @trace_calls
        def my_function(x):
            return x * 2
    \"\"\"
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[TRACE] Calling {func.__name__}")
        print(f"  Args: {args}")
        print(f"  Kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"  Result: {result}")
            return result
        except Exception as e:
            print(f"  Error: {e}")
            raise
    return wrapper

def dump_state(*variables: tuple) -> str:
    \"\"\"
    Dump variables state for debugging.
    
    Args:
        *variables: Tuples of (name, value)
        
    Returns:
        Formatted string with all variable info
    \"\"\"
    lines = ["=== Debug State ==="]
    for name, value in variables:
        info = inspect_variable(value, name)
        lines.append(f"{name}:")
        lines.append(f"  Type: {info['type']}")
        lines.append(f"  Value: {info['value']}")
        if info['length'] is not None:
            lines.append(f"  Length: {info['length']}")
    lines.append("==================")
    return "\n".join(lines)

def find_bug_suggestion(error: Exception) -> List[str]:
    \"\"\"
    Suggest fixes based on error type.
    
    Args:
        error: The exception
        
    Returns:
        List of suggested fixes
    \"\"\"
    suggestions = {
        "NameError": [
            "Check if variable is defined before use",
            "Check for spelling mistakes",
            "Verify import statements",
        ],
        "TypeError": [
            "Check variable types",
            "Use type conversion (str(), int(), etc.)",
            "Add type checking",
        ],
        "AttributeError": [
            "Check if object is None",
            "Verify attribute exists",
            "Add None check before access",
        ],
        "KeyError": [
            "Use .get() with default value",
            "Check if key exists with 'in' operator",
            "Validate dictionary structure",
        ],
        "IndexError": [
            "Check list length before access",
            "Use try/except for edge cases",
            "Consider using .get() for dict-like access",
        ],
        "ValueError": [
            "Validate input values",
            "Add try/except for conversion",
            "Check value ranges",
        ],
        "ZeroDivisionError": [
            "Add check for zero before division",
            "Use try/except",
            "Consider default value",
        ],
    }
    
    error_type = type(error).__name__
    return suggestions.get(error_type, [
        "Read the error message carefully",
        "Check the line number",
        "Add debug logging",
        "Use print statements",
    ])

def format_error_report(error: Exception) -> str:
    \"\"\"
    Generate a comprehensive error report.
    
    Args:
        error: The exception
        
    Returns:
        Formatted error report
    \"\"\"
    analysis = analyze_error(error)
    suggestions = find_bug_suggestion(error)
    
    lines = [
        "\n=== ERROR REPORT ===",
        f"Type: {analysis['type']}",
        f"Message: {analysis['message']}",
        f"File: {analysis['file']}",
        f"Line: {analysis['line']}",
        f"Function: {analysis['function']}",
        "\nTraceback:",
        analysis['traceback'],
        "\nSuggestions:",
    ]
    
    for i, suggestion in enumerate(suggestions, 1):
        lines.append(f"  {i}. {suggestion}")
    
    lines.append("\n===================")
    return "\n".join(lines)

def main():
    \"\"\"Demo usage.\"\"\"
    print("Debug Helper Demo")
    print("=" * 40)
    
    # Example: Analyze an error
    try:
        x = None
        y = x.name  # AttributeError
    except Exception as e:
        print(format_error_report(e))
    
    # Example: Inspect variable
    my_list = [1, 2, 3, 4, 5]
    print(inspect_variable(my_list, "my_list"))
    
    # Example: Stack info
    print(get_stack_info())

if __name__ == "__main__":
    main()

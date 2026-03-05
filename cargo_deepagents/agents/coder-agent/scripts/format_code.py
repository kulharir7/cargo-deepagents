#!/usr/bin/env python3
\"\"\"Code formatting utility script.

Formats code using various formatters based on file type.
Supports: Python (black, isort), JavaScript/TypeScript (prettier), Go (gofmt).
\"\"\"

import subprocess
import sys
from pathlib import Path

FORMATTERS = {
    '.py': ['black', 'isort'],
    '.js': ['prettier'],
    '.ts': ['prettier'],
    '.jsx': ['prettier'],
    '.tsx': ['prettier'],
    '.go': ['gofmt'],
    '.rs': ['rustfmt'],
}

def format_file(file_path: str, check_only: bool = False) -> dict:
    \"\"\"
    Format a file using appropriate formatter.
    
    Args:
        file_path: Path to the file
        check_only: If True, only check formatting without modifying
        
    Returns:
        dict with 'success', 'output', 'formatter'
    \"\"\"
    path = Path(file_path)
    ext = path.suffix
    
    if ext not in FORMATTERS:
        return {
            'success': True,
            'output': f'No formatter for {ext}',
            'formatter': None
        }
    
    formatter = FORMATTERS[ext][0]
    cmd = [formatter]
    
    if check_only:
        if formatter == 'black':
            cmd.append('--check')
        elif formatter == 'isort':
            cmd.append('--check')
        elif formatter == 'prettier':
            cmd.append('--check')
        # gofmt and rustfmt use -d for diff
    
    cmd.append(file_path)
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        return {
            'success': result.returncode == 0,
            'output': result.stdout or result.stderr,
            'formatter': formatter
        }
    except FileNotFoundError:
        return {
            'success': False,
            'output': f'Formatter {formatter} not installed',
            'formatter': formatter
        }
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'output': 'Formatting timed out',
            'formatter': formatter
        }

def main():
    if len(sys.argv) < 2:
        print('Usage: python format_code.py <file> [--check]')
        sys.exit(1)
    
    file_path = sys.argv[1]
    check_only = '--check' in sys.argv
    
    result = format_file(file_path, check_only)
    
    print(f"Formatter: {result['formatter']}")
    print(f"Success: {result['success']}")
    if result['output']:
        print(result['output'])
    
    sys.exit(0 if result['success'] else 1)

if __name__ == '__main__':
    main()

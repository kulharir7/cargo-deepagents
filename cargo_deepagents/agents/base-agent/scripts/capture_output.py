#!/usr/bin/env python3
\"\"\"Capture command output for analysis.\"\"\"

import subprocess
import sys
import json
from pathlib import Path

def capture_output(command: str, timeout: int = 30) -> dict:
    \"\"\"
    Run a command and capture its output.
    
    Args:
        command: Shell command to run
        timeout: Timeout in seconds
        
    Returns:
        dict with 'stdout', 'stderr', 'returncode', 'success'
    \"\"\"
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        return {
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode,
            'success': result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {
            'stdout': '',
            'stderr': f'Command timed out after {timeout}s',
            'returncode': -1,
            'success': False
        }
    except Exception as e:
        return {
            'stdout': '',
            'stderr': str(e),
            'returncode': -1,
            'success': False
        }

def main():
    if len(sys.argv) < 2:
        print('Usage: python capture_output.py "<command>" [timeout]')
        sys.exit(1)
    
    command = sys.argv[1]
    timeout = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    
    result = capture_output(command, timeout)
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()

# Base Agent Examples

## Example 1: Create a Python Script

**User Request:** "Create a script that processes CSV files"

**Agent Workflow:**
1. Plan the script structure
2. Search for best practices
3. Write the implementation

```python
# scripts/process_csv.py
import csv
from pathlib import Path

def process_csv(input_path: str, output_path: str):
    \"\"\"Process CSV file and save results.\"\"\"
    with open(input_path, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    # Process data...
    processed = [row for row in data if row.get('active')]
    
    with open(output_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(processed)
    
    return len(processed)

if __name__ == '__main__':
    import sys
    process_csv(sys.argv[1], sys.argv[2])
```

---

## Example 2: Fix a Bug

**User Request:** "Fix the authentication error in login.py"

**Agent Workflow:**
1. Read the error message
2. Find the file
3. Identify the issue
4. Fix it

```
# Step 1: Read error from user
# Step 2: read login.py
# Step 3: Identify issue (e.g., missing import)

# Before:
def authenticate(user, password):
    # Missing import
    return jwt.encode(...)

# After:
import jwt

def authenticate(user, password):
    return jwt.encode(...)
```

---

## Example 3: Web Search and Implement

**User Request:** "Add rate limiting to the API - search for Python solutions"

**Agent Workflow:**
1. Search for solutions
2. Evaluate options
3. Implement chosen solution

```python
# After web_search("python rate limiting fastapi")
# Found: slowapi, fastapi-limiter

# Choose slowapi for simplicity

from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.get("/api/data")
@limiter.limit("100/minute")
async def get_data():
    return {"data": "..."}

```

---

## Example 4: Refactor Code

**User Request:** "Refactor the user module to use async"

**Agent Workflow:**
1. Read current implementation
2. Plan changes
3. Make incremental edits
4. Test

```python
# Before:

def get_user(user_id):
    return db.query(User).get(user_id)

def create_user(data):
    user = User(**data)
    db.add(user)
    db.commit()
    return user

# After:

async def get_user(user_id):
    return await db.query(User).get(user_id)

async def create_user(data):
    user = User(**data)
    db.add(user)
    await db.commit()
    return user

```

---

## Example 5: Browser Automation

**User Request:** "Check the dashboard at example.com and take a screenshot"

**Agent Workflow:**
1. Start browser
2. Navigate to URL
3. Take screenshot
4. Return result

```
browser start
browser navigate https://example.com/dashboard
browser screenshot
# Screenshot saved, shows current dashboard state
```

---

## Example 6: Multi-file Search and Replace

**User Request:** "Replace deprecated function 'get_data' with 'fetch_data' everywhere"

**Agent Workflow:**
1. Search all occurrences
2. Plan replacements
3. Edit each file

```
# Step 1: Search
grep -r "get_data" src/

# Step 2: Read each file and plan edit
# Step 3: Edit each file

edit src/api.py "get_data" "fetch_data"
edit src/models.py "get_data" "fetch_data"
edit tests/test_api.py "get_data" "fetch_data"

```

---

## Example 7: Create Test Coverage

**User Request:** "Add unit tests for utils.py"

**Agent Workflow:**
1. Read the module
2. Identify functions
3. Write tests

```python
# tests/test_utils.py
import pytest
from utils import calculate_total, format_name

class TestCalculateTotal:
    def test_positive_numbers(self):
        assert calculate_total([1, 2, 3]) == 6
    
    def test_empty_list(self):
        assert calculate_total([]) == 0
    
    def test_negative_numbers(self):
        assert calculate_total([-1, -2, -3]) == -6

class TestFormatName:
    def test_simple_name(self):
        assert format_name("john") == "John"
    
    def test_full_name(self):
        assert format_name("john doe") == "John Doe"
```

---

*Load this reference for task-specific implementation patterns*

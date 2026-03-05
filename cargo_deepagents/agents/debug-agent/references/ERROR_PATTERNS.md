# Error Patterns Library

Comprehensive list of common error patterns and their solutions.

## Python Error Patterns

### NameError

```python
# Error
NameError: name 'variable' is not defined

# Cause
def process():
    print(variable)  # variable not defined

# Fix
def process():
    variable = "value"  # Define first
    print(variable)
```

### TypeError

```python
# Error
TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Cause
count = 5
message = "Count: " + count

# Fix
count = 5
message = f"Count: {count}"  # Use f-string
# or
message = "Count: " + str(count)  # Convert type
```

### AttributeError

```python
# Error
AttributeError: 'NoneType' object has no attribute 'name'

# Cause
user = get_user()  # Returns None
print(user.name)  # None has no 'name'

# Fix
user = get_user()
if user:
    print(user.name)
else:
    print("User not found")
```

### KeyError

```python
# Error
KeyError: 'missing_key'

# Cause
data = {"name": "John"}
value = data["email"]  # Key doesn't exist

# Fix
data = {"name": "John"}
value = data.get("email", "default@example.com")
# or
value = data["email"] if "email" in data else "default"
```

### IndexError

```python
# Error
IndexError: list index out of range

# Cause
items = [1, 2, 3]
value = items[5]  # Only 3 items

# Fix
items = [1, 2, 3]
value = items[5] if len(items) > 5 else None
# or
value = items[5]  # Handle exception
```

### ValueError

```python
# Error
ValueError: invalid literal for int() with base 10: 'abc'

# Cause
num = int("abc")  # Can't convert

# Fix
try:
    num = int(value)
except ValueError:
    num = 0
    print(f"Invalid number: {value}")
```

### ImportError

```python
# Error
ImportError: No module named 'requests'

# Cause
import requests  # Module not installed

# Fix
# Install module
# pip install requests

# Or use try/except
try:
    import requests
except ImportError:
    print("Please install: pip install requests")
```

### ZeroDivisionError

```python
# Error
ZeroDivisionError: division by zero

# Cause
result = numerator / denominator  # denominator is 0

# Fix
if denominator != 0:
    result = numerator / denominator
else:
    result = 0
    # or raise ValueError("Denominator cannot be zero")
```

---

## JavaScript Error Patterns

### TypeError: undefined is not a function

```javascript
// Error
TypeError: undefined is not a function

// Cause
const result = user.getName()  // user is undefined

// Fix
if (user && typeof user.getName === 'function') {
    const result = user.getName();
}
```

### TypeError: Cannot read property of undefined

```javascript
// Error
TypeError: Cannot read property 'name' of undefined

// Cause
const name = user.profile.name  // user.profile is undefined

// Fix
const name = user?.profile?.name ?? 'Unknown';
// or
const name = user && user.profile ? user.profile.name : 'Unknown';
```

### ReferenceError

```javascript
// Error
ReferenceError: variable is not defined

// Cause
console.log(myVariable)  // myVariable not declared

// Fix
let myVariable = "value";
console.log(myVariable);
```

### SyntaxError

```javascript
// Error
SyntaxError: Unexpected token '}'

// Cause
// Missing opening brace
function test()
    return "value";
}

// Fix
function test() {
    return "value";
}
```

---

## Common Bug Patterns

### Off-by-One Error

```python
# Bug
for i in range(len(items)):  # Access items[i+1] causes IndexError
    print(items[i + 1])

# Fix
for i in range(len(items) - 1):
    print(items[i + 1])
# or better
for item in items:
    print(item)
```

### Infinite Loop

```python
# Bug
while True:
    print("Forever!")

# Fix
while condition:
    print("Processing")
    condition = update_condition()
```

### Mutable Default Argument

```python
# Bug
def add_item(item, items=[]):
    items.append(item)
    return items

# Fix
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Race Condition

```python
# Bug (async)
async def process():
    result = cache["key"]  # Multiple coroutines access
    result["count"] += 1
    cache["key"] = result

# Fix
import asyncio

lock = asyncio.Lock()

async def process():
    async with lock:
        result = cache["key"]
        result["count"] += 1
        cache["key"] = result
```

---

## Environment Issues

### Module Not Found

```
# Check installed packages
pip list

# Install missing package
pip install package_name

# Check Python path
import sys
print(sys.path)

# Use virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Permission Denied

```
# Check file permissions
ls -la file.txt

# Fix permissions
chmod 644 file.txt  # Read/write for owner

# Run with proper permissions
sudo python script.py  # If needed
```

### Port Already in Use

```
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>

# Use different port
python manage.py runserver 8001
```

---

## Performance Issues

### Slow Query

```python
# Slow N+1 query
for user in users:
    orders = Order.query.filter_by(user_id=user.id).all()

# Fix: Eager loading
users = User.query.options(db.joinedload(Order)).all()
```

### Memory Leak

```python
# Potential leak
cache = {}

def store(key, value):
    cache[key] = value  # Never cleared

# Fix: Limit cache
from functools import lru_cache

@lru_cache(maxsize=1000)
def store(key, value):
    return value
```

### Slow Loops

```python
# Slow
result = []
for item in items:
    result.append(str(item))

# Fast: List comprehension
result = [str(item) for item in items]

# Faster: Map (for simple operations)
result = list(map(str, items))
```

---

*Error Patterns v1.0*

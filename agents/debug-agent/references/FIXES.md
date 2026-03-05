# Common Fixes Reference

Quick reference for common fixes organized by issue type.

## Quick Fix Index

| Issue | Fix | Section |
|-------|-----|----------|
| Null/None error | Add null check | [Null Fixes](#null-fixes) |
| Type mismatch | Convert types | [Type Fixes](#type-fixes) |
| Missing import | Install/import | [Import Fixes](#import-fixes) |
| Slow code | Optimize | [Performance Fixes](#performance-fixes) |
| Memory leak | Free resources | [Memory Fixes](#memory-fixes) |
| Async issues | Use await | [Async Fixes](#async-fixes) |

---

## Null Fixes

### Python None Check

```python
# Before
def get_name(user):
    return user.name

# After
def get_name(user):
    return user.name if user else "Unknown"
```

### JavaScript Undefined Check

```javascript
// Before
const name = user.profile.name;

// After
const name = user?.profile?.name ?? 'Unknown';
```

### Dict Key Check

```python
# Before
value = data["key"]

# After
value = data.get("key", default_value)

# Or check
if "key" in data:
    value = data["key"]
else:
    value = default_value
```

---

## Type Fixes

### String + Number

```python
# Before
result = "Count: " + count

# After
result = f"Count: {count}"
# or
result = "Count: " + str(count)
```

### List to String

```python
# Before
text = items  # Want string

# After
text = ", ".join(str(item) for item in items)
```

### JSON Parse Error

```python
import json

# Before
data = json.loads(text)  # Might fail

# After
try:
    data = json.loads(text)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
    data = {}
```

---

## Import Fixes

### Module Not Found

```python
# Before
import requests  # ImportError

# After
try:
    import requests
except ImportError:
    import subprocess
    subprocess.run(["pip", "install", "requests"])
    import requests
```

### Circular Import

```python
# Before (circular)
# a.py
from b import B
# b.py
from a import A

# After (deferred)
# a.py
def use_b():
    from b import B  # Import inside function
    return B()
```

### Relative Import Error

```python
# Before
from .module import func  # ImportError

# After
try:
    from .module import func
except ImportError:
    from module import func
```

---

## Performance Fixes

### Slow Query

```python
# Before
for user in users:
    profile = Profile.query.filter_by(user_id=user.id).first()

# After (eager loading)
users = User.query.options(joinedload(Profile)).all()

# Or (batch query)
user_ids = [u.id for u in users]
profiles = Profile.query.filter(Profile.user_id.in_(user_ids)).all()
profile_map = {p.user_id: p for p in profiles}
for user in users:
    profile = profile_map.get(user.id)
```

### Slow Loop

```python
# Before
result = []
for item in large_list:
    result.append(transform(item))

# After
result = [transform(item) for item in large_list]

# Or parallel
from multiprocessing import Pool
with Pool() as pool:
    result = pool.map(transform, large_list)
```

### Repeated Calculations

```python
# Before
def get_data():
    return expensive_calculation()  # Called every time

# After
from functools import lru_cache

@lru_cache(maxsize=128)
def get_data():
    return expensive_calculation()  # Cached
```

---

## Memory Fixes

### Memory Leak

```python
# Before (leak)
cache = {}
def store(key, value):
    cache[key] = value  # Never cleared

# After (bounded)
from collections import OrderedDict

class BoundedCache:
    def __init__(self, max_size=1000):
        self.cache = OrderedDict()
        self.max_size = max_size
    
    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)
```

### Resource Not Closed

```python
# Before (leak)
f = open("file.txt")
data = f.read()
# Forgot to close!

# After
with open("file.txt") as f:
    data = f.read()
# Auto-closed
```

### Large Data Processing

```python
# Before (memory heavy)
data = list(all_records())  # Loads all into memory

# After (chunks)
def process_chunks(chunk_size=1000):
    for offset in range(0, total, chunk_size):
        chunk = get_records(offset, chunk_size)
        process(chunk)
```

---

## Async Fixes

### Missing Await

```python
# Before (wrong)
async def fetch_data():
    result = async_operation()  # Missing await!
    return result

# After (correct)
async def fetch_data():
    result = await async_operation()
    return result
```

### Async in Loop

```python
# Before (sequential)
for url in urls:
    await fetch(url)  # One by one

# After (parallel)
import asyncio
results = await asyncio.gather(*[fetch(url) for url in urls])
```

### Blocking Async

```python
# Before (blocking)
async def process():
    time.sleep(5)  # Blocks event loop!

# After (non-blocking)
async def process():
    await asyncio.sleep(5)  # Proper async
```

---

## Error Handling Fixes

### Bare Except

```python
# Before
try:
    do_something()
except:  # Catches everything, including KeyboardInterrupt
    pass

# After
try:
    do_something()
except Exception as e:
    logger.error(f"Error: {e}")
    raise
```

### Silently Ignoring Errors

```python
# Before
try:
    risky_operation()
except:
    pass  # Silent failure

# After
try:
    risky_operation()
except SpecificError as e:
    logger.warning(f"Expected error: {e}")
    # Handle gracefully
```

### Not Reraising

```python
# Before
def process():
    try:
        operation()
    except ValueError:
        cleanup()
        # Error swallowed!

# After
def process():
    try:
        operation()
    except ValueError as e:
        cleanup()
        raise  # Re-raise
```

---

## Security Fixes

### SQL Injection

```python
# Before (vulnerable)
query = f"SELECT * FROM users WHERE id = {user_input}"

# After (safe)
cursor.execute("SELECT * FROM users WHERE id = ?", (user_input,))
```

### XSS (Cross-Site Scripting)

```python
# Before (vulnerable)
return f"<div>{user_input}</div>"

# After (safe)
from html import escape
return f"<div>{escape(user_input)}</div>"
```

### Path Traversal

```python
# Before (vulnerable)
with open(f"uploads/{filename}") as f:
    data = f.read()

# After (safe)
from pathlib import Path
base = Path("uploads")
file = base / filename
if not file.resolve().is_relative_to(base.resolve()):
    raise ValueError("Invalid path")
with open(file) as f:
    data = f.read()
```

---

## Testing Fixes

### Flaky Test

```python
# Before (flaky)
def test_timing():
    start = time.time()
    operation()
    assert time.time() - start < 0.1  # Depends on system load

# After (stable)
def test_timing():
    start = time.time()
    operation()
    assert time.time() - start < 1.0  # Reasonable margin
```

### Unmocked Dependency

```python
# Before (calls real API)
def test_api():
    result = call_api()

# After (mocked)
from unittest.mock import patch

@patch("module.call_api")
def test_api(mock_call):
    mock_call.return_value = {"status": "ok"}
    result = call_api()
    assert result["status"] == "ok"
```

---

*Common Fixes v1.0*

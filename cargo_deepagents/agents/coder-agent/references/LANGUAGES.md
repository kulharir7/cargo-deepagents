# Language-Specific Patterns

## Python

### Project Structure

```
project/
├── src/
│   ├── __init__.py
│   ├── module.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_module.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Common Patterns

#### Context Manager

```python
class ResourceManager:
    def __init__(self, resource):
        self.resource = resource
    
    def __enter__(self):
        self.resource.open()
        return self.resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.resource.close()
        return False

# Usage
with ResourceManager(resource) as r:
    r.process()
```

#### Decorator

```python
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__}: {end-start:.4f}s')
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
```

#### Async Pattern

```python
import asyncio

async def fetch_all(urls: list[str]) -> list:
    tasks = [fetch(url) for url in urls]
    return await asyncio.gather(*tasks)

# Run
results = asyncio.run(fetch_all(urls))
```

---

## JavaScript/TypeScript

### Project Structure

```
project/
├── src/
│   ├── index.ts
│   ├── utils/
│   │   └── helpers.ts
│   └── modules/
│       └── feature.ts
├── tests/
│   └── feature.test.ts
├── package.json
├── tsconfig.json
└── README.md
```

### Common Patterns

#### API Handler

```typescript
import express from 'express';

const app = express();

app.get('/api/users/:id', async (req, res) => {
  try {
    const user = await userService.getById(req.params.id);
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```

#### React Component

```typescript
import React from 'react';

interface Props {
  title: string;
  onSubmit: (data: FormData) => void;
}

export const Form: React.FC<Props> = ({ title, onSubmit }) => {
  const [data, setData] = useState<FormData>({});
  
  return (
    <form onSubmit={(e) => {
      e.preventDefault();
      onSubmit(data);
    }}>
      <h1>{title}</h1>
      {/* ... */}
    </form>
  );
};
```

---

## Go

### Project Structure

```
project/
├── cmd/
│   └── app/
│       └── main.go
├── internal/
│   ├── handler/
│   ├── service/
│   └── repository/
├── pkg/
│   └── utils/
├── go.mod
└── go.sum
```

### Common Patterns

#### HTTP Handler

```go
func (h *Handler) GetUser(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    id := vars["id"]
    
    user, err := h.service.GetByID(id)
    if err != nil {
        http.Error(w, err.Error(), http.StatusNotFound)
        return
    }
    
    json.NewEncoder(w).Encode(user)
}
```

---

## Rust

### Project Structure

```
project/
├── src/
│   ├── main.rs
│   ├── lib.rs
│   └── module.rs
├── Cargo.toml
└── README.md
```

### Common Patterns

#### Error Handling

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    
    #[error("Parse error: {0}")]
    Parse(#[from] std::num::ParseIntError),
}

pub type Result<T> = std::result::Result<T, AppError>;
```

---

## Best Practices by Language

| Language | Style Guide | Testing | Linting |
|----------|-------------|---------|---------|
| Python | PEP 8 | pytest | ruff |
| JavaScript | Airbnb | Jest | ESLint |
| TypeScript | TypeScript Handbook | Vitest | ESLint |
| Go | Effective Go | go test | golint |
| Rust | Rust API Guidelines | cargo test | clippy |


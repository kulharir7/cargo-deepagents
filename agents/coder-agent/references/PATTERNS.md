# Design Patterns Reference

## Creational Patterns

### Singleton

Ensure only one instance exists.

```python
class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def query(self, sql):
        # Execute query
        pass
```

### Factory

Create objects without specifying exact class.

```python
class AnimalFactory:
    @staticmethod
    def create(type_: str) -> Animal:
        if type_ == "dog":
            return Dog()
        elif type_ == "cat":
            return Cat()
        raise ValueError(f"Unknown animal: {type_}")
```

### Builder

Construct complex objects step by step.

```python
class QueryBuilder:
    def __init__(self):
        self._table = None
        self._columns = []
        self._where = []
    
    def select(self, *columns):
        self._columns.extend(columns)
        return self
    
    def from_table(self, table):
        self._table = table
        return self
    
    def where(self, condition):
        self._where.append(condition)
        return self
    
    def build(self):
        query = f"SELECT {', '.join(self._columns)} FROM {self._table}"
        if self._where:
            query += f" WHERE {' AND '.join(self._where)}"
        return query

# Usage
query = QueryBuilder().select("*").from_table("users").where("active=1").build()
```

---

## Structural Patterns

### Adapter

Make incompatible interfaces work together.

```python
class OldAPI:
    def get_data(self):
        return {"data": "old format"}

class Adapter:
    def __init__(self, old_api):
        self.old_api = old_api
    
    def fetch(self):
        data = self.old_api.get_data()
        return {"result": data["data"]}

# Usage
adapter = Adapter(OldAPI())
new_format = adapter.fetch()
```

### Decorator

Add behavior without altering structure.

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned from {func.__name__}")
        return result
    return wrapper

@log_calls
def process(data):
    return data.upper()
```

### Composite

Treat individual and group objects uniformly.

```python
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def operation(self):
        results = [c.operation() for c in self.children]
        return f"Composite({', '.join(results)})"
```

---

## Behavioral Patterns

### Strategy

Define interchangeable algorithms.

```python
class SortStrategy:
    @staticmethod
    def bubble(data):
        # Bubble sort
        pass
    
    @staticmethod
    def quick(data):
        # Quick sort
        pass

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def sort(self, data):
        return self.strategy(data)

# Usage
sorter = Sorter(SortStrategy.quick)
sorted_data = sorter.sort(data)
```

### Observer

Notify multiple objects about events.

```python
class Observable:
    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

class Observer:
    def update(self, event):
        print(f"Received: {event}")
```

### Command

Encapsulate requests as objects.

```python
class Command:
    def execute(self):
        pass

class CopyCommand(Command):
    def __init__(self, editor):
        self.editor = editor
    
    def execute(self):
        return self.editor.copy()

class Editor:
    def copy(self):
        return "Copied!"

# Usage
command = CopyCommand(editor)
result = command.execute()
```

---

## Architectural Patterns

### Repository Pattern

Separate data access from business logic.

```python
class UserRepository:
    def __init__(self, db):
        self.db = db
    
    def get_by_id(self, id):
        return self.db.query("SELECT * FROM users WHERE id = ?", id)
    
    def save(self, user):
        self.db.execute("INSERT INTO users VALUES (?)", user)

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
    
    def get_user(self, id):
        return self.repo.get_by_id(id)
```

### Dependency Injection

Inject dependencies instead of creating them.

```python
class App:
    def __init__(self, db, cache, logger):
        self.db = db
        self.cache = cache
        self.logger = logger

# Container
class Container:
    def __init__(self):
        self.db = Database()
        self.cache = Redis()
        self.logger = Logger()
    
    def create_app(self):
        return App(self.db, self.cache, self.logger)
```

---

## Pattern Selection Guide

| Problem | Pattern | When to Use |
|---------|---------|-------------|
| One instance needed | Singleton | Database, logger, config |
| Complex creation | Builder | SQL queries, API requests |
| Interface mismatch | Adapter | Legacy code, external APIs |
| Add behavior | Decorator | Logging, caching, validation |
| Interchangeable algo | Strategy | Sorting, payment methods |
| Event notification | Observer | UI updates, pub/sub |
| Undo operations | Command | Editor actions, transactions |

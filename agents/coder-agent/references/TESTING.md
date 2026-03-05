# Testing Best Practices

## Test Structure

### AAA Pattern (Arrange-Act-Assert)

```python
def test_user_creation():
    # Arrange
    name = "John"
    email = "john@example.com"
    
    # Act
    user = User(name, email)
    
    # Assert
    assert user.name == name
    assert user.email == email
```

### Test Organization

```
tests/
├── unit/
│   ├── test_module.py
│   └── test_utils.py
├── integration/
│   └── test_api.py
├── conftest.py          # Shared fixtures
└── __init__.py
```

---

## Unit Testing

### Basic Test

```python
import pytest
from calculator import add, subtract

class TestCalculator:
    def test_add_positive(self):
        assert add(2, 3) == 5
    
    def test_add_negative(self):
        assert add(-1, -2) == -3
        
    def test_add_zero(self):
        assert add(0, 5) == 5
    
    def test_subtract(self):
        assert subtract(5, 3) == 2
    
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(5, 0)
```

### Fixtures

```python
import pytest

@pytest.fixture
def database():
    db = Database(":memory:")
    db.create_tables()
    yield db
    db.close()

@pytest.fixture
def user_factory():
    def create(name="test", email="test@test.com"):
        return User(name=name, email=email)
    return create

def test_with_fixtures(database, user_factory):
    user = user_factory()
    database.insert(user)
    assert database.get(user.id) is not None
```

---

## Integration Testing

### API Testing

```python
import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def client():
    return TestClient(app)

def test_create_user(client):
    response = client.post("/users", json={
        "name": "John",
        "email": "john@example.com"
    })
    assert response.status_code == 201
    
def test_get_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
```

### Database Testing

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope="module")
def engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()
```

---

## Mocking

### Mock External Calls

```python
from unittest.mock import Mock, patch, MagicMock

def test_api_call():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"data": "test"}
        
        result = fetch_data("http://api.example.com")
        
        mock_get.assert_called_once_with("http://api.example.com")
        assert result == {"data": "test"}

def test_service_with_mocks():
    db_mock = Mock()
    db_mock.query.return_value = [User(id=1, name="test")]
    
    service = UserService(db_mock)
    result = service.get_users()
    
    db_mock.query.assert_called_once()
    assert len(result) == 1
```

---

## Test Coverage

### Run with Coverage

```bash
pytest --cov=src --cov-report=html --cov-report=term
```

### Coverage Config (pyproject.toml)

```toml
[tool.coverage.run]
source = ["src"]
omit = ["tests/*", "**/__init__.py"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
]
```

---

## Test Best Practices

### What to Test

| Test Type | Focus |
|-----------|-------|
| Unit | Single function/method |
| Integration | Component interaction |
| E2E | User workflows |
| Performance | Speed, memory |
| Security | Vulnerabilities |

### Test Naming

```python
# Good: test_<function>_<scenario>_<expected>
def test_process_payment_valid_card_success():
    pass

def test_process_payment_expired_card_raises_error():
    pass

def test_process_payment_insufficient_funds_declined():
    pass
```

### Test Categories

```python
import pytest

@pytest.mark.unit
def test_fast():
    pass

@pytest.mark.integration
def test_slow():
    pass

@pytest.mark.skip(reason="Not implemented")
def test_future():
    pass

# Run specific tests
# pytest -m unit
# pytest -m "not slow"
```

---

## JavaScript/TypeScript Testing

### Jest Example

```typescript
import { describe, test, expect, beforeEach } from '@jest/globals';
import { Calculator } from './calculator';

describe('Calculator', () => {
  let calc: Calculator;
  
  beforeEach(() => {
    calc = new Calculator();
  });
  
  test('adds 1 + 2 to equal 3', () => {
    expect(calc.add(1, 2)).toBe(3);
  });
  
  test('handles division by zero', () => {
    expect(() => calc.divide(5, 0)).toThrow('Division by zero');
  });
});
```

---

## Checklist

Before submitting code:

- [ ] All tests pass
- [ ] Coverage > 80%
- [ ] Edge cases covered
- [ ] Error cases tested
- [ ] No flaky tests
- [ ] Fast execution (< 5s for units)

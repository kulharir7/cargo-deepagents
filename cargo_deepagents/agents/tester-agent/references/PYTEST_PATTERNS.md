# Pytest Patterns

## Basic Test Structure

def test_function_description():
    # Arrange
    input_data = create_test_data()
    expected = expected_result()
    
    # Act
    result = function_under_test(input_data)
    
    # Assert
    assert result == expected

## Common Patterns

### Parametrize Tests
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert double(input) == expected

### Fixtures
@pytest.fixture
def database():
    db = create_test_db()
    yield db
    db.cleanup()

### Mocking
from unittest.mock import Mock, patch

def test_api_call():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"data": "test"}
        result = fetch_data()
        assert result == {"data": "test"}

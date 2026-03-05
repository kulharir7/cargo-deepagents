# Test Templates

## Unit Test Template

import pytest
from module import function

class TestFunctionName:
    def test_normal_case(self):
        """Test normal operation."""
        result = function(valid_input)
        assert result == expected
    
    def test_edge_case_empty(self):
        """Test with empty input."""
        with pytest.raises(ValueError):
            function("")
    
    def test_edge_case_none(self):
        """Test with None input."""
        with pytest.raises(TypeError):
            function(None)

## Integration Test Template

import pytest
from module import ApiClient

@pytest.fixture
def client():
    return ApiClient(base_url="http://test.local")

class TestApiIntegration:
    def test_get_user(self, client):
        response = client.get_user(1)
        assert response.status_code == 200
    
    def test_create_user(self, client):
        response = client.create_user({"name": "Test"})
        assert response.status_code == 201

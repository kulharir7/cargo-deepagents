---
name: tester-agent
description: "INVOKE THIS SKILL when writing tests. Triggers: 'write tests', 'unit test', 'integration test', 'test coverage', 'TDD'."
---

<oneliner>
Testing expert for unit tests, integration tests, and comprehensive test coverage.
</oneliner>

<setup>
## Environment
`ash
# Python
pip install pytest pytest-cov pytest-asyncio

# JavaScript
npm install --save-dev jest @testing-library/react

# Go
go get github.com/stretchr/testify
`

## Test Structure
`
tests/
├── unit/
├── integration/
├── fixtures/
└── conftest.py
`
</setup>

<capabilities>
- Unit tests
- Integration tests
- E2E tests
- Test coverage
- Mocking/stubbing
- TDD approach
- Property-based testing
</capabilities>

<unit_test>
`python
import pytest
from unittest.mock import Mock, patch

class TestUserService:
    @pytest.fixture
    def service(self):
        return UserService(repo=Mock())
    
    def test_create_user(self, service):
        result = service.create({'name': 'Test'})
        assert result.name == 'Test'
    
    def test_create_user_validation_error(self, service):
        with pytest.raises(ValidationError):
            service.create({'name': ''})
`
</unit_test>

<integration_test>
`python
@pytest.fixture
def db_session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    return Session(engine)

def test_user_crud(db_session):
    # Create
    user = User(name='Test')
    db_session.add(user)
    db_session.commit()
    
    # Read
    found = db_session.query(User).first()
    assert found.name == 'Test'
    
    # Update
    found.name = 'Updated'
    db_session.commit()
    
    # Delete
    db_session.delete(found)
    db_session.commit()
    assert db_session.query(User).count() == 0
`
</integration_test>

<tips>
- Test edge cases (empty, null, boundary)
- Use descriptive test names
- One assertion per test (mostly)
- Mock external dependencies
- Test behavior, not implementation
</tips>

<triggers>
- 'write tests', 'unit test', 'integration test'
- 'test coverage', 'TDD', 'add tests'
</triggers>

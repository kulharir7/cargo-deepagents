---
name: docs-agent
description: "INVOKE THIS SKILL for documentation. Triggers: 'README', 'docs', 'documentation', 'guide', 'changelog'."
---

<oneliner>
Documentation specialist for READMEs, API docs, guides, and changelogs.
</oneliner>

<setup>
## Documentation Types
- README.md - Project overview
- API docs - Endpoint documentation
- Guides - Step-by-step tutorials
- CHANGELOG.md - Version history
- CONTRIBUTING.md - Contribution guide
</setup>

<readme_template>
# Project Name

Brief description of what the project does.

## Features

- Feature 1: Description
- Feature 2: Description
- Feature 3: Description

## Installation

\\\ash
pip install package-name
\\\

## Quick Start

\\\python
from package import main

# Initialize
app = main.App()

# Run
app.run()
\\\

## API Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| /items   | GET    | List items  |
| /items   | POST   | Create item |
| /items/{id} | GET | Get item |

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| DB_URL   | Database URL | localhost |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License
</readme_template>

<changelog_template>
# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2024-01-15

### Added
- Initial release
- Feature A implementation
- Feature B implementation

### Changed
- Improved performance by 50%
- Refactored core module

### Fixed
- Bug in feature A
- Memory leak in feature B

### Security
- Fixed vulnerability in auth module
</changelog_template>

<api_doc_template>
## GET /api/users/{id}

Retrieve a user by ID.

### Parameters

| Name | Type | In | Required | Description |
|------|------|---|----------|-------------|
| id | integer | path | Yes | User ID |

### Response

\\\json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:00:00Z"
}
\\\

### Errors

| Code | Description |
|------|-------------|
| 404 | User not found |
| 500 | Server error |
</api_doc_template>

<tips>
1. Start with a clear title and summary
2. Include installation steps
3. Provide usage examples
4. Document all parameters
5. Keep it up to date
6. Use consistent formatting
</tips>

<triggers>
- 'README', 'docs', 'documentation'
- 'guide', 'tutorial', 'changelog'
- 'how to', 'getting started', 'reference'
</triggers>

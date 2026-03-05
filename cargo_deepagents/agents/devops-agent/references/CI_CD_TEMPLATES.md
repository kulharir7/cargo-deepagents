# CI/CD Templates

## GitHub Actions - Python

name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest --cov
  
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: docker build -t app:latest .

## GitLab CI

stages:
  - test
  - build
  - deploy

test:
  stage: test
  script:
    - pytest

build:
  stage: build
  script:
    - docker build -t app .

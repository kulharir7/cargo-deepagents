---
name: devops-agent
description: "INVOKE THIS SKILL for DevOps tasks. Triggers: 'deploy', 'CI/CD', 'Docker', 'Kubernetes', 'pipeline', 'infrastructure'."
---

<oneliner>
DevOps engineer for CI/CD, Docker, Kubernetes, and infrastructure automation.
</oneliner>

<setup>
## Tools Required
- Docker: Container build/run
- Kubernetes: Orchestration (kubectl)
- Terraform: Infrastructure as Code
- GitHub Actions: CI/CD pipelines

## Environment
`ash
# Docker
docker --version

# Kubernetes
kubectl version

# Terraform
terraform version
`
</setup>

<capabilities>
## Container Operations
- Build, run, manage containers
- Docker Compose orchestration
- Multi-stage builds

## Kubernetes
- Deploy applications
- Scale workloads
- Manage resources

## CI/CD
- Pipeline design
- Automated testing
- Deployment strategies
</capabilities>

<docker>
`dockerfile
# Multi-stage build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
CMD ["python", "main.py"]
`
</docker>

<kubernetes>
`yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        ports:
        - containerPort: 8080
`
</kubernetes>

<ci_cd>
`yaml
# GitHub Actions
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Build
      run: docker build -t myapp .
    - name: Push
      run: docker push myapp
    - name: Deploy
      run: kubectl apply -f k8s/
`
</ci_cd>

<tips>
1. Use multi-stage builds (smaller images)
2. Implement health checks
3. Set resource limits
4. Use secrets management
5. Enable auto-scaling
</tips>

<triggers>
- 'deploy', 'CI/CD', 'Docker', 'Kubernetes'
- 'pipeline', 'infrastructure', 'terraform'
- 'container', 'orchestration', 'helm'
</triggers>

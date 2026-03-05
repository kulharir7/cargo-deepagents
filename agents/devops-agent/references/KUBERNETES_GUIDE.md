# Kubernetes Guide

## Basic Commands

# Deploy
kubectl apply -f deployment.yaml

# Scale
kubectl scale deployment/app --replicas=3

# Logs
kubectl logs -f deployment/app

# Port forward
kubectl port-forward svc/app 8080:80

## Deployment Template

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
        - containerPort: 8000

## Service Template

apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer

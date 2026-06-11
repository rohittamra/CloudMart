# CloudMart

A cloud-native e-commerce platform built to demonstrate modern DevOps, Platform Engineering, and Site Reliability Engineering practices.

## Overview

CloudMart is a microservices-based marketplace application designed to showcase an end-to-end DevOps workflow using containerization, orchestration, CI/CD, observability, and event-driven architecture.

The project simulates a production-grade environment where multiple services communicate through APIs and Kafka events while being monitored through Prometheus and Grafana.

---

## Architecture

Developer
↓
GitHub
↓
Jenkins CI/CD
↓
Docker Build
↓
Kubernetes Deployment
↓
CloudMart Services

Services:

* Frontend Service
* User Service
* Product Service
* Order Service
* Notification Service

Infrastructure:

* Kubernetes
* Docker
* Helm
* Kafka
* PostgreSQL
* Prometheus
* Grafana
* Trivy


## Architecture Diagram

                 +----------------+
                 |   Developer    |
                 +-------+--------+
                         |
                         v
                 +----------------+
                 |     GitHub     |
                 +-------+--------+
                         |
                         v
                 +----------------+
                 |    Jenkins     |
                 +-------+--------+
                         |
                         v
                 +----------------+
                 | Docker Images  |
                 +-------+--------+
                         |
                         v
             +------------------------+
             | Kubernetes Cluster     |
             +------------------------+
                  |     |      |
                  v     v      v
              User  Product  Order
             Service Service Service
                  \     |     /
                   \    |    /
                    v   v   v
                    Kafka Bus
                         |
                         v
                Notification Service

      Prometheus <----- Metrics -----
           |
           v
        Grafana


## Kafka

                        Frontend
                        │
                        ▼
                        Order Service
                        │
                        ▼
                        Kafka Topic
                        (order-created)
                        │
                        ▼
                        Notification Service
---

## Features

### User Management

* User registration
* User authentication
* User profile management

### Product Management

* Browse products
* Search products
* Product inventory tracking

### Order Management

* Create orders
* Track orders
* Order history

### Notifications

* Event-driven notifications
* Kafka message consumption

### Monitoring

* Application metrics
* Kubernetes metrics
* Kafka metrics
* Infrastructure metrics

---

## Tech Stack

### Frontend

* React
* Nginx

### Backend

* FastAPI
* Python

### Database

* PostgreSQL

### Messaging

* Apache Kafka

### Containerization

* Docker

### Orchestration

* Kubernetes
* Helm

### CI/CD

* Jenkins

### Security

* Trivy

### Monitoring

* Prometheus
* Grafana

---

## Microservices

### Frontend Service

Responsible for user interface and API interactions.

### User Service

Responsible for user operations.

Endpoints:

GET /users

POST /users

GET /health

GET /metrics

### Product Service

Responsible for product catalog operations.

Endpoints:

GET /products

POST /products

GET /health

GET /metrics

### Order Service

Responsible for order creation and processing.

Endpoints:

GET /orders

POST /orders

GET /health

GET /metrics

### Notification Service

Consumes Kafka events and processes notifications.

---

## Kafka Event Flow

Order Created
↓
Kafka Topic
↓
Notification Service
↓
Processing Complete

Topics:

* order-created
* order-updated
* notification-created

---

## Monitoring

Prometheus collects metrics from:

* User Service
* Product Service
* Order Service
* Kubernetes Cluster
* Kafka Exporter
* PostgreSQL Exporter

Grafana dashboards include:

* Application Metrics
* Kubernetes Metrics
* Kafka Metrics
* Infrastructure Metrics

---

## CI/CD Pipeline

1. Developer pushes code to GitHub
2. Jenkins pipeline starts
3. Unit tests execute
4. Docker images build
5. Trivy security scan runs
6. Images are published
7. Kubernetes deployment updates
8. Health checks verify deployment

---

## Kubernetes Components

* Deployments
* Services
* ConfigMaps
* Secrets
* Ingress
* Persistent Volumes
* Horizontal Pod Autoscaler

---

## Repository Structure

cloudmart/

frontend/

services/

user-service/

product-service/

order-service/

notification-service/

k8s/

helm/

monitoring/

prometheus/

grafana/

jenkins/

docs/

---

## Local Development

Prerequisites:

* Docker
* Kubernetes (Minikube or Kind)
* Helm
* Kubectl
* Jenkins

Clone repository:

git clone <repository-url>

Start services:

docker compose up -d

Deploy to Kubernetes:

helm install cloudmart ./helm/cloudmart

---

## Future Enhancements

* ArgoCD GitOps deployment
* OpenTelemetry tracing
* Loki centralized logging
* Jaeger distributed tracing
* Multi-cluster Kubernetes deployment
* Service Mesh with Istio

---

## Project Goals

CloudMart is intended as a portfolio project demonstrating:

* DevOps Engineering
* Kubernetes Administration
* CI/CD Automation
* Infrastructure as Code
* Observability
* Event-Driven Architecture
* Site Reliability Engineering
* Cloud-Native Application Design

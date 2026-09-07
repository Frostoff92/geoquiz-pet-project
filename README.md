# GeoQuiz

GeoQuiz is a backend pet-project for learning backend development, DevOps practices, API design, Docker workflows, Kubernetes, observability, and PostgreSQL integration.

The project provides a REST API for geography and vexillology quizzes using FastAPI, PostgreSQL, SQLAlchemy, Docker, Kubernetes, and automated testing.

---

# Features

- Random quiz generation
- Quiz modes: `flag`, `capital`, `continent`
- Unified quiz response contract using `question_type` and `question_value`
- Difficulty filtering
- Answer validation
- Quiz option integrity checks
- PostgreSQL database integration
- SQLAlchemy ORM
- Alembic schema and data migrations
- REST API architecture
- FastAPI automatic Swagger/OpenAPI docs
- Docker support
- Docker Compose support
- Kubernetes deployment with Minikube
- Kubernetes readiness and liveness probes
- GitHub Actions CI pipeline
- Automated API testing with pytest
- Isolated PostgreSQL test database
- Service layer architecture
- Environment-based configuration
- Prometheus metrics
- Grafana dashboard and automatic provisioning

---

# Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Pytest
- HTTPX
- psycopg2
- python-dotenv
- Docker
- Docker Compose
- Kubernetes
- Minikube
- Prometheus
- Grafana
- GitHub Actions

---

# Architecture

```text
countries.json
      ↓
seed.py
      ↓
PostgreSQL
      ↓
SQLAlchemy ORM
      ↓
Service Layer
      ↓
FastAPI Routers
      ↓
REST API
```

Observability:

```text
GeoQuiz API
     ↓
 /metrics
     ↓
Prometheus
     ↓
 Grafana
```

Kubernetes deployment:

```text
Docker Image
     ↓
Minikube
     ↓
Kubernetes Deployment
     ↓
GeoQuiz API
     ↓
PostgreSQL + PVC
```

---

# Project Structure

```text
geoquiz/
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 30c13b3ec001_add_capital_field_to_countries.py
│       ├── 44c2a2cfe613_create_countries_table.py
│       ├── a66e5e35335e_backfill_country_capitals.py
│       └── c25af52a672b_add_continent_field.py
├── alembic.ini
├── app
│   ├── config.py
│   ├── data
│   │   └── countries.json
│   ├── database.py
│   ├── enums.py
│   ├── init_db.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routers
│   │   ├── countries.py
│   │   ├── health.py
│   │   ├── __init__.py
│   │   └── quiz.py
│   ├── schemas.py
│   ├── seed.py
│   └── services
│       ├── __init__.py
│       └── quiz_service.py
├── docker-compose.yml
├── Dockerfile
├── grafana
│   ├── dashboards
│   │   └── geoquiz-dashboard.json
│   └── provisioning
│       ├── dashboards
│       │   └── dashboard.yml
│       └── datasources
│           └── datasource.yml
├── k8s
│   ├── api-configmap.yaml
│   ├── api-deployment.yaml
│   ├── api-secret.yaml
│   ├── api-service.yaml
│   ├── migration-job.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-pvc.yaml
│   ├── postgres-service.yaml
│   └── seed-job.yaml
├── prometheus.yml
├── README.md
├── requirements.txt
└── tests
    ├── conftest.py
    └── test_api.py
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/namedb
DATABASE_URL_TEST=postgresql://username:password@localhost:5432/test_db
```

---

# Run with Docker Compose

Build and start the project:

```bash
docker compose up --build
```

Check containers:

```bash
docker compose ps
```

The API will be available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

Prometheus:

```text
http://localhost:9090
```

Grafana:

```text
http://localhost:3000
```

---

# Run in Kubernetes (Minikube)

Start Minikube and verify the context:

```bash
minikube status
kubectl config current-context
```

Use the Docker daemon inside Minikube:

```bash
eval $(minikube docker-env)
```

Build the current application image:

```bash
docker build -t geoquiz-api:v7 .
```

The Kubernetes manifests at the current project checkpoint use:

```text
geoquiz-api:v7
```

Deploy infrastructure:

```bash
kubectl apply -f k8s/
```

Check resources:

```bash
kubectl get pods
kubectl get deployments
kubectl get svc
kubectl get jobs
```

The backend includes:

- FastAPI Deployment
- PostgreSQL Deployment
- PersistentVolumeClaim (PVC)
- ConfigMap + Secret
- readiness/liveness probes
- Alembic migration Job
- seed Job
- automatic Job cleanup via TTL

---

# Kubernetes Deployment / Upgrade

Before building a new image, synchronize the repository:

```bash
git fetch origin
git pull --ff-only
```

Build a new image inside Minikube:

```bash
eval $(minikube docker-env)
docker build -t geoquiz-api:<version> .
```

Update the image version in:

```text
k8s/api-deployment.yaml
k8s/migration-job.yaml
k8s/seed-job.yaml
```

Apply the updated Deployment:

```bash
kubectl apply -f k8s/api-deployment.yaml
kubectl rollout status deployment/geoquiz-api
```

Check the deployed image:

```bash
kubectl get deployment geoquiz-api \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Check application Pods:

```bash
kubectl get pods -l app=geoquiz-api
```

---

# Database Migrations in Kubernetes

Check which Alembic revision is available in the application image:

```bash
kubectl exec deploy/geoquiz-api -- alembic heads
```

Check which revision is currently applied to PostgreSQL:

```bash
kubectl exec deploy/geoquiz-api -- alembic current
```

Apply pending migrations:

```bash
kubectl exec deploy/geoquiz-api -- alembic upgrade head
```

Verify again:

```bash
kubectl exec deploy/geoquiz-api -- alembic current
```

The value returned by `alembic current` should match the current Alembic head.

> A migration file being present in the Docker image does not mean that the migration has already been applied to the database.

The project also contains a Kubernetes migration Job:

```text
k8s/migration-job.yaml
```

---

# Kubernetes Functional Smoke Test

Forward the Kubernetes Service to the local machine:

```bash
kubectl port-forward service/geoquiz-api-service 8001:8000
```

Then test all quiz modes:

```bash
curl "http://localhost:8001/quiz/random?mode=flag"
curl "http://localhost:8001/quiz/random?mode=capital"
curl "http://localhost:8001/quiz/random?mode=continent"
```

A successful Kubernetes rollout and healthy readiness/liveness probes do not replace a functional smoke test.

The probes verify service health, while a functional request can reveal application-level problems such as database schema or data mismatches.

---

# Kubernetes Rollback

Rollback to the previous Deployment revision:

```bash
kubectl rollout undo deployment/geoquiz-api
kubectl rollout status deployment/geoquiz-api
```

Check the resulting image:

```bash
kubectl get deployment geoquiz-api \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Database migrations must be considered separately when performing an application rollback.

---

# Seed Database

Populate PostgreSQL with countries data.

Local environment:

```bash
py -m app.seed
```

Seed is idempotent and safe to rerun.

Inside Docker Compose, use the appropriate API service name from:

```bash
docker compose config --services
```

Then run:

```bash
docker compose exec <api-service> python -m app.seed
```

Kubernetes also includes a seed Job:

```text
k8s/seed-job.yaml
```

---

# Running Tests

Run tests locally:

```bash
python -m pytest
```

The test suite uses:

- isolated PostgreSQL test database
- FastAPI dependency overrides
- pytest fixtures
- integration-style API testing

Current test coverage includes:

- Health check endpoints
- Countries API
- Quiz generation
- `flag` quiz contract
- `capital` quiz contract
- `continent` quiz contract
- Default quiz mode behavior
- Difficulty validation
- Answer validation
- End-to-end quiz answer flow
- Quiz option integrity
- Insufficient-country edge case
- Error handling

---

# CI/CD

The project includes a GitHub Actions CI pipeline with:

- automated pytest execution
- PostgreSQL service container
- Docker build validation
- smoke testing

---

# Observability

The project includes a basic observability stack.

FastAPI metrics endpoint:

```text
http://localhost:8000/metrics
```

Prometheus UI:

```text
http://localhost:9090
```

Grafana UI:

```text
http://localhost:3000
```

Prometheus scrapes metrics from the GeoQuiz API.

The Grafana dashboard includes service-level information such as:

- API status
- service uptime
- request rate
- total requests
- HTTP 4xx errors
- HTTP 5xx errors
- request latency

Grafana provisioning:

```text
grafana/
├── dashboards/
│   └── geoquiz-dashboard.json
└── provisioning/
    ├── dashboards/
    │   └── dashboard.yml
    └── datasources/
        └── datasource.yml
```

The dashboard and Prometheus datasource are provisioned automatically when the Grafana container starts.

---

# API Endpoints

## Health Checks

```http
GET /health/live
GET /health/ready
```

---

## Get All Countries

```http
GET /countries
```

---

## Get Country By ID

```http
GET /countries/{id}
```

---

## Generate Random Quiz

```http
GET /quiz/random
```

Supported quiz modes:

```text
flag
capital
continent
```

Examples:

```http
GET /quiz/random?mode=flag
GET /quiz/random?mode=capital
GET /quiz/random?mode=continent
```

Difficulty can also be supplied as a query parameter:

```http
GET /quiz/random?difficulty=hard
```

The quiz response uses a unified contract:

```json
{
  "question_country_id": 1,
  "question": "Which country has this flag?",
  "question_type": "flag",
  "question_value": "🇮🇩",
  "options": [
    {
      "id": 1,
      "name": "Indonesia"
    }
  ]
}
```

`question_type` identifies the quiz mode.

`question_value` contains the value needed to render the question, such as a flag, capital, or continent.

---

## Submit Answer

```http
POST /quiz/answer
```

Example request body:

```json
{
  "question_country_id": 1,
  "selected_country_id": 2
}
```

Answer validation is independent of the quiz mode.

The backend compares the selected country with the country associated with the generated question.

---

# Deployment Verification Checklist

Before considering a deployment complete:

```text
[ ] Tests pass
[ ] Current Git branch is synchronized
[ ] Docker image is built from current code
[ ] Kubernetes Deployment uses the expected image
[ ] Pod is Running and Ready
[ ] Kubernetes rollout completed successfully
[ ] Alembic current matches Alembic head
[ ] Functional smoke tests pass
[ ] Prometheus target is UP
[ ] Grafana dashboard receives metrics
```

---

# Future Improvements

- Async SQLAlchemy support
- Redis caching
- JWT authentication
- Helm charts
- Production-ready CI/CD deployment pipeline
- Frontend integration
- Difficulty balancing logic
- Automated Kubernetes migration execution as part of the deployment workflow
- SLI/SLO-based alerting

---

# Learning Goals

This project is used for practicing:

- backend architecture
- REST API development
- PostgreSQL integration
- schema and data migrations
- Docker workflows
- Kubernetes deployments
- rollout and rollback workflows
- DevOps practices
- CI/CD pipelines
- automated testing
- observability
- functional smoke testing
- service-oriented design
- environment configuration
- infrastructure troubleshooting
- infrastructure thinking
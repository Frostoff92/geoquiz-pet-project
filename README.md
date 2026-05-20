# GeoQuiz

GeoQuiz is a backend pet-project for learning backend development, DevOps practices, API design, Docker workflows, and PostgreSQL integration.

The project provides a REST API for geography and vexillology quizzes using FastAPI, PostgreSQL, SQLAlchemy, Docker, and automated testing.

---

# Features

- Random quiz generation
- Difficulty filtering
- Answer validation
- PostgreSQL database integration
- SQLAlchemy ORM
- REST API architecture
- FastAPI automatic Swagger/OpenAPI docs
- Docker support
- Docker Compose support
- GitHub Actions CI pipeline
- Automated API testing with pytest
- Isolated PostgreSQL test database
- Service layer architecture
- Environment-based configuration

---

# Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest
- HTTPX
- psycopg2
- python-dotenv
- Docker
- Docker Compose
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

---

# Project Structure

```text
geoquiz/
├── app/
│   ├── data/
│   │   └── countries.json
│   │
│   ├── routers/
│   │   ├── countries.py
│   │   └── quiz.py
│   │
│   ├── services/
│   │   └── quiz_service.py
│   │
│   ├── database.py
│   ├── enums.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── seed.py
│
├── tests/
│   ├── conftest.py
│   └── test_api.py
│
├── .github/workflows/
│   └── ci.yml
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/geoquizdb

DATABASE_URL_TEST=postgresql://username:password@localhost:5432/geoquiz_test
```

---

# Run with Docker Compose

Build and start the project:

```bash
docker compose up --build
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

---

# Seed Database

Populate PostgreSQL with countries data.

Local environment:

```bash
py -m app.seed
```

Inside Docker container:

```bash
docker compose exec api python -m app.seed
```

---

# Running Tests

Run tests locally:

```bash
py -m pytest
```

The test suite uses:

- isolated PostgreSQL test database
- FastAPI dependency overrides
- pytest fixtures
- integration-style API testing

Current test coverage includes:

- Health check endpoint
- Countries API
- Quiz generation
- Difficulty validation
- Answer validation
- Error handling

---

# CI/CD

The project includes GitHub Actions CI pipeline with:

- automated pytest execution
- PostgreSQL service container
- Docker build validation
- smoke testing

---

# API Endpoints

## Health Check

```http
GET /health
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

Optional query parameter:

```text
difficulty=hard
```

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

---

# Future Improvements

- Alembic migrations
- Async SQLAlchemy support
- Redis caching
- JWT authentication
- Kubernetes deployment
- Helm charts
- Prometheus/Grafana monitoring
- Production-ready CI/CD pipeline
- Frontend integration
- Difficulty balancing logic

---

# Learning Goals

This project is used for practicing:

- backend architecture
- REST API development
- PostgreSQL integration
- Docker workflows
- DevOps practices
- CI/CD pipelines
- automated testing
- service-oriented design
- environment configuration
- infrastructure thinking
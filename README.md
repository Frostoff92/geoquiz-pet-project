# Geoquiz

# GeoQuiz is a pet-project for learning backend-development, Devops-practices and API design.

The project provides a quiz APi for geography and vexillology training using FastAPI and Docker.

---

## Features

- Random quiz generation
- Difficulty filtering
- Answer validation
- Swagger/OpenAPI documentation
- Docker support
- Docker Compose support
- GitHub Actions CI pipeline
- FastAPI + Pydantic schemas
- Automated API tests
- CI-integrrated testing

---

## Tech Stack

- Python 3.13
- FastAPI
- Pytest
- HTTPX
- Pydantic
- Docker
- Docker Compose
- GitHub Actions
  
---

## Project Structure

```text
geoquiz/
├── app/
│   ├── data/
│   │   └── countries.json
│   │
│   ├── enums.py
│   ├── data.py
│   ├── main.py
│   └── schemas.py
│
├── tests/
│   └── test_api.py
│
├── .github/workflows/
│   └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## Testing

Run tests locally:

```bash
py -m pytest
```

Current test coverage includes:

- Health check endpoint
- Countries API
- Quiz generation
- Difficulty validation
- Answer validation
- Error handling
```
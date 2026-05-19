# Geoquiz

# GeoQuiz is a pet-project for learning backend-development, Devops-practices and API design.

The project provides a quiz APi for geography and vexillology training using FastAPI and Docker.

---

## Tech Stack

- Python 3.13
- FastAPI
- Pydantic
- Docker
- Docker Compose
- GitHub Actions
  
---

## Project Structure

```text
geoquiz/
├── app/
│   ├── data.py
│   ├── enums.py
│   ├── main.py
│   └── schemas.py
│
├── .github/workflows/
│   └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
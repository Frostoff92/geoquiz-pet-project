from fastapi import FastAPI

from app.routers.quiz import router as quiz_router


app = FastAPI(
    title="GeoQuiz API",
    description="Flag quiz API for geography and vexillology training",
    version="0.9.0"
)


@app.get("/")
def root():
    return {"message": "GeoQuiz API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(quiz_router)
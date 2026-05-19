from fastapi import FastAPI, HTTPException
from app.data import COUNTRIES
from app.schemas import Country, QuizQuestion, AnswerRequest, AnswerResult
import random

app = FastAPI(
    title="GeoQuiz API",
    description="Flag quiz API for geography and vexillology training",
    version="0.2.0"
)

@app.get("/")
def root():
    return {"message": "GeoQuiz API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/countries", response_model=list[Country])
def get_countries():
    return COUNTRIES

@app.get("/countries/{country_id}", response_model=Country)
def get_country(country_id: int):
    for country in COUNTRIES:
        if country["id"] == country_id:
            return country
    
    raise HTTPException(status_code=404, detail="Country not found")

@app.get("/quiz/random", response_model=QuizQuestion)
def get_random_quiz(difficulty: str | None = None):

    filtered_countries = COUNTRIES

    if difficulty:
        filtered_countries = [
            country
            for country in COUNTRIES
            if country["difficulty"] == difficulty
        ]

    if not filtered_countries:
        raise HTTPException(
            status_code=404,
            detail="No countries found for this difficulty"
        )

    correct_country = random.choice(filtered_countries)

    options_pool = COUNTRIES.copy()

    options = random.sample(
        options_pool,
        k=min(3, len(options_pool))
    )

    if correct_country not in options:
        options[0] = correct_country

    random.shuffle(options)

    return {
        "question_country_id": correct_country["id"],
        "question": "Which country has this flag?",
        "flag": correct_country["flag"],
        "options": [
            {
                "id": country["id"],
                "name": country["name"]
            }
            for country in options
        ]

    }

@app.post("/quiz/answer", response_model=AnswerResult)
def check_answer(answer: AnswerRequest):
    correct_country_id = answer.question_country_id
    selected_country_id = answer.selected_country_id

    country_exists = any(
        country["id"] == correct_country_id
        for country in COUNTRIES
    )

    if not country_exists:
        raise HTTPException(status_code=404, detail="Question country not found")
    
    is_correct = correct_country_id == selected_country_id

    return {
        "correct": is_correct,
        "correct_country_id": correct_country_id,
        "selected_country_id": selected_country_id,
        "message": "Correct answer!" if is_correct else "Wrong answer!"
    }


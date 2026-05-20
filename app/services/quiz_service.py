import random

from fastapi import HTTPException

from app.enums import DifficultyLevel
from app.schemas import AnswerRequest

from sqlalchemy.orm import Session
from app.models import CountryModel


def get_all_countries(db: Session):
    return db.query(CountryModel).all()


def get_country_by_id(db: Session, country_id: int):
    country = (
        db.query(CountryModel)
        .filter(CountryModel.id == country_id)
        .first()
)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    
    return country

def generate_random_quiz(db: Session, difficulty: DifficultyLevel | None = None):
    query = db.query(CountryModel)

    if difficulty:
        query = query.filter(CountryModel.difficulty == difficulty.value)

    filtered_countries = query.all()

    if not filtered_countries:
        raise HTTPException(
            status_code=404,
            detail="No countries found for this difficulty"
        )

    correct_country = random.choice(filtered_countries)

    options_pool = db.query(CountryModel).all()

    options = random.sample(
        options_pool,
        k=min(3, len(options_pool))
    )

    if correct_country not in options:
        options[0] = correct_country

    random.shuffle(options)

    return {
        "question_country_id": correct_country.id,
        "question": "Which country has this flag?",
        "flag": correct_country.flag,
        "options": [
            {
                "id": country.id,
                "name": country.name
            }
            for country in options
        ]
    }


def check_answer(db: Session, answer: AnswerRequest):
    correct_country_id = answer.question_country_id
    selected_country_id = answer.selected_country_id

    country = (
        db.query(CountryModel)
        .filter(CountryModel.id == correct_country_id)
        .first()
    )

    if not country:
        raise HTTPException(status_code=404, detail="Question country not found")

    is_correct = correct_country_id == selected_country_id

    return {
        "correct": is_correct,
        "correct_country_id": correct_country_id,
        "selected_country_id": selected_country_id,
        "message": "Correct answer!" if is_correct else "Wrong answer!"
    }
from fastapi import APIRouter

from app.enums import DifficultyLevel
from app.schemas import Country, QuizQuestion, AnswerRequest, AnswerResult
from app.services.quiz_service import (
    get_all_countries,
    get_country_by_id,
    generate_random_quiz,
    check_answer,
)


router = APIRouter()


@router.get("/countries", response_model=list[Country])
def countries():
    return get_all_countries()


@router.get("/countries/{country_id}", response_model=Country)
def country_by_id(country_id: int):
    return get_country_by_id(country_id)


@router.get("/quiz/random", response_model=QuizQuestion)
def random_quiz(difficulty: DifficultyLevel | None = None):
    return generate_random_quiz(difficulty)


@router.post("/quiz/answer", response_model=AnswerResult)
def answer_quiz(answer: AnswerRequest):
    return check_answer(answer)
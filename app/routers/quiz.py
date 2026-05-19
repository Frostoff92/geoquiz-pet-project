from fastapi import APIRouter

from app.enums import DifficultyLevel
from app.schemas import Country, QuizQuestion, AnswerRequest, AnswerResult
from app.services.quiz_service import (
    get_all_countries,
    get_country_by_id,
    generate_random_quiz,
    check_answer,
)


router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)

@router.get("/random", response_model=QuizQuestion)
def random_quiz(difficulty: DifficultyLevel | None = None):
    return generate_random_quiz(difficulty)


@router.post("/answer", response_model=AnswerResult)
def answer_quiz(answer: AnswerRequest):
    return check_answer(answer)
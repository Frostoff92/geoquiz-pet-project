from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.enums import DifficultyLevel, QuizMode
from app.schemas import QuizQuestion, AnswerRequest, AnswerResult
from app.services.quiz_service import (
    generate_random_quiz,
    check_answer,
)


router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)


@router.get("/random", response_model=QuizQuestion)
def random_quiz(
    difficulty: DifficultyLevel | None = None,
    mode: QuizMode = QuizMode.flag,
    db: Session = Depends(get_db),
):
    return generate_random_quiz(
        db=db,
        difficulty=difficulty,
        mode=mode
    )


@router.post("/answer", response_model=AnswerResult)
def answer_quiz(
    answer: AnswerRequest,
    db: Session = Depends(get_db),
):
    return check_answer(db, answer)
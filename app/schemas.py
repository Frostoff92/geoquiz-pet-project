from pydantic import BaseModel

class Country(BaseModel):
    id: int
    name: str
    flag: str
    difficulty: str
    similar_to: list[str]

class QuizOption(BaseModel):
    id: int
    name: str

class QuizQuestion(BaseModel):
    question_country_id: int
    question: str
    flag: str
    options: list[QuizOption]

class AnswerRequest(BaseModel):
    question_country_id: int
    selected_country_id: int

class AnswerResult(BaseModel):
    correct: bool
    correct_country_id: int
    selected_country_id: int
    message: str
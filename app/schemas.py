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
    question: str
    flag: str
    options: list[QuizOption]
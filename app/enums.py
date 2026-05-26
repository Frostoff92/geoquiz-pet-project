from enum import Enum

class DifficultyLevel(str, Enum):
    hard = "hard"
    medium = "medium"

class QuizMode(str, Enum):
    flag = "flag"
    capital = "capital"
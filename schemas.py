from pydantic import BaseModel
from typing import List

class Answer(BaseModel):
    question_id: int
    answer: str

class Submission(BaseModel):
    answers: List[Answer]

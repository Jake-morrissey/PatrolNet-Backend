from fastapi import FastAPI
from schemas import Submission
from scoring import calculate_score, convert_to_grade  # keep scoring.py separate

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.post("/submit")
def submit_form(data: Submission):
    score = calculate_score(data.answers)
    grade = convert_to_grade(score)
    return {"score": score, "grade": grade}

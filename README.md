# PatrolNet Backend

FastAPI backend for calculating security risk scores from user-submitted answers.

## Features
- FastAPI REST API
- `/submit` scoring endpoint
- Clean scoring logic in separate module
- Pydantic v2 schemas
- CORS enabled for frontend
- Works on Render

## Tech Stack
- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy (optional)
- CORS Middleware

## Project Structure
backend/
│── main.py
│── schemas.py
│── scoring.py
│── requirements.txt
│── venv/

## Installation

### 1. Clone repo
git clone https://github.com/Jake-morrissey/PatrolNet-Backend.git
cd PatrolNet-Backend

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install requirements
pip install -r requirements.txt

## Run the server
uvicorn main:app --reload

Backend runs at:
http://127.0.0.1:8000

## Endpoint

### POST /submit
Submit questionnaire answers and get a score and grade.

Request example:
{
  "answers": [
    { "question_id": 1, "answer": "yes" },
    { "question_id": 2, "answer": "no" },
    { "question_id": 3, "answer": "weekly" }
  ]
}

Response example:
{
  "score": 45,
  "grade": "C"
}

## Render Deployment Notes
- Ensure `requirements.txt` exists in root
- Start command:
uvicorn main:app --host 0.0.0.0 --port $PORT

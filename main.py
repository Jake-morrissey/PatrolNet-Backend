from fastapi import FastAPI
from schemas import Submission
from scoring import calculate_score, convert_to_grade  # keep scoring.py separate
from supabase_client import supabase


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.post("/submit")
def submit_form(data: Submission):
    score = calculate_score(data.answers)
    grade = convert_to_grade(score)
    return {"score": score, "grade": grade}

from reportlab.pdfgen import canvas
from io import BytesIO

@app.post("/submit")
def submit_form(data: Submission):
    score = calculate_score(data.answers)
    grade = convert_to_grade(score)

    # --- Generate PDF ---
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer)
    c.drawString(100, 750, f"Score: {score}")
    c.drawString(100, 730, f"Grade: {grade}")
    c.save()
    pdf_buffer.seek(0)
    file_data = pdf_buffer.read()

    # --- Upload to Supabase ---
    filename = f"user_{data.user_id}_report.pdf"  # unique filename per submission
    supabase.storage.from_("reports").upload(filename, file_data)

    # --- Get signed URL for user to download ---
    url = supabase.storage.from_("reports").create_signed_url(filename, 3600)  # valid for 1 hour

    return {"score": score, "grade": grade, "report_url": url}

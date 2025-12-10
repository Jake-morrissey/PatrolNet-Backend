from reportlab.pdfgen import canvas

def generate_pdf(score, grade):
    filename = "report.pdf"
    c = canvas.Canvas(filename)
    c.drawString(100, 750, f"Security Score: {score}")
    c.drawString(100, 730, f"Grade: {grade}")
    c.save()
    return filename

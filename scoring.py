def calculate_score(answers):
    score = 0
    for a in answers:
        if a.question_id == 1 and a.answer.lower() == "yes":
            score += 20
        if a.question_id == 2 and a.answer.lower() == "yes":
            score += 10
        if a.question_id == 3 and a.answer.lower() == "weekly":
            score += 15
    return score

def convert_to_grade(score):
    if score >= 80: return "A"
    if score >= 60: return "B"
    if score >= 40: return "C"
    return "D"

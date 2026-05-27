import re


# =========================
# ATS SCORE CALCULATION
# =========================
def calculate_ats_score(skills, resume_text):

    score = 0

    # =========================
    # SKILL SCORE
    # =========================
    skill_score = min(len(skills) * 5, 40)

    score += skill_score

    # =========================
    # EXPERIENCE DETECTION
    # =========================
    experience_keywords = [
        "experience",
        "internship",
        "worked",
        "developer",
        "engineer",
        "project"
    ]

    exp_matches = 0

    for word in experience_keywords:

        if word.lower() in resume_text.lower():
            exp_matches += 1

    exp_score = min(exp_matches * 5, 25)

    score += exp_score

    # =========================
    # EDUCATION SCORE
    # =========================
    education_keywords = [
        "b.tech",
        "bachelor",
        "master",
        "university",
        "college",
        "cgpa"
    ]

    edu_matches = 0

    for word in education_keywords:

        if word.lower() in resume_text.lower():
            edu_matches += 1

    edu_score = min(edu_matches * 4, 20)

    score += edu_score

    # =========================
    # FORMATTING SCORE
    # =========================
    if len(resume_text) > 1000:
        score += 10

    # =========================
    # CONTACT INFO CHECK
    # =========================
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    phone_pattern = r"\+?\d[\d -]{8,12}\d"

    if re.search(email_pattern, resume_text):
        score += 3

    if re.search(phone_pattern, resume_text):
        score += 2

    return min(score, 100)
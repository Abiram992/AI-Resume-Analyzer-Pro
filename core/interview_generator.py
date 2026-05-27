from services.gemini_service import get_gemini_response


# =========================
# INTERVIEW QUESTIONS
# =========================
def generate_interview_questions(
    resume_text,
    job_description
):

    prompt = f"""
    Generate professional interview questions.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Generate:
    - Technical Questions
    - HR Questions
    - Project Questions
    - Scenario Based Questions
    """

    response = get_gemini_response(prompt)

    return response
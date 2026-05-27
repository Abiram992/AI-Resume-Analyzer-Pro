from services.gemini_service import get_gemini_response


# =========================
# AI FEEDBACK GENERATOR
# =========================
def generate_feedback(resume_text):

    prompt = f"""
    Analyze this resume professionally.

    Give:
    1. Strengths
    2. Weaknesses
    3. ATS Improvements
    4. Missing Skills
    5. Resume Suggestions

    Resume:
    {resume_text}
    """

    response = get_gemini_response(prompt)

    return response
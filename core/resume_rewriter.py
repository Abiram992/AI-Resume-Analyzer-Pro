import google.generativeai as genai
import os

from dotenv import load_dotenv

# =========================
# LOAD ENV
# =========================
load_dotenv()

# =========================
# CONFIGURE GEMINI
# =========================
genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

# =========================
# MODEL
# =========================
model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

# =========================
# RESUME REWRITER
# =========================
def rewrite_resume_section(
    content
):

    prompt = f"""

    You are an expert ATS resume writer.

    Rewrite the following resume content
    professionally with:

    - Better grammar
    - Strong action verbs
    - ATS optimization
    - Quantified achievements
    - Professional tone

    Resume Content:

    {content}

    Return ONLY the improved version.

    """

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"
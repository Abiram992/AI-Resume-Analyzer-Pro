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
# CHATBOT FUNCTION
# =========================
def ask_resume_chatbot(
    resume_text,
    job_description,
    question
):

    prompt = f"""

    You are an expert AI Resume Coach.

    Analyze the following resume and
    answer the user's question professionally.

    =========================
    RESUME
    =========================

    {resume_text}

    =========================
    JOB DESCRIPTION
    =========================

    {job_description}

    =========================
    USER QUESTION
    =========================

    {question}

    Give:
    - professional guidance
   
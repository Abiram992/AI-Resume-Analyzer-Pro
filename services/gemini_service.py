import os
import google.generativeai as genai

from dotenv import load_dotenv


# =========================
# LOAD ENV VARIABLES
# =========================
load_dotenv()

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

# =========================
# CONFIGURE GEMINI
# =========================
genai.configure(
    api_key=API_KEY
)

# =========================
# LOAD MODEL
# =========================
model = genai.GenerativeModel(
    "gemini-1.5-pro"
)

# =========================
# GEMINI RESPONSE
# =========================
def get_gemini_response(prompt):

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"""
⚠️ Gemini API Error

Possible reasons:
- API quota exceeded
- Invalid API key
- Billing not enabled
- Rate limit reached

Error Details:
{str(e)}
"""
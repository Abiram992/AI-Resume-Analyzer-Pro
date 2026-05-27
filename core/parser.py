import pdfplumber
import fitz
from docx import Document


# =========================
# PDF TEXT EXTRACTION
# =========================
def extract_pdf_text(uploaded_file):

    text = ""

    try:

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

    except Exception:

        uploaded_file.seek(0)

        doc = fitz.open(
            stream=uploaded_file.read(),
            filetype="pdf"
        )

        for page in doc:
            text += page.get_text()

    return text


# =========================
# DOCX TEXT EXTRACTION
# =========================
def extract_docx_text(uploaded_file):

    text = ""

    doc = Document(uploaded_file)

    for para in doc.paragraphs:

        text += para.text + "\n"

    return text


# =========================
# MAIN EXTRACTION FUNCTION
# =========================
def extract_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):

        return extract_pdf_text(uploaded_file)

    elif file_name.endswith(".docx"):

        return extract_docx_text(uploaded_file)

    else:

        return "Unsupported File Format"
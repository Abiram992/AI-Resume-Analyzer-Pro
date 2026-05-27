from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


# =========================
# GENERATE PDF REPORT
# =========================
def generate_report(
    filename,
    ats_score,
    jd_score,
    skills,
    missing_skills
):

    pdf_name = "resume_report.pdf"

    doc = SimpleDocTemplate(
        pdf_name
    )

    styles = getSampleStyleSheet()

    elements = []

    # =========================
    # TITLE
    # =========================
    elements.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles['Title']
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # =========================
    # SCORES
    # =========================
    elements.append(
        Paragraph(
            f"<b>Resume:</b> {filename}",
            styles['BodyText']
        )
    )

    elements.append(
        Paragraph(
            f"<b>ATS Score:</b> {ats_score}/100",
            styles['BodyText']
        )
    )

    elements.append(
        Paragraph(
            f"<b>JD Match:</b> {jd_score}%",
            styles['BodyText']
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # =========================
    # SKILLS
    # =========================
    elements.append(
        Paragraph(
            "<b>Detected Skills:</b>",
            styles['Heading2']
        )
    )

    elements.append(
        Paragraph(
            ", ".join(skills),
            styles['BodyText']
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # =========================
    # MISSING SKILLS
    # =========================
    elements.append(
        Paragraph(
            "<b>Missing Skills:</b>",
            styles['Heading2']
        )
    )

    elements.append(
        Paragraph(
            ", ".join(missing_skills[:10]),
            styles['BodyText']
        )
    )

    # =========================
    # BUILD PDF
    # =========================
    doc.build(elements)

    return pdf_name
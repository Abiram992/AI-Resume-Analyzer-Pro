import streamlit as st


# =========================
# METRICS DASHBOARD
# =========================
def render_metrics(
    ats_score,
    skills,
    missing,
    jd_score
):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "ATS Score",
        f"{ats_score}/100"
    )

    col2.metric(
        "Skills Found",
        len(skills)
    )

    col3.metric(
        "Missing Skills",
        len(missing)
    )

    col4.metric(
        "JD Match",
        f"{jd_score}%"
    )


# =========================
# SKILLS SECTION
# =========================
def render_skills(skills):

    st.subheader("📌 Detected Skills")

    skill_cols = st.columns(4)

    for i, skill in enumerate(skills):

        with skill_cols[i % 4]:

            st.success(skill)


# =========================
# MISSING SKILLS
# =========================
def render_missing_skills(missing):

    st.subheader("❌ Missing Skills")

    if missing:

        for skill in missing[:10]:

            st.warning(skill)

    else:

        st.success(
            "No major missing skills detected."
        )


# =========================
# JD MATCH UI
# =========================
def render_jd_match(jd_score):

    st.subheader(
        "💼 Job Description Match"
    )

    st.progress(int(jd_score))

    if jd_score >= 80:

        st.success(
            "Excellent Match!"
        )

    elif jd_score >= 60:

        st.warning(
            "Moderate Match."
        )

    else:

        st.error(
            "Low Match."
        )
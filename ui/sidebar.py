import streamlit as st


# =========================
# SIDEBAR UI
# =========================
def render_sidebar():

    st.sidebar.title(
        "🚀 Resume Analyzer Pro"
    )

    st.sidebar.info("""
    ### Features

    ✅ ATS Score
    ✅ Skill Detection
    ✅ AI Feedback
    ✅ JD Matching
    ✅ Resume Analytics
    ✅ Interview Questions
    ✅ NLP Skill Analysis
    """)

    st.sidebar.success(
        "Built with AI + NLP + Streamlit"
    )

    st.sidebar.divider()

    st.sidebar.write(
        "Made for Students & Recruiters"
    )
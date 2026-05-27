import streamlit as st
import time
import plotly.graph_objects as go

# =========================
# CORE IMPORTS
# =========================
from core.parser import extract_text
from core.ats_engine import calculate_ats_score
from core.jd_matcher import calculate_jd_match
from core.resume_rewriter import (
    rewrite_resume_section
)
from core.feedback_engine import generate_feedback
from core.interview_generator import (
    generate_interview_questions
)

from core.analytics_engine import (
    generate_resume_analytics,
    create_skill_dataframe
)

from core.report_generator import (
    generate_report
)

# =========================
# NLP IMPORTS
# =========================
from nlp.skill_extractor import (
    extract_skills,
    missing_skills,
    analyze_role_fit
)

# =========================
# UI IMPORTS
# =========================
from ui.sidebar import render_sidebar
from ui.themes import apply_theme

from ui.dashboard import (
    render_skills,
    render_missing_skills,
    render_jd_match
)

from ui.charts import (
    create_skill_chart,
    create_radar_chart
)

# =========================
# DATABASE
# =========================
from services.database_service import (
    save_analysis,
    fetch_analyses
)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="🚀",
    layout="wide"
)

# =========================
# APPLY THEME
# =========================
apply_theme()
render_sidebar()

# =========================
# HERO SECTION
# =========================
st.markdown(
    """
    <div style='padding-top:20px;'>

    <h1>
    🚀 AI Resume Analyzer Pro
    </h1>

    <p style='
    font-size:22px;
    color:#94a3b8;
    margin-top:-10px;
    '>

    Next-Generation AI Resume Intelligence Platform

    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# GLASS CONTAINER START
# =========================
st.markdown(
    """
    <div style='
    padding:25px;
    border-radius:24px;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);
    margin-bottom:20px;
    '>
    """,
    unsafe_allow_html=True
)

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx"]
)

# =========================
# SAMPLE JD
# =========================
sample_jd = st.selectbox(
    "🎯 Choose Sample Job Description",
    [
        "None",
        "Full Stack Developer",
        "AI/ML Engineer",
        "Data Analyst",
        "Cloud Engineer"
    ]
)

jd_examples = {

    "Full Stack Developer":
    """
    Looking for a Full Stack Developer
    with React, Node.js, MongoDB,
    Express.js, Git and Docker.
    """,

    "AI/ML Engineer":
    """
    Looking for an AI Engineer with
    Python, Machine Learning,
    NLP, TensorFlow and PyTorch.
    """,

    "Data Analyst":
    """
    Looking for a Data Analyst with
    SQL, Excel, Power BI and Python.
    """,

    "Cloud Engineer":
    """
    Looking for a Cloud Engineer
    with AWS, Kubernetes,
    Docker and Linux.
    """
}

# =========================
# JOB DESCRIPTION
# =========================
job_description = st.text_area(
    "📋 Paste Job Description",
    value=jd_examples.get(sample_jd, ""),
    height=200
)

# =========================
# GLASS CONTAINER END
# =========================
st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# =========================
# MAIN APP
# =========================
if uploaded_file:

    analyze = st.button(
        "🚀 Analyze Resume"
    )

    if analyze:

        # =========================
        # LOADING BAR
        # =========================
        progress = st.progress(0)

        for i in range(100):

            time.sleep(0.01)

            progress.progress(i + 1)

        # =========================
        # LOADING SPINNER
        # =========================
        with st.spinner(
            "🚀 AI is analyzing your resume..."
        ):

            time.sleep(2)

            # =========================
            # EXTRACT TEXT
            # =========================
            resume_text = extract_text(
                uploaded_file
            )

            # =========================
            # SKILLS
            # =========================
            skills = extract_skills(
                resume_text
            )

            # =========================
            # MISSING SKILLS
            # =========================
            missing = missing_skills(
                skills
            )

            # =========================
            # ATS SCORE
            # =========================
            ats_score = calculate_ats_score(
                skills,
                resume_text
            )

            # =========================
            # JD SCORE
            # =========================
            jd_score = 0

            if job_description:

                jd_score = calculate_jd_match(
                    resume_text,
                    job_description
                )

            # =========================
            # SAVE ANALYSIS
            # =========================
            save_analysis(
                uploaded_file.name,
                ats_score,
                jd_score,
                skills
            )

            # =========================
            # ANALYTICS
            # =========================
            analytics = generate_resume_analytics(
                skills,
                ats_score,
                jd_score,
                resume_text
            )

            # =========================
            # PDF REPORT
            # =========================
            report_path = generate_report(
                uploaded_file.name,
                ats_score,
                jd_score,
                skills,
                missing
            )

        # =========================
        # SUCCESS CARD
        # =========================
        st.markdown(
            """
            <div style="
            padding:18px;
            border-radius:18px;
            background:linear-gradient(
            90deg,
            #059669,
            #10b981
            );
            color:white;
            font-size:20px;
            font-weight:700;
            text-align:center;
            margin-top:10px;
            margin-bottom:20px;
            ">

            ✅ Resume Analyzed Successfully

            </div>
            """,
            unsafe_allow_html=True
        )

        # =========================
        # METRICS
        # =========================
        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "ATS Score",
                f"{ats_score}/100"
            )

        with col2:

            st.metric(
                "Skills Found",
                len(skills)
            )

        with col3:

            st.metric(
                "Missing Skills",
                len(missing)
            )

        with col4:

            st.metric(
                "JD Match",
                f"{jd_score}%"
            )

        st.divider()

        # =========================
        # DOWNLOAD REPORT
        # =========================
        with open(
            report_path,
            "rb"
        ) as file:

            st.download_button(
                label="📥 Download Resume Report",
                data=file,
                file_name="resume_report.pdf",
                mime="application/pdf"
            )

        st.divider()

        # =========================
        # TABS
        # =========================
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
            "📊 Dashboard",
            "📄 Resume",
            "🤖 AI Feedback",
            "📈 Analytics",
            "🎯 Interview Prep",
            "💼 Career Fit",
            "🗂 History",
            "✍ AI Rewriter"
        ])

        # ==================================================
        # TAB 1 — DASHBOARD
        # ==================================================
        with tab1:

            render_skills(skills)

            st.divider()

            render_missing_skills(missing)

            st.divider()

            render_jd_match(jd_score)

        # ==================================================
        # TAB 2 — RESUME CONTENT
        # ==================================================
        with tab2:

            st.subheader(
                "📄 Extracted Resume Content"
            )

            st.text_area(
                "Resume Text",
                resume_text,
                height=500
            )

        # ==================================================
        # TAB 3 — AI FEEDBACK
        # ==================================================
        with tab3:

            st.subheader(
                "🤖 AI Resume Analysis"
            )

            feedback = generate_feedback(
                resume_text
            )

            st.markdown(feedback)

        # ==================================================
        # TAB 4 — ANALYTICS
        # ==================================================
        with tab4:

            st.subheader(
                "🎯 ATS Score Gauge"
            )

            gauge = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=ats_score,

                    title={
                        'text': "ATS Score"
                    },

                    gauge={

                        'axis': {
                            'range': [0, 100]
                        },

                        'bar': {
                            'color': "#10b981"
                        },

                        'steps': [

                            {
                                'range': [0, 50],
                                'color': "#ef4444"
                            },

                            {
                                'range': [50, 75],
                                'color': "#f59e0b"
                            },

                            {
                                'range': [75, 100],
                                'color': "#10b981"
                            }
                        ]
                    }
                )
            )

            st.plotly_chart(
                gauge,
                use_container_width=True
            )

            st.subheader(
                "📈 Resume Analytics"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.info(
                    f"Experience Level: {analytics['experience_level']}"
                )

            with col2:

                st.info(
                    f"Resume Word Count: {analytics['resume_length']}"
                )

            st.write(
                "### 🧠 Communication Score"
            )

            st.progress(
                analytics["communication_score"]
            )

            st.write(
                "### 💻 Project Strength"
            )

            st.progress(
                analytics["project_score"]
            )

            # =========================
            # SKILL CHART
            # =========================
            skill_data = create_skill_dataframe(
                skills
            )

            fig = create_skill_chart(
                skill_data
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # =========================
            # RADAR CHART
            # =========================
            radar = create_radar_chart(
                skills,
                ats_score
            )

            st.plotly_chart(
                radar,
                use_container_width=True
            )

        # ==================================================
        # TAB 5 — INTERVIEW PREP
        # ==================================================
        with tab5:

            st.subheader(
                "🎯 AI Interview Questions"
            )

            if st.button(
                "Generate Interview Questions"
            ):

                with st.spinner(
                    "Generating Questions..."
                ):

                    questions = generate_interview_questions(
                        resume_text,
                        job_description
                    )

                st.markdown(
                    questions
                )

        # ==================================================
        # TAB 6 — CAREER FIT
        # ==================================================
        with tab6:

            st.subheader(
                "💼 Career Role Match"
            )

            role_scores = analyze_role_fit(
                skills
            )

            for role, score in role_scores.items():

                st.write(
                    f"### {role}"
                )

                st.progress(
                    int(score)
                )

                st.info(
                    f"Match Score: {score}%"
                )

        # ==================================================
        # TAB 7 — HISTORY
        # ==================================================
        with tab7:

            st.subheader(
                "🗂 Previous Analyses"
            )

            history = fetch_analyses()

            st.dataframe(
                history,
                use_container_width=True
            )

        # ==================================================
        # TAB 8 — AI RESUME REWRITER
        # ==================================================
        with tab8:
            st.subheader(
                "✍ AI Resume Rewriter"
            )

            st.write(
                "Improve weak resume content using AI."
            )

        rewrite_input = st.text_area(
            "Paste Resume Content",
            height=250,
            placeholder="""
 Example:

Worked on Python project
Made website using React
Responsible for team tasks
"""
        )

        if st.button(
            "🚀 Rewrite Professionally"
        ):

            with st.spinner(
                 "AI is rewriting..."
            ):

                improved = rewrite_resume_section(
                    rewrite_input
                )

            st.success(
                "Resume Content Improved!"
            )

            st.text_area(
                "✨ Improved Version",
                improved,
                height=300
            )
                  

    


# =========================
# EMPTY STATE
# =========================
else:

    st.info(
        "📤 Upload a resume to begin AI analysis."
    )
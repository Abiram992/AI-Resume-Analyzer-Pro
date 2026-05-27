import pandas as pd


# =========================
# RESUME ANALYTICS ENGINE
# =========================
def generate_resume_analytics(
    skills,
    ats_score,
    jd_score,
    resume_text
):

    analytics = {}

    # =========================
    # BASIC COUNTS
    # =========================
    analytics["total_skills"] = len(skills)

    analytics["resume_length"] = len(
        resume_text.split()
    )

    analytics["ats_score"] = ats_score

    analytics["jd_score"] = jd_score

    # =========================
    # EXPERIENCE LEVEL
    # =========================
    experience_keywords = [
        "internship",
        "experience",
        "developer",
        "engineer",
        "manager",
        "lead"
    ]

    exp_count = 0

    for word in experience_keywords:

        if word.lower() in resume_text.lower():
            exp_count += 1

    if exp_count >= 5:
        analytics["experience_level"] = "Advanced"

    elif exp_count >= 3:
        analytics["experience_level"] = "Intermediate"

    else:
        analytics["experience_level"] = "Beginner"

    # =========================
    # PROJECT SCORE
    # =========================
    project_keywords = [
        "project",
        "developed",
        "designed",
        "implemented",
        "built"
    ]

    project_count = 0

    for word in project_keywords:

        if word.lower() in resume_text.lower():
            project_count += 1

    analytics["project_score"] = min(
        project_count * 10,
        100
    )

    # =========================
    # COMMUNICATION SCORE
    # =========================
    communication_keywords = [
        "team",
        "leadership",
        "communication",
        "presentation",
        "collaboration"
    ]

    comm_count = 0

    for word in communication_keywords:

        if word.lower() in resume_text.lower():
            comm_count += 1

    analytics["communication_score"] = min(
        comm_count * 20,
        100
    )

    return analytics


# =========================
# SKILL DATAFRAME
# =========================
def create_skill_dataframe(skills):

    df = pd.DataFrame({
        "Skill": skills,
        "Count": [1] * len(skills)
    })

    return df


# =========================
# CATEGORY ANALYSIS
# =========================
def categorize_skills(skills):

    categories = {
        "Programming": [
            "python",
            "java",
            "c++",
            "javascript"
        ],

        "Web Development": [
            "html",
            "css",
            "react",
            "nodejs"
        ],

        "Database": [
            "mysql",
            "mongodb",
            "sql"
        ],

        "AI/ML": [
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch"
        ]
    }

    result = {}

    for category, keywords in categories.items():

        matched = []

        for skill in skills:

            if skill.lower() in keywords:
                matched.append(skill)

        result[category] = matched

    return result
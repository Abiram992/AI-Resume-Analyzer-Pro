import re
import pandas as pd

import json


# =========================
# LOAD SKILLS CSV
# =========================
skills_df = pd.read_csv(
    "data/skills.csv"
)

SKILLS_DB = skills_df[
    "skill"
].tolist()

# =========================
# LOAD JOB ROLES
# =========================
with open(
    "data/job_roles.json",
    "r"
) as file:

    JOB_ROLES = json.load(file)

# =========================
# CLEAN TEXT
# =========================
def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9+# ]",
        " ",
        text
    )

    return text


# =========================
# SKILL EXTRACTION
# =========================
def extract_skills(resume_text):

    cleaned = clean_text(
        resume_text
    )

    detected = []

    for skill in SKILLS_DB:

        if skill.lower() in cleaned:

            detected.append(skill)

    return sorted(
        list(set(detected))
    )


# =========================
# MISSING SKILLS
# =========================
def missing_skills(skills):

    detected = [
        skill.lower()
        for skill in skills
    ]

    missing = []

    for skill in SKILLS_DB:

        if skill.lower() not in detected:

            missing.append(skill)

    return missing


# =========================
# CATEGORY ANALYSIS
# =========================
def categorize_skills(skills):

    result = {}

    for _, row in skills_df.iterrows():

        category = row["category"]

        skill = row["skill"]

        if category not in result:

            result[category] = []

        if skill in skills:

            result[category].append(
                skill
            )

    return result


# =========================
# ROLE FIT ANALYSIS
# =========================
def analyze_role_fit(skills):

    result = {}

    lower_skills = [
        skill.lower()
        for skill in skills
    ]

    for role, required_skills in JOB_ROLES.items():

        matched = 0

        for skill in required_skills:

            if skill.lower() in lower_skills:

                matched += 1

        score = round(
            (matched / len(required_skills)) * 100,
            2
        )

        result[role] = score

    return result
import sqlite3
import pandas as pd


# =========================
# DATABASE CONNECTION
# =========================
conn = sqlite3.connect(
    "resume_analyzer.db",
    check_same_thread=False
)

cursor = conn.cursor()


# =========================
# CREATE TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS analyses (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    filename TEXT,

    ats_score INTEGER,

    jd_score REAL,

    skills TEXT
)
""")

conn.commit()


# =========================
# SAVE ANALYSIS
# =========================
def save_analysis(
    filename,
    ats_score,
    jd_score,
    skills
):

    skills_text = ", ".join(skills)

    cursor.execute("""
    INSERT INTO analyses (
        filename,
        ats_score,
        jd_score,
        skills
    )

    VALUES (?, ?, ?, ?)
    """, (
        filename,
        ats_score,
        jd_score,
        skills_text
    ))

    conn.commit()


# =========================
# FETCH ANALYSES
# =========================
def fetch_analyses():

    query = """
    SELECT * FROM analyses
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    return df
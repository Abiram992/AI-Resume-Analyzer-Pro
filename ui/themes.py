import streamlit as st


def apply_theme():

    st.markdown(
        """
        <style>

        /* =========================
           GLOBAL
        ========================== */

        html, body, [class*="css"] {

            font-family: 'Inter', sans-serif;
            background-color: #050816;
            color: white;
        }

        .stApp {

            background:
            radial-gradient(circle at top left, #0f172a, #020617);
        }

        /* =========================
           MAIN TITLE
        ========================== */

        h1 {

            font-size: 4rem !important;
            font-weight: 800 !important;

            background: linear-gradient(
                90deg,
                #38bdf8,
                #8b5cf6,
                #ec4899
            );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

            margin-bottom: 10px;
        }

        /* =========================
           SIDEBAR
        ========================== */

        section[data-testid="stSidebar"] {

            background: rgba(15, 23, 42, 0.95);
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        /* =========================
           METRIC CARDS
        ========================== */

        div[data-testid="metric-container"] {

            background: rgba(255,255,255,0.06);

            border: 1px solid rgba(255,255,255,0.08);

            padding: 25px;

            border-radius: 22px;

            backdrop-filter: blur(14px);

            transition: 0.3s;

            box-shadow:
            0 4px 30px rgba(0,0,0,0.2);
        }

        div[data-testid="metric-container"]:hover {

            transform: translateY(-6px);

            border: 1px solid #38bdf8;

            box-shadow:
            0 0 30px rgba(56,189,248,0.4);
        }

        /* =========================
           BUTTONS
        ========================== */

        .stButton > button {

            width: 100%;

            height: 60px;

            border-radius: 18px;

            border: none;

            font-size: 20px;

            font-weight: 700;

            background:
            linear-gradient(
                90deg,
                #3b82f6,
                #8b5cf6
            );

            color: white;

            transition: 0.3s;
        }

        .stButton > button:hover {

            transform: scale(1.02);

            box-shadow:
            0 0 25px rgba(139,92,246,0.6);
        }

        /* =========================
           INPUTS
        ========================== */

        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"],
        .stFileUploader {

            background: rgba(255,255,255,0.04);

            border-radius: 16px !important;

            border: 1px solid rgba(255,255,255,0.08);

            color: white;
        }

        /* =========================
           TABS
        ========================== */

        button[data-baseweb="tab"] {

            font-size: 17px;

            font-weight: 600;

            color: white;

            padding: 14px 28px;

            border-radius: 14px;

            transition: 0.3s;
        }

        button[data-baseweb="tab"]:hover {

            background: rgba(255,255,255,0.08);
        }

        button[aria-selected="true"] {

            background:
            linear-gradient(
                90deg,
                #2563eb,
                #7c3aed
            ) !important;

            color: white !important;
        }

        /* =========================
           SUCCESS BOX
        ========================== */

        .stAlert {

            border-radius: 18px;
        }

        /* =========================
           SCROLLBAR
        ========================== */

        ::-webkit-scrollbar {

            width: 10px;
        }

        ::-webkit-scrollbar-thumb {

            background: #7c3aed;
            border-radius: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
import streamlit as st


# =========================
# SIMPLE AUTH SYSTEM
# =========================
def login(username, password):

    # DEMO LOGIN

    if (
        username == "admin"
        and password == "admin123"
    ):

        return True

    return False


# =========================
# LOGIN UI
# =========================
def login_page():

    st.title("🔐 Login")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if login(username, password):

            st.success(
                "Login Successful"
            )

            st.session_state[
                "logged_in"
            ] = True

        else:

            st.error(
                "Invalid Credentials"
            )
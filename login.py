import streamlit as st
import json
import os
import hashlib

st.set_page_config(
    page_title="CareerCompass - Login",
    page_icon="🧭",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_FILE = os.path.join(BASE_DIR, "users.json")


def load_users():
    if not os.path.exists(USER_FILE):
        return {}

    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return {}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


st.markdown("""
<style>

header {
    display: none !important;
}

#MainMenu {
    display: none !important;
}

footer {
    display: none !important;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

.stApp {
    background: linear-gradient(
        90deg,
        #8B4CF5 0%,
        #B957C9 45%,
        #FF8A4C 100%
    );

    min-height: 100vh;
}

.logo {
    position: absolute;
    top: 20px;
    left: 25px;
    font-size: 35px;
    font-weight: 700;

    background: linear-gradient(
        90deg,
        #2E005D,
        #8E008B,
        #EF2E78
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.stTextInput label {
    color: #35106C !important;
    font-weight: 600 !important;
}

.stTextInput input {
    border-radius: 9px !important;
    border: 1px solid #d5c5e8 !important;
}

.stButton > button {
    width: 100%;

    background: linear-gradient(
        90deg,
        #7135E7,
        #E94B88
    ) !important;

    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    height: 45px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="logo">CareerCompass</div>',
    unsafe_allow_html=True
)


st.markdown("""
<div style="
    width:430px;
    background:white;
    border-radius:20px;
    padding:35px;
    margin:80px auto 30px auto;
    box-shadow:0px 15px 40px rgba(0,0,0,0.25);
">

<h1 style="
    text-align:center;
    color:#35106C;
">
Welcome Back
</h1>

<p style="
    text-align:center;
    color:#666;
">
Login to continue your CareerCompass journey
</p>

</div>
""", unsafe_allow_html=True)


left, center, right = st.columns([1, 2, 1])

with center:

    phone = st.text_input(
        "📱 Phone Number",
        placeholder="Enter registered phone number",
        max_chars=10
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        placeholder="Enter 8 character password",
        max_chars=8
    )

    if st.button("Login"):

        users = load_users()

        if phone not in users:

            st.error(
                "Account not found. Please Sign Up first."
            )

        elif users[phone]["password"] != hash_password(password):

            st.error(
                "Incorrect password."
            )

        else:

            st.session_state["logged_in"] = True
            st.session_state["username"] = users[phone]["username"]
            st.session_state["phone"] = phone

            st.success(
                f"Welcome {users[phone]['username']}! 🎉"
            )

            st.switch_page("landing.py")

    st.write("")

    if st.button("Forgot Password?"):

        st.switch_page(
            "pages/forgot_password.py"
        )

    st.write("")

    if st.button("Create New Account"):

        st.switch_page(
            "pages/signup.py"
        )
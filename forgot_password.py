import streamlit as st
import json
import os
import hashlib
import re

st.set_page_config(
    page_title="CareerCompass - Forgot Password",
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
    except:
        return {}


def save_users(users):

    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


def valid_phone(phone):

    return re.fullmatch(
        r"[6-9][0-9]{9}",
        phone
    ) is not None


st.markdown("""
<style>

header {
    display:none !important;
}

#MainMenu {
    display:none !important;
}

footer {
    display:none !important;
}

.block-container {
    padding:0 !important;
    max-width:100% !important;
}

.stApp {
    background:linear-gradient(
        90deg,
        #8B4CF5 0%,
        #B957C9 45%,
        #FF8A4C 100%
    );

    min-height:100vh;
}

.logo {
    position:absolute;
    top:20px;
    left:25px;
    font-size:35px;
    font-weight:700;

    background:linear-gradient(
        90deg,
        #2E005D,
        #8E008B,
        #EF2E78
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.stTextInput label {
    color:#35106C !important;
    font-weight:600 !important;
}

.stTextInput input {
    border-radius:9px !important;
    border:1px solid #d5c5e8 !important;
}

.stButton > button {
    width:100%;

    background:linear-gradient(
        90deg,
        #7135E7,
        #E94B88
    ) !important;

    color:white !important;
    border:none !important;
    border-radius:9px !important;
    height:45px;
    font-weight:700;
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
Reset Password
</h1>

<p style="
    text-align:center;
    color:#666;
">
Enter your registered phone number
</p>

</div>
""", unsafe_allow_html=True)


left, center, right = st.columns([1, 2, 1])

with center:

    phone = st.text_input(
        "📱 Registered Phone Number",
        placeholder="Enter your phone number",
        max_chars=10
    )

    if st.button("Verify Phone Number"):

        users = load_users()

        if not valid_phone(phone):

            st.error(
                "Enter a valid 10-digit phone number."
            )

        elif phone not in users:

            st.error(
                "No account found with this phone number."
            )

        else:

            st.session_state["reset_phone"] = phone
            st.session_state["phone_verified"] = True

            st.success(
                "Phone number verified! You can reset your password."
            )


    if st.session_state.get("phone_verified", False):

        st.divider()

        new_password = st.text_input(
            "🔒 New Password",
            type="password",
            placeholder="Enter exactly 8 characters",
            max_chars=8
        )

        confirm_password = st.text_input(
            "🔒 Confirm New Password",
            type="password",
            placeholder="Re-enter your password",
            max_chars=8
        )

        if st.button("Reset Password"):

            if len(new_password) != 8:

                st.error(
                    "Password must contain exactly 8 characters."
                )

            elif new_password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            else:

                users = load_users()

                phone = st.session_state["reset_phone"]

                users[phone]["password"] = hash_password(
                    new_password
                )

                save_users(users)

                st.success(
                    "Password reset successfully! 🎉"
                )

                st.session_state["phone_verified"] = False

                st.info(
                    "Now you can login using your new password."
                )


    st.write("")

    if st.button("Back to Login"):

        st.session_state["phone_verified"] = False

        st.switch_page("pages/login.py")
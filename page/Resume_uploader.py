import streamlit as st
import requests

# -----------------------
#       navbar
# -----------------------

st.markdown("""
            <link
              rel="stylesheet"
              href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.3.0/css/all.min.css"
              integrity="sha512-ApSLB1Pd3/bZN8fWB/RG9YhN/7bd9Hkf3AGaE2mPfebjrxagjuBtx2GcgdqIlJkUzwylBo61r9Xa9NmgBI0swA=="
              crossorigin="anonymous"
              referrerpolicy="no-referrer"
            />

            <div class = "nav">

            <div class="title">
                <a href="/landing"> CareerCompass</a>
            </div>

            <div class="nav-items">
                <a href="/" class="Home">
                    <i class="fa-solid fa-house"></i>
                    Home
                </a>
                <a href="/Resume_uploader" class="resume">
                    <i class="fa-sharp fa-solid fa-file-import"></i>
                    Resume Upload
                </a>
                <a href="/Dashboard" class="ATS">
                    <i class="fa-solid fa-tachograph-digital"></i>
                    ATS Dashnoard
                </a>
                <a href="#">
                    <i class="fa-solid fa-microphone"></i>
                    Mock Interview
                </a>
                <a href="#">
                    <i class="fa-solid fa-circle-info"></i>
                    About
                </a>
                <div class="login">
                    <i class="fa-regular fa-user"></i>
                    <a href="#"> Login/Sign Up </a>
                </div>
            </div>

            </div> """, unsafe_allow_html=True)

# -----------------------
#     hero (text only - no fake widget overlays here)
# -----------------------

st.markdown("""
            <div class="hero-section">
                <div class="main">
                    <h6> Resume Analyzer </h6>
                    <h1>
                        Is your resume good <br>
                        enough?
                    </h1>
                    <p class="description">
                        "Is your resume ready for your next opportunity? Check your resume for content, formatting, keywords, and ATS compatibility, and identify areas that can be improved to make your resume stronger and more effective."
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)

# -----------------------
#     backend config
# -----------------------

BACKEND_URL = "http://localhost:8000"

# -----------------------
#  upload box + job role + analyze button
#  (all three live in ONE real container, which is what gets the
#   gradient background - no negative-margin hacks needed)
# -----------------------

with st.container(key="upload_section"):
    uploaded_file = st.file_uploader(
        "Upload",
        type=["pdf", "docx"],
        label_visibility="collapsed",
        key="resume_uploader",
    )

    job_role = st.selectbox(
        "Job Role :",
        [
            "Software Engineer",
            "Data Scientist",
            "Data Analyst",
            "Product Manager",
            "UI/UX Designer",
            "DevOps Engineer",
            "Marketing",
            "Sales",
            "Other",
        ],
        key="job_role",
        label_visibility="visible"
    )

    if uploaded_file and uploaded_file.size > 5 * 1024 * 1024:
        st.error("File size must be less than 5MB.")

    analyze_clicked = st.button("Analyze Resume", key="analyze_btn")

if analyze_clicked:
    if not uploaded_file:
        st.warning("Please select a resume file first.")
    elif uploaded_file.size > 5 * 1024 * 1024:
        st.error("File size must be less than 5MB.")
    else:
        with st.spinner("Analyzing your resume..."):
            try:
                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type,
                    )
                }
                data = {"job_role": job_role}
                response = requests.post(
                    f"{BACKEND_URL}/analyze-resume",
                    files=files,
                    data=data,
                    timeout=30,
                )

                if response.status_code == 200:
                    st.session_state["ats_result"] = response.json()
                    st.switch_page("pages/Dashboard.py")
                else:
                    detail = response.json().get("detail", "Unknown error")
                    st.error(f"Analysis failed: {detail}")

            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not reach the analysis server. "
                    "Make sure the FastAPI backend is running on "
                    f"{BACKEND_URL}."
                )
            except requests.exceptions.Timeout:
                st.error("The analysis server took too long to respond. Please try again.")


# -----------------------
#          styles
# -----------------------

st.markdown("""
                <style>

            /* Remove Streamlit top area */

            header { display: none !important; }
            [data-testid="stHeader"] { display: none !important; }
            #MainMenu { display: none !important; }
            footer { display: none !important; }

            .block-container {
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100% !important;
            }

            [data-testid="stVerticalBlock"] {
                gap: 10px !important;
            }

            .stMarkdown {
                margin: 0 !important;
                padding: 0 !important;
            }

            /* =========================
            NAVBAR
            ========================= */

            .nav{
                display:flex;
                justify-content: space-between;
                align-items:flex-end;
                background: linear-gradient(90deg, #8B4CF5 0%, #B957C9 45%, #FF8A4C 100%);
                text-decoration: none;
            }

            .resume{ color:#FFFFFF !important; }

            .title a{
                padding-left:20px;
                padding-top:15px;
                font-size: 35px;
                background: linear-gradient(90deg, #2E005D, #8E008B, #EF2E78);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-decoration: none;
                font-weight:700;
            }

            .nav-items { display: flex; gap: 50px; }
            .nav-items a { color: #2E005D; text-decoration: none; font-size: 15px; }
            .login { color: #2E005D; border: 1px solid transparent; padding-right:12px; }
            .nav-items a:hover { color: #ffffff; transform: translateY(-2px); }
            .login:hover{ color: #ffffff; transform: translateY(-2px); }

            /* =========================
            HERO SECTION (text only now)
            ========================= */

            .hero-section {
                color:white;
                background: linear-gradient(90deg, #8B4CF5 0%, #B957C9 45%, #FF8A4C 100%);
                padding: 120px 200px 40px 200px;
                box-sizing: border-box;
            }

            .hero-section p { width:500px; }

            /* =========================
            UPLOAD SECTION CONTAINER
            (this is the real Streamlit container that holds the
            uploader + dropdown + button - it carries the gradient
            forward so it visually reads as one continuous hero block)
            ========================= */

            div.st-key-upload_section {
                background: linear-gradient(90deg, #8B4CF5 0%, #B957C9 45%, #FF8A4C 100%);
                padding: 0px 200px 60px 200px;
                box-sizing: border-box;
                display: flex !important;
                flex-direction: column !important;
                align-items: flex-start !important;
                gap: 16px !important;
            }

            /* keep everything inside the upload section at a fixed width,
               no left/top margins needed - the container already handles it */
            div.st-key-upload_section div[data-testid="stFileUploader"],
            div.st-key-upload_section div[data-testid="stSelectbox"],
            div.st-key-upload_section div[data-testid="stButton"] {
                width: 400px !important;
                margin: 0 !important;
            }

            /* =========================
            JOB ROLE DROPDOWN
            ========================= */

            div[data-testid="stSelectbox"] > div > div {
                background: rgba(255,255,255,0.95) !important;
                border-radius: 8px !important;
                border: none !important;
                height: 46px !important;
                color: #6B24C9 !important;
                font-weight: 600 !important;
            }

            div[data-testid="stSelectbox"] div[data-baseweb="select"] * {
    color: #6B24C9 !important;
    fill: #6B24C9 !important;

}
            /* =========================
            RESUME UPLOADER
            ========================= */

            [data-testid="stFileUploader"] [data-testid="stWidgetLabel"] {
                display: none !important;

            }

            [data-testid="stFileUploader"] > div {
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                gap: 12px !important;
                width: 100% !important;
            }

            /* outer dashed dropzone */
            [data-testid="stFileUploader"] section {
                width: 400px !important;
                min-width: 400px !important;
                max-width: 400px !important;
                min-height: 180px !important;
                height: auto !important;
                box-sizing: border-box !important;
                background: rgba(255,255,255,0.08) !important;
                border: 2px dashed rgba(255,255,255,0.9) !important;
                border-radius: 14px !important;
                padding: 20px !important;
                box-shadow: none !important;
                overflow: hidden !important;
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: center !important;
                gap: 12px !important;
            }

            /* hide Streamlit's default drag/drop + size text ... */
            [data-testid="stFileUploaderDropzoneInstructions"] {
                display: none !important;
            }
            [data-testid="stFileUploader"] small {
                display: none !important;
            }

            /* ...replace with our own copy, in normal flow (no absolute
               positioning), so it can never overlap another widget */
            [data-testid="stFileUploader"] section::before {
                content: "Drop your resume here or choose a file";
                order: -1;
                color: rgba(255,255,255,0.9);
                font-size: 14px;
                font-weight: 600;
                text-align: center;
            }

            [data-testid="stFileUploader"] section::after {
                content: "PDF & DOCX only. Max 5MB file size.";
                color: rgba(255,255,255,0.75);
                font-size: 12px;
                text-align: center;
            }

            /* upload button */
            [data-testid="stFileUploader"] section button {
                width: auto !important;
                min-width: 0 !important;
                max-width: none !important;
                flex: 0 0 auto !important;
                align-self: center !important;
                height: 42px !important;
                background: #FFFFFF !important;
                color: #6B24C9 !important;
                border: none !important;
                border-radius: 7px !important;
                margin: 0 !important;
                padding: 0 20px !important;
                box-sizing: border-box !important;
                overflow: visible !important;
                white-space: nowrap !important;
                font-size: 14px !important;
                font-weight: 600 !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                gap: 8px !important;
            }

            [data-testid="stFileUploader"] section > div {
                width: auto !important;
                flex: 0 0 auto !important;
                display: flex !important;
                justify-content: center !important;
            }

            [data-testid="stFileUploader"] section button svg {
                width: 16px !important;
                height: 16px !important;
                flex-shrink: 0 !important;
            }

            [data-testid="stFileUploader"] section button span {
                display: none !important;
            }

            [data-testid="stFileUploader"] section button::after {
                content: "Upload";
                font-size: 14px;
                font-weight: 600;
                color: #6B24C9;
                white-space: nowrap;
            }

            /* uploaded file row */
            [data-testid="stFileUploaderFile"] {
                width: 100% !important;
                max-width: 100% !important;
                box-sizing: border-box !important;
                margin: 0 !important;
                display: flex !important;
                align-items: center !important;
            }

            [data-testid="stFileUploaderFile"] span {
                max-width: 180px !important;
                overflow: hidden !important;
                text-overflow: ellipsis !important;
                white-space: nowrap !important;
            }

            [data-testid="stFileUploaderFile"] ~ button {
                width: 36px !important;
                min-width: 36px !important;
                max-width: 36px !important;
                height: 36px !important;
                padding: 0 !important;
                background: #FFFFFF !important;
                color: #6B24C9 !important;
                border: none !important;
                border-radius: 7px !important;
                box-sizing: border-box !important;
                overflow: hidden !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                flex-shrink: 0 !important;
            }

            [data-testid="stFileUploaderFile"] ~ button::after {
                content: "" !important;
            }

            [data-testid="stFileUploaderFile"] ~ button svg {
                width: 14px !important;
                height: 14px !important;
            }

            /* =========================
            ANALYZE RESUME BUTTON
            ========================= */

            div[data-testid="stButton"] button {
                width: 100% !important;
                height: 46px !important;
                background: #FFFFFF !important;
                color: #6B24C9 !important;
                border: none !important;
                border-radius: 8px !important;
                font-size: 15px !important;
                font-weight: 700 !important;
                box-shadow: 0 4px 14px rgba(0,0,0,0.15) !important;
            }

            div[data-testid="stButton"] button:hover {
                background: #f3e8ff !important;
            }

            </style>
            """, unsafe_allow_html=True)
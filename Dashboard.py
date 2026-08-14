import streamlit as st

st.set_page_config(
    page_title="CareerCompass ATS Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🎯 CareerCompass ATS Dashboard")

st.write("Dashboard is working!")

st.divider()

# Dummy data
overall_score = 78
word_count = 542
keyword_score = 72
section_score = 90
contact_score = 100
length_score = 80

# Top cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🎯 ATS Score", "78%")

with col2:
    st.metric("📄 Resume Words", "542")

with col3:
    st.metric("🔑 Keywords", "10")

with col4:
    st.metric("⚠️ Issues", "2")

st.divider()

st.subheader("📊 Score Breakdown")

col1, col2 = st.columns(2)

with col1:
    st.write("📚 Resume Sections")
    st.progress(section_score / 100)
    st.write("90%")

    st.write("📞 Contact Information")
    st.progress(contact_score / 100)
    st.write("100%")

with col2:
    st.write("🔑 Keywords")
    st.progress(keyword_score / 100)
    st.write("72%")

    st.write("📏 Resume Length")
    st.progress(length_score / 100)
    st.write("80%")

st.divider()

st.subheader("📄 Resume Information")

st.write("**Resume:** Mayuri_Satani_Resume.pdf")
st.write("**Target Role:** Software Developer")
st.write("**Word Count:** 542")

st.divider()

st.subheader("🔑 Matched Keywords")

keywords = [
    "Python",
    "Java",
    "SQL",
    "JavaScript",
    "Git",
    "API",
    "Data Analysis",
    "Machine Learning"
]

for keyword in keywords:
    st.write("✅", keyword)

st.divider()

st.subheader("⚠️ Issues Found")

st.warning("Some important technical keywords are missing.")
st.warning("Project descriptions could include more measurable achievements.")

st.subheader("💡 Suggestions")

st.info("Add keywords from the job description.")
st.info("Mention measurable achievements.")
st.info("Use stronger action verbs.")

st.success("Dashboard loaded successfully!")
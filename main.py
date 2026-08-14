from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import docx
import re
import io

app = FastAPI(title="CareerCompass Resume Analyzer API")

# Allow your Streamlit frontend (running on a different port) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # tighten this to your Streamlit URL before demo/prod
    allow_methods=["*"],
    allow_headers=["*"],
)

SECTION_KEYWORDS = {
    "experience": ["experience", "work historay", "employment"],
    "education": ["education", "academic"],
    "skills": ["skills", "technical skills", "competencies"],
    "projects": ["projects", "portfolio"],
}

# Simple generic ATS keyword list - swap this for a job-description-driven
# match if you have time (compare resume text against a pasted JD instead).
ATS_KEYWORDS = [
    "python", "java", "sql", "javascript", "react", "aws", "docker",
    "kubernetes", "machine learning", "data analysis", "agile",
    "communication", "leadership", "teamwork", "project management",
    "git", "api", "cloud", "linux", "problem solving",
]


def extract_text_from_pdf(file_bytes: bytes) -> str:
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_text_from_docx(file_bytes: bytes) -> str:
    doc = docx.Document(io.BytesIO(file_bytes))
    return "\n".join(p.text for p in doc.paragraphs)


def check_sections(text_lower: str):
    return {
        section: any(kw in text_lower for kw in keywords)
        for section, keywords in SECTION_KEYWORDS.items()
    }


def check_contact_info(text: str):
    email_found = bool(re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text))
    phone_found = bool(re.search(r"(\+?\d[\d\-\s\(\)]{8,}\d)", text))
    return email_found, phone_found


def keyword_match(text_lower: str):
    matched = [kw for kw in ATS_KEYWORDS if kw in text_lower]
    score = round((len(matched) / len(ATS_KEYWORDS)) * 100)
    return matched, score


def analyze_resume(text: str) -> dict:
    text_lower = text.lower()
    word_count = len(text.split())

    sections = check_sections(text_lower)
    section_score = round((sum(sections.values()) / len(sections)) * 100)

    email_found, phone_found = check_contact_info(text)
    contact_score = 100 if (email_found and phone_found) else (50 if (email_found or phone_found) else 0)

    matched_keywords, keyword_score = keyword_match(text_lower)

    if word_count < 150:
        length_score, length_note = 40, "Resume seems too short - add more detail."
    elif word_count > 1000:
        length_score, length_note = 60, "Resume may be too long - aim for 1-2 pages."
    else:
        length_score, length_note = 100, "Resume length looks good."

    overall_score = round(
        section_score * 0.30
        + contact_score * 0.15
        + keyword_score * 0.35
        + length_score * 0.20
    )

    issues, suggestions = [], []

    for section, present in sections.items():
        if not present:
            issues.append(f"Missing a clear '{section.title()}' section.")
            suggestions.append(f"Add a dedicated '{section.title()}' section with a standard heading.")

    if not email_found:
        issues.append("No email address detected.")
        suggestions.append("Add a professional email address near the top of your resume.")
    if not phone_found:
        issues.append("No phone number detected.")
        suggestions.append("Add a contact phone number.")

    if keyword_score < 40:
        issues.append("Low match with common ATS/industry keywords.")
        suggestions.append("Tailor your resume with keywords relevant to your target role.")

    if length_note != "Resume length looks good.":
        issues.append(length_note)

    return {
        "word_count": word_count,
        "overall_score": overall_score,
        "breakdown": {
            "sections": section_score,
            "contact_info": contact_score,
            "keywords": keyword_score,
            "length": length_score,
        },
        "sections_found": sections,
        "contact_info": {"email_found": email_found, "phone_found": phone_found},
        "matched_keywords": matched_keywords,
        "issues": issues,
        "suggestions": suggestions,
    }


@app.get("/")
def root():
    return {"status": "CareerCompass API is running"}


@app.post("/analyze-resume")
async def analyze_resume_endpoint(
    file: UploadFile = File(...),
    job_role: str = Form(None),
):
    filename = (file.filename or "").lower()
    if not (filename.endswith(".pdf") or filename.endswith(".docx")):
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported.")

    file_bytes = await file.read()
    if len(file_bytes) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File size must be under 5MB.")

    try:
        text = extract_text_from_pdf(file_bytes) if filename.endswith(".pdf") else extract_text_from_docx(file_bytes)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Could not read file: {e}")

    if not text.strip():
        raise HTTPException(status_code=422, detail="Could not extract any text from the file. Is it scanned/image-based?")

    result = analyze_resume(text)
    result["filename"] = file.filename
    result["target_role"] = job_role
    return result

from fastapi import FastAPI, UploadFile, File, Form, HTTPException

app = FastAPI(title="CareerCompass API")


@app.get("/")
def root():
    return {
        "status": "CareerCompass API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze-resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_role: str = Form("AI Engineer")
):

    if not file.filename.lower().endswith((".pdf", ".docx")):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )

    file_bytes = await file.read()

    if len(file_bytes) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="File size must be under 5MB."
        )

    return {
        "filename": file.filename,
        "target_role": job_role,
        "score": 75,
        "matched_skills": [
            "python",
            "sql",
            "pandas"
        ],
        "missing_skills": [
            "tensorflow",
            "docker"
        ],
        "feedback": [
            "Resume is moderately optimized for ATS systems."
        ]
    }
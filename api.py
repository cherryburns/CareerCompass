from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import tempfile
import os

from analyzer import analyze_resume

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
async def analyze_resume_api(
    file: UploadFile = File(...),
    job_role: str = Form(...)
):
    # Check file type
    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )

    # Read uploaded file
    contents = await file.read()

    # Temporary file
    suffix = ".pdf" if file.filename.lower().endswith(".pdf") else ".docx"

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            temp_file.write(contents)
            temp_path = temp_file.name

        # Call friend's backend analysis
        result = analyze_resume(
            temp_path,
            job_role
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
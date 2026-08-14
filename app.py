from parser import extract_text
from skills import extract_skills
from scorer import calculate_ats_score
import json
from analyzer import analyze_resume
from database import save_resume_analysis

def analyze_resume(file_path, role):
    text = extract_text(file_path)
    skills = extract_skills(text, role)
    result = calculate_ats_score(skills, role)

    output = {
        "target_role": role,
        "extracted_skills": skills,
        **result
    }

    return output

user_id = 1

result = analyze_resume("Warehouse_Management.docx", "AI Engineer")

save_resume_analysis(
    user_id,
    "Warehouse_Management.docx",
    result
)

if __name__ == "__main__":
    analysis = analyze_resume(
        "sample_resumes/resume1.pdf",
        "AI Engineer"
    )

    print(json.dumps(analysis, indent=4))
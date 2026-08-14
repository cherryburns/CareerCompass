'''from parser import extract_text

text = extract_text("Warehouse_Management.docx")
print(text[:1000])'''
from parser import extract_text
from skills import extract_skills

text = extract_text("sample_resumes/resume1.pdf")
skills = extract_skills(text, "AI Engineer")

print(skills)

'''from analyzer import analyze_resume
from database import save_resume_analysis

# Simulated logged-in user
user_id = 1

result = analyze_resume("Warehouse_Management.docx", "AI Engineer")

save_resume_analysis(
    user_id,
    "Warehouse_Management.docx",
    result
)'''
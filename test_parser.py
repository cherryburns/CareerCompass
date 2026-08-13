'''from parser import extract_text

text = extract_text("Warehouse_Management.docx")
print(text[:1000])'''
from parser import extract_text
from skills import extract_skills

text = extract_text("sample_resumes/resume1.pdf")
skills = extract_skills(text, "AI Engineer")

print(skills)
SKILLS_DB = {
    "AI Engineer": [
        "python", "sql", "pandas", "numpy",
        "tensorflow", "pytorch", "machine learning",
        "deep learning", "git", "docker", "fastapi"
    ],

    "Frontend Developer": [
        "html", "css", "javascript", "react",
        "tailwind", "typescript"
    ],

    "Backend Developer": [
        "python", "java", "fastapi", "flask",
        "mysql", "postgresql", "rest api", "docker"
    ]
}
import spacy
from skills import SKILLS_DB

nlp = spacy.load("en_core_web_sm")

def extract_skills(text, role):
    text_lower = text.lower()
    found_skills = []

    for skill in SKILLS_DB.get(role, []):
        if skill in text_lower:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))
def extract_skills(text, role):
    text_lower = text.lower()
    found_skills = []

    for skill in SKILLS_DB.get(role, []):
        if skill in text_lower:
            found_skills.append(skill)

    confidence = round(len(found_skills) / len(SKILLS_DB[role]) * 100, 1)

    return found_skills, confidence
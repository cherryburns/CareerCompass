import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Role-based skill database
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

def extract_skills(text, role):
    text_lower = text.lower()
    found_skills = []

    # Match skills from the selected role
    for skill in SKILLS_DB.get(role, []):
        if skill in text_lower:
            found_skills.append(skill)

    # Remove duplicates and sort alphabetically
    found_skills = sorted(list(set(found_skills)))

    # Calculate extraction confidence
    total_skills = len(SKILLS_DB.get(role, []))
    confidence = round((len(found_skills) / total_skills) * 100, 1) if total_skills > 0 else 0.0

    return found_skills, confidence
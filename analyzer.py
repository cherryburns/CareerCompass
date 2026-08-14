from parser import extract_text
from skills import extract_skills
from scorer import (
    calculate_ats_score,
    generate_feedback,
    interview_context
)

def analyze_resume(file_path, role="AI Engineer"):
    text = extract_text(file_path)

    found_skills, confidence = extract_skills(text, role)

    score_result = calculate_ats_score(found_skills, role)

    feedback = generate_feedback(
        score_result["score"],
        score_result["missing_skills"]
    )

    analysis = {
        "target_role": role,
        "score": score_result["score"],
        "matched_skills": score_result["matched_skills"],
        "missing_skills": score_result["missing_skills"],
        "feedback": feedback
    }

    analysis["interview_context"] = interview_context(analysis)

    return analysis
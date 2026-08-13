from skills import SKILLS_DB

def calculate_ats_score(found_skills, role):
    required = SKILLS_DB.get(role, [])

    matched = len(found_skills)
    total = len(required)

    score = int((matched / total) * 100) if total > 0 else 0

    missing = [s for s in required if s not in found_skills]

    return {
        "score": score,
        "matched_skills": found_skills,
        "missing_skills": missing
    }


def generate_feedback(score, missing_skills):
    feedback = []

    if score < 50:
        feedback.append("Resume needs significant improvement.")
    elif score < 75:
        feedback.append("Resume is moderately optimized for ATS systems.")
    else:
        feedback.append("Resume is well optimized for the target role.")

    if missing_skills:
        feedback.append(
            f"Consider learning: {', '.join(missing_skills[:3])}"
        )

    return feedback


def interview_context(analysis):
    return {
        "role": analysis["target_role"],
        "skills": analysis["matched_skills"],
        "focus_areas": analysis["missing_skills"][:3]
    }
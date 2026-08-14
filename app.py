import json
import os

from analyzer import analyze_resume
from database import init_db, save_resume_analysis
from chatbot import (
    generate_ai_questions,
    evaluate_answer,
    speak,
    listen
)

# Initialize database
init_db()

# Main execution
if __name__ == "__main__":

    user_id = 1

    file_path = input("Enter resume file name: ")
    role = input("Enter target role: ") or "AI Engineer"

    # -------- FILE VALIDATION --------
    if not os.path.exists(file_path):
        print("❌ File not found!")
        exit()

    if not file_path.endswith((".pdf", ".docx")):
        print("❌ Only PDF and DOCX files are supported.")
        exit()

    # -------- MAIN ANALYSIS --------
    try:
        result = analyze_resume(file_path, role)

        save_resume_analysis(user_id, file_path, result)

        print("Resume analysis saved successfully!")
        print(json.dumps(result, indent=4))

    except Exception as e:
        print(f"❌ Analysis failed: {e}")
        exit()

    # -------- SPEECH-BASED MOCK INTERVIEW --------
    speak("Starting your AI mock interview.")

    questions = generate_ai_questions(
        result["interview_context"]
    )

    for i, question in enumerate(questions[:3], 1):

        speak(f"Question {i}. {question}")

        answer = listen()

        # Fallback to typing if speech fails
        if not answer:
            speak("I could not understand your answer. Please type it.")
            answer = input("Your answer: ")

        feedback = evaluate_answer(question, answer)

        speak("Here is your feedback.")
        print(feedback)
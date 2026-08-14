'''import json
from analyzer import analyze_resume
from database import init_db, save_resume_analysis

# Create tables if they do not exist
init_db()

user_id = 1
file_path = "Resume.docx"
role = "AI Engineer"

# Run analysis
result = analyze_resume(file_path, role)

# Save analysis
save_resume_analysis(user_id, file_path, result)

# Display result
print(json.dumps(result, indent=4))'''
import json
import os
from analyzer import analyze_resume
from database import init_db, save_resume_analysis

# Initialize database
init_db()

# Main execution
if __name__ == "__main__":
    user_id = 1
    file_path = "Resume.docx"
    role = "AI Engineer"

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
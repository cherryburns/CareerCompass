import json
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
print(json.dumps(result, indent=4))
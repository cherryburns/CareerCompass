import sqlite3

def init_db():
    conn = sqlite3.connect("career_compass.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            phone_number TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resumes (
    resume_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    file_name TEXT,
    target_role TEXT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ats_score INTEGER,
    matched_skills TEXT,
    missing_skills TEXT,
    feedback TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_sessions (
            session_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            current_step TEXT,
            last_saved TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized perfectly!")

# FUNCTION 1: Add a new user safely
def register_user(username, phone_number, password_hash):
    try:
        conn = sqlite3.connect("career_compass.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, phone_number, password_hash) VALUES (?, ?, ?)",
            (username, phone_number, password_hash)
        )
        conn.commit()
        conn.close()
        return True, "User registered successfully!"
    except sqlite3.IntegrityError:
        return False, "Error: This phone number is already registered!"

# FUNCTION 2: Save the resume analysis score
import json

def save_resume_analysis(user_id, file_name, analysis):
    conn = sqlite3.connect("career_compass.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO resumes (
            user_id,
            file_name,
            target_role,
            ats_score,
            matched_skills,
            missing_skills,
            feedback
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        file_name,
        analysis["target_role"],
        analysis["score"],
        json.dumps(analysis["matched_skills"]),
        json.dumps(analysis["missing_skills"]),
        json.dumps(analysis["feedback"])
    ))

    conn.commit()
    conn.close()

    print("Resume analysis saved successfully!")

if __name__ == "__main__":
    init_db()

import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# ---------------- GEMINI SETUP ----------------
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- TEXT TO SPEECH ----------------
engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(text):
    print(f"\n🤖 {text}\n")
    engine.say(text)
    engine.runAndWait()

# ---------------- SPEECH TO TEXT ----------------
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""

# ---------------- QUESTION GENERATION ----------------
def generate_ai_questions(context):
    prompt = f"""
You are a technical interviewer.

Candidate target role: {context['role']}

Candidate skills:
{', '.join(context['skills']) if context['skills'] else 'No major skills detected'}

Missing skills:
{', '.join(context['focus_areas']) if context['focus_areas'] else 'None'}

Generate exactly 3 personalized technical interview questions.
Return only the questions as separate lines.
"""

    response = model.generate_content(prompt)
    return [q.strip() for q in response.text.split("\n") if q.strip()]

# ---------------- ANSWER EVALUATION ----------------
def evaluate_answer(question, answer):
    prompt = f"""
Question: {question}

Candidate Answer: {answer}

Evaluate the answer for a technical interview.

Provide:
- Score out of 5
- One strength
- One improvement suggestion
"""

    response = model.generate_content(prompt)
    return response.text
from PyPDF2 import PdfReader
from docx import Document

def extract_text(file_path):
    try:
        if file_path.endswith(".pdf"):
            reader = PdfReader(file_path)
            text = ""

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            return text.strip()

        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            return "\n".join([p.text for p in doc.paragraphs]).strip()

        else:
            raise ValueError("Only PDF and DOCX files are supported.")

    except Exception as e:
        return f"Error reading file: {str(e)}"
import re
from PyPDF2 import PdfReader

def parse_resume(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() + " "

    print("=== Extracted Text Preview ===")
    print(text[:1000])  # Debug preview in terminal

    # Clean and normalize
    text = text.lower()

    # ✅ Define skill keywords
    skill_keywords = [
        "c++", "java", "python", "r", "html", "css", "javascript", "bootstrap", "react",
        "spring boot", "mysql", "power bi", "tkinter", "nlp", "java swing",
        "time management", "critical thinking", "resilience", "persistence"
    ]

    # ✅ Match skills present in text
    extracted_skills = [skill for skill in skill_keywords if skill in text]

    print("=== Extracted Skills ===")
    print(extracted_skills)

    return extracted_skills

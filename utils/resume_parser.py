import re
import spacy
import PyPDF2

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + " "
    return text

def extract_skills(text):
    skills = [
        "python", "java", "c++", "sql", "html", "css", "javascript",
        "react", "node", "django", "flask", "machine learning",
        "deep learning", "data analysis", "excel", "communication"
    ]
    found = [skill for skill in skills if skill.lower() in text.lower()]
    return list(set(found))

def extract_education(text):
    edu_keywords = ["bca", "mca", "b.tech", "m.tech", "b.sc", "m.sc", "mba", "phd"]
    edu_found = [e for e in edu_keywords if e.lower() in text.lower()]
    return list(set(edu_found))

def extract_experience(text):
    exp_pattern = r"(\d+)\s*(?:years|year|yrs|yr)\s*(?:of)?\s*(?:experience)?"
    matches = re.findall(exp_pattern, text.lower())
    if matches:
        return f"{max([int(m) for m in matches])} years"
    else:
        return "Not specified"

def extract_projects(text):
    doc = nlp(text)
    projects = []
    for sent in doc.sents:
        if any(word in sent.text.lower() for word in ["project", "developed", "built", "created", "designed"]):
            projects.append(sent.text.strip())
    return projects[:3]  # return top 3

def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    return {
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
        "projects": extract_projects(text)
    }

if __name__ == "__main__":
    path = "data/resumes/finalcv.pdf"  # update this path as needed
    details = parse_resume(path)
    print(details)

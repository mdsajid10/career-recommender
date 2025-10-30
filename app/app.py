import streamlit as st
import pickle
import os
import sys
import tempfile

# ✅ Add project root to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.resume_parser import parse_resume


# Load model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "career_model.pkl")

vectorizer_path = os.path.join(os.path.dirname(__file__), "..","models","vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="AI Career Recommender", page_icon="🎯")
st.title("AI Career Recommender")
st.write("Upload your resume to get career insights and recommendations based on your profile!")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        resume_path = tmp_file.name

    # Parse the resume
    resume_data = parse_resume(resume_path)
    
    st.subheader("📄 Extracted Information")
    st.write("**Skills:**", ", ".join(resume_data["skills"]))
    st.write("**Education:**", ", ".join(resume_data["education"]))
    st.write("**Experience:**", ", ".join(resume_data["experience"]))
    st.write("**Projects:**", ", ".join(resume_data["projects"]))

    # Prepare text for ML model
    combined_text = " ".join(resume_data["skills"] + resume_data["education"])
    X_vectorized = vectorizer.transform([combined_text])
    prediction = model.predict(X_vectorized)[0]

    st.subheader("🎯 Career Recommendation")
    st.success(f"Based on your resume, you could explore a career as a **{prediction}**.")

import streamlit as st
import pandas as pd
import os, sys, pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.resume_parser import parse_resume
from utils.career_recommender import recommend_career

model_path = os.path.join(os.path.dirname(__file__), "..", "models", "career_model.pkl")
vectorizer_path = os.path.join(os.path.dirname(__file__), "..", "models", "vectorizer.pkl")

st.set_page_config(page_title="AI Career Recommender", page_icon="🎓", layout="wide")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("### 👨‍💻 Developer")
    st.markdown("**Md Sajid Salim**  \nMCA, Lovely Professional University (2024–26)  \n📍 Phugwala, Punjab, India")
    st.divider()
    st.markdown("### 📘 About Project")
    st.write("This AI-powered system analyzes your resume to extract key skills, understands your personality and interests, and recommends the most suitable career paths using NLP and Machine Learning.")
    st.markdown("---")
    st.caption("Built with ❤️ using Python, Streamlit & Scikit-learn")

# Title
st.markdown("<h1 style='text-align:center;'>🎓 AI Career Recommender System</h1>", unsafe_allow_html=True)
st.write("Upload your resume and answer a few questions to receive AI-based career guidance tailored to your skills and interests!")

uploaded_file = st.file_uploader("📂 Upload your resume (PDF)", type=["pdf"])
skills = None

col1, col2 = st.columns(2)
with col1:
    personality = st.selectbox("🧠 Select your personality type", ["Analytical", "Creative", "Leader", "Supportive"])
with col2:
    interests = st.multiselect("💡 Select your areas of interest", ["Coding", "Data", "Design", "Management", "Teaching", "Research"])

if uploaded_file is not None:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    skills = parse_resume("temp_resume.pdf")

    st.markdown("## 🧩 Extracted Skills")

    if skills:
        if isinstance(skills, dict):
            for category, items in skills.items():
                st.markdown(f"### {category}")
                if isinstance(items, list):
                    st.markdown(
                        "<div style='display:flex; flex-wrap:wrap; gap:8px;'>"
                        + "".join(
                            [f"<span style='background-color:#262730; color:#00ADB5; padding:8px 12px; border-radius:20px; font-size:14px;'>{item}</span>"
                             for item in items]
                        )
                        + "</div>",
                        unsafe_allow_html=True,
                    )
                else:
                    st.write(items)
        elif isinstance(skills, list):
            st.markdown(
                "<div style='display:flex; flex-wrap:wrap; gap:8px;'>"
                + "".join(
                    [f"<span style='background-color:#262730; color:#00ADB5; padding:8px 12px; border-radius:20px; font-size:14px;'>{item}</span>"
                     for item in skills]
                )
                + "</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div style='display:flex; flex-wrap:wrap; gap:8px;'>"
                + "".join(
                    [f"<span style='background-color:#262730; color:#00ADB5; padding:8px 12px; border-radius:20px; font-size:14px;'>{item.strip()}</span>"
                     for item in skills.split(",")]
                )
                + "</div>",
                unsafe_allow_html=True,
            )
    else:
        st.warning("⚠️ No skills could be extracted. Try another resume or check parser logic.")

    # ✅ Recommendation Section
    if not skills:
        skills = []

    recommended = recommend_career(skills, personality, interests)
    st.markdown("## 🏆 Recommended Careers")

    if isinstance(recommended, list):
        for i, career in enumerate(recommended, 1):
            st.markdown(
                f"<div style='background-color:#262730; color:white; padding:12px; border-radius:10px; margin-bottom:8px;'>{i}. {career}</div>",
                unsafe_allow_html=True
            )
    else:
        st.info("💡 " + str(recommended))

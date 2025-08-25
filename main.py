from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()



class CareerRequest(BaseModel):
    skills: list[str]
    interests: list[str]

# Simple dataset of careers
career_data = [
    {
        "career": "Data Scientist",
        "skills": ["python", "sql", "machine learning", "statistics"],
        "interests": ["data analysis", "ai", "problem solving"]
    },
    {
        "career": "Web Developer",
        "skills": ["html", "css", "javascript", "python"],
        "interests": ["web development", "design", "frontend"]
    },
    {
        "career": "Database Administrator",
        "skills": ["sql", "database", "backup", "optimization"],
        "interests": ["data management", "backend"]
    },
    {
        "career": "AI Engineer",
        "skills": ["python", "deep learning", "pytorch", "tensorflow"],
        "interests": ["ai", "neural networks", "automation"]
    },
    {
        "career": "Software Engineer",
        "skills": ["java", "python", "c++", "algorithms"],
        "interests": ["software development", "problem solving", "team projects"]
    },
    {
        "career": "Mobile App Developer",
        "skills": ["java", "kotlin", "swift", "flutter"],
        "interests": ["mobile apps", "user experience", "design"]
    },
    {
        "career": "Cloud Engineer",
        "skills": ["aws", "azure", "docker", "kubernetes"],
        "interests": ["cloud computing", "scalability", "automation"]
    },
    {
        "career": "Cybersecurity Analyst",
        "skills": ["network security", "firewalls", "linux", "cryptography"],
        "interests": ["cybersecurity", "ethical hacking", "risk management"]
    },
    {
        "career": "DevOps Engineer",
        "skills": ["linux", "docker", "kubernetes", "ci/cd"],
        "interests": ["automation", "system reliability", "cloud infrastructure"]
    },
    {
        "career": "Business Analyst",
        "skills": ["excel", "sql", "communication", "documentation"],
        "interests": ["business strategy", "data analysis", "requirements gathering"]
    },
    {
        "career": "UI/UX Designer",
        "skills": ["figma", "adobe xd", "wireframing", "prototyping"],
        "interests": ["design", "user experience", "visual creativity"]
    },
    {
        "career": "Machine Learning Engineer",
        "skills": ["python", "scikit-learn", "pandas", "tensorflow"],
        "interests": ["ai", "automation", "mathematics"]
    },
    {
        "career": "Game Developer",
        "skills": ["c#", "unity", "c++", "graphics programming"],
        "interests": ["gaming", "creativity", "animation"]
    },
    {
        "career": "Network Engineer",
        "skills": ["tcp/ip", "routing", "switching", "network security"],
        "interests": ["networking", "infrastructure", "cybersecurity"]
    },
    {
        "career": "Digital Marketer",
        "skills": ["seo", "content writing", "social media", "google ads"],
        "interests": ["marketing", "branding", "analytics"]
    },
    {
        "career": "Product Manager",
        "skills": ["roadmap planning", "communication", "analytics", "leadership"],
        "interests": ["innovation", "teamwork", "business strategy"]
    },
    {
        "career": "Data Engineer",
        "skills": ["python", "hadoop", "spark", "sql"],
        "interests": ["data pipelines", "big data", "scalability"]
    },
    {
        "career": "Research Scientist",
        "skills": ["mathematics", "python", "experimentation", "data analysis"],
        "interests": ["innovation", "scientific research", "exploration"]
    },
    {
        "career": "Teacher / Educator",
        "skills": ["communication", "presentation", "organization", "subject expertise"],
        "interests": ["teaching", "guiding students", "public speaking"]
    },
    {
        "career": "Content Writer",
        "skills": ["writing", "creativity", "storytelling", "seo"],
        "interests": ["blogging", "literature", "storytelling"]
    }
]

from pydantic import BaseModel

class CareerRequest(BaseModel):
    skills: list[str]
    interests: list[str]


@app.get("/")
def home():
    return {"message": "Hello, Career Recommender!"}

@app.post("/recommend")
def recommend_career(request: CareerRequest):
    recommendations = []

    # Normalize user input
    user_skills = [s.strip().lower() for s in request.skills]
    user_interests = [i.strip().lower() for i in request.interests]

    for career in career_data:
        # Normalize dataset too
        career_skills = [s.strip().lower() for s in career["skills"]]
        career_interests = [i.strip().lower() for i in career["interests"]]

        # Partial matching: count if any skill/interest contains substring
        matched_skills = sum(any(us in cs or cs in us for cs in career_skills) for us in user_skills)
        matched_interests = sum(any(ui in ci or ci in ui for ci in career_interests) for ui in user_interests)

        score = (matched_skills * 2) + (matched_interests * 1)

        if score > 0:
            recommendations.append({
                "career": career["career"],
                "matched_skills": matched_skills,
                "matched_interests": matched_interests,
                "score": score
            })

    recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)
    return {"recommendations": recommendations}

def recommend_career(skills):
    career_map = {
        "python": "Data Scientist / AI Engineer",
        "machine learning": "Data Scientist",
        "deep learning": "AI Engineer",
        "excel": "Business Analyst",
        "powerbi": "Business Analyst",
        "sql": "Database Administrator",
        "aws": "Cloud Engineer",
        "docker": "DevOps Engineer",
        "react": "Frontend Developer",
        "javascript": "Full Stack Developer",
        "spring": "Java Backend Developer",
        "statistics": "Research Analyst",
        "communication": "HR / Manager",
        "leadership": "Team Lead / Project Manager"
    }

    recommendations = set()
    for skill in skills:
        skill_lower = skill.lower()
        if skill_lower in career_map:
            recommendations.add(career_map[skill_lower])
    
    return list(recommendations)

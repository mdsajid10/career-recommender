def recommend_career(skills, personality, interests):
    base_careers = {
        "python": "Data Scientist",
        "react": "Frontend Developer",
        "sql": "Database Engineer",
        "excel": "Business Analyst",
        "aws": "Cloud Engineer",
        "management": "Project Manager"
    }

    recommendations = {}

    # Skill-based weighting
    for skill in skills:
        for key, job in base_careers.items():
            if key.lower() in skill.lower():
                recommendations[job] = recommendations.get(job, 0) + 0.6

    # Personality influence
    if personality.lower() in ["leader", "supportive"]:
        recommendations["Project Manager"] = recommendations.get("Project Manager", 0) + 0.2
    elif personality.lower() in ["analytical"]:
        recommendations["Data Scientist"] = recommendations.get("Data Scientist", 0) + 0.2
    elif personality.lower() in ["creative"]:
        recommendations["Frontend Developer"] = recommendations.get("Frontend Developer", 0) + 0.2

    # Interest influence
    for interest in interests:
        if interest.lower() in ["coding", "data"]:
            recommendations["Data Scientist"] = recommendations.get("Data Scientist", 0) + 0.2
        if interest.lower() == "design":
            recommendations["Frontend Developer"] = recommendations.get("Frontend Developer", 0) + 0.2
        if interest.lower() == "management":
            recommendations["Project Manager"] = recommendations.get("Project Manager", 0) + 0.2

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [career for career, score in sorted_recommendations]

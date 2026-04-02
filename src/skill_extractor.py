
SKILLS_DB = {
    # Programming
    "python", "java", "c++", "c#", "javascript",

    # Data / ML
    "machine learning", "deep learning", "nlp",
    "data analysis", "data science",

    # Libraries
    "pandas", "numpy", "scikit-learn",
    "tensorflow", "keras",

    # Tools
    "sql", "excel", "tableau", "powerbi",

    # Cloud / DevOps
    "aws", "azure", "docker", "kubernetes"
}

def extract_skills(text):
    found_skills = set()

    for skill in SKILLS_DB:
        if " " in skill and skill in text:
            found_skills.add(skill)

    words = text.split()

    for word in words:
        if word in SKILLS_DB:
            found_skills.add(word)

    return list(found_skills)
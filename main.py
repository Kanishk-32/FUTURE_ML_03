from src.data_loader import load_resumes, load_job_descriptions
from src.preprocess import clean_text
from src.skill_extractor import extract_skills


# =========================
# LOAD RESUMES (ONLY IT)
# =========================
print("\nLoading resumes...\n")

resumes = load_resumes("data/INFORMATION-TECHNOLOGY", limit=5)


# =========================
# LOAD JOB DESCRIPTIONS
# =========================
print("Loading job descriptions...\n")

job_df = load_job_descriptions("data/job_descriptions.csv")

# 🔥 Normalize column names (IMPORTANT FIX)
job_df.columns = job_df.columns.str.lower().str.strip()

# Limit dataset size (avoid 1.5GB overload)
job_df = job_df.head(1000)


# =========================
# FILTER RELEVANT JOBS (IT DOMAIN)
# =========================
job_df = job_df[
    job_df['job title'].str.contains(
        "data|engineer|developer|machine learning|software",
        case=False,
        na=False
    )
]

print("\nFiltered Job Titles:\n")
print(job_df['job title'].head())


# =========================
# SELECT ONE JOB
# =========================
job_text = job_df.iloc[0]['job description']

# Clean job description
job_text_clean = clean_text(job_text)

# Extract job skills
job_skills = extract_skills(job_text_clean)


# =========================
# PRINT JOB INFO
# =========================
print("\n=== SELECTED JOB ===\n")

print("Job Description (cleaned preview):\n")
print(job_text_clean[:300])

print("\nJob Skills:\n")
print(job_skills)


# =========================
# PROCESS RESUMES
# =========================
print("\n=== RESUME SKILL EXTRACTION ===\n")

for r in resumes:
    cleaned = clean_text(r["text"])
    skills = extract_skills(cleaned)

    print("=" * 50)
    print(f"File: {r['file_name']}")
    print(f"Category: {r['category']}")

    print("\nExtracted Skills:")
    print(skills)
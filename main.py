from src.data_loader import load_resumes, load_job_descriptions

resumes = load_resumes("data", limit=10)

job_df = load_job_descriptions("data/job_descriptions.csv")

print("\n=== JOB DESCRIPTIONS SAMPLE ===\n")
print(job_df.head())


print("\n=== RESUMES SAMPLE ===\n")

for r in resumes:
    print("=" * 50)
    print(f"File: {r['file_name']}")
    print(f"Category: {r['category']}")
    print(r["text"][:300])
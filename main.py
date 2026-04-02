from src.data_loader import load_resumes, load_job_descriptions
from src.preprocess import clean_text

print("\nLoading resumes...")
resumes = load_resumes("data", limit=5)

print("Loading job descriptions...")
job_df = load_job_descriptions("data/job_descriptions.csv")


print("\n=== JOB DESCRIPTIONS SAMPLE ===\n")

if job_df is not None:
    print(job_df.head())
else:
    print("No job data loaded.")


print("\n=== CLEANED RESUMES ===\n")

for r in resumes:
    cleaned = clean_text(r["text"])

    print("=" * 50)
    print(f"File: {r['file_name']}")
    print(f"Category: {r['category']}")
    print("\nCLEANED TEXT:\n")
    print(cleaned[:300])  
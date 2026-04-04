"""Quick audit: what skills do our resumes actually contain?"""
import sys
sys.path.insert(0, ".")
from src.data_loader import load_resumes
from src.preprocess import clean_text
from src.skill_extractor import extract_skills

resumes = load_resumes("data/INFORMATION-TECHNOLOGY", limit=30)
all_skills = set()
for r in resumes:
    c = clean_text(r["text"])
    s = extract_skills(c)
    all_skills.update(s)
    print(f"{r['file_name']}: {s}")

print(f"\nAll detected skills across {len(resumes)} resumes: {sorted(all_skills)}")
print(f"Total unique skills found: {len(all_skills)}")

# Also look for common tech terms that our extractor MISSES
import re
common_tech = [
    "oracle", "sap", "jira", "agile", "scrum", "rest", "api",
    "selenium", "jenkins", "angular", "vue", "hadoop", "tableau",
    "power bi", "powerbi", "sharepoint", "servicenow", "networking",
    "cisco", "vmware", "windows server", "active directory",
    "php", "perl", "ruby", "c ", "xml", "json", "soap",
    "hibernate", "maven", "gradle", ".net", "asp.net",
    "machine learning", "data analysis", "project management",
    "networking", "troubleshooting", "technical support",
]
print("\n--- Terms in resumes but NOT in our skill DB ---")
for r in resumes[:10]:
    text = r["text"].lower()
    found_extra = [t for t in common_tech if t in text and t not in all_skills]
    if found_extra:
        print(f"  {r['file_name']}: {found_extra}")

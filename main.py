"""
main.py
-------
Entry point for the AI-powered resume ranking pipeline.

Usage
-----
    python main.py

Adjust the constants in the CONFIG section below to point at your data.
"""

from __future__ import annotations

import logging
import sys

from src.data_loader import load_resumes, load_job_descriptions
from src.preprocess import clean_text
from src.skill_extractor import extract_skills
from src.similarity import compute_similarity
from src.ranker import rank_candidates

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
RESUME_FOLDER = "data/INFORMATION-TECHNOLOGY"
JOB_DESC_CSV = "data/job_descriptions.csv"
RESUME_LIMIT = 120
JOB_TITLE_PATTERN = r"data|engineer|developer|machine learning|software"
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)


def _separator(title: str = "", width: int = 60) -> None:
    if title:
        side = (width - len(title) - 2) // 2
        print(f"\n{'=' * side} {title} {'=' * side}")
    else:
        print("=" * width)


def main() -> int:
    # ------------------------------------------------------------------
    # 1. Load resumes
    # ------------------------------------------------------------------
    logger.info("Loading resumes …")
    resumes = load_resumes(RESUME_FOLDER, limit=RESUME_LIMIT)

    if not resumes:
        logger.error("No resumes loaded.  Check RESUME_FOLDER path and PDF files.")
        return 1

    logger.info(f"Loaded {len(resumes)} resume(s).")

    # ------------------------------------------------------------------
    # 2. Load job descriptions
    # ------------------------------------------------------------------
    logger.info("Loading job descriptions …")
    job_df = load_job_descriptions(JOB_DESC_CSV)

    if job_df is None or job_df.empty:
        logger.error("Job descriptions could not be loaded.")
        return 1

    # Filter to relevant roles
    job_df = job_df[
        job_df["job title"].str.contains(
            JOB_TITLE_PATTERN, case=False, na=False, regex=True
        )
    ].reset_index(drop=True)

    if job_df.empty:
        logger.error(f"No job titles matched pattern: {JOB_TITLE_PATTERN!r}")
        return 1

    _separator("SELECTED JOB")
    selected_job = job_df.iloc[0]
    print(f"Title      : {selected_job['job title']}")
    job_text_raw = selected_job["job description"]
    job_text_clean = clean_text(job_text_raw)
    job_skills = extract_skills(job_text_clean)

    print(f"Description: {job_text_clean[:300]} …")
    print(f"\nSkills ({len(job_skills)}): {', '.join(job_skills) or 'none detected'}")

    # ------------------------------------------------------------------
    # 3. Per-resume skill extraction preview
    # ------------------------------------------------------------------
    _separator("RESUME SKILL EXTRACTION")
    for resume in resumes:
        cleaned = clean_text(resume["text"])
        skills = extract_skills(cleaned)
        _separator()
        print(f"File     : {resume['file_name']}")
        print(f"Category : {resume['category']}")
        print(f"Skills   : {', '.join(skills) or 'none detected'}")

    # ------------------------------------------------------------------
    # 4. Rank candidates
    # ------------------------------------------------------------------
    logger.info("Ranking candidates …")
    ranked = rank_candidates(
        resumes=resumes,
        job_text=job_text_clean,
        job_skills=job_skills,
        clean_text=clean_text,
        extract_skills=extract_skills,
        compute_similarity=compute_similarity,
    )

    # ------------------------------------------------------------------
    # 5. Display results
    # ------------------------------------------------------------------
    _separator("RANKED CANDIDATES")
    for rank, candidate in enumerate(ranked, start=1):
        _separator()
        print(f"Rank  : #{rank}")
        print(f"File  : {candidate['file_name']}")
        print(f"Score : {candidate['score']:.2f} / 100")
        print(f"Matched ({len(candidate['matched_skills'])}): "
              f"{', '.join(candidate['matched_skills']) or '—'}")
        print(f"Missing ({len(candidate['missing_skills'])}): "
              f"{', '.join(candidate['missing_skills']) or '—'}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

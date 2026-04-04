"""
ranker.py
---------
Scores and ranks resume candidates against a job description.

Scoring formula (configurable via weights)
------------------------------------------
  final_score = (SKILL_WEIGHT × skill_match%) + (SIM_WEIGHT × similarity%)

Where:
  skill_match% = |matched_skills| / |job_skills| × 100
  similarity%  = cosine_similarity(resume, job) × 100
"""

from __future__ import annotations

from typing import Callable

# Default blend weights (must sum to 1.0).
SKILL_WEIGHT: float = 0.7
SIM_WEIGHT: float = 0.3


def calculate_skill_match(
    resume_skills: list[str],
    job_skills: list[str],
) -> float:
    """
    Return the fraction of *job_skills* that appear in *resume_skills*.

    Returns 0.0 when *job_skills* is empty.
    """
    if not job_skills:
        return 0.0
    matched = set(resume_skills) & set(job_skills)
    return len(matched) / len(job_skills)


def rank_candidates(
    resumes: list[dict],
    job_text: str,
    job_skills: list[str],
    clean_text: Callable[[str], str],
    extract_skills: Callable[[str], list[str]],
    compute_similarity: Callable[[str, str], float],
    skill_weight: float = SKILL_WEIGHT,
    sim_weight: float = SIM_WEIGHT,
) -> list[dict]:
    """
    Score each resume and return them sorted by descending *score*.

    Parameters
    ----------
    resumes:
        List of resume dicts (must have at least ``file_name``, ``category``,
        and ``text`` keys).
    job_text:
        Cleaned job-description text used for similarity comparison.
    job_skills:
        Skills extracted from the job description.
    clean_text:
        Preprocessing function ``(str) -> str``.
    extract_skills:
        Skill extraction function ``(str) -> list[str]``.
    compute_similarity:
        Similarity function ``(resume_text, job_text) -> float`` in [0, 1].
    skill_weight:
        Weight for the skill-match component (default 0.7).
    sim_weight:
        Weight for the similarity component (default 0.3).

    Returns
    -------
    list[dict]
        Each element contains:
        ``file_name``, ``category``, ``score`` (0–100, 2 d.p.),
        ``matched_skills``, ``missing_skills``.
    """
    if abs(skill_weight + sim_weight - 1.0) > 1e-6:
        raise ValueError(
            f"skill_weight + sim_weight must equal 1.0, "
            f"got {skill_weight + sim_weight}"
        )

    ranked: list[dict] = []

    for resume in resumes:
        cleaned = clean_text(resume["text"])
        resume_skills = extract_skills(cleaned)

        skill_score = calculate_skill_match(resume_skills, job_skills)  # [0,1]
        sim_score = compute_similarity(cleaned, job_text)               # [0,1]

        final_score = (skill_weight * skill_score + sim_weight * sim_score) * 100

        matched_skills = sorted(set(resume_skills) & set(job_skills))
        missing_skills = sorted(set(job_skills) - set(resume_skills))

        ranked.append({
            "file_name": resume["file_name"],
            "category": resume["category"],
            "score": round(final_score, 2),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked

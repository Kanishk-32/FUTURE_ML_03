"""
skill_extractor.py
------------------
Extracts technology / domain skills from cleaned text.

The extraction order is:
  1. Multi-word skills  – matched as substrings (order: longest first to
     avoid partial matches, e.g. "deep learning" before "learning").
  2. Single-word skills – matched against individual tokens.
"""

from __future__ import annotations

# Canonical skill list.  Add / remove entries here to update the vocabulary.
SKILLS_DB: frozenset[str] = frozenset({
    # Languages
    "python", "java", "javascript", "typescript",
    "c++", "c#", "r", "go", "scala", "kotlin", "swift", "rust",
    # Web / backend frameworks
    "node.js", "react.js", "django", "flask", "fastapi", "spring",
    "html", "css",
    # ML / AI
    "machine learning", "deep learning", "nlp",
    "computer vision", "reinforcement learning",
    # ML libraries
    "scikit-learn", "tensorflow", "keras", "pytorch",
    "pandas", "numpy", "scipy", "matplotlib",
    # Data & BI
    "data analysis", "data science", "data engineering",
    "sql", "mysql", "postgresql", "mongodb",
    "excel", "tableau", "powerbi",
    # Cloud & DevOps
    "aws", "azure", "gcp",
    "docker", "kubernetes", "terraform", "ci/cd",
    # Tools
    "git", "linux", "bash",
})

# Pre-compute sorted lists once at import time.
_MULTI_WORD: list[str] = sorted(
    (s for s in SKILLS_DB if " " in s), key=len, reverse=True
)
_SINGLE_WORD: frozenset[str] = frozenset(s for s in SKILLS_DB if " " not in s)


def extract_skills(text: str) -> list[str]:
    """
    Return a deduplicated, sorted list of skills found in *text*.

    Parameters
    ----------
    text:
        Cleaned (lowercased) text produced by ``preprocess.clean_text``.
    """
    if not isinstance(text, str) or not text.strip():
        return []

    found: set[str] = set()

    # --- Multi-word skills ---
    for skill in _MULTI_WORD:
        if skill in text:
            found.add(skill)

    # --- Single-word skills (token-level matching avoids false positives) ---
    tokens = set(text.split())
    found.update(tokens & _SINGLE_WORD)

    return sorted(found)

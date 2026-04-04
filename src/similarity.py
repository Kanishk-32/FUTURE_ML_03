"""
similarity.py
-------------
Computes text-similarity scores between a resume and a job description.

Uses TF-IDF cosine similarity as the default strategy.  The vectoriser is
re-fitted per call to keep the module stateless and safe for concurrent use.
"""

from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as _cosine_similarity


def compute_similarity(resume_text: str, job_text: str) -> float:
    """
    Return a cosine similarity score in **[0, 1]** between *resume_text* and
    *job_text* using TF-IDF vectors.

    Parameters
    ----------
    resume_text:
        Cleaned resume text.
    job_text:
        Cleaned job description text.

    Returns
    -------
    float
        0.0 if either input is empty or only whitespace; otherwise the
        cosine similarity in [0, 1].
    """
    if not resume_text.strip() or not job_text.strip():
        return 0.0

    vectorizer = TfidfVectorizer()
    try:
        vectors = vectorizer.fit_transform([resume_text, job_text])
    except ValueError:
        # Raised when the vocabulary is empty after TF-IDF filtering.
        return 0.0

    score: float = _cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return float(score)

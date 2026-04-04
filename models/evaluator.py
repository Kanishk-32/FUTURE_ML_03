"""
models/evaluator.py
-------------------
Calculates programmatic proxy accuracy metrics for the ranking pipeline.
Because there is no human ground-truth labeled dataset for newly uploaded resumes,
we use heuristic confidence checks:
1. Precision@K (How many top candidates passed a minimum baseline fit threshold?)
2. Skill Extraction Confidence (Are the skills extracted standard or noisy?)
3. Score Distribution Health (Did the model successfully create a high variance margin?)
"""

from __future__ import annotations
import numpy as np

class PipelineEvaluator:
    def __init__(self, ranked_candidates: list[dict], required_skills: list[str]):
        """
        Initialize with the final output of the ranker and the target skills.
        """
        self.candidates = ranked_candidates
        self.job_skills = set(required_skills)
        self.total_candidates = len(ranked_candidates)
        
    def calculate_precision_at_k(self, k: int = 5, score_threshold: float = 20.0) -> float:
        """
        Precision@K checks the Top K candidates. 
        If a candidate's score is > score_threshold, they are deemed a 'True Positive' proxy.
        Returns percentage 0.0 to 100.0.
        """
        if not self.candidates:
            return 0.0
            
        top_k = self.candidates[:k]
        true_positives = sum(1 for c in top_k if c["score"] >= score_threshold)
        
        return (true_positives / len(top_k)) * 100.0

    def calculate_skill_confidence(self) -> float:
        """
        Checks the average skill coverage among the top 20% of candidates.
        If the 'best' candidates only have 5% of the required skills, model confidence is very low.
        Returns percentage 0.0 to 100.0.
        """
        if not self.candidates or not self.job_skills:
            return 0.0
            
        top_20_pct_count = max(1, int(self.total_candidates * 0.2))
        top_tier = self.candidates[:top_20_pct_count]
        
        coverage_rates = []
        for cand in top_tier:
            matched = len(cand.get("matched_skills", []))
            coverage = matched / len(self.job_skills)
            coverage_rates.append(coverage)
            
        avg_coverage = np.mean(coverage_rates)
        
        # We assume covering >50% of mandatory skills is a 100% confidence rating
        # So we scale it.
        confidence = min(1.0, avg_coverage * 2.0) * 100.0
        return float(confidence)

    def calculate_distribution_health(self) -> float:
        """
        A model that gives everyone a 30% is broken. 
        A healthy scoring distribution should have high standard deviation.
        Returns a normalized score (0-100) where SD > 10 is considered 100% healthy.
        """
        if self.total_candidates < 2:
            return 100.0
            
        scores = [c["score"] for c in self.candidates]
        std_dev = np.std(scores)
        
        # Standard deviation of 15 is excellent variance. (Scale: SD 15 -> 100%)
        health = min(1.0, std_dev / 15.0) * 100.0
        return float(health)
        
    def generate_report(self, k: int = 5) -> dict[str, float]:
        """Runs all heuristics and returns a summary report."""
        return {
            "precision_at_k": self.calculate_precision_at_k(k=k),
            "skill_confidence": self.calculate_skill_confidence(),
            "distribution_health": self.calculate_distribution_health()
        }

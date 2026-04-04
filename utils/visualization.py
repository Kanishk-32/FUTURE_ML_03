"""
visualization.py
----------------
Charts and visual helpers for resume screening results.

Used by both the CLI pipeline (main.py) and the Streamlit web app.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import matplotlib
matplotlib.use("Agg")                       # non-interactive backend (safe for servers)
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

if TYPE_CHECKING:
    from matplotlib.figure import Figure


# ── Colour palette ────────────────────────────────────────────
_PALETTE = {
    "primary":    "#6C63FF",
    "secondary":  "#FF6584",
    "accent":     "#43E97B",
    "bg_dark":    "#1E1E2F",
    "bg_card":    "#2A2A3D",
    "text_light": "#E0E0E0",
    "grid":       "#3A3A50",
}


def _apply_dark_style(ax: plt.Axes, fig: Figure) -> None:
    """Apply a consistent dark style to charts."""
    fig.patch.set_facecolor(_PALETTE["bg_dark"])
    ax.set_facecolor(_PALETTE["bg_card"])
    ax.tick_params(colors=_PALETTE["text_light"], labelsize=9)
    ax.xaxis.label.set_color(_PALETTE["text_light"])
    ax.yaxis.label.set_color(_PALETTE["text_light"])
    ax.title.set_color(_PALETTE["text_light"])
    for spine in ax.spines.values():
        spine.set_color(_PALETTE["grid"])


# ── Public API ────────────────────────────────────────────────

def score_bar_chart(
    ranked: list[dict],
    *,
    title: str = "Candidate Ranking",
    figsize: tuple[float, float] = (10, 5),
) -> Figure:
    """Horizontal bar chart of candidate scores (0-100)."""
    names = [c["file_name"].removesuffix(".pdf") for c in ranked]
    scores = [c["score"] for c in ranked]

    fig, ax = plt.subplots(figsize=figsize)
    _apply_dark_style(ax, fig)

    colours = [_PALETTE["primary"] if s >= 50 else _PALETTE["secondary"] for s in scores]
    bars = ax.barh(names, scores, color=colours, edgecolor="none", height=0.6)

    for bar, score in zip(bars, scores):
        ax.text(
            bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
            f"{score:.1f}", va="center", fontsize=9,
            color=_PALETTE["text_light"],
        )

    ax.set_xlim(0, 105)
    ax.xaxis.set_major_formatter(mtick.FormatStrFormatter("%.0f"))
    ax.set_xlabel("Score (0 – 100)")
    ax.set_title(title, fontsize=13, fontweight="bold", pad=12)
    ax.invert_yaxis()
    fig.tight_layout()
    return fig


def skill_match_chart(
    candidate: dict,
    job_skills: list[str],
    *,
    figsize: tuple[float, float] = (8, 5),
) -> Figure:
    """Show matched vs missing skills for a single candidate."""
    matched = set(candidate.get("matched_skills", []))
    skills = sorted(job_skills)
    colors = [_PALETTE["accent"] if s in matched else _PALETTE["secondary"] for s in skills]
    values = [1 if s in matched else 0 for s in skills]

    fig, ax = plt.subplots(figsize=figsize)
    _apply_dark_style(ax, fig)

    ax.barh(skills, values, color=colors, edgecolor="none", height=0.6)
    ax.set_xlim(-0.1, 1.5)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Missing", "Matched"])
    ax.set_title(
        f"Skill Match — {candidate.get('file_name', 'Unknown')}",
        fontsize=13, fontweight="bold", pad=12,
    )
    ax.invert_yaxis()

    # Legend patches
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=_PALETTE["accent"], label="Matched"),
        Patch(facecolor=_PALETTE["secondary"], label="Missing"),
    ]
    ax.legend(handles=legend_elements, loc="lower right",
              facecolor=_PALETTE["bg_card"], edgecolor=_PALETTE["grid"],
              labelcolor=_PALETTE["text_light"])

    fig.tight_layout()
    return fig


def radar_chart(
    candidates: list[dict],
    job_skills: list[str],
    *,
    max_candidates: int = 5,
    figsize: tuple[float, float] = (8, 8),
) -> Figure:
    """Radar (spider) chart comparing skill coverage of top candidates."""
    candidates = candidates[:max_candidates]
    if not job_skills or not candidates:
        fig, ax = plt.subplots(figsize=figsize)
        ax.text(0.5, 0.5, "Not enough data", ha="center", va="center", fontsize=14)
        return fig

    skills = sorted(job_skills)
    n = len(skills)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]  # close the polygon

    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(polar=True))
    fig.patch.set_facecolor(_PALETTE["bg_dark"])
    ax.set_facecolor(_PALETTE["bg_card"])

    cmap = plt.cm.get_cmap("Set2", max_candidates)

    for i, cand in enumerate(candidates):
        matched = set(cand.get("matched_skills", []))
        values = [1 if s in matched else 0 for s in skills]
        values += values[:1]
        colour = cmap(i)
        ax.plot(angles, values, linewidth=2, color=colour,
                label=cand["file_name"].removesuffix(".pdf"))
        ax.fill(angles, values, alpha=0.15, color=colour)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(skills, fontsize=8, color=_PALETTE["text_light"])
    ax.set_yticks([0, 0.5, 1])
    ax.set_yticklabels(["", "", ""], fontsize=1)
    ax.set_title("Skill Coverage Comparison", fontsize=13, fontweight="bold",
                 pad=20, color=_PALETTE["text_light"])
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1),
              facecolor=_PALETTE["bg_card"], edgecolor=_PALETTE["grid"],
              labelcolor=_PALETTE["text_light"], fontsize=8)
    ax.tick_params(colors=_PALETTE["grid"])
    ax.spines["polar"].set_color(_PALETTE["grid"])
    fig.tight_layout()
    return fig


def score_distribution_chart(
    ranked: list[dict],
    *,
    figsize: tuple[float, float] = (8, 4),
) -> Figure:
    """Histogram of candidate scores."""
    scores = [c["score"] for c in ranked]

    fig, ax = plt.subplots(figsize=figsize)
    _apply_dark_style(ax, fig)

    ax.hist(scores, bins=10, range=(0, 100), color=_PALETTE["primary"],
            edgecolor=_PALETTE["bg_dark"], alpha=0.85)
    ax.set_xlabel("Score")
    ax.set_ylabel("Count")
    ax.set_title("Score Distribution", fontsize=13, fontweight="bold", pad=12)
    fig.tight_layout()
    return fig

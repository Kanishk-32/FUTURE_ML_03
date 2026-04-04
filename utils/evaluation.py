"""
evaluation.py
-------------
Visual analytics tools for unsupervised model evaluation.
Generates heatmaps, scatter plots, and KDE charts.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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

def plot_cross_matrix_heatmap(df_matrix: pd.DataFrame, figsize=(10, 6)) -> Figure:
    """
    Plot a heatmap of resume scores across multiple job roles.
    df_matrix: DataFrame where rows are resume filenames, columns are Job Titles, 
               and values are scores.
    """
    fig, ax = plt.subplots(figsize=figsize)
    _apply_dark_style(ax, fig)
    
    # Custom diverging colormap suitable for dark mode
    cmap = sns.color_palette("mako", as_cmap=True)
    
    sns.heatmap(
        df_matrix, 
        cmap=cmap, 
        ax=ax, 
        annot=True, 
        fmt=".0f", 
        linewidths=.5,
        linecolor=_PALETTE["grid"],
        cbar_kws={'label': 'Total Score'}
    )
    
    ax.set_title("Job Role Differentiation Heatmap\n(Rows: Top Resumes, Cols: Diverse Job Roles)", 
                 pad=15, fontweight="bold", fontsize=13)
    ax.set_xlabel("Job Role")
    ax.set_ylabel("Resume File")
    
    # Colorbar label styling
    cbar = ax.collections[0].colorbar
    cbar.ax.yaxis.label.set_color(_PALETTE["text_light"])
    cbar.ax.tick_params(colors=_PALETTE["text_light"])
    
    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()
    return fig

def plot_feature_correlation(skill_scores: list[float], sim_scores: list[float], figsize=(8, 6)) -> Figure:
    """
    Scatter plot showing relation between raw TF-IDF similarity and Skill Match score.
    Demonstrates model feature interplay.
    """
    fig, ax = plt.subplots(figsize=figsize)
    _apply_dark_style(ax, fig)
    
    sns.scatterplot(
        x=sim_scores, 
        y=skill_scores, 
        ax=ax, 
        color=_PALETTE["accent"],
        s=80, 
        alpha=0.7, 
        edgecolor=_PALETTE["bg_dark"]
    )
    
    ax.set_title("Feature Correlation: TF-IDF vs Skill Match", pad=15, fontweight="bold", fontsize=13)
    ax.set_xlabel("TF-IDF Similarity Score (0 - 1.0)")
    ax.set_ylabel("Skill Match Score (0 - 1.0)")
    ax.set_xlim(-0.05, max(max(sim_scores) if sim_scores else 0 + 0.1, 1.05))
    ax.set_ylim(-0.05, max(max(skill_scores) if skill_scores else 0 + 0.1, 1.05))
    
    fig.tight_layout()
    return fig

def plot_score_kde(all_scores: list[float], figsize=(8, 5)) -> Figure:
    """
    Plot Kernel Density Estimation (KDE) to show score distribution curve.
    Shows the separation between top talent and poor matches.
    """
    fig, ax = plt.subplots(figsize=figsize)
    _apply_dark_style(ax, fig)
    
    if len(all_scores) < 2:
        ax.text(0.5, 0.5, "Not enough data for KDE", ha='center', va='center', color=_PALETTE["text_light"])
        return fig
        
    sns.kdeplot(
        all_scores, 
        ax=ax, 
        fill=True, 
        color=_PALETTE["primary"], 
        alpha=0.5, 
        linewidth=2
    )
    
    # Also add rugplot to show individual data points
    sns.rugplot(all_scores, ax=ax, color=_PALETTE["secondary"], height=0.05)
    
    ax.set_title("Density Curve: Quality Separation", pad=15, fontweight="bold", fontsize=13)
    ax.set_xlabel("Total Final Score (0 - 100)")
    ax.set_ylabel("Density")
    ax.set_xlim(0, 100)
    
    fig.tight_layout()
    return fig

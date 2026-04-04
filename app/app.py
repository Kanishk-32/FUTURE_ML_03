"""
app.py – Streamlit Web Interface for Resume Screening
------------------------------------------------------
Run:
    streamlit run app/app.py
"""

from __future__ import annotations

import sys
import os

# Ensure project root is on Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd

from src.data_loader import load_resumes, load_job_descriptions, extract_text_from_pdf
from src.preprocess import clean_text
from src.skill_extractor import extract_skills
from src.similarity import compute_similarity
from src.ranker import rank_candidates
from utils.visualization import (
    score_bar_chart,
    skill_match_chart,
    radar_chart,
    score_distribution_chart,
)

# ── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    /* Dark theme overrides */
    .main { background-color: #0E1117; }

    .stMetric {
        background: linear-gradient(135deg, #1E1E2F 0%, #2A2A3D 100%);
        border: 1px solid #3A3A50;
        border-radius: 12px;
        padding: 16px;
    }

    .candidate-card {
        background: linear-gradient(135deg, #1E1E2F 0%, #2A2A3D 100%);
        border: 1px solid #3A3A50;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
    }

    .skill-tag-matched {
        display: inline-block;
        background: linear-gradient(135deg, #43E97B 0%, #38F9D7 100%);
        color: #1E1E2F;
        padding: 4px 12px;
        border-radius: 20px;
        margin: 3px;
        font-size: 13px;
        font-weight: 600;
    }

    .skill-tag-missing {
        display: inline-block;
        background: linear-gradient(135deg, #FF6584 0%, #FF4B6E 100%);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        margin: 3px;
        font-size: 13px;
        font-weight: 600;
    }

    .score-badge {
        font-size: 28px;
        font-weight: 800;
        text-align: center;
    }

    .header-gradient {
        background: linear-gradient(90deg, #6C63FF, #FF6584, #43E97B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 800;
    }

    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
</style>
""", unsafe_allow_html=True)


# ── Helper Functions ──────────────────────────────────────────

@st.cache_data(show_spinner=False)
def load_job_data(csv_path: str) -> pd.DataFrame | None:
    """Load and cache job descriptions."""
    return load_job_descriptions(csv_path)


@st.cache_data(show_spinner=False)
def load_resume_data(folder: str, limit: int) -> list[dict]:
    """Load and cache resumes."""
    return load_resumes(folder, limit=limit)


def render_skill_tags(skills: list[str], css_class: str) -> str:
    """Render a list of skills as HTML tags."""
    return " ".join(f'<span class="{css_class}">{s}</span>' for s in skills)


def get_score_color(score: float) -> str:
    """Return a colour based on score."""
    if score >= 70:
        return "#43E97B"
    elif score >= 40:
        return "#FFD93D"
    else:
        return "#FF6584"


# ── Sidebar ───────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    st.markdown("---")

    mode = st.radio(
        "Job Description Source",
        ["Select from Dataset", "Paste Custom"],
        index=0,
    )

    st.markdown("---")
    st.markdown("### Resume Settings")

    resume_source = st.radio(
        "Resume Source",
        ["Load from Folder", "Upload PDFs"],
        index=0,
    )

    if resume_source == "Load from Folder":
        resume_folder = st.text_input(
            "Resume Folder",
            value="data/INFORMATION-TECHNOLOGY",
        )
        resume_limit = st.slider("Max Resumes to Load", 3, 50, 10)

    st.markdown("---")
    st.markdown("### Scoring Weights")
    skill_weight = st.slider(
        "Skill Match Weight", 0.0, 1.0, 0.7, 0.05,
        help="How much to weigh skill matching (remaining goes to text similarity)",
    )
    sim_weight = round(1.0 - skill_weight, 2)
    st.caption(f"Text Similarity Weight: **{sim_weight}**")

    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; color:#888; font-size:12px;'>"
        "AI Resume Screener v1.0<br>TF-IDF + Skill Matching"
        "</div>",
        unsafe_allow_html=True,
    )


# ── Main Content ──────────────────────────────────────────────

st.markdown('<p class="header-gradient">AI Resume Screener</p>', unsafe_allow_html=True)
st.markdown(
    "Rank candidates against job descriptions using **TF-IDF similarity** "
    "and **skill matching**."
)

# ── Step 1: Job Description ──────────────────────────────────

st.markdown("---")
st.markdown("### 📋 Job Description")

job_text_clean = ""
job_skills: list[str] = []
job_title = ""

if mode == "Select from Dataset":
    csv_path = "data/job_descriptions.csv"
    job_df = load_job_data(csv_path)

    if job_df is not None and not job_df.empty:
        # Build display options
        titles = job_df["job title"].tolist()
        selected_idx = st.selectbox(
            "Select a Job Posting",
            range(len(titles)),
            format_func=lambda i: f"{titles[i]}  —  {job_df.iloc[i].get('company', '')}",
        )

        selected_job = job_df.iloc[selected_idx]
        job_title = selected_job["job title"]
        job_text_raw = str(selected_job["job description"])

        with st.expander(f"📖 Full Description — {job_title}", expanded=False):
            st.markdown(job_text_raw)

        job_text_clean = clean_text(job_text_raw)
        job_skills = extract_skills(job_text_clean)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Job Title", job_title)
        with col2:
            st.metric("Skills Detected", len(job_skills))

        if job_skills:
            st.markdown(
                render_skill_tags(job_skills, "skill-tag-matched"),
                unsafe_allow_html=True,
            )
    else:
        st.error("Could not load job descriptions CSV. Check the file path.")
else:
    job_title = st.text_input("Job Title", "Software Engineer")
    job_text_raw = st.text_area(
        "Paste the full job description here",
        height=250,
        placeholder="We are looking for a Software Engineer with experience in...",
    )
    if job_text_raw.strip():
        job_text_clean = clean_text(job_text_raw)
        job_skills = extract_skills(job_text_clean)
        st.info(f"Detected **{len(job_skills)}** skills: {', '.join(job_skills) or 'none'}")


# ── Step 2: Load Resumes ──────────────────────────────────────

st.markdown("---")
st.markdown("### 📑 Resumes")

resumes: list[dict] = []

if resume_source == "Load from Folder":
    if st.button("🔄 Load Resumes", type="primary"):
        with st.spinner("Extracting text from PDF resumes..."):
            resumes = load_resume_data(resume_folder, resume_limit)
        if resumes:
            st.success(f"Loaded **{len(resumes)}** resumes from `{resume_folder}`")
        else:
            st.error(f"No resumes found in `{resume_folder}`. Check the path.")
        st.session_state["resumes"] = resumes

    # Persist across reruns
    if "resumes" in st.session_state:
        resumes = st.session_state["resumes"]
else:
    uploaded_files = st.file_uploader(
        "Upload PDF resumes",
        type=["pdf"],
        accept_multiple_files=True,
    )
    if uploaded_files:
        import tempfile

        resumes = []
        for uf in uploaded_files:
            # Write to temp file for pdfplumber
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp.write(uf.read())
                tmp_path = tmp.name

            text = extract_text_from_pdf(tmp_path)
            if text:
                resumes.append({
                    "file_name": uf.name,
                    "file_path": tmp_path,
                    "category": "Uploaded",
                    "text": text,
                })
            os.unlink(tmp_path)

        st.success(f"Processed **{len(resumes)}** uploaded resume(s)")
        st.session_state["resumes"] = resumes

    if "resumes" in st.session_state and not resumes:
        resumes = st.session_state.get("resumes", [])


# ── Step 3: Rank ──────────────────────────────────────────────

if resumes and job_text_clean:
    st.markdown("---")
    st.markdown("### 🏆 Ranking Results")

    with st.spinner("Ranking candidates..."):
        ranked = rank_candidates(
            resumes=resumes,
            job_text=job_text_clean,
            job_skills=job_skills,
            clean_text=clean_text,
            extract_skills=extract_skills,
            compute_similarity=compute_similarity,
            skill_weight=skill_weight,
            sim_weight=sim_weight,
        )

    if not ranked:
        st.warning("No candidates to rank.")
    else:
        # ── Summary Metrics ───────────────────────────────────
        mcol1, mcol2, mcol3, mcol4 = st.columns(4)
        mcol1.metric("Candidates", len(ranked))
        mcol2.metric("Top Score", f"{ranked[0]['score']:.1f}")
        avg_score = sum(c["score"] for c in ranked) / len(ranked)
        mcol3.metric("Avg Score", f"{avg_score:.1f}")
        mcol4.metric("Job Skills", len(job_skills))

        # ── Charts ────────────────────────────────────────────
        tab_chart, tab_radar, tab_dist = st.tabs(
            ["📊 Score Ranking", "🕸️ Skill Radar", "📈 Distribution"]
        )

        with tab_chart:
            fig = score_bar_chart(ranked, title=f"Candidates vs {job_title}")
            st.pyplot(fig)

        with tab_radar:
            fig = radar_chart(ranked, job_skills, max_candidates=5)
            st.pyplot(fig)

        with tab_dist:
            fig = score_distribution_chart(ranked)
            st.pyplot(fig)

        # ── Candidate Cards ───────────────────────────────────
        st.markdown("---")
        st.markdown("### 📋 Detailed Results")

        for rank, cand in enumerate(ranked, start=1):
            score_color = get_score_color(cand["score"])
            with st.expander(
                f"**#{rank}**  {cand['file_name']}  —  "
                f"Score: {cand['score']:.1f}/100",
                expanded=(rank <= 3),
            ):
                c1, c2 = st.columns([1, 3])

                with c1:
                    st.markdown(
                        f'<div class="score-badge" style="color: {score_color};">'
                        f'{cand["score"]:.1f}</div>'
                        f'<div style="text-align:center; color:#888;">out of 100</div>',
                        unsafe_allow_html=True,
                    )
                    st.caption(f"Category: {cand['category']}")

                with c2:
                    st.markdown("**Matched Skills:**")
                    if cand["matched_skills"]:
                        st.markdown(
                            render_skill_tags(cand["matched_skills"], "skill-tag-matched"),
                            unsafe_allow_html=True,
                        )
                    else:
                        st.caption("No skills matched")

                    st.markdown("**Missing Skills:**")
                    if cand["missing_skills"]:
                        st.markdown(
                            render_skill_tags(cand["missing_skills"], "skill-tag-missing"),
                            unsafe_allow_html=True,
                        )
                    else:
                        st.caption("All required skills matched!")

                # Skill match chart for this candidate
                fig = skill_match_chart(cand, job_skills)
                st.pyplot(fig)

        # ── Export ────────────────────────────────────────────
        st.markdown("---")
        results_df = pd.DataFrame([
            {
                "Rank": i + 1,
                "File": c["file_name"],
                "Category": c["category"],
                "Score": c["score"],
                "Matched Skills": ", ".join(c["matched_skills"]),
                "Missing Skills": ", ".join(c["missing_skills"]),
            }
            for i, c in enumerate(ranked)
        ])

        st.download_button(
            "📥 Download Results as CSV",
            data=results_df.to_csv(index=False),
            file_name="screening_results.csv",
            mime="text/csv",
        )

elif not resumes:
    st.info("👆 Load or upload resumes to begin screening.")
elif not job_text_clean:
    st.info("👆 Select or paste a job description to begin screening.")

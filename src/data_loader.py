import os
import logging
import pdfplumber
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = {".pdf"}


def extract_text_from_pdf(file_path: str) -> str:
    """Extract and return all text from a PDF file."""
    text_parts = []

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except Exception as e:
        logger.error(f"Failed to read {file_path}: {e}")

    return "\n".join(text_parts).strip()


def load_resumes(base_folder: str, limit: int = 20) -> list[dict]:
    """
    Walk base_folder recursively and load up to `limit` PDF resumes.

    Returns a list of dicts with keys:
        file_name  – original filename
        file_path  – absolute path
        category   – immediate parent folder name (treated as job role)
        text       – raw extracted text
    """
    if not os.path.isdir(base_folder):
        logger.error(f"Resume folder not found: {base_folder}")
        return []

    resumes = []

    for root, _dirs, files in os.walk(base_folder):
        for file in sorted(files):                        # deterministic order
            if len(resumes) >= limit:
                return resumes

            _, ext = os.path.splitext(file)
            if ext.lower() not in SUPPORTED_EXTENSIONS:
                continue

            file_path = os.path.join(root, file)
            text = extract_text_from_pdf(file_path)

            if text:
                resumes.append({
                    "file_name": file,
                    "file_path": file_path,
                    "category": os.path.basename(root),
                    "text": text,
                })
            else:
                logger.warning(f"Empty or unreadable resume skipped: {file}")

    return resumes


def load_job_descriptions(file_path: str) -> pd.DataFrame | None:
    """
    Load a CSV of job descriptions.

    Normalises column names to lowercase-stripped strings and drops rows
    where *all* values are NaN.  Returns None on failure.
    """
    if not os.path.isfile(file_path):
        logger.error(f"Job descriptions file not found: {file_path}")
        return None

    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.lower().str.strip()
        df.dropna(how="all", inplace=True)
        df.reset_index(drop=True, inplace=True)
        logger.info(f"Loaded {len(df)} job descriptions from {file_path}")
        return df
    except pd.errors.ParserError as e:
        logger.error(f"CSV parse error in {file_path}: {e}")
    except Exception as e:
        logger.error(f"Failed to load job descriptions: {e}")

    return None

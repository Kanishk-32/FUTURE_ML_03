import os
import pdfplumber
import pandas as pd

def extract_text_from_pdf(file_path):
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        print(f"[ERROR] Failed to read {file_path}: {e}")

    return text.strip()

def load_resumes(base_folder, limit=20):
    resumes = []
    count = 0

    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".pdf"):

                # Stop if limit reached
                if count >= limit:
                    return resumes

                file_path = os.path.join(root, file)

                text = extract_text_from_pdf(file_path)

                if text:
                    resumes.append({
                        "file_name": file,
                        "category": os.path.basename(root),  # folder = job role
                        "text": text
                    })
                    count += 1
                else:
                    print(f"[WARNING] Empty resume: {file}")

    return resumes


def load_job_descriptions(file_path):
    try:
        df = pd.read_csv(file_path)

        # Clean column names
        df.columns = [col.lower().strip() for col in df.columns]

        # Optional: drop empty rows
        df = df.dropna()

        return df

    except Exception as e:
        print(f"[ERROR] Failed to load job descriptions: {e}")
        return None
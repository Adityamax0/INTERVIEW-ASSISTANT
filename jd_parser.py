"""
jd_parser.py

Takes an HR-uploaded job description file (PDF or DOCX only), extracts
its raw text, then asks the LLM to structure it into a fixed JSON shape
so brain.py can compare it against the candidate profile.

pip install pdfplumber python-docx
"""

import json
import os

import pdfplumber
from docx import Document
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

ALLOWED_EXTENSIONS = {".pdf", ".docx"}

JD_JSON_SCHEMA_PROMPT = """
You are extracting structured data from a job description. Return
ONLY valid JSON, no preamble, no markdown fences, matching exactly
this shape:

{
  "role_title": "string",
  "experience_level": "string, e.g. entry-level / 1-3 years / senior",
  "must_have_skills": ["string", ...],
  "nice_to_have_skills": ["string", ...],
  "responsibilities": ["string", ...]
}

Rules:
- Only include what the source text actually states. Never invent
  requirements that aren't in the text.
- If a field isn't mentioned in the source text, use an empty list
  (for list fields) or an empty string (for string fields).

Job description text:
---
{jd_text}
---
"""


class UnsupportedFileType(Exception):
    pass


def extract_text(file_path: str) -> str:
    """Extract raw text from a .pdf or .docx file. Rejects anything else."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise UnsupportedFileType(
            f"Only PDF and DOCX are supported for job descriptions (got {ext})."
        )

    if ext == ".pdf":
        return _extract_pdf_text(file_path)
    return _extract_docx_text(file_path)


def _extract_pdf_text(file_path: str) -> str:
    text_chunks = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_chunks.append(page_text)
    return "\n".join(text_chunks).strip()


def _extract_docx_text(file_path: str) -> str:
    doc = Document(file_path)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n".join(paragraphs).strip()


def structure_jd(jd_text: str) -> dict:
    """
    Sends raw JD text to the LLM and returns it structured as JSON.
    Raises ValueError if the model doesn't return parseable JSON.
    """
    if not jd_text.strip():
        raise ValueError("Extracted job description text is empty.")

    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": JD_JSON_SCHEMA_PROMPT.replace("{jd_text}", jd_text),
            }
        ],
        temperature=0.1,
    )

    raw = response.choices[0].message.content.strip()
    # Strip accidental markdown fences just in case.
    if raw.startswith("```"):
        raw = raw.strip("`")
        raw = raw[4:] if raw.lower().startswith("json") else raw

    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"Model did not return valid JSON: {e}\nRaw: {raw}")


def parse_job_description_file(file_path: str) -> dict:
    """One-shot helper: file path in, structured JD JSON out."""
    raw_text = extract_text(file_path)
    return structure_jd(raw_text)

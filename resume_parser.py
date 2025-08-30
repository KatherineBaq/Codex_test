"""Functions for extracting information from resumes."""
from typing import Set
from PyPDF2 import PdfReader
from skills import extract_skills


def extract_text_from_pdf(file_stream) -> str:
    """Extract raw text from a PDF file-like object."""
    reader = PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def parse_resume(file_stream) -> Set[str]:
    """Parse a resume PDF and return the set of skills found."""
    text = extract_text_from_pdf(file_stream)
    return extract_skills(text)

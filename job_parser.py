"""Functions for extracting information from job descriptions."""
from typing import Set
from skills import extract_skills


def parse_job_description(text: str) -> Set[str]:
    """Return the set of skills mentioned in a job description."""
    return extract_skills(text)

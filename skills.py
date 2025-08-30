"""Utility functions for skill extraction."""
from typing import Set, Iterable

# A simple list of known skills. In a real application this could be
# replaced with a more comprehensive database or a machine learning model.
KNOWN_SKILLS = {
    "python", "java", "javascript", "html", "css", "flask",
    "django", "react", "sql", "machine learning", "data analysis",
    "communication", "leadership", "project management", "git"
}

def extract_skills(text: str, known_skills: Iterable[str] = KNOWN_SKILLS) -> Set[str]:
    """Return the set of skills found in *text*.

    The function performs a simple case-insensitive substring search for each
    item in ``known_skills``.
    """
    text_lower = text.lower()
    return {skill for skill in known_skills if skill.lower() in text_lower}

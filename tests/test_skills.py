from skills import extract_skills

def test_extract_skills_basic():
    text = "Experienced in Python and project management."
    skills = extract_skills(text)
    assert "python" in skills
    assert "project management" in skills
    assert "java" not in skills

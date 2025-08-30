from flask import Flask, render_template, request, redirect, url_for, session
from resume_parser import parse_resume
from job_parser import parse_job_description
from skills import extract_skills

app = Flask(__name__)
app.secret_key = "dev"  # In production, load this from an environment variable


def choose_theme(job_text: str) -> str:
    job_text = job_text.lower()
    if "design" in job_text or "designer" in job_text:
        return "design"
    elif "engineer" in job_text or "developer" in job_text:
        return "tech"
    return "default"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    resume_file = request.files.get("resume")
    job_description = request.form.get("job_description", "")
    if not resume_file or not job_description:
        return redirect(url_for("index"))

    resume_skills = parse_resume(resume_file.stream)
    job_skills = parse_job_description(job_description)
    missing_skills = sorted(job_skills - resume_skills)

    session["resume_skills"] = list(resume_skills)
    session["job_skills"] = list(job_skills)
    session["job_description"] = job_description
    session["theme"] = choose_theme(job_description)

    if missing_skills:
        return render_template("missing_skills.html", missing_skills=missing_skills)

    # If no missing skills, generate immediately
    return redirect(url_for("generate"))


@app.route("/generate", methods=["GET", "POST"])
def generate():
    resume_skills = set(session.get("resume_skills", []))
    job_description = session.get("job_description", "")

    if request.method == "POST":
        added_skills = request.form.getlist("add_skill")
        resume_skills.update(added_skills)
        session["resume_skills"] = list(resume_skills)

    theme = session.get("theme", "default")
    job_skills = set(session.get("job_skills", []))

    return render_template(
        "result.html",
        skills=sorted(resume_skills),
        job_skills=sorted(job_skills),
        job_description=job_description,
        theme=theme,
    )


if __name__ == "__main__":
    app.run(debug=True)

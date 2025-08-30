# CV Generator

This project is a simple web application that generates a CV and cover letter
based on a user's existing resume and a job description. The application:

* Extracts skills from an uploaded resume PDF.
* Extracts required skills from a job description.
* Asks the user about missing skills and optionally adds them.
* Produces a basic CV and cover letter with a theme derived from the job description.

## Running

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser.

## Testing

Run the unit tests with:

```bash
pytest
```

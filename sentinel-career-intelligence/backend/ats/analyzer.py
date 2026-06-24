from backend.gpt.client import ask_gpt
from backend.ats.prompts import ATS_PROMPT


def analyze_resume(resume_text):
    prompt = ATS_PROMPT.format(
        resume=resume_text
    )

    return ask_gpt(prompt)

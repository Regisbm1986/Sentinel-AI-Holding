from backend.ats.pdf_reader import extract_text_from_pdf
from backend.ats.analyzer import analyze_resume

resume_text = extract_text_from_pdf(
    "curriculo.pdf"
)

resultado = analyze_resume(resume_text)

print(resultado)

from backend.ats.pdf_reader import extract_text_from_pdf
from backend.ats.optimizer import optimize_resume

resume = extract_text_from_pdf(
    "curriculo.pdf"
)

result = optimize_resume(
    resume,
    "Analista de Suporte Técnico Microsoft 365"
)

print(result)

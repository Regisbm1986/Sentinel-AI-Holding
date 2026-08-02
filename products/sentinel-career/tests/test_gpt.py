from backend.ats.analyzer import analyze_resume

resume = """
Reginaldo Soares

Bacharel em Sistemas de Informação.

Experiência em Microsoft 365,
Azure,
AWS,
Service Desk,
Suporte Técnico,
Cybersecurity.

Fundador do Sentinel OS.

Certificações Cisco:
Ethical Hacking
Cybersecurity Essentials
"""

resultado = analyze_resume(resume)

print(resultado)

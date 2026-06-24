from backend.recruiter.analyzer import analyze_profile

profile = """
Reginaldo Soares

Analista de TI | Microsoft 365 | Azure | AWS | Cybersecurity

Bacharel em Sistemas de Informação.

Fundador do Sentinel OS.

Experiência com:
Microsoft 365
Azure
AWS
Service Desk
Cybersecurity
Suporte Técnico
Cisco Ethical Hacking
"""

print(
    analyze_profile(profile)
)

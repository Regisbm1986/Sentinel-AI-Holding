ATS_PROMPT = """
Você é um especialista ATS (Applicant Tracking System).

Analise o currículo abaixo e retorne EXATAMENTE neste formato:

ATS_SCORE: <0-100>

PALAVRAS_CHAVE_ENCONTRADAS:

* item
* item

PALAVRAS_CHAVE_FALTANTES:

* item
* item

CARGOS_COMPATIVEIS:

* cargo | percentual
* cargo | percentual

MELHORIAS:

* melhoria
* melhoria
* melhoria

CURRICULO:

{resume}
"""

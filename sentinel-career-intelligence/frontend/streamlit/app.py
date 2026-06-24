import os
import re
import tempfile
import streamlit as st

from backend.ats.pdf_reader import extract_text_from_pdf
from backend.ats.analyzer import analyze_resume
from backend.recruiter.analyzer import analyze_profile
from backend.ats.optimizer import optimize_resume

st.set_page_config(
    page_title="Sentinel Career Intelligence",
    page_icon="🎯",
    layout="wide"
)

# =========================
# Funções auxiliares
# =========================

def extract_ats_score(text):
    match = re.search(r'ATS_SCORE:\s*(\d+)', text)

    if match:
        return int(match.group(1))

    return 0


# =========================
# Sidebar
# =========================

with st.sidebar:

    st.title("🎯 Sentinel Career")

    st.markdown("---")

    st.success("Plano FREE")

    st.markdown("""
### Inclui

✅ ATS Score

✅ Recruiter Score

✅ 1 análise por dia

❌ Currículo otimizado

❌ LinkedIn Optimizer

❌ Simulação de entrevista
""")

    st.markdown("---")

    st.warning("Plano PRO")

    st.markdown("""
### Inclui

✅ Análises ilimitadas

✅ Currículo otimizado

✅ LinkedIn Optimizer

✅ Simulação de entrevista

✅ Vagas compatíveis
""")

    if st.button("🚀 Assinar PRO"):
        st.info(
            "Em breve integração com PIX, Cartão e Mercado Pago."
        )


# =========================
# Cabeçalho
# =========================

st.markdown("""
# 🎯 Sentinel Career Intelligence

### Descubra por que seu currículo não gera entrevistas

ATS Score • Recruiter Score • Resume Optimizer

---
""")


# =========================
# Upload
# =========================

uploaded_file = st.file_uploader(
    "📄 Envie seu currículo PDF",
    type=["pdf"]
)

if uploaded_file:

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(uploaded_file.read())
            pdf_path = tmp.name

        st.info("Extraindo informações do currículo...")

        resume_text = extract_text_from_pdf(pdf_path)

        st.success("Currículo processado com sucesso")

        with st.expander("📄 Texto extraído do currículo"):
            st.text(resume_text[:3000])

        if st.button("🔍 Executar Análise Completa"):

            with st.spinner("Executando ATS Analysis..."):
                ats_result = analyze_resume(resume_text)

            with st.spinner("Executando Recruiter Analysis..."):
                recruiter_result = analyze_profile(resume_text)

            ats_score = extract_ats_score(ats_result)

            recruiter_score = 68
            interview_score = 72

            st.markdown("---")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "ATS Score",
                    f"{ats_score}/100"
                )

            with col2:
                st.metric(
                    "Recruiter Score",
                    f"{recruiter_score}/100"
                )

            with col3:
                st.metric(
                    "Chance de Entrevista",
                    f"{interview_score}%"
                )

            st.markdown("---")

            with st.expander("📊 ATS Analysis"):
                st.text(ats_result)

            with st.expander("👨‍💼 Recruiter Analysis"):
                st.text(recruiter_result)

            st.markdown("---")

            st.subheader("🚀 Currículo Otimizado")

            target_role = st.text_input(
                "Cargo desejado",
                value="Analista de Suporte Técnico Microsoft 365"
            )

            if st.button("✨ Otimizar Currículo"):

                with st.spinner("Otimizando currículo..."):

                    optimized = optimize_resume(
                        resume_text,
                        target_role
                    )

                st.success(
                    "Currículo otimizado com sucesso."
                )

                st.text_area(
                    "Versão otimizada",
                    optimized,
                    height=500
                )

    except Exception as e:

        st.error(
            f"Erro durante processamento: {str(e)}"
        )

    finally:

        try:
            os.remove(pdf_path)
        except:
            pass
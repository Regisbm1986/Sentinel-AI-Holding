"""Landing page for the Sentinel AI holding rendered via Streamlit."""

from __future__ import annotations

import streamlit as st


CYBER_CSS = """
<style>
    .stApp {
        background-color: #030712;
        background-image: radial-gradient(ellipse at top, rgba(0, 255, 102, 0.08), transparent 55%),
                          radial-gradient(ellipse at bottom, rgba(0, 102, 255, 0.08), transparent 60%);
        color: #e2e8f0;
        font-family: "Inter", "Segoe UI", sans-serif;
    }

    .sentinel-container {
        max-width: 1180px;
        margin: 0 auto;
        padding: 3rem 1.75rem 5rem;
    }

    .sentinel-values {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.85rem;
        margin: 3rem auto 4rem;
        font-size: 0.8rem;
        letter-spacing: 0.35rem;
        text-transform: uppercase;
        """Institutional landing page for Sentinel AI rendered with Streamlit."""

        from __future__ import annotations

        import streamlit as st


        DARK_NEON_CSS = """
        <style>
            .stApp {
                background-color: #020617;
                background-image: radial-gradient(circle at 20% 20%, rgba(34, 197, 94, 0.08), transparent 55%),
                                  radial-gradient(circle at 80% 10%, rgba(56, 189, 248, 0.08), transparent 60%);
                color: #e2e8f0;
                font-family: "Inter", "Segoe UI", sans-serif;
            }

            .sentinel-buttons {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 1rem;
                margin: 2.5rem auto 3.5rem;
            }

            .sentinel-button {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 0.95rem 2.75rem;
                border-radius: 999px;
                border: 1px solid rgba(34, 197, 94, 0.55);
                background: linear-gradient(120deg, rgba(34, 197, 94, 0.2), rgba(45, 212, 191, 0.18));
                color: #e2fcef;
                text-decoration: none;
                text-transform: uppercase;
                letter-spacing: 0.32rem;
                font-size: 0.78rem;
                transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
            }

            .sentinel-button:hover {
                transform: translateY(-4px);
                border-color: rgba(34, 197, 94, 0.9);
                box-shadow: 0 18px 42px -16px rgba(16, 185, 129, 0.55);
            }

            .sentinel-badges {
                display: flex;
                flex-wrap: wrap;
                gap: 0.6rem;
                margin-top: 1.5rem;
            }

            .sentinel-badges span {
                display: inline-block;
                padding: 0.45rem 0.9rem;
                border-radius: 999px;
                background: rgba(30, 41, 59, 0.7);
                border: 1px solid rgba(34, 197, 94, 0.35);
                font-size: 0.74rem;
                letter-spacing: 0.08rem;
                color: #cbd5f5;
            }
        </style>
        """


        def render_dashboard() -> None:
            """Render the Sentinel AI institutional landing page."""

            st.set_page_config(
                page_title="Sentinel AI",
                page_icon="🛡️",
                layout="wide",
                initial_sidebar_state="collapsed",
            )

            st.markdown(DARK_NEON_CSS, unsafe_allow_html=True)
            st.image(
                "/home/sentineladmin/sentinel-os/sentinel-career-intelligence/SentinelAI.png",
                use_container_width=True,
            )

            st.markdown(
                """
                ### Inteligência que trabalha por você.

                A Sentinel AI orquestra um ecossistema de plataformas autônomas que combinam Inteligência Artificial Generativa,
                arquitetura orientada a agentes e automação confiável de ponta a ponta. Nossa missão é acelerar resultados mensuráveis
                em carreiras, residências e operações corporativas com governança, segurança e telemetry em tempo real. Visamos ser o
                sistema operacional de confiança para organizações que desejam delegar tarefas complexas a agentes inteligentes sem
                abrir mão de compliance, proteção de dados e experiência premium.
                """
            )

            st.info(
                """
                🚀 **Em Destaque: Sentinel Career**

                Estamos concluindo a Fase 3 do Sentinel Career, integrando PagSeguro e liberando o fluxo completo de assinatura.
                O MVP encontra-se em testes internos com squads multidisciplinares, garantindo jornada de onboarding inteligente,
                análises ATS avançadas e motores de recomendação operando em ambiente de observabilidade total.
                """
            )

            st.markdown("#### Ecossistema Sentinel AI")
            col_career, col_home, col_os = st.columns(3)

            with col_career:
                st.subheader("Sentinel Career")
                st.write(
                    """
                    Plataforma de aceleração profissional que utiliza IA para impulsionar carreiras em tecnologia, produto
                    e operações. Do ATS inteligente ao simulador de entrevistas, cada interação é personalizada com dados de mercado.
                    """
                )
                st.markdown(
                    """
                    **Recursos principais:**
                    - Motor ATS com Inteligência Generativa
                    - Benchmarks salariais e de senioridade
                    - Orquestração de entrevistas e rotinas LinkedIn
                    - Telemetria de desenvolvimento de carreira em dashboards executivos
                    """
                )

            with col_home:
                st.subheader("Sentinel Home")
                st.write(
                    """
                    Hub de automação residencial com agentes contextuais que aprendem hábitos, controlam dispositivos conectados
                    e entregam jornadas personalizadas de segurança e bem-estar. Tudo com governança e privacidade desde a origem.
                    """
                )
                st.markdown(
                    """
                    **Funcionalidades em destaque:**
                    - Gestão unificada de dispositivos IoT
                    - Rotinas autônomas de eficiência energética
                    - Monitoramento preditivo de segurança residencial
                    - Assistentes de voz com entendimento contextual
                    """
                )

            with col_os:
                st.subheader("Sentinel OS")
                st.write(
                    """
                    Sistema operacional inteligente que coordena agentes de negócio, pipelines de dados e fluxos operacionais
                    críticos. Ideal para squads que precisam de insights acionáveis e ações autônomas em escala corporativa.
                    """
                )
                st.markdown(
                    """
                    **Recursos estratégicos:**
                    - Orquestração de agentes especializados
                    - Painéis de missão crítica com telemetria contínua
                    - Integrações com ERPs, CRMs e plataformas cloud
                    - Camadas de automação com aprovação humana no loop
                    """
                )

            button_html = """
            <div class="sentinel-buttons">
                <a class="sentinel-button" href="http://localhost:3000" target="_blank" rel="noopener noreferrer">Sentinel Career</a>
                <a class="sentinel-button" href="https://sentinel.ia.br/home" target="_blank" rel="noopener noreferrer">Sentinel Home</a>
                <a class="sentinel-button" href="https://sentinel.ia.br/os" target="_blank" rel="noopener noreferrer">Sentinel OS</a>
            </div>
            """
            st.markdown(button_html, unsafe_allow_html=True)

            with st.expander("Tecnologia & Infraestrutura", expanded=False):
                st.markdown(
                    """
                    **Plataforma Sentinel AI**
                    - Núcleo baseado em microsserviços e orquestração de agentes.
                    - Telemetry centralizada com observabilidade full stack.
                    - Mecanismos de auto-escalabilidade para workloads sensíveis.

                    **Integrações**
                    - Conectores nativos com Azure, AWS, PagSeguro, LinkedIn e CRMs corporativos.
                    - Pipelines de dados estruturados e semi-estruturados com sincronização contínua.

                    **Arquitetura**
                    - Camadas independentes para ingestão, inteligência, automação e experiência.
                    - Governança de APIs com policy enforcement dinâmico e SLOs monitorados.

                    **Segurança**
                    - Criptografia ponta a ponta, segregação de ambientes e auditoria contínua.
                    - Compliance orientado a LGPD, ISO 27001 e frameworks de Zero Trust.
                    """
                )

            st.markdown("#### Identidade Institucional")
            st.markdown(
                """
                **Missão**
                - Transformar operações e experiências humanas com agentes autônomos confiáveis.

                **Visão**
                - Ser a holding referência em plataformas inteligentes que unem resultados exponenciais
                  e governança responsável.

                **Valores**
                - Inovação orientada a propósito.
                - Segurança por design.
                - Transparência e ética digital.
                - Crescimento sustentável com impacto positivo.
                """
            )

            st.markdown("#### Especialidades Sentinel AI")
            tags = [
                "Artificial Intelligence",
                "Generative AI",
                "Autonomous Agents",
                "Machine Learning",
                "Data Engineering",
                "MLOps",
                "DevSecOps",
                "Cloud Architecture",
                "Edge Computing",
                "Process Automation",
                "Product Intelligence",
                "Operational Analytics",
                "Cybersecurity",
                "Zero Trust",
                "Digital Twins",
                "Experience Design",
                "Telemetry",
                "Enterprise Integrations",
                "Observability",
                "Responsible AI",
            ]

            badges_html = "<div class='sentinel-badges'>" + "".join(
                f"<span>{tag}</span>" for tag in tags
            ) + "</div>"
            st.markdown(badges_html, unsafe_allow_html=True)


        def main() -> None:
            render_dashboard()


        if __name__ == "__main__":
            main()
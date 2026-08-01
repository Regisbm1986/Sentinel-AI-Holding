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
        """Landing page for the Sentinel AI holding rendered via Streamlit."""

        from __future__ import annotations

        import streamlit as st


        def render_dashboard() -> None:
            """Render Sentinel AI landing with banner, values, and product cards."""

            st.set_page_config(
                page_title="Sentinel AI",
                page_icon="🛡️",
                layout="wide",
                initial_sidebar_state="collapsed",
            )

            st.image(
                "/home/sentineladmin/sentinel-os/sentinel-career-intelligence/SentinelAI.png",
                use_container_width=True,
            )

            html = """
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
                    color: #a5b4fc;
                }

                .sentinel-values span {
                    padding: 0.75rem 1.5rem;
                    border-radius: 999px;
                    background: rgba(15, 23, 42, 0.65);
                    border: 1px solid rgba(148, 163, 184, 0.25);
                }

                .sentinel-cards {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                    gap: 1.5rem;
                    width: 100%;
                }

                .sentinel-card {
                    display: flex;
                    flex-direction: column;
                    gap: 1rem;
                    padding: 2.25rem;
                    border-radius: 1.75rem;
                    border: 1px solid rgba(0, 255, 102, 0.28);
                    background: rgba(3, 7, 18, 0.8);
                    text-decoration: none;
                    color: inherit;
                    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
                    backdrop-filter: blur(8px);
                }

                .sentinel-card:hover {
                    transform: translateY(-6px);
                    border-color: rgba(0, 255, 102, 0.85);
                    box-shadow: 0 18px 44px -16px rgba(0, 255, 102, 0.55);
                }

                .sentinel-card h3 {
                    margin: 0;
                    font-size: 1.35rem;
                    color: #f8fafc;
                    letter-spacing: 0.25rem;
                    text-transform: uppercase;
                }

                .sentinel-card p {
                    margin: 0;
                    color: #cbd5f5;
                    font-size: 0.98rem;
                    line-height: 1.6;
                }

                .sentinel-card span.cta {
                    margin-top: auto;
                    font-size: 0.82rem;
                    text-transform: uppercase;
                    letter-spacing: 0.35rem;
                    color: #00ff66;
                }

                .sentinel-footer {
                    text-align: center;
                    font-size: 0.82rem;
                    letter-spacing: 0.3rem;
                    text-transform: uppercase;
                    color: #64748b;
                    padding: 2rem 1.5rem 3rem;
                    border-top: 1px solid rgba(148, 163, 184, 0.25);
                    background: rgba(2, 6, 14, 0.7);
                }

                @media (max-width: 680px) {
                    .sentinel-values {
                        letter-spacing: 0.18rem;
                    }
                }
            </style>

            <div class="sentinel-container">
                <div class="sentinel-values">
                    <span>Inteligência Artificial</span>
                    <span>Agentes Inteligentes</span>
                    <span>Automação Inteligente</span>
                    <span>Segurança e Privacidade</span>
                    <span>Dados que geram valor</span>
                </div>

                <div class="sentinel-cards">
                    <a class="sentinel-card" href="http://localhost:3000" target="_blank" rel="noopener noreferrer">
                        <h3>SENTINEL CAREER</h3>
                        <p>Sua carreira, potencializada por IA.</p>
                        <span class="cta">Explorar</span>
                    </a>
                    <a class="sentinel-card" href="https://sentinel.ia.br/home" target="_blank" rel="noopener noreferrer">
                        <h3>SENTINEL HOME</h3>
                        <p>Sua casa inteligente, simplificada.</p>
                        <span class="cta">Conhecer</span>
                    </a>
                    <a class="sentinel-card" href="https://sentinel.ia.br/os" target="_blank" rel="noopener noreferrer">
                        <h3>SENTINEL OS</h3>
                        <p>Um sistema operacional inteligente para o seu dia a dia.</p>
                        <span class="cta">Descobrir</span>
                    </a>
                </div>
            </div>

            <div class="sentinel-footer">
                Construindo o futuro com inteligência, inovação e propósito. www.sentinel.ia.br
            </div>
            """

            st.markdown(html, unsafe_allow_html=True)


        def main() -> None:
            render_dashboard()


        if __name__ == "__main__":
            main()
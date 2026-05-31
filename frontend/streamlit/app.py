import os
import sys
import shlex
import subprocess
import tempfile
import streamlit as st
import requests
import socket
from backend.modules.nikto.module import run_nikto
from backend.modules.spiderfoot.module import run_spiderfoot
from backend.modules.enum4linux.module import run_enum4linux
from backend.modules.john.module import run_john_the_ripper
from backend.modules.dagda.module import (
    run_dagda,
    check_dagda_status
)
from backend.modules.kubehunter.module import run_kube_hunter
from backend.modules.beef.module import run_beef_daemon
from backend.modules.setoolkit.module import run_setoolkit_daemon

IP_DA_VM = "20.46.250.89"


def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

st.sidebar.subheader("Status das Ferramentas")
st.sidebar.write(f"BeEF (3000): {'🟢 Online' if check_port(3000) else '🔴 Offline'}")
st.sidebar.write(f"SET (80): {'🟢 Online' if check_port(80) else '🔴 Offline'}")

class SentinelOS:
    def __init__(self):
        """
        Construtor Estrutural de Classe.
        Instancia o ecossistema tático e assegura a persistência de logs
        de auditoria de alta sensibilidade contra ciclos de recarregamento web.
        """
        # Configuração estética e perimetral de nível institucional (Dark/Sóbrio)
        st.set_page_config(
            page_title="Sentinel OS — Cyber Security Framework",
            page_icon="🛡️",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        # Inicialização estrutural de estados persistentes do sistema (Session State)
        if "logs" not in st.session_state:
            st.session_state.logs = (
                "=====================================================================\n"
                "🛡️ SENTINEL OS — ADVANCED OPERATIONAL LOG TERMINAL\n"
                "=====================================================================\n"
                "[ℹ️] Núcleo tático instanciado com sucesso via POO Constructor.\n"
                "[ℹ️] Prontidão de Guerra: Aguardando inserção de vetor de ataque...\n"
            )

        if "modo_furtivo_ativo" not in st.session_state:
            st.session_state.modo_furtivo_ativo = False

        if "consultoria_nome" not in st.session_state:
            st.session_state.consultoria_nome = "Sentinel Intelligence Command"

        if "relatorio_ia" not in st.session_state:
            st.session_state.relatorio_ia = ""

        if "gemini_key_input" not in st.session_state:
            st.session_state.gemini_key_input = os.getenv("GEMINI_API_KEY", "")

        if "openai_key_input" not in st.session_state:
            st.session_state.openai_key_input = os.getenv("OPENAI_API_KEY", "")

        if "motor_ia_selecionado" not in st.session_state:
            st.session_state.motor_ia_selecionado = "Google Gemini Core"

    def registrar_log(self, mensagem):
        """Alimenta continuamente o terminal tático centralizando os eventos do sistema"""
        st.session_state.logs += f"{mensagem}\n"

    def executar_modulo_tatico(self, comando, identificador_modulo):
        """
        Subprocess Core Engine: Invoca utilitários binários do Linux e transmite
        o output bruto linha por linha em tempo real para a interface de controle.
        """
        self.registrar_log(f"\n[🚀] INICIANDO ENGRENAGEM DE ATAQUE: {identificador_modulo}")
        
        # Placeholder dinâmico para streaming do console no frontend Streamlit
        terminal_dinamico = st.empty()
        acumulador_saida = ""
        
        try:
            processo = subprocess.Popen(
                comando, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, 
                text=True
            )
            
            # Monitorização e captura em tempo real de fluxos STDOUT/STDERR
            for linha in processo.stdout:
                linha_limpa = linha.strip()
                if linha_limpa:
                    # Filtro de auditoria específico para alertas críticos
                    if "ACCOUNT FOUND" in linha_limpa.upper() or "SUCCESS" in linha_limpa.upper() or "VULNERABILITY" in linha_limpa.upper():
                        linha_formatada = f"[¡] ALERTA CRÍTICO DE EXPLOIT: {linha_limpa}"
                    else:
                        linha_formatada = f"[{identificador_modulo}] {linha_limpa}"
                    
                    acumulador_saida += linha_formatada + "\n"
                    self.registrar_log(linha_formatada)
                    
                    # Injeção em tempo real na tela do operador
                    terminal_dinamico.code(acumulador_saida, language="bash")
                    
            # Correto: Fora do loop 'for', mas ainda DENTRO do bloco 'try'
            processo.wait()
            self.registrar_log(f"[+] Módulo {identificador_modulo} executed até o fim. Coleta consolidada.")
            st.success(f"Missão concluída para o módulo: {identificador_modulo}")
            st.rerun()
            
        except Exception as e:
            # Correto: Alinhado EXATAMENTE na mesma coluna do 'try'
            erro_direto = f"[-] FALHA OPERACIONAL NO MÓDULO {identificador_modulo}: {e}"
            self.registrar_log(erro_direto)
            st.error(erro_direto)


    # =====================================================================
    # MÓDULOS DE ARMA RESTRITA E AUDITORIA OFENSIVA
    # ====================================================================

    def run_setoolkit_daemon(self):
        import os
        # Usamos o setoolkit no modo não-interativo ou via CLI
        os.system("nohup sudo /usr/bin/setoolkit > /tmp/set.log 2>&1 &")

    def gerar_relatorio_inteligencia(self):
        """
        AI Forensic Intelligence: Alimenta o motor de inteligência artificial com os logs
        operacionais para gerar relatórios táticos de vulnerabilidade de alto impacto institucional.
        """
        if len(st.session_state.logs) < 150:
            st.warning("Volume de logs táticos insuficiente para consolidar inteligência forense.")
            return

        prompt_corporativo = f"""
        Você é o Especialista Chefe em Operações Cibernéticas Forenses do Sentinel OS. 
        Analise friamente os logs de intrusão e inteligência abaixo e extraia dados precisos.

        LOGS DO CONSOLE OPERACIONAL:
        {st.session_state.logs}

        Gere um relatório cibernético estruturado de alto padrão exatamente nos seguintes tópicos:

        1. IDENTIFICAÇÃO DE ALVOS E ATIVOS CRÍTICOS
        - Liste de forma cirúrgica todos os IPs, Subredes, Portas, Serviços e Endereços Físicos identificados.

        2. VULNERABILIDADES E VETORES DE EXPLOIT CONSTATADOS
        - Aponte falhas de configuração, serviços obsoletos ou vazamentos de informações identificados pelas ferramentas.

        3. DIRETRIZES DE MITIGAÇÃO E HARDENING MILITAR
        - Apresente planos técnicos de correção imediata e comandos de remediação defensiva.
        """

        # INTERFACES DE EXECUÇÃO MULTI-CLOUD DE IA
        if st.session_state.motor_ia_selecionado == "Google Gemini Core":
            if not st.session_state.gemini_key_input:
                st.error("Chave de API do Google Gemini ausente.")
                return
            try:
                import google.generativeai as genai
                st.info("Processando dados com o motor Google Gemini Core...")
                genai.configure(api_key=st.session_state.gemini_key_input)
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content(prompt_corporativo)
                st.session_state.relatorio_ia = response.text
                st.success("Dossiê consolidado via Gemini Core.")
                st.rerun()
            except Exception as e:
                st.error(f"Falha de resposta no Gemini Engine: {e}")

        elif st.session_state.motor_ia_selecionado == "OpenAI ChatGPT Core":
            if not st.session_state.openai_key_input:
                st.error("Chave de API da OpenAI ausente.")
                return
            try:
                from openai import OpenAI
                st.info("Processando dados com o motor OpenAI ChatGPT Enterprise...")
                client = OpenAI(api_key=st.session_state.openai_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "Você é um perito em operações cibernéticas militares e contra-inteligência."},
                        {"role": "user", "content": prompt_corporativo}
                    ],
                    temperature=0.1
                )
                st.session_state.relatorio_ia = response.choices[0].message.content
                st.success("Dossiê consolidado via ChatGPT Core.")
                st.rerun()
            except Exception as e:
                st.error(f"Falha de resposta no OpenAI Engine: {e}")

    # =====================================================================
    # GRAPHICAL WAR ROOM INTERFACE (STREAMLIT RENDERING)
    # =====================================================================
    def renderizar_painel(self):
        """Renderiza e vincula as estruturas visuais aos comandos lógicos da classe"""
        
        # --- SIDEBAR: PAINEL DE CONTROLE DE MISSÃO ---
        
        st.sidebar.markdown("---")
        st.sidebar.subheader("⚡ Modo Avançado & Execução Livre")

        # 1. Campo para Flags Extras nos módulos padrão
        flags_extras = st.sidebar.text_input(
            "Flags Customizadas (opcional)", 
            placeholder="-v --active --rules",
            help="Adicione parâmetros extras que serão anexados ao comando do módulo selecionado."
        )

        # 2. Expansor para o terminal totalmente livre
        with st.sidebar.expander("🚀 INSTÂNCIA UNRESTRICTED (Console Livre)"):
            st.markdown("<small>Cole aqui as recomendações do relatório de IA ou comandos customizados:</small>", unsafe_allow_html=True)
            comando_livre = st.text_area("Comando Completo", placeholder="kube-hunter --remote 192.168.1.1 --active")
            
            if st.button("Disparar Comando Na Máquina", use_container_width=True, type="primary"):
                if comando_livre:
                    # Quebra o texto digitado em uma lista de argumentos válida
                    lista_comando = shlex.split(comando_livre)
                    
                    # Identifica visualmente no log o nome do primeiro binário executado
                    binario_base = lista_comando[0] if lista_comando else "Livre"
                    
                    # Dispara no motor de tempo real do Sentinel
                    self.executar_modulo_tatico(lista_comando, f"Console-{binario_base}")
                else:
                    st.error("O campo de comando está vazio.")

        st.sidebar.title("🛡️ Sentinel Command")
        st.sidebar.markdown(f"**Emissor Operacional:** `{st.session_state.consultoria_nome}`")

        if st.session_state.modo_furtivo_ativo:
            st.sidebar.warning("🕵️ MODO FURTIVO: EVASÃO ATIVA")
        else:
            st.sidebar.info("🌐 CONEXÃO PERIMETRAL DIRETA")

        st.sidebar.divider()

        # Input Unificado de Alvo
        alvo_global = st.sidebar.text_input(
            "🎯 Alvo Estratégico (IP, URL ou Domínio):", 
            placeholder="Ex: 10.0.0.1 ou target-gov.br"
        )

        st.sidebar.subheader("⚔️ Arsenal Ofensivo (Módulos)")

        if st.sidebar.button("Módulo Enum4Linux (SMB Active Scan)", use_container_width=True):

            run_enum4linux(
                alvo_global,
                self.executar_modulo_tatico
            )

        if st.sidebar.button(
          "Módulo Dagda (Docker Static Analysis)",
           use_container_width=True
):

           resultado = run_dagda(alvo_global)

           if resultado["status"] == "success":

                st.success(resultado["message"])

                if "data" in resultado:
                    st.json(resultado["data"])

           elif resultado["status"] == "running":

                    st.info(resultado["message"])

           elif resultado["status"] == "warning":

               st.warning(resultado["message"])

           else:

               st.error(resultado["message"])

        if st.sidebar.button("Kube Hunter"):

            run_kube_hunter(
                alvo_global,
                self.executar_modulo_tatico,
                self.registrar_log,
                flags_extras
            )

        if st.sidebar.button("Módulo Nikto DAST (Evasion Scan)", use_container_width=True):

            run_nikto(
              alvo_global,
              self.executar_modulo_tatico
            )

        if st.sidebar.button("Módulo SpiderFoot (Massive OSINT)", use_container_width=True):

           run_spiderfoot(
               alvo_global,
               self.executar_modulo_tatico
           )

        st.sidebar.divider()
        st.sidebar.subheader("🔑 Criptoanálise / Cracking")
        hash_input_area = st.sidebar.text_area("Entrada de Hashes Capturados:", placeholder="Cole hashes de senhas...")

        if st.sidebar.button("Disparar Força Bruta (John)", use_container_width=True):

           run_john_the_ripper(
               hash_input_area,
               self.executar_modulo_tatico,
               self.registrar_log
           )

        run_setoolkit_daemon(
            self.registrar_log
        )

        run_beef_daemon(
            self.registrar_log
         )

        st.sidebar.divider()
        st.sidebar.subheader("🤖 Núcleo de Inteligência Artificial")
        
        with st.sidebar.expander("Chaves de Autenticação de IA", expanded=False):
            st.session_state.motor_ia_selecionado = st.selectbox(
                "Motor Analítico:",
                ["Google Gemini Core", "OpenAI ChatGPT Core"]
            )
            
            gemini_key = st.text_input("Chave API Google Gemini:", value=st.session_state.gemini_key_input, type="password")
            if gemini_key != st.session_state.gemini_key_input:
                st.session_state.gemini_key_input = gemini_key

            openai_key = st.text_input("Chave API OpenAI ChatGPT:", value=st.session_state.openai_key_input, type="password")
            if openai_key != st.session_state.openai_key_input:
                st.session_state.openai_key_input = openai_key

        st.sidebar.divider()
        st.sidebar.subheader("🏢 Governança & Customização")

        with st.sidebar.expander("Assinatura Corporativa (White-Label)"):
            workspace_name = st.text_input("Nome do Novo Contrato:")
            if st.button("Criar Workspace Isolado", use_container_width=True):
                if workspace_name:
                    ws_limpo = workspace_name.strip().replace(" ", "_")
                    os.makedirs(os.path.expanduser(f"~/sentinel_projects/{ws_limpo}"), exist_ok=True)
                    self.registrar_log(f"[📁] Novo Workspace de Operação instanciado para o cliente: {ws_limpo}")
                    st.success("Workspace Isolado.")
                    
            branding_input = st.text_input("Nome da Organização Emissora:")
            if st.button("Atualizar Firmamento", use_container_width=True):
                if branding_input:
                    st.session_state.consultoria_nome = branding_input
                    self.registrar_log(f"[🖼️] Identidade visual do sistema alterada para: {branding_input}")
                    st.rerun()

        if st.sidebar.button("Mudar Rota (Alternar Modo Furtivo)", use_container_width=True):
            st.session_state.modo_furtivo_ativo = not st.session_state.modo_furtivo_ativo
            self.registrar_log(f"[🕵️] Mudança de estado de rede. Modo Furtivo: {st.session_state.modo_furtivo_ativo}")
            st.rerun()

        # --- VIEW CENTRAL: WAR ROOM INTERFACE ---
        st.title("🛡️ SENTINEL OS — CYBER WARFARE OPERATIONS PLATFORM")
        st.markdown("---")

        painel_esquerdo, painel_direito = st.columns([2, 1])

        with painel_esquerdo:
            st.subheader("📟 Console Central de Comando (Real-Time Streams)")
            st.text_area(
                label="Terminal Output",
                value=st.session_state.logs,
                height=560,
                disabled=True,
                label_visibility="collapsed"
            )
            
            if st.button("Limpar Histórico de Logs do Console", use_container_width=True):
                st.session_state.logs = "=====================================================================\n🛡️ SENTINEL OS — ADVANCED OPERATIONAL LOG TERMINAL\n=====================================================================\n"
                st.rerun()

        with painel_direito:
            st.subheader("📊 Inteligência e Análise Pós-Missão")
            
            if st.button(f"Gerar Dossiê de Inteligência Cibernética ({st.session_state.motor_ia_selecionado})", use_container_width=True):
                self.gerar_relatorio_inteligencia()

            if st.session_state.relatorio_ia:
                with st.expander("📄 Dossiê Técnico Confidencial", expanded=True):
                    st.markdown(st.session_state.relatorio_ia)
                    st.download_button(
                        label="📥 Exportar Relatório de Inteligência Governamental (TXT)",
                        data=st.session_state.relatorio_ia,
                        file_name="Dossie_Militar_Sentinel_OS.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
            else:
                st.info("Aguardando execução de módulos operacionais para consolidar inteligência forense.")

            with st.expander("ℹ️ Especificações Governamentais do Ecossistema"):
                st.markdown(
                    "**Framework State:** `v1.2.0 (Tactical Weaponized Edition)`  \n"
                    "**Classificação:** Auditoria de Infraestruturas Críticas e Defesa Perimetral  \n"
                    "**Desenvolvedor Principal:** Reginaldo Soares  \n\n"
                    "O **Sentinel OS** é uma arma de inteligência defensiva que unifica as ferramentas "
                    "mais destrutivas e cirúrgicas de auditoria de redes (Red Team) sob uma casca única "
                    "gerenciada por inteligência artificial avançada. Projetado para suportar auditorias de conformidade, "
                    "simulações de adversários de Estado e relatórios executivos de altíssimo escalão político e industrial."
                )

        # 4. INTERFACE DO USUÁRIO (UI)
        st.title("🛡️ Sentinel OS - Análise de Containers")

        # Bloco de Validação de Status em Tempo Real
        status_dagda = check_dagda_status()

        if "Offline" in status_dagda.get("status", ""):
            st.error(f"❌ **Dagda Server:** {status_dagda.get('error', 'Offline')}")
        elif "Erro" in status_dagda.get("status", ""):
            st.warning(f"⚠️ **Dagda Server:** Respondeu com erro ({status_dagda.get('code')})")
        else:
            st.success("🟢 **Dagda Server:** Online e conectado!")
            if "status" in status_dagda:
                st.caption(f"Status do Banco de Dados: {status_dagda['status']}")

        st.divider()

        # Formulário de Escaneamento
        st.subheader("🔍 Escanear Nova Imagem Docker")
        docker_image_input = st.text_input("Nome da imagem (ex: ubuntu:20.04 ou nginx:latest)")

        if st.button("Disparar Análise"):
            if docker_image_input:
                with st.spinner(f"Enviando '{docker_image_input}' para auditoria..."):
                    resultado = scan_docker_image(docker_image_input)
            
                    if resultado["sucesso"]:
                        st.success(resultado["msg"])
                    else:
                        st.error(f"Falha ao iniciar análise: {resultado['error']}")
            else:
                st.warning("Por favor, digite o nome de uma imagem válida.")

        st.divider()

        # Histórico de Relatórios
        st.subheader("📊 Histórico de Vulnerabilidades")
        if docker_image_input:
            historico = get_scan_history(docker_image_input)
            if historico:
                st.json(historico)
            else:
                st.info(f"Nenhum relatório encontrado para a imagem '{docker_image_input}'.")

# =====================================================================
# INTERFACE MAIN LOOP EXECUTOR
# =====================================================================
if __name__ == "__main__":
    framework = SentinelOS()
    framework.renderizar_painel()

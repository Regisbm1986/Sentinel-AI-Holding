import os
import sys
import shlex
import subprocess
import tempfile
import streamlit as st
import requests
import socket
from backend.modules.nikto.module import run_nikto


IP_DA_VM = "20.46.250.89"
DAGDA_API_URL = "http://127.0.0.1:5000/v1"

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

st.sidebar.subheader("Status das Ferramentas")
st.sidebar.write(f"BeEF (3000): {'🟢 Online' if check_port(3000) else '🔴 Offline'}")
st.sidebar.write(f"SET (80): {'🟢 Online' if check_port(80) else '🔴 Offline'}")

def check_dagda_status():
    """Verifica se o servidor Dagda está online e o status de inicialização."""
    try:
        response = requests.get(f"{DAGDA_API_URL}/vuln/init-status", timeout=5)
        if response.status_code == 200:
            return response.json()
        return {"status": "Erro na API", "code": response.status_code}
    except requests.exceptions.ConnectionError:
        return {"status": "Offline", "error": "Servidor Dagda não está respondendo na porta 5000."}
    except Exception as e:
        return {"status": "Erro Inesperado", "error": str(e)}



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
        
        DAGDA_API_URL = "http://127.0.0.1:5000/v1"

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

    def check_dagda_status():
        """Verifica se o servidor Dagda está online e o status de inicialização."""
        try:
            # Endpoint corrigido para init-status (Evita o erro 404)
            response = requests.get(f"{DAGDA_API_URL}/vuln/init-status", timeout=5)
            if response.status_code == 200:
                return response.json()
            return {"status": "Erro na API", "code": response.status_code}
        except requests.exceptions.ConnectionError:
            return {"status": "Offline", "error": "Servidor Dagda não está respondendo na porta 5000."}
        except Exception as e:
            return {"status": "Erro Inesperado", "error": str(e)}

    def scan_docker_image(image_name):
        """Dispara a análise de vulnerabilidades em uma imagem Docker."""
        try:
            response = requests.post(f"{DAGDA_API_URL}/check/images/{image_name}", timeout=10)
            if response.status_code == 202:
                return {"sucesso": True, "msg": f"Análise da imagem '{image_name}' iniciada com sucesso!"}
            elif response.status_code == 404:
                return {"sucesso": False, "error": f"Imagem '{image_name}' não foi encontrada localmente."}
            return {"sucesso": False, "error": response.text}
        except requests.exceptions.ConnectionError:
            return {"sucesso": False, "error": "Não foi possível conectar ao Dagda Server."}
        except Exception as e:
            return {"sucesso": False, "error": str(e)}

    def get_scan_history(image_name):
        """Recupera o histórico completo de relatórios de segurança."""
        try:
            response = requests.get(f"{DAGDA_API_URL}/history/{image_name}", timeout=5)
            if response.status_code == 200:
                return response.json()
            return []
        except Exception:
            return []

    # =====================================================================
    # MÓDULOS DE ARMA RESTRITA E AUDITORIA OFENSIVA
    # =====================================================================
    def run_enum4linux(self, alvo):
        """Enumeração agressiva de SAMBA, IPC$ Shares e LSA Querying"""
        if alvo:
            # Comando com verbosidade total (-a) para extrair todos os metadados possíveis
            self.executar_modulo_tatico(["enum4linux", "-a", alvo], "Enum4Linux-Core")
        else:
            st.sidebar.error("Especifique um Vetor de Destino Alvo.")

    def run_kube_hunter(self, cluster_ip):
        """Caça ativa de falhas em clusters Kubernetes com suporte a flags dinâmicas"""
        if cluster_ip:
            self.registrar_log(f"[☸️] Preparando Kube-Hunter contra: {cluster_ip}")
            
            # Comando base
            comando = ["kube-hunter", "--remote", cluster_ip]
            
            # Se o operador digitou algo em flags_extras, nós injetamos no arsenal
            if flags_extras:
                comando.extend(shlex.split(flags_extras))
                
            self.executar_modulo_tatico(comando, "KubeHunter-K8s")
        else:
            st.sidebar.error("Especifique o IP/Domínio do Cluster Kubernetes.")


    def run_spiderfoot(self, alvo):
        """Módulo de Guerra de Informação e Inteligência OSINT Total"""
        if alvo:
            sf_script = os.path.expanduser("~/spiderfoot/sf.py")
            if os.path.exists(sf_script):
                # Execução silenciosa em backend com coleta massiva de inteligência pública
                cmd_sf = ["python3", sf_script, "-t", "ALL", "-u", "all", "-q", "-s", alvo]
                self.executar_modulo_tatico(cmd_sf, "SpiderFoot-OSINT")
            else:
                st.sidebar.error("Diretório binário do SpiderFoot não localizado no Servidor.")
        else:
            st.sidebar.error("Especifique um Vetor de Destino Alvo.")

    def run_john_the_ripper(self, hash_text):
        """Auditoria Cracking Offline de Criptografia e Quebra de Sentenças de Senhas"""
        if hash_text:
            with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
                temp_file.write(hash_text + "\n")
                temp_file_path = temp_file.name
            
            wordlist_path = "/usr/share/wordlists/rockyou.txt"
            if os.path.exists(wordlist_path):
                # Regras táticas de mutação de palavras ativadas (--rules)
                cmd_john = ["john", f"--wordlist={wordlist_path}", "--rules", temp_file_path]
            else:
                cmd_john = ["john", "--incremental", temp_file_path]
                self.registrar_log("[⚠️] Wordlist militar ausente. Chaveando força bruta para Modo Incremental.")
                
            self.executar_modulo_tatico(cmd_john, "John-Cracker")
            
            try:
                resultado_show = subprocess.run(["john", "--show", temp_file_path], capture_output=True, text=True)
                if resultado_show.stdout:
                    self.registrar_log("\n[=== EXTRACTED CRACKED CREDENTIALS ===]")
                    self.registrar_log(resultado_show.stdout.strip())
                os.unlink(temp_file_path)
            except Exception as ex:
                self.registrar_log(f"[-] Erro ao expurgar resíduos criptográficos: {ex}")
        else:
            st.sidebar.error("Insira hashes válidos para quebra.")

    def run_dagda(self, image_name):
        """
        Método da classe SentinelOS que faz a ponte com a API do Dagda.
        """
        import streamlit as st
        import requests

        DAGDA_API_URL = "http://127.0.0.1:5000/v1"
        
        st.subheader("🛡️ Análise de Containers (Dagda)")
        
        if not image_name:
            st.warning("Nenhum alvo/imagem global foi definido para a análise.")
            return

        with st.spinner(f"Auditando a imagem '{image_name}' no Dagda..."):
            try:
                # 1. Dispara o escaneamento
                response = requests.post(f"{DAGDA_API_URL}/check/images/{image_name}", timeout=10)
                
                if response.status_code == 202:
                    st.success(f"Análise da imagem '{image_name}' iniciada com sucesso!")
                    
                    # 2. Tenta buscar o histórico logo em seguida
                    hist_response = requests.get(f"{DAGDA_API_URL}/history/{image_name}", timeout=5)
                    if hist_response.status_code == 200:
                        st.json(hist_response.json())
                    else:
                        st.info("A análise está rodando em segundo plano. Verifique os relatórios em instantes.")
                
                elif response.status_code == 404:
                    st.error(f"A imagem '{image_name}' não foi encontrada localmente no Docker.")
                else:
                    st.error(f"Erro no Dagda: {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("Não foi possível conectar ao Dagda Server. Verifique se ele está rodando na porta 5000.")
            except Exception as e:
                st.error(f"Erro inesperado: {str(e)}")

    def run_beef_daemon(self):
        import os
        # O '&' no final coloca em background. O log permite ver se houve erro.
        os.system("nohup beef-xss > /tmp/beef.log 2>&1 &")

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
            self.run_enum4linux(alvo_global)

        if st.sidebar.button("Módulo Dagda (Docker Static Analysis)", use_container_width=True):
            # Nota: O 'alvo_global' aqui será interpretado como o nome da imagem Docker (ex: nginx:latest)
            self.run_dagda(alvo_global)

        if st.sidebar.button("Módulo Kube-Hunter (K8s Infiltration)", use_container_width=True):
            # Nota: O 'alvo_global' aqui será o IP ou domínio do cluster Kubernetes
            self.run_kube_hunter(alvo_global)

        if st.sidebar.button("Módulo Nikto DAST (Evasion Scan)", use_container_width=True):

            run_nikto(
              alvo_global,
              self.executar_modulo_tatico
            )

        if st.sidebar.button("Módulo SpiderFoot (Massive OSINT)", use_container_width=True):
            self.run_spiderfoot(alvo_global)

        st.sidebar.divider()
        st.sidebar.subheader("🔑 Criptoanálise / Cracking")
        hash_input_area = st.sidebar.text_area("Entrada de Hashes Capturados:", placeholder="Cole hashes de senhas...")

        if st.sidebar.button("Disparar Força Bruta (John)", use_container_width=True):
            self.run_john_the_ripper(hash_input_area)

        st.sidebar.divider()
        st.sidebar.subheader("📡 Infraestrutura Remota")

        if st.sidebar.button("Spawn Daemon SEToolkit", use_container_width=True):
            self.run_setoolkit_daemon()
            st.sidebar.success("Servidor SEToolkit iniciado em segundo plano!")
        
        IP_DA_VM = "20.46.250.89" # Seu IP Público
        st.sidebar.link_button("🎣 Acessar Terminal do SET", "http://20.46.250.89:7681")


        if st.sidebar.button("Spawn Daemon BeEF Server", use_container_width=True):
            self.run_beef_daemon()
            st.sidebar.success("Servidor BeEF iniciado em segundo plano!")
        
        IP_DA_VM = "20.46.250.89" # Seu IP Público
        st.sidebar.link_button(
            "💻 Acessar Painel do BeEF", 
            f"http://{IP_DA_VM}:3000/ui/panel", 
            use_container_width=True)

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

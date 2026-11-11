# Motor de avaliação

Faz a avaliação passiva do domínio **da própria empresa**. O responsável confirma que é dono do domínio antes de cada execução.

## O que ele usa

| Fonte | Para quê |
|---|---|
| DNS sobre HTTPS (Cloudflare) | Registros de e-mail, DNSSEC, CAA, nomes dos subdomínios |
| Logs públicos de certificados (crt.sh; CertSpotter como alternativa) | Descobrir subdomínios e validade dos certificados |
| Site da própria empresa | Requisições GET simples à página inicial e a poucos caminhos conhecidos |
| API pública do Have I Been Pwned (`breaches?domain`) | Saber se o domínio consta como alvo de vazamento |
| Busca de código do GitHub | Credenciais do domínio em repositórios públicos |

Dados do Have I Been Pwned: © Troy Hunt, licença CC BY 4.0 (haveibeenpwned.com).

## O que ele **não** faz

Varredura de portas, força bruta, injeção de payloads, tentativa de login, exploração de falhas. O conteúdo dos arquivos encontrados nunca é guardado: só o fato de existirem.

## Verificações (44)

### E-mail e DNS

| Verificação | Observação |
|---|---|
| SPF ausente, duplicado, permissivo (`+all`/`?all`) ou acima de 10 consultas | Severidade sobe se o domínio recebe e-mail (tem MX) |
| DMARC ausente, em `p=none` ou sem `rua=` | |
| DKIM nos seletores mais comuns | Ausência não é prova, por isso só severidade baixa |
| MTA-STS | Só para domínios com MX |
| CAA | Quem pode emitir certificados |
| DNSSEC | |
| Servidor de nomes único | Ponto único de falha |

### Certificados e subdomínios

| Verificação | Observação |
|---|---|
| Certificado vencendo em menos de 14 dias | |
| Possível sequestro de subdomínio | CNAME para serviço de terceiros que não existe mais |
| Subdomínios apontando para nomes inexistentes | |
| Ambientes internos ou de teste na internet | `admin`, `staging`, `vpn`, `jenkins`, `grafana` e similares |

### Site

| Verificação | Observação |
|---|---|
| HTTPS ausente e HTTP sem redirecionamento | |
| Cabeçalhos de segurança | HSTS, CSP e proteção contra clickjacking, entre outros |
| Cookies sem `Secure`/`HttpOnly` | Página inicial |
| Arquivos sensíveis expostos | `.git`, `.env`, `phpinfo`, `server-status`, `.DS_Store` |
| `security.txt` | Canal para pesquisadores reportarem falhas |

### Vazamentos e marca

| Verificação | Observação |
|---|---|
| Domínio consta em vazamento de dados | API pública do HIBP, sem chave |
| E-mails corporativos em vazamentos | Opcional: só roda se houver chave configurada. Não está ativa hoje; a empresa pode consultar o próprio domínio de graça em haveibeenpwned.com/DomainSearch |
| Domínios parecidos registrados | Até 90 permutações; destaca os que já têm e-mail configurado |
| Credenciais do domínio em código público no GitHub | |

## Como os resultados viram trabalho

- Cada verificação tem um identificador estável. Isso permite **reabrir** um achado que voltou e **fechar sozinho** o que sumiu.
- Só verificações concluídas com segurança podem fechar achados.
- As notas da execução registram o que não foi possível checar (por exemplo, "crt.sh indisponível; usei o CertSpotter").
- Cada achado traz severidade (CVSS), recomendação em linguagem simples e o mapeamento para LGPD, ISO 27001 e NIST CSF.

## Proteções do próprio motor

- Só segue para hosts do domínio autorizado que resolvam para IP público; redirecionamentos são seguidos manualmente e revalidados.
- Identifica-se com o agente `SentinelBot/1.0`, informando que a avaliação é autorizada pelo dono do domínio.
- Tempo limite por consulta e limites de quantidade (por exemplo, até 40 subdomínios checados por execução).

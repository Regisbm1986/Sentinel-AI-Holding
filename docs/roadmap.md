# Roteiro do Sentinel

## Entregue

- [x] Site público com planos e cadastro da empresa
- [x] Painel com ativos, achados priorizados por CVSS e score de segurança
- [x] Avaliação OSINT passiva do domínio (44 verificações)
- [x] Ciclo de vida dos achados: responsável, prazo, comentários, evidência obrigatória, fechamento e reabertura automáticos
- [x] Equipe Blue Team com termo de autorização e trilha de auditoria
- [x] Convite por link, sem e-mail, e página "Meus achados" para cada membro
- [x] Relatórios executivo, técnico e de conformidade com hash SHA-256 e seção de escopo
- [x] Checagem de higiene de senhas no navegador
- [x] Verificação de vazamentos de domínio sem custo por empresa
- [x] Assinaturas pelo Stripe, em reais, na conta do proprietário
- [x] Área do proprietário: funil, proposta e demonstração com empresa fictícia
- [x] Subdomínios com nova tentativa e segunda fonte de certificados (CertSpotter)

## Em andamento

- [ ] **Monitoramento semanal automático.** Implementado; depende de um plano de hospedagem que permita tarefas agendadas.
- [ ] **Alertas e convites por e-mail.** Dependem de um domínio de envio verificado.
- [ ] **Painel do proprietário lendo o Stripe.** Hoje o MRR vem do funil, digitado pelo proprietário. A ideia é calcular a receita e a situação do pagamento direto do Stripe.

## Próximos (em avaliação)

- [ ] **Correção assistida.** Propor e, com autorização da empresa, aplicar correções de DNS de e-mail (SPF, DMARC, CAA) por meio de um token do provedor de DNS, com registro do que foi alterado e como desfazer.
- [ ] **E-mails de funcionários em vazamentos.** Exige uma fonte paga ou a verificação feita pela própria empresa; avaliar o custo.
- [ ] **Aviso de novo contato** para o proprietário quando chegar um lead.
- [ ] **Login próprio para membros**, se o link pessoal deixar de ser suficiente.

## Ideias para depois

Recursos como login único (SSO) e integração com SIEM e sistemas de chamados aparecem no plano Enterprise como direção de produto. **Ainda não existem.**

## Princípio

Só entra no produto, e só é prometido ao cliente, o que está feito e testado.

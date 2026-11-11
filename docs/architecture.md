# Arquitetura do Sentinel

Visão de alto nível do produto em produção. O código-fonte fica na plataforma de hospedagem (Floot) e não é público; este documento descreve como as peças se encaixam.

## Visão geral

```text
                 Responsável / membro do Blue Team / proprietário
                                     │
                                     ▼
                   Interface web (React 19 + TypeScript)
   site público · painel da empresa · área do proprietário · páginas por link
                                     │
                           /_api/*  (JSON)
                                     ▼
                  Endpoints serverless (TypeScript + Zod)
   ┌────────────┬─────────────┬──────────────┬──────────────┬───────────┐
   │ Avaliação  │  Achados e  │   Equipe e   │  Relatórios  │ Cobrança  │
   │   OSINT    │  delegação  │   convites   │  (SHA-256)   │ (Stripe)  │
   └─────┬──────┴──────┬──────┴──────┬───────┴──────┬───────┴─────┬─────┘
         │             │             │              │             │
         ▼             └─────────────┴──────┬───────┘             ▼
  Fontes públicas                           ▼                  Stripe
  DNS-over-HTTPS · logs de           PostgreSQL (Kysely)    Checkout · Portal
  certificados · site da             empresas, ativos,      Webhook assinado
  própria empresa · HIBP ·           achados, comentários,
  GitHub                             equipe, relatórios
```

## Papéis e acesso

| Papel | Como entra | O que enxerga |
|---|---|---|
| **Proprietário** da plataforma | Conta com papel `admin` (nenhum cadastro público cria esse papel) | Funil de vendas, propostas, roteiro de demonstração, lista de empresas e modo de demonstração |
| **Responsável da empresa** | Cadastro com e-mail e senha | O painel da própria empresa: ativos, achados, avaliação, equipe, relatórios e plano |
| **Membro do Blue Team** | Link de convite de uso único (7 dias) e depois link pessoal permanente | Somente os achados atribuídos a ele |

Os links guardam apenas o hash SHA-256 no banco. Revogar o membro ou gerar um novo link invalida o anterior na hora. Senhas de usuários são guardadas com hash.

## Fluxos principais

**Avaliação.** O responsável confirma que é dono do domínio e dispara a avaliação. O motor consulta as fontes públicas, compara com os achados existentes e, para cada verificação:

- problema novo: abre o achado;
- problema que voltou: reabre;
- verificação concluída sem problema: fecha o achado sozinha, com comentário do sistema;
- fonte indisponível: a verificação fica "não executada" e **nunca fecha achados por engano**.

**Delegação.** Achado atribuído a um membro ativo (termo aceito) com prazo. O membro comenta, inicia a correção e só marca como corrigido com evidência escrita.

**Relatório.** O conteúdo é montado em formato canônico, recebe a seção de escopo e limites, e o hash SHA-256 é calculado sobre o resultado final.

**Cobrança.** Checkout de assinatura do Stripe, em reais, na conta do proprietário. O plano só muda depois que o Stripe confirma pelo webhook, que é verificado por assinatura HMAC e processado uma única vez por evento.

## Decisões de projeto

- **Passivo por construção.** O motor só faz consultas DNS públicas, leitura de logs públicos e requisições GET simples ao site da própria empresa. Hosts fora do domínio ou que resolvam para IP privado são recusados (proteção contra SSRF).
- **Provar antes de fechar.** Corrigir exige evidência, e a reavaliação confirma.
- **Escopo explícito.** Todo relatório informa o que foi e o que não foi coberto.
- **Sem dependência de custo por cliente.** As fontes usadas têm uso gratuito para este fim.

## Limites conhecidos

- O monitoramento semanal automático está implementado, mas só roda com um plano de hospedagem que permita tarefas agendadas.
- Alertas e convites por e-mail dependem de um domínio de envio verificado.

Veja o [roteiro](roadmap.md).

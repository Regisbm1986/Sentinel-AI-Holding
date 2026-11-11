# Ética, autorização e escopo

O Sentinel foi desenhado para que a empresa possa confiar nele e para que ninguém seja enganado sobre o que ele entrega.

## Autorização

- **Domínio.** Antes de cada avaliação, o responsável confirma que é dono do domínio. A avaliação só roda no domínio da própria empresa.
- **Equipe.** Seguindo o código do hacker ético, ninguém fica ativo no Blue Team sem aceitar o **termo de autorização**, que trata de escopo autorizado, regras de engajamento, sigilo e base legal (Lei 12.737/2012 e LGPD). O aceite registra data, versão do termo e, no convite por link, o nome digitado por quem assinou.
- **Escopo por pessoa.** Cada membro tem função e escopo definidos (todos os ativos autorizados, apenas homologação ou somente leitura).
- **Trilha de auditoria.** Cadastro, aceite, revogação, atribuição, mudança de status e geração de relatório ficam registrados com autor e horário.
- **Menor acesso.** O membro vê somente os achados atribuídos a ele, e um membro revogado perde o acesso imediatamente.

## Escopo da avaliação

**Cobre:** a exposição pública do domínio cadastrado, vista de fora, com fontes públicas (veja a lista em [assessment-engine.md](assessment-engine.md)).

**Não cobre:**

- teste de intrusão (pentest) ou qualquer forma de ataque;
- redes internas, estações de trabalho, aplicações e código-fonte da empresa;
- falhas que só aparecem com login ou com interação ativa;
- credenciais de funcionários vazadas (a menos que a empresa configure essa fonte; veja o [roteiro](roadmap.md));
- garantia de conformidade com LGPD, ISO 27001 ou NIST CSF. O mapeamento ajuda a organizar o trabalho, mas não substitui auditoria.

Esses limites aparecem em todo relatório, na seção **"Escopo e limites desta avaliação"**, junto com a data da última avaliação.

## Dados

- A verificação de senhas acontece no navegador. **A senha nunca é enviada nem salva.**
- O conteúdo de arquivos sensíveis encontrados no site nunca é guardado, apenas o fato de existirem.
- Links de convite e de acesso são guardados como hash.
- Pagamentos passam pelo Stripe. O Sentinel não recebe nem guarda dados de cartão.

## Transparência

- Toda requisição ao site da empresa se identifica como `SentinelBot/1.0` e informa que a avaliação é autorizada.
- Relatórios têm hash SHA-256 para provar que não foram alterados depois de gerados.

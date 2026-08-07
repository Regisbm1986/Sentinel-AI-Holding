# CÉREBRO DO PROJETO - SENTINEL AI HOLDING
**Última Atualização:** 07 de Agosto de 2026
**VM Azure:** Linux (Ubuntu) - Acesso via SSH.

## 1. Domínios Oficiais (PRODUÇÃO)
- **Site Institucional (Landing):** https://sentinel-os.ia.br
- **Sentinel Career (App React):** https://career.sentinel-os.ia.br
- **API Backend (FastAPI):** Roda na VM na porta 8000.

## 2. Status das APIs e Integrações
- **Google OAuth / LinkedIn SSO:** As chaves estão no `.env`. **PENDÊNCIA:** O Google Cloud Console precisa ser atualizado com a URI de redirecionamento: `https://career.sentinel-os.ia.br/api/auth/google/callback` e precisa da página de LGPD/Privacidade pública para liberar a tela de consentimento.
- **Mercado Pago:** Faltando a variável `MERCADOPAGO_ACCESS_TOKEN` no `.env` de produção.
- **Frontend Vite:** Configurado com `VITE_API_URL=https://career.sentinel-os.ia.br` no arquivo `.env.production`.

## 3. Estrutura de Pastas Chave
- **Institucional (Index HTML):** `products/sentinel-career/frontend/landing/`
- **Career Frontend (React):** `products/sentinel_career/frontend/`
- **Backend API (Python):** `products/sentinel_career/backend/app/`

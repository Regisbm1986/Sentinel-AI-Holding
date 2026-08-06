#!/usr/bin/env bash
set -euo pipefail

# Script de migração para reestruturar o repositório sentinel-os
# Execução: ./migracao.sh (a partir da raiz do repositório)

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

# Passo de segurança: garantir que estamos na raiz esperada
if [[ ! -d "backend" || ! -f "README.md" ]]; then
  echo "[ERRO] Execute este script a partir da raiz do repositório sentinel-os." >&2
  exit 1
fi

shopt -s nullglob dotglob

########################################
# Fase 1: Limpeza (Garbage Collection) #
########################################

# 1) Remover pastas vazias conhecidas
echo "[Fase 1] Removendo pastas vazias..."
for empty_dir in automation-runs docker scripts infrastructure; do
  if [[ -d "$empty_dir" ]]; then
    rm -rf "$empty_dir"
  fi
done

# 2) Eliminar artefatos temporários e ambientes virtuais
echo "[Fase 1] Removendo artefatos temporários..."
find . -type d -name '__pycache__' -prune -exec rm -rf {} +
[[ -d tmp ]] && rm -rf tmp
[[ -d venv ]] && rm -rf venv
[[ -d sentinel-career-intelligence/venv ]] && rm -rf sentinel-career-intelligence/venv
[[ -f streamlit.log ]] && rm -rf streamlit.log
[[ -f frontend/streamlit/app.py.bkp ]] && rm -rf frontend/streamlit/app.py.bkp

# 3) Remover duplicidades de dados em JSON
echo "[Fase 1] Removendo duplicidades de dados..."
[[ -f payments.json ]] && rm -rf payments.json
[[ -f subscriptions.json ]] && rm -rf subscriptions.json

###################################################
# Fase 2: Criação da nova estrutura (Pastas alvo) #
###################################################

# 4) Criar diretórios da plataforma
echo "[Fase 2] Criando estrutura do diretório Platform..."
mkdir -p sentinel_os/platform/backend sentinel_os/platform/tests sentinel_os/platform/requirements

# 5) Criar diretórios dos produtos
echo "[Fase 2] Criando estrutura dos produtos..."
mkdir -p products/sentinel_career/backend
mkdir -p products/sentinel_career/frontend
mkdir -p products/sentinel_career/data
mkdir -p products/sentinel_career/tests
mkdir -p products/sentinel_os/frontend


# 6) Recriar infraestrutura alvo
echo "[Fase 2] Recriando infraestrutura..."
mkdir -p infrastructure/docker infrastructure/nginx infrastructure/scripts

# 7) Preparar diretórios de documentação
echo "[Fase 2] Preparando diretórios de documentação..."
mkdir -p docs/platform docs/products/sentinel_career

#########################################
# Fase 3: Movimentação (De -> Para)     #
#########################################

# 8) Migrar backend da plataforma
echo "[Fase 3] Migrando componentes de plataforma..."
if [[ -d backend ]]; then
  for item in backend/*; do
    mv "$item" sentinel_os/platform/backend/
  done
fi

# 9) Migrar suíte de testes para a nova base
if [[ -d tests ]]; then
  for item in tests/*; do
    mv "$item" sentinel_os/platform/tests/
  done
fi

# 10) Realocar arquivos de documentação da plataforma
for doc_file in CHANGELOG.md RELEASES.md; do
  if [[ -f "$doc_file" ]]; then
    mv "$doc_file" docs/platform/
  fi
done
# 11) Reagrupar configurações de testes da plataforma
if [[ -f conftest.py ]]; then
  mv conftest.py sentinel_os/platform/tests/
fi
if [[ -f pytest.ini ]]; then
  mv pytest.ini sentinel_os/platform/tests/
fi
if [[ -f dryrun_files.txt ]]; then
  mv dryrun_files.txt docs/platform/
fi
if [[ -f test_list.txt ]]; then
  mv test_list.txt docs/platform/
fi

# 12) Migrar frontend do Sentinel OS
echo "[Fase 3] Migrando Sentinel OS..."
if [[ -d frontend/streamlit ]]; then
  mkdir -p products/sentinel_os/frontend
  mv frontend/streamlit products/sentinel_os/frontend/
fi

# 13) Migrar backend do Sentinel Career (intelligence)
echo "[Fase 3] Migrando Sentinel Career (backends)..."
if [[ -d sentinel-career-intelligence/backend ]]; then
  for item in sentinel-career-intelligence/backend/*; do
    mv "$item" products/sentinel_career/backend/
  done
fi
# 14) Migrar backend legado do Sentinel Career deduplicando arquivos vazios
if [[ -d products/sentinel_career/backend ]]; then
  for item in products/sentinel_career/backend/*; do
    base_name="$(basename "$item")"
    dest_path="products/sentinel_career/backend/$base_name"
    if [[ -f "$item" && -f "$dest_path" && ! -s "$item" && ! -s "$dest_path" ]]; then
      rm -rf "$item"
    else
      mv "$item" products/sentinel_career/backend/
    fi
  done
fi

# 15) Migrar frontend, dados e documentação do Sentinel Career
echo "[Fase 3] Migrando Sentinel Career (frontend, dados, docs)..."
if [[ -d sentinel-career-intelligence/frontend ]]; then
  for item in sentinel-career-intelligence/frontend/*; do
    mv "$item" products/sentinel_career/frontend/
  done
fi
# 16) Reposicionar arquivos de dados do Sentinel Career
for data_file in sentinel-career-intelligence/payments.json sentinel-career-intelligence/subscriptions.json; do
  if [[ -f "$data_file" ]]; then
    mv "$data_file" products/sentinel_career/data/
  fi
done
# 17) Migrar documentação específica do Sentinel Career
if [[ -d sentinel-career-intelligence/docs ]]; then
  for item in sentinel-career-intelligence/docs/*; do
    mv "$item" docs/products/sentinel_career/
  done
fi

# 18) Reposicionar testes específicos do Sentinel Career
for product_test in sentinel-career-intelligence/test_*.py; do
  mv "$product_test" products/sentinel_career/tests/
done

########################################
# Fase 4: Limpeza Final                #
########################################

# 19) Remover diretórios originais que ficaram vazios
echo "[Fase 4] Removendo diretórios antigos vazios..."
rm -rf sentinel-career-intelligence
rm -rf products/sentinel_career
rm -rf frontend
rm -rf backend
rm -rf tests

echo "[OK] Migração concluída com sucesso. Revise o resultado antes de commitar."

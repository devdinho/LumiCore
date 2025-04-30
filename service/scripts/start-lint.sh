#!/usr/bin/env sh

set -e

echo "Executando Black"
black -q $1
echo "Executando Isort"
isort -q $1
echo "Executando Flake8"
flake8 --ignore=E211,E999,F821,W503,E203 --max-line-length=121 --exclude=migrations,settings,__pycache__,tests,'URLs e Endpoints.py' $1
echo "Fim"
#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

echo "[lab01] BACKEND=${BACKEND:-openai} OFFLINE=${OFFLINE:-1}"

# Python
python py/app.py >/dev/null

# Node
node ts/app.js >/dev/null || (echo "[warn] Node não disponível"; true)

# Pytests (quiet)
pytest -q tests || (echo "[fail] testes falharam. Rode: make fix LAB=01_sdk_boot"; exit 1)

touch ../../.passports/lab01.ok
echo "[lab01] OK — outputs gerados e testes passaram."

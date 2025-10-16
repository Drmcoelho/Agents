#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
echo "[fix] aplicando gabarito mínimo (stub)..."

# Regera os outputs caso estejam ausentes
python py/app.py >/dev/null || true
node ts/app.js >/dev/null || true

# Re-roda testes
pytest -q tests || true
echo "[fix] pronto. Consulte outputs/ e reexecute make lab."

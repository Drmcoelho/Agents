#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
echo "[fix] regenerando outputs do Lab 02"
python client.py >/dev/null || true
echo "[fix] pronto."

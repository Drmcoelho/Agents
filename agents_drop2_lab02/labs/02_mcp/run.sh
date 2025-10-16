#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

python client.py >/dev/null

python - <<'PY'
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "labs" / "02_mcp" / "outputs" / "session.jsonl"
data = [json.loads(x) for x in OUT.read_text(encoding="utf-8").splitlines()]
assert any(x["type"]=="health" and x["data"].get("ok") for x in data)
assert any(x["type"]=="list_pdfs" for x in data)
assert any(x["type"]=="summarize_pdf" for x in data)
print("[lab02] OK — outputs gerados e verificados.")
PY

touch ../../.passports/lab02.ok

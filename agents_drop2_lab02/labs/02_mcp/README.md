# Lab 02 — MCP server (stub) com 2 tools + healthcheck

## Endpoints (HTTP simplificados)
- `GET /health` → `{"ok": true}`
- `POST /tools/list_pdfs` → `{"files": ["a.txt", ...]}`
- `POST /tools/summarize_pdf` (json: `{ "path": "assets/pdfs/a.txt", "max_words": 40 }`) → `{"summary": "..."}`
- `POST /shutdown` → encerra o servidor

## Como rodar
```bash
make lab LAB=02_mcp      # inicia servidor, chama tools e gera outputs
make fix LAB=02_mcp      # gabarito (regenera outputs)
```

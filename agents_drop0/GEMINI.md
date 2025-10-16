# GEMINI.md — Guia rápido (CLI 2.5 Pro)

Este projeto é **multi-backend**. Para usar o **Gemini CLI 2.5**, siga:

## Instalação (local/Codespaces)
- Pré-requisitos: Node LTS, Python 3.12
- Instale o CLI (ajuste conforme seu ambiente):
```bash
npm i -g @google/gemini-cli@latest
```

## Autenticação
- Defina `GEMINI_API_KEY` no `.env.local` (veja `env/.env.example`).
- Em CI, configure o segredo no *Environment* adequado.

## Uso básico neste repo
```bash
BACKEND=gemini make lab LAB=01_sdk_boot
# O driver invocará o CLI com arquivos e prompts preparados
```

## Boas práticas
- Limite de contexto e *rate limits* variam por plano — trate erros com *retry/backoff*.
- Para dados sensíveis, use *mock inputs* nos labs; nunca faça upload acidental.

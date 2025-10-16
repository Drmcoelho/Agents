# Lab 01 — Boot & SDKs (Responses API)

Objetivos:
1) Fazer uma chamada ao modelo com *structured output*;
2) Usar *streaming* (simulado no modo OFFLINE);
3) Fazer upload/ingest simulado de arquivo;
4) Gerar `outputs/output.jsonl` com rastro da execução.

## Como rodar
```bash
# Python (OFFLINE por padrão)
make lab LAB=01_sdk_boot

# Se quiser trocar backend (ainda no modo offline):
BACKEND=anthropic make lab LAB=01_sdk_boot

# Para ver gabarito
make fix LAB=01_sdk_boot
```

> **OFFLINE=1** evita chamadas externas; o lab valida o **contrato** e cria saídas
determinísticas. Quando quiser usar as APIs reais, edite `env/.env.local` e defina `OFFLINE=0`.

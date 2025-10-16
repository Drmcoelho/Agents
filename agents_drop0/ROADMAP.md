# ROADMAP — Curso Agents

> **Meta:** curso *hands-on* com avaliação automática e “gabarito que corrige”.

## Drops
- **Drop 0 (este):** scaffolding, docs base, Makefile, CI stub, GEMINI.md
- **Drop 1:** Lab 01 (SDKs/Responses), Lab 02 (MCP server), Evals básicos
- **Drop 2:** Agents SDK + Agent Builder (multiagente) + docs de guardrails
- **Drop 3:** AgentKit/ChatKit (UI) + métricas + custos + preview deploy
- **Drop 4:** Capstones, regressão completa, playbooks e postmortem

## Milestones técnicas
1) **SDKs** funcionando (OpenAI/Claude/Gemini) via *driver* `.env`  
2) **MCP** com 2 tools: `list_pdfs`, `summarize_pdf` (educacional)  
3) **Agents** com planner/testes e traces OTLP  
4) **AgentKit** com UI, flags e RBAC básico

## Qualidade e segurança
- Guardrails (input/output), *rate limits*, `secrets` isolados
- CI: lint, typecheck, smoke de labs; link-check de docs
- Evals: structured output, tool-call success, custos e latência

# Agents — Etapa 0 (Seed)

Repositório do curso **100% prático** sobre agentes com quatro eixos centrais:
**SDKs**, **MCP**, **Agents** e **AgentKit** (com **ChatKit**). Este seed entrega
estrutura mínima para começarmos os *labs* e a documentação.

## Como usar (Codespaces/devcontainer ou local)
```bash
# clonagem
git clone <seu-fork-ou-repo> && cd Agents

# preparação rápida (local ou codespaces)
make bootstrap   # instala deps mínimas e prepara .env.local
make docs        # aponta para docs/agents/00_conceitos_iniciais.md
```

## Trilho do curso
1. Boot & SDKs (Responses API)  
2. Ferramentas & **MCP**  
3. Orquestração com Responses + Hosted MCP  
4. **Agents SDK** (agente único)  
5. **Agent Builder** (multiagente)  
6. **AgentKit + ChatKit** (UI e deploy)  
7. Segurança, guardrails e **evals**  
8. Capstones (educacional médico; B2C)

## Estado desta entrega (2025-10-16)
- Documentação base criada (`docs/agents/00_conceitos_iniciais.md`)
- Esqueleto de *labs* e *Makefile* mínimo
- Roadmap inicial em `ROADMAP.md`
- Guia de uso do **Gemini CLI 2.5** em `GEMINI.md`

> Próximo passo: adicionar Lab 01 (Responses + streaming + arquivos).

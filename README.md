# Bem-vindo ao Curso de Agentes de IA!

Este repositório contém um curso completo e prático para você aprender a construir Agentes de IA, desde os conceitos básicos até a implantação em produção. O curso é projetado para ser uma experiência de aprendizado `hands-on`, com avaliação automática e um sistema de "gabarito que corrige" para ajudá-lo em sua jornada.

## Visão Geral do Projeto

O objetivo deste curso é fornecer uma base sólida em engenharia de Agentes de IA, cobrindo desde a interação com modelos de linguagem (LLMs) até a criação de agentes autônomos e sua implantação. O curso é estruturado em "drops", que são entregas incrementais de conteúdo, permitindo que você aprenda de forma progressiva.

**Filosofia de Aprendizagem:**

*   **Aprenda fazendo:** O curso é centrado em laboratórios práticos, onde você escreverá código para resolver problemas reais.
*   **Feedback imediato:** Cada laboratório possui testes automatizados que fornecem feedback instantâneo sobre o seu progresso.
*   **Aprendizagem progressiva:** O conteúdo é dividido em módulos e laboratórios, começando dos conceitos mais simples e avançando para os mais complexos.
*   **Independência de plataforma:** O curso é projetado para ser agnóstico em relação ao provedor de LLM, com suporte para OpenAI, Anthropic (Claude) e Google Gemini.

## Estrutura do Curso

O repositório é organizado em "drops", onde cada `drop` representa uma etapa do desenvolvimento do curso. Para uma melhor experiência, **recomenda-se utilizar sempre o `drop` mais recente**.

*   `agents_drop0`: Contém o esqueleto inicial do projeto, documentação e scripts básicos.
*   `agents_drop1_lab01`: Contém o primeiro laboratório focado em SDKs e a interação com as respostas dos modelos.

**Atenção:** Existe uma redundância intencional entre os `drops` para mostrar a evolução do projeto. No entanto, para evitar confusão, sempre trabalhe no diretório do `drop` mais recente.

## Módulos de Aprendizagem

O curso é dividido em quatro módulos principais:

1.  **SDKs (Software Development Kits):** Neste módulo, você aprenderá os fundamentos da interação com modelos de linguagem.
    *   **Conceitos:** Chamadas de API, prompts de sistema, controle de temperatura, streaming de respostas e processamento de saída estruturada.
    *   **Laboratórios:** `01_sdk_boot`

2.  **MCP (Model Context Protocol):** Este módulo introduz o conceito de ferramentas (tools) e como os modelos podem usá-las para interagir com o mundo exterior.
    *   **Conceitos:** Registro e execução de ferramentas, implementação de um servidor MCP com FastAPI.
    *   **Ferramentas de Exemplo:** Calculadora, analisador de texto, `list_pdfs`, `summarize_pdf`.

3.  **Agents:** O coração do curso, onde você aprenderá a construir agentes autônomos.
    *   **Conceitos:** Arquitetura de agentes (ReAct), planejamento, gerenciamento de ferramentas, histórico de conversação e loops de raciocínio.
    *   **SDKs de Agentes:** Construção de um agente `single-player` com lógica de planejamento.

4.  **AgentKit:** Este módulo foca na implantação de agentes em produção.
    *   **Conceitos:** Boas práticas de produção, monitoramento, orquestração, interface de usuário (UI) com ChatKit, e controle de acesso (RBAC).

## Projetos Finais

Após concluir os módulos, você aplicará seus conhecimentos em dois projetos finais:

1.  **Leitor de PDF Médico:** Um agente capaz de analisar documentos médicos em PDF, extrair informações e responder a perguntas usando técnicas de RAG (Retrieval-Augmented Generation).
2.  **Agente de Atendimento ao Cliente B2C:** Um chatbot inteligente para atendimento ao cliente, com classificação de intenção, integração com base de conhecimento e gerenciamento de histórico de conversas.

## Fluxo de Trabalho do Aluno

Siga estas etapas para uma experiência de aprendizado bem-sucedida:

1.  **Abra em GitHub Codespaces:** A maneira mais fácil de começar é usando o GitHub Codespaces, que fornece um ambiente de desenvolvimento pré-configurado.
2.  **Instale as dependências:** `make bootstrap`
3.  **Configure suas chaves de API:** Copie `env/.env.example` para `env/.env.local` e adicione suas chaves de API.
4.  **Execute um laboratório:** `make lab LAB=<nome_do_lab>`
5.  **Entenda e modifique o código:** Explore o código do laboratório e tente resolver os desafios propostos.
6.  **Obtenha ajuda se necessário:** `make fix LAB=<nome_do_lab>`
7.  **Verifique seu progresso:** `make passport`
8.  **Avance para o próximo laboratório:** Continue o ciclo até concluir todos os módulos.
9.  **Construa os projetos finais:** Aplique suas habilidades nos projetos finais.
10. **Implante seus projetos:** `make deploy`

## Ambiente de Desenvolvimento

*   **Multi-Backend:** Selecione o backend de LLM desejado (openai, anthropic, gemini) através da variável de ambiente `BACKEND`.
*   **Modo Offline:** Execute os laboratórios em modo offline (`OFFLINE=1`) para testar a lógica sem incorrer em custos de API.
*   **GitHub Codespaces:** Ambiente de desenvolvimento pronto para uso com todas as dependências e extensões do VS Code pré-instaladas.

## Testes e Qualidade de Código

*   **Testes:** O projeto usa `pytest` para testes automatizados. Execute `make test` para rodar todos os testes.
*   **Linting e Formatação:** `ruff` e `black` são usados para garantir a qualidade e a consistência do código. Execute `make lint` e `make format`.
*   **CI/CD:** Um pipeline de GitHub Actions é executado a cada commit para garantir que o código esteja sempre funcional.

## Como Contribuir

Contribuições são bem-vindas! Se você encontrar um bug, tiver uma sugestão de melhoria ou quiser adicionar um novo laboratório, por favor, abra uma issue no GitHub.

## FAQ (Perguntas Frequentes)

*   **P: Por que existem diretórios `agents_drop0` e `agents_drop1_lab01`? Qual devo usar?**
    *   **R:** Os diretórios representam a evolução do curso. Use sempre o diretório com o número de `drop` mais alto.

*   **P: Preciso de chaves de API para fazer o curso?**
    *   **R:** Não necessariamente. O curso pode ser feito em modo offline, que simula as respostas da API. No entanto, para interagir com os modelos reais, você precisará de chaves de API.

*   **P: O que fazer se eu ficar preso em um laboratório?**
    *   **R:** Use o comando `make fix LAB=<nome_do_lab>` para obter dicas e, em último caso, a solução.

## Roadmap do Curso

*   **Drop 0:** Estrutura inicial, documentação, Makefile e CI.
*   **Drop 1:** Lab 01 (SDKs/Responses), Lab 02 (MCP server), Evals básicos.
*   **Drop 2:** Agents SDK + Agent Builder (multiagente) + docs de guardrails.
*   **Drop 3:** AgentKit/ChatKit (UI) + métricas + custos + preview deploy.
*   **Drop 4:** Projetos Finais, testes de regressão completos, playbooks e postmortem.

Bom aprendizado!

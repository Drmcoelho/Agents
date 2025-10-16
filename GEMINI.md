# GEMINI - Guia Completo do Projeto de Agentes de IA

Este documento é um guia centralizado e robusto para o curso prático de Agentes de IA. Ele consolida as informações de toda a documentação do projeto, oferecendo uma visão completa da arquitetura, módulos, fluxo de trabalho e conceitos fundamentais.

## 1. Visão Geral do Curso

O objetivo deste repositório é fornecer um **curso 100% prático sobre Agentes de IA**, cobrindo desde os fundamentos de SDKs até a orquestração de múltiplos agentes e deployment.

### 1.1. Trilha de Aprendizagem

O curso é estruturado em quatro módulos principais, complementados por projetos finais (capstones) para aplicação prática do conhecimento.

1.  **SDKs (Software Development Kits)**: Fundamentos do consumo de APIs de IA, incluindo chamadas, streaming e controle de parâmetros.
2.  **MCP (Model Context Protocol)**: Implementação de servidores de ferramentas (tools) que os agentes podem consumir.
3.  **Agents**: Construção de agentes autônomos, começando com um agente único (ReAct) e evoluindo para sistemas multi-agente.
4.  **AgentKit & ChatKit**: Foco em deployment, boas práticas de produção, monitoramento e integração com interfaces de usuário (UI).

### 1.2. Projetos Capstone

-   **Leitor de PDF Médico**: Um sistema didático para análise de documentos médicos usando técnicas de RAG (Retrieval-Augmented Generation).
-   **Agente de Atendimento ao Cliente (B2C)**: Um chatbot inteligente para interação com clientes, com classificação de intenção e integração com base de conhecimento.

## 2. Arquitetura e Fluxo de Trabalho

O projeto é desenhado para uma experiência de aprendizado fluida e prática, especialmente otimizada para ambientes como o GitHub Codespaces.

### 2.1. Interface Unificada com `Makefile`

Todas as operações do curso são centralizadas em um `Makefile`, seguindo um fluxo padrão:

-   `make bootstrap`: Configura o ambiente, instala dependências e cria o arquivo `.env.local`.
-   `make lab MODULE=<modulo> LAB=<lab>`: Inicia um laboratório prático.
-   `make fix LAB=<lab>`: Fornece dicas progressivas ou a solução completa para um laboratório.
-   `make passport`: Exibe seu progresso no curso.
-   `make test`: Executa os testes automatizados.

### 2.2. Suporte Multi-Backend

O sistema é flexível e permite a troca entre diferentes provedores de IA através da configuração no arquivo `.env.local`.

-   **Google Gemini** (Gemini Pro)
-   OpenAI (GPT-3.5/GPT-4)
-   Anthropic (Claude 3)

### 2.3. Modo OFFLINE

Para acelerar o desenvolvimento e validar a lógica sem custos, os laboratórios podem ser executados em modo `OFFLINE=1`. Nesse modo, as chamadas para as APIs são simuladas, permitindo a validação dos contratos de dados e do fluxo de execução de forma determinística.

## 3. Conceitos Fundamentais de Agentes de IA

Um **Agente de IA** é um sistema que percebe seu ambiente e atua sobre ele para atingir objetivos.

### 3.1. Características Principais

-   **Autonomia**: Opera sem intervenção humana direta.
-   **Percepção**: Recebe informações do ambiente (via sensores ou APIs).
-   **Ação**: Executa ações que modificam o ambiente (via atuadores ou comandos).
-   **Orientação a Objetivos**: Trabalha para alcançar metas predefinidas.
-   **Adaptabilidade**: Aprende e melhora com a experiência.

### 3.2. Tipos de Agentes

| Tipo | Descrição | Exemplo |
| :--- | :--- | :--- |
| **Reativo Simples** | Responde a percepções com regras `if-then`. | Termostato |
| **Baseado em Modelo** | Mantém um estado interno do mundo. | GPS |
| **Baseado em Objetivos** | Planeja ações para alcançar um objetivo. | Planejador de rotas |
| **Baseado em Utilidade** | Maximiza uma métrica de "felicidade" ou utilidade. | Sistemas de recomendação |
| **De Aprendizado** | Melhora seu desempenho com o tempo. | Chatbots avançados |

### 3.3. Componentes de um Agente

-   **Sensores**: Coletam dados do ambiente (e.g., APIs, arquivos).
-   **Atuadores**: Executam ações no ambiente (e.g., chamadas de API, escrita de arquivos).
-   **Função Agente**: O "cérebro" que mapeia percepções em ações.
-   **Base de Conhecimento**: A memória ou estado interno do agente.

## 4. Guia de Uso (Quick Start)

Siga estes passos para começar a aprender:

1.  **Abra em um Ambiente de Desenvolvimento**: Use o GitHub Codespaces para uma configuração automática.
2.  **Bootstrap**:
    ```bash
    make bootstrap
    ```
3.  **Configure suas Chaves de API**: Edite o arquivo `env/.env.local` com suas chaves dos provedores de IA (Gemini, OpenAI, etc.).
4.  **Inicie o Primeiro Laboratório**:
    ```bash
    make lab LAB=01_sdk_boot
    ```
5.  **Precisa de Ajuda?**: Se ficar preso, use o sistema de "gabarito":
    ```bash
    make fix LAB=01_sdk_boot
    ```
6.  **Acompanhe seu Progresso**:
    ```bash
    make passport
    ```

Este guia consolida o conhecimento distribuído nos diversos arquivos `README.md` e documentos conceituais, servindo como a fonte única de verdade para o projeto.

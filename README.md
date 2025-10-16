# Bem-vindo ao Curso de Agentes de IA!

Este repositório contém um curso completo e prático para você aprender a construir Agentes de IA, desde os conceitos básicos até a implantação em produção.

## Os 10 Passos para o Sucesso

Siga estas 10 etapas para concluir o curso e se tornar um especialista em Agentes de IA:

### 1. Configuração do Ambiente (GitHub Codespaces)

A maneira mais fácil de começar é usando o GitHub Codespaces. Clique no botão "Code" e selecione "Open with Codespaces" para iniciar um ambiente de desenvolvimento completo no seu navegador.

### 2. Instalação das Dependências (`make bootstrap`)

Após o ambiente ser criado, abra um terminal e execute o seguinte comando para instalar todas as dependências necessárias:

```bash
make bootstrap
```

### 3. Configuração das Chaves de API (`.env.local`)

Para usar os modelos de IA, você precisará de chaves de API. Copie o arquivo de exemplo e adicione suas chaves:

```bash
cp env/.env.example env/.env.local
```

Em seguida, edite o arquivo `env/.env.local` e adicione suas chaves de API para OpenAI, Anthropic ou Gemini.

### 4. Iniciando o Primeiro Laboratório (`make lab LAB=01_sdk_boot`)

Agora você está pronto para começar o primeiro laboratório! Execute o seguinte comando:

```bash
make lab LAB=01_sdk_boot
```

Este comando executará o código do laboratório e os testes correspondentes.

### 5. Entendendo o Código do Laboratório

Abra o diretório `labs/01_sdk_boot` para explorar o código. Você encontrará implementações em Python (`py/app.py`) e JavaScript (`ts/app.js`). Analise o código para entender como ele funciona.

### 6. Executando os Testes (`pytest`)

Os testes são uma parte fundamental do desenvolvimento. Você pode executar os testes para o laboratório atual com o seguinte comando:

```bash
pytest labs/01_sdk_boot/tests/
```

### 7. Obtendo Ajuda (`make fix`)

Se você tiver dificuldades em um laboratório, pode usar o comando `fix` para obter dicas e até mesmo a solução completa:

```bash
make fix LAB=01_sdk_boot
```

### 8. Acompanhando o Progresso (`make passport`)

Você pode verificar seu progresso no curso a qualquer momento com o comando `passport`:

```bash
make passport
```

### 9. Avançando para os Próximos Módulos

Depois de concluir o primeiro laboratório, você pode avançar para os próximos. A estrutura é a mesma: use `make lab LAB=<nome_do_lab>` para iniciar um novo laboratório.

### 10. Desenvolvendo os Projetos Finais

Após concluir todos os módulos, você estará pronto para enfrentar os projetos finais! As instruções para cada projeto estão nos respectivos diretórios em `capstones/`.

## Módulos do Curso

*   **SDKs:** Fundamentos de APIs de IA.
*   **MCP (Model Context Protocol):** Protocolo de contexto de modelo.
*   **Agents:** Sistemas de IA autônomos.
*   **AgentKit:** Implantação em produção.

## Projetos Finais

*   **Leitor de PDF Médico:** Um analisador de documentos médicos didático.
*   **Agente de Atendimento ao Cliente B2C:** Um chatbot inteligente.

Bom aprendizado!
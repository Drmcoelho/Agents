# Capstone 2: B2C Customer Service Agent

An intelligent customer service agent with ChatKit UI for B2C interactions.

## Features

- **ChatKit UI**: Modern chat interface
- **Multi-turn Conversations**: Context-aware dialogue
- **Intent Recognition**: Understand customer needs
- **Knowledge Base**: Answer common questions
- **Escalation**: Route complex issues to humans
- **Metrics**: Track conversation quality and satisfaction
- **Multi-language**: Support for multiple languages

## Architecture

```
┌──────────────┐
│   ChatKit    │ ← Web UI
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   WebSocket  │ ← Real-time communication
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Agent     │ ← LangChain Agent
└──────┬───────┘
       │
       ├─→ Intent Recognition
       ├─→ Knowledge Base (RAG)
       ├─→ Customer History
       └─→ Escalation Logic
       │
       ▼
┌──────────────┐
│   Response   │
└──────────────┘
```

## Prerequisites

- Completed all four modules (SDKs, MCP, Agents, AgentKit)
- Understanding of web development
- Knowledge of WebSockets

## Getting Started

```bash
# Install dependencies
make bootstrap

# Run the application
make capstone-b2c

# Or directly
cd capstones/b2c_service
python main.py
```

The application will start on `http://localhost:3000`

## Usage

### As a customer:
1. Open the web interface
2. Start chatting with the AI agent
3. Ask questions about products, orders, returns, etc.
4. Get instant, intelligent responses

### As a developer:
```python
from b2c_service import B2CAgent

agent = B2CAgent()

# Process a message
response = agent.process_message(
    message="I want to return my order",
    customer_id="12345"
)
print(response)
```

## Configuration

Configure in `.env`:
- `B2C_SERVICE_PORT`: Port for web server (default: 3000)
- `B2C_CHATKIT_THEME`: UI theme (light/dark)
- Guardrails for customer interactions
- Escalation thresholds

## Features to Implement

- [ ] Intent classification
- [ ] Knowledge base RAG
- [ ] Multi-turn conversation memory
- [ ] Sentiment analysis
- [ ] Escalation to human agents
- [ ] Conversation logging and metrics
- [ ] Multi-language support
- [ ] Customer satisfaction tracking

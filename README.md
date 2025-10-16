# Agents Course - 100% Practical AI Development

A comprehensive, hands-on course covering AI development through four core modules: **SDKs**, **MCP**, **Agents**, and **AgentKit**. Each module delivers executable labs, automated testing, and self-correction capabilities.

[![CI Status](https://github.com/Drmcoelho/Agents/workflows/CI/badge.svg)](https://github.com/Drmcoelho/Agents/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## 🎯 Course Overview

This course provides a practical, project-based learning experience for building AI applications. Everything runs in GitHub Codespaces with a unified Makefile for streamlined development.

### Four Core Modules

1. **SDKs** - Master OpenAI, Anthropic Claude, and Google Gemini APIs
2. **MCP** - Learn Model Context Protocol for tool integration
3. **Agents** - Build autonomous AI agents with LangChain
4. **AgentKit** - Deploy production-ready agent systems

### Capstone Projects

- 🏥 **Medical PDF Reader** - Didactic medical document analyzer
- 💬 **B2C Customer Service** - Intelligent customer support chatbot

## 🚀 Quick Start

### Prerequisites

- GitHub account (for Codespaces)
- API keys for at least one provider (OpenAI, Claude, or Gemini)

### Setup

1. **Open in Codespaces**
   ```bash
   # Click "Code" → "Codespaces" → "Create codespace on main"
   # Or clone locally:
   git clone https://github.com/Drmcoelho/Agents.git
   cd Agents
   ```

2. **Bootstrap the environment**
   ```bash
   make bootstrap
   ```

3. **Configure API keys**
   ```bash
   # Edit .env file with your API keys
   nano .env
   ```

4. **Verify setup**
   ```bash
   make check-env
   ```

## 📚 Learning Path

### Standard Workflow

```
bootstrap → lab → fix → evals → deploy
```

Each module follows this pattern:

1. **Bootstrap**: Setup environment and dependencies
2. **Lab**: Complete hands-on exercises
3. **Fix**: Get hints and auto-corrections via gabarito (answer key)
4. **Evals**: Run evaluations to assess progress
5. **Deploy**: Deploy working applications

### Module Progression

```
┌─────────┐
│  SDKs   │ → Fundamentals of AI APIs
└────┬────┘
     │
     ▼
┌─────────┐
│   MCP   │ → Tool integration & context
└────┬────┘
     │
     ▼
┌─────────┐
│ Agents  │ → Autonomous AI systems
└────┬────┘
     │
     ▼
┌──────────┐
│AgentKit  │ → Production deployment
└────┬─────┘
     │
     ▼
┌──────────┐
│Capstones │ → Real-world projects
└──────────┘
```

## 🛠️ Makefile Commands

### Essential Commands

```bash
make help           # Show all available commands
make bootstrap      # Initial setup (run once)
make check-env      # Verify configuration
make lab MODULE=sdks         # Run labs for a module
make fix MODULE=sdks         # Auto-correct with hints
make test                    # Run all tests
make test-module MODULE=sdks # Test specific module
make evals                   # Run progress evaluations
make passport               # Check your progress
```

### Capstone Commands

```bash
make capstone-medical  # Run Medical PDF Reader
make capstone-b2c      # Run B2C Customer Service
make deploy            # Deploy all applications
```

### Development Commands

```bash
make lint      # Run code linters
make format    # Format code
make clean     # Clean build artifacts
make ci        # Run all CI checks
```

## 🎓 Course Structure

```
Agents/
├── sdks/                    # SDK Module
│   ├── labs/               # Hands-on exercises
│   ├── tests/              # Automated tests
│   ├── solutions/          # Reference solutions
│   └── gabarito.json       # Auto-correction hints
├── mcp/                     # MCP Module
├── agents/                  # Agents Module
├── agentkit/               # AgentKit Module
├── capstones/
│   ├── medical_pdf_reader/ # Capstone 1
│   └── b2c_service/        # Capstone 2
├── shared/                  # Shared utilities
│   ├── check_env.py        # Environment checker
│   ├── gabarito.py         # Auto-correction system
│   ├── evaluator.py        # Progress evaluator
│   ├── passport.py         # Progress tracker
│   └── deploy.py           # Deployment manager
├── .devcontainer/          # Codespaces config
├── Makefile                # Unified command interface
├── requirements.txt        # Python dependencies
└── .env.example            # Configuration template
```

## 🔧 Multi-Backend Support

Configure your preferred AI backend in `.env`:

```bash
# Choose your backend
DEFAULT_BACKEND=openai  # or anthropic, google

# OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4-turbo-preview

# Anthropic Claude
ANTHROPIC_API_KEY=sk-ant-...
CLAUDE_MODEL=claude-3-opus-20240229

# Google Gemini
GOOGLE_API_KEY=...
GEMINI_MODEL=gemini-pro
```

## 🎫 Progress Tracking

Track your progress with the **Passport System**:

```bash
make passport
```

This shows:
- Module completion status
- Labs completed
- Overall progress percentage
- Unlocked capstones
- Achievements earned

## 🔒 Features

- ✅ **Auto-Correction**: Get hints and solutions via `make fix`
- ✅ **Multi-Backend**: Switch between OpenAI, Claude, and Gemini
- ✅ **Guardrails**: Safety checks and content filtering
- ✅ **Metrics**: Track performance and costs
- ✅ **ChatKit UI**: Modern chat interface for capstones
- ✅ **MCP Integration**: Both local and hosted MCP servers
- ✅ **CI/CD**: Automated testing and deployment
- ✅ **Progress Tracking**: Visual progress with passports

## 📦 Deployment

### Local Development
```bash
make deploy
```

### Production Deployment
See individual capstone READMEs for deployment instructions:
- [Medical PDF Reader Deployment](capstones/medical_pdf_reader/README.md)
- [B2C Service Deployment](capstones/b2c_service/README.md)

## 🧪 Testing

```bash
# Run all tests
make test

# Run tests for specific module
make test-module MODULE=sdks

# Run labs as tests
make lab MODULE=agents

# Run evaluations
make evals
```

## 📖 Documentation

Each module has detailed documentation:

- [SDKs Module](sdks/README.md)
- [MCP Module](mcp/README.md)
- [Agents Module](agents/README.md)
- [AgentKit Module](agentkit/README.md)
- [Medical PDF Reader](capstones/medical_pdf_reader/README.md)
- [B2C Service](capstones/b2c_service/README.md)

## 🤝 Contributing

This is an educational repository. Students are encouraged to:
- Complete labs and exercises
- Share solutions (after completing)
- Report issues or suggest improvements
- Add new labs or capstone projects

## 📄 License

MIT License - See LICENSE file for details

## 🆘 Support

- Check `make help` for available commands
- Use `make fix MODULE=<name>` for hints
- Review module READMEs for detailed guides
- Run `make check-env` to verify configuration

## 🎉 Getting Started Checklist

- [ ] Open in Codespaces or clone locally
- [ ] Run `make bootstrap`
- [ ] Configure `.env` with API keys
- [ ] Run `make check-env` to verify setup
- [ ] Start with `make lab MODULE=sdks`
- [ ] Track progress with `make passport`
- [ ] Complete capstones
- [ ] Deploy your projects!

---

**Ready to build AI applications? Start with `make bootstrap`!** 🚀

# Architecture Overview

This document explains the architecture and design decisions of the Agents Course.

## Repository Structure

```
Agents/
├── Module Directories (sdks, mcp, agents, agentkit)
├── Capstone Projects
├── Shared Utilities
├── Tests
└── Configuration Files
```

## Core Components

### 1. Module System

Each module follows a consistent structure:

```
module_name/
├── labs/           # Hands-on exercises
├── tests/          # Automated tests
├── solutions/      # Reference implementations
├── gabarito.json   # Auto-correction data
└── README.md       # Module documentation
```

**Design Rationale**: 
- Consistent structure makes navigation easy
- Separation of concerns (labs vs solutions vs tests)
- Self-contained modules can be worked on independently

### 2. Unified Makefile

The Makefile provides a single interface for all operations:

```makefile
bootstrap → lab → fix → evals → deploy
```

**Design Rationale**:
- Single command interface reduces cognitive load
- Consistent workflow across all modules
- Easy to extend with new commands
- Works in any environment (local, Codespaces, CI)

### 3. Gabarito (Answer Key) System

The gabarito system provides progressive hints and solutions:

```json
{
  "exercise_name": {
    "description": "...",
    "hints": ["hint1", "hint2"],
    "solution_file": "solution.py",
    "target_file": "lab.py"
  }
}
```

**Design Rationale**:
- Students can get hints without seeing full solutions
- Solutions are version-controlled separately
- Easy to add new exercises
- Supports automated correction

### 4. Multi-Backend Support

Environment-based backend selection:

```python
# .env
DEFAULT_BACKEND=openai  # or anthropic, google
```

**Design Rationale**:
- Students can use any AI provider
- No vendor lock-in
- Easy to switch between backends
- Cost flexibility

### 5. Progress Tracking (Passport)

JSON-based progress tracking:

```json
{
  "modules": {
    "sdks": {
      "status": "in_progress",
      "labs_completed": ["lab1", "lab2"],
      "progress": 50
    }
  }
}
```

**Design Rationale**:
- Visual feedback on progress
- Gamification through achievements
- Unlockable capstones
- Local storage (no server needed)

## Key Design Decisions

### 1. Python-First Approach

**Decision**: Use Python as primary language

**Rationale**:
- Most popular language for AI/ML
- Rich ecosystem of AI libraries
- Easy to learn and read
- Strong typing support with type hints

### 2. Executable Labs

**Decision**: Labs are runnable Python files with TODOs

**Rationale**:
- Students can test as they code
- Main function provides examples
- Self-documenting code
- Easy to verify correctness

### 3. Test-Driven Learning

**Decision**: Include tests for each lab

**Rationale**:
- Immediate feedback on correctness
- Teaches testing best practices
- Automated evaluation
- Industry-standard approach

### 4. Devcontainer Support

**Decision**: Include full devcontainer config

**Rationale**:
- Zero setup in Codespaces
- Consistent environment for all students
- Pre-installed extensions
- Automated bootstrap

### 5. Incremental Complexity

**Decision**: Modules build on each other

**Rationale**:
```
SDKs (basics) → MCP (integration) → Agents (autonomy) → AgentKit (production)
```
- Natural learning progression
- Each module adds concepts
- Can skip if experienced
- Clear prerequisites

## Module Architecture

### SDKs Module

**Purpose**: Learn AI API fundamentals

**Components**:
- OpenAI SDK labs
- Anthropic Claude labs
- Google Gemini labs
- Multi-backend abstraction

**Key Concepts**:
- API authentication
- Completion vs chat models
- Streaming responses
- Error handling

### MCP Module

**Purpose**: Connect AI to external tools

**Components**:
- MCP server implementation
- Tool registration
- Local and hosted servers
- Context management

**Key Concepts**:
- Model Context Protocol
- Tool schemas
- Server/client architecture
- Resource management

### Agents Module

**Purpose**: Build autonomous AI systems

**Components**:
- ReAct agent pattern
- Multi-agent systems
- Tool composition
- Agent memory

**Key Concepts**:
- Reasoning and acting
- Agent coordination
- State management
- Self-correction

### AgentKit Module

**Purpose**: Production-ready deployment

**Components**:
- Monitoring and metrics
- Error recovery
- Orchestration patterns
- Testing frameworks

**Key Concepts**:
- Production best practices
- Observability
- Cost optimization
- Deployment strategies

## Capstone Architecture

### Medical PDF Reader

**Architecture**:
```
PDF → Extraction → Chunking → Embeddings → Vector Store → RAG → Response
```

**Components**:
- PDF parser (PyMuPDF/PDFPlumber)
- Text chunker (semantic)
- Embedding generator
- Vector store (in-memory)
- RAG chain
- Safety guardrails

### B2C Customer Service

**Architecture**:
```
User → WebSocket → Agent → Tools → Knowledge Base → Response → UI
```

**Components**:
- Flask web server
- WebSocket handler
- Intent classifier
- Knowledge base (RAG)
- Escalation logic
- ChatKit UI (HTML/JS)

## Testing Strategy

### Test Pyramid

```
        ╱╲         E2E Tests (few)
       ╱  ╲
      ╱────╲       Integration Tests (some)
     ╱      ╲
    ╱────────╲     Unit Tests (many)
   ╱          ╲
```

### Test Types

1. **Structure Tests**: Verify directory structure
2. **Unit Tests**: Test individual functions
3. **Integration Tests**: Test module interactions
4. **E2E Tests**: Test complete workflows

## CI/CD Pipeline

```
Push → Lint → Test → Module Tests → Deploy
```

**Stages**:
1. Code linting (Ruff, Black)
2. Unit tests
3. Module-specific tests
4. Coverage reporting
5. Deploy (manual trigger)

## Extensibility

### Adding New Modules

1. Create module directory structure
2. Add labs, tests, solutions
3. Create gabarito.json
4. Update Makefile
5. Add CI tests
6. Document in README

### Adding New Labs

1. Create lab file in `labs/`
2. Add solution in `solutions/`
3. Write tests in `tests/`
4. Update gabarito.json
5. Update module README

### Adding New Capstones

1. Create capstone directory
2. Implement main application
3. Add README with architecture
4. Add to Makefile
5. Update main README

## Security Considerations

### API Keys

- Stored in `.env` (gitignored)
- Never committed to repository
- Optional test mode for CI
- Per-backend configuration

### User Data

- No user data collection
- Local progress tracking
- No external analytics
- Privacy-first design

## Performance Considerations

### API Costs

- Configurable models (cheaper options available)
- Test mode to avoid API calls
- Local caching where possible
- Cost tracking utilities

### Resource Usage

- Minimal dependencies
- In-memory data structures
- No database required
- Lightweight web servers

## Future Enhancements

### Planned Features

- [ ] Interactive web UI for all modules
- [ ] Real-time collaboration features
- [ ] More advanced capstones
- [ ] Video tutorials
- [ ] Community solutions gallery
- [ ] Automated grading system
- [ ] Certificate generation

### Potential Modules

- [ ] Fine-tuning module
- [ ] Embeddings and vector stores
- [ ] Prompt engineering
- [ ] AI safety and alignment
- [ ] Multi-modal AI
- [ ] Deployment and scaling

## References

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Python Best Practices](https://docs.python-guide.org/)

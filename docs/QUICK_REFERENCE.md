# Quick Reference

Fast access to common commands and resources.

## Essential Commands

```bash
# Setup
make bootstrap          # Initial setup
make check-env          # Verify configuration

# Learning
make lab MODULE=sdks    # Run labs
make fix MODULE=sdks    # Get hints

# Progress
make passport           # Check progress
make evals             # Run evaluations

# Testing
make test              # Run all tests
make lint              # Check code style

# Help
make help              # Show all commands
```

## Module Order

1. **SDKs** - AI API fundamentals
2. **MCP** - Tool integration
3. **Agents** - Autonomous systems
4. **AgentKit** - Production deployment
5. **Capstones** - Real projects

## File Locations

### Configuration
- `.env` - API keys and settings
- `.env.example` - Configuration template
- `pyproject.toml` - Python config

### Documentation
- `README.md` - Main documentation
- `docs/GETTING_STARTED.md` - Setup guide
- `docs/ARCHITECTURE.md` - Design docs
- `CONTRIBUTING.md` - Contribution guide
- `{module}/README.md` - Module guides

### Code
- `{module}/labs/` - Exercises
- `{module}/solutions/` - Solutions
- `{module}/tests/` - Tests
- `shared/` - Utilities

## Environment Variables

### Required
```bash
DEFAULT_BACKEND=openai   # or anthropic, google
```

### OpenAI
```bash
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-3.5-turbo
```

### Anthropic
```bash
ANTHROPIC_API_KEY=sk-ant-...
CLAUDE_MODEL=claude-3-opus-20240229
```

### Google
```bash
GOOGLE_API_KEY=...
GEMINI_MODEL=gemini-pro
```

## Common Issues

### "Module not found"
```bash
make bootstrap
```

### "API key not found"
```bash
# Edit .env and add your key
nano .env
make check-env
```

### Tests failing
```bash
# Check test mode
# Set TEST_MODE=false for real API calls
nano .env
```

## Workflow

```
1. Bootstrap → 2. Lab → 3. Fix → 4. Eval → 5. Deploy
```

## Learning Path

```
SDKs (basics)
  ↓
MCP (integration)
  ↓
Agents (autonomy)
  ↓
AgentKit (production)
  ↓
Capstones (practice)
```

## Progress Tracking

```bash
make passport      # Check progress
```

Shows:
- Module completion
- Labs finished
- Overall percentage
- Achievements

## Testing

```bash
# All tests
make test

# Specific module
make test-module MODULE=sdks

# Single lab
pytest sdks/labs/test_lab1.py -v
```

## Code Quality

```bash
make lint          # Check style
make format        # Auto-format
make ci            # Run all checks
```

## Capstones

```bash
# Medical PDF Reader
make capstone-medical

# B2C Customer Service
make capstone-b2c

# Deploy all
make deploy
```

## Getting Help

1. **Built-in hints**: `make fix MODULE=<name>`
2. **Module docs**: Check `{module}/README.md`
3. **Test examples**: Look at test files
4. **GitHub issues**: Report bugs/questions

## Tips

- **Save often**: Git commits after each exercise
- **Test early**: Run tests while coding
- **Use hints**: Don't struggle alone
- **Read errors**: Error messages are helpful
- **Check examples**: Look at test files

## Resources

- [OpenAI Docs](https://platform.openai.com/docs/)
- [Anthropic Docs](https://docs.anthropic.com/)
- [LangChain Guide](https://python.langchain.com/)
- [MCP Spec](https://modelcontextprotocol.io/)

## Next Steps

1. Run `make bootstrap`
2. Configure `.env`
3. Start with `make lab MODULE=sdks`
4. Use `make passport` to track progress
5. Complete all modules
6. Build capstone projects!

---

**Need more details?** Check `docs/GETTING_STARTED.md`

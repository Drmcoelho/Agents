# SDKs Module

This module covers AI SDK fundamentals with hands-on labs for OpenAI, Anthropic Claude, and Google Gemini.

## Labs

1. **Lab 1: OpenAI SDK Basics**
   - Setting up OpenAI client
   - Making your first completion
   - Working with chat models
   - Streaming responses

2. **Lab 2: Anthropic Claude SDK**
   - Claude API configuration
   - Creating conversations
   - Working with system prompts
   - Multi-turn conversations

3. **Lab 3: Google Gemini SDK**
   - Gemini API setup
   - Text generation
   - Multi-modal inputs
   - Safety settings

4. **Lab 4: Multi-Backend Abstraction**
   - Creating a unified interface
   - Switching between backends
   - Error handling and retries
   - Cost tracking

## Learning Objectives

- Understand the core concepts of AI SDKs
- Work with multiple AI providers
- Handle streaming and async operations
- Implement error handling and best practices

## Prerequisites

- Python 3.11+
- API keys for OpenAI, Anthropic, and/or Google

## Getting Started

```bash
# Run all SDK labs
make lab MODULE=sdks

# Run specific lab
pytest sdks/labs/test_lab1_openai.py -v

# Get hints and solutions
make fix MODULE=sdks
```

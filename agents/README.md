# Agents Module

This module covers AI agent development using LangChain and related frameworks.

## Labs

1. **Lab 1: Simple ReAct Agent**
   - Understanding agent architectures
   - Building a ReAct (Reasoning + Acting) agent
   - Tool selection and execution
   - Agent memory and state

2. **Lab 2: Multi-Agent Systems**
   - Agent communication patterns
   - Coordinating multiple agents
   - Task delegation and planning
   - Conflict resolution

3. **Lab 3: Agent Tools and Skills**
   - Creating custom agent tools
   - Tool composition
   - Dynamic tool loading
   - Error recovery

4. **Lab 4: Advanced Agent Patterns**
   - Self-correction and reflection
   - Chain-of-thought reasoning
   - Tree of thought exploration
   - Agent evaluation metrics

## Learning Objectives

- Build autonomous AI agents
- Implement agent reasoning patterns
- Create and compose agent tools
- Design multi-agent systems

## Prerequisites

- Completed SDKs and MCP modules
- Understanding of LangChain
- Async programming knowledge

## Getting Started

```bash
# Run all Agent labs
make lab MODULE=agents

# Run specific lab
pytest agents/labs/test_lab1_react.py -v

# Get hints and solutions
make fix MODULE=agents
```

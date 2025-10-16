# Getting Started Guide

Welcome to the Agents Course! This guide will walk you through setting up your environment and starting your first lab.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Options](#setup-options)
3. [Initial Configuration](#initial-configuration)
4. [Your First Lab](#your-first-lab)
5. [Understanding the Workflow](#understanding-the-workflow)
6. [Troubleshooting](#troubleshooting)

## Prerequisites

### Required

- **GitHub Account**: For Codespaces or cloning the repository
- **API Keys**: At least one of:
  - OpenAI API key ([get one here](https://platform.openai.com/api-keys))
  - Anthropic Claude API key ([get one here](https://console.anthropic.com/))
  - Google Gemini API key ([get one here](https://makersuite.google.com/app/apikey))

### Recommended

- Basic Python knowledge
- Understanding of REST APIs
- Familiarity with command line

## Setup Options

### Option 1: GitHub Codespaces (Recommended)

The easiest way to get started:

1. Navigate to https://github.com/Drmcoelho/Agents
2. Click the **Code** button
3. Select **Codespaces** tab
4. Click **Create codespace on main**

Codespaces will automatically:
- Set up the development environment
- Install all dependencies
- Configure VS Code with helpful extensions

### Option 2: Local Development

Clone and set up locally:

```bash
# Clone the repository
git clone https://github.com/Drmcoelho/Agents.git
cd Agents

# Run bootstrap (installs dependencies)
make bootstrap
```

#### Local Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Node.js 18+ (for web UI components)
- Git

## Initial Configuration

### 1. Configure Environment Variables

After bootstrap completes, you'll have a `.env` file. Edit it:

```bash
# Open in your editor
nano .env

# Or use VS Code
code .env
```

### 2. Add Your API Keys

Add at least one API key:

```bash
# For OpenAI
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-3.5-turbo

# For Claude
ANTHROPIC_API_KEY=sk-ant-your-key-here
CLAUDE_MODEL=claude-3-opus-20240229

# For Gemini
GOOGLE_API_KEY=your-key-here
GEMINI_MODEL=gemini-pro

# Set your default backend
DEFAULT_BACKEND=openai  # or anthropic, google
```

### 3. Verify Configuration

```bash
make check-env
```

You should see a success message and your configured backends.

## Your First Lab

Let's complete your first exercise in the SDKs module!

### Step 1: View Available Modules

```bash
# See all modules
ls -d */

# Read about SDKs module
cat sdks/README.md
```

### Step 2: Open the First Lab

```bash
# View the lab file
cat sdks/labs/lab1_openai.py
```

You'll see exercises with `TODO` comments indicating what to implement.

### Step 3: Implement the Exercises

Open `sdks/labs/lab1_openai.py` in your editor and implement the exercises.

For Exercise 1 (Simple Completion), you need to:

```python
def exercise_1_simple_completion(self, prompt: str) -> str:
    response = self.client.chat.completions.create(
        model=self.model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
```

### Step 4: Test Your Implementation

```bash
# Run the lab file directly to test
python sdks/labs/lab1_openai.py

# Or run the tests
pytest sdks/tests/test_lab1_openai.py -v
```

### Step 5: Need Help?

If you're stuck, use the gabarito system:

```bash
# Get hints for an exercise
make fix MODULE=sdks

# Follow the prompts to:
# - See hints
# - View the solution
# - Apply automatic fixes
```

### Step 6: Run All Module Tests

Once you've completed all exercises:

```bash
make lab MODULE=sdks
```

## Understanding the Workflow

### The Standard Flow

```
1. bootstrap → 2. lab → 3. fix → 4. evals → 5. deploy
```

1. **Bootstrap**: Initial setup (run once)
2. **Lab**: Complete exercises and labs
3. **Fix**: Get hints and solutions when stuck
4. **Evals**: Run evaluations to check progress
5. **Deploy**: Deploy your capstone projects

### Key Commands

```bash
# View all commands
make help

# Setup
make bootstrap        # Initial setup
make check-env        # Verify configuration

# Learning
make lab MODULE=sdks  # Run labs for a module
make fix MODULE=sdks  # Get hints and solutions

# Progress
make passport         # Check your progress
make evals           # Run evaluations

# Testing
make test            # Run all tests
make test-module MODULE=sdks  # Test specific module

# Code Quality
make lint            # Check code style
make format          # Format code

# Cleanup
make clean           # Clean build artifacts
```

### Progress Tracking

Check your progress anytime:

```bash
make passport
```

This shows:
- Modules completed
- Labs finished
- Overall progress percentage
- Unlocked capstones
- Achievements earned

## Module Progression

Follow this order for best results:

1. **SDKs** (Start here)
   - Learn AI API fundamentals
   - Work with OpenAI, Claude, Gemini
   - Master prompting and streaming

2. **MCP** (Model Context Protocol)
   - Understand tool integration
   - Build MCP servers
   - Connect AI to external systems

3. **Agents**
   - Create autonomous agents
   - Implement ReAct pattern
   - Multi-agent coordination

4. **AgentKit**
   - Production deployment
   - Monitoring and optimization
   - Advanced patterns

5. **Capstones**
   - Medical PDF Reader
   - B2C Customer Service

## Troubleshooting

### "Module not found" errors

```bash
# Reinstall dependencies
make bootstrap
```

### API key issues

```bash
# Check your configuration
make check-env

# Verify .env file exists and has correct keys
cat .env
```

### Tests failing

```bash
# Check if you're in test mode
# Set TEST_MODE=false in .env for API calls
nano .env
```

### Import errors

```bash
# Make sure you're in the project root
cd /path/to/Agents

# Check Python path
echo $PYTHONPATH
```

### "Command not found" errors

```bash
# Make sure make is installed
make --version

# On Ubuntu/Debian
sudo apt-get install make

# On macOS
xcode-select --install
```

## Next Steps

1. ✅ Complete SDKs module labs
2. ✅ Move to MCP module
3. ✅ Build your first agent
4. ✅ Learn AgentKit patterns
5. ✅ Complete capstone projects

## Resources

- **Module READMEs**: Each module has detailed documentation
- **Gabarito System**: Built-in hints and solutions
- **Tests**: Example usage in test files
- **Community**: Open issues for questions

## Getting Help

- Run `make help` for command reference
- Check module READMEs for detailed guides
- Use `make fix MODULE=<name>` for exercise hints
- Open GitHub issues for bugs or questions

Happy learning! 🚀

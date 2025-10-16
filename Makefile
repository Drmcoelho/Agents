.PHONY: help bootstrap lab fix evals deploy test clean install lint format check-env

# Default target
.DEFAULT_GOAL := help

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)Agents Course - Unified Makefile$(NC)"
	@echo ""
	@echo "$(GREEN)Available targets:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(BLUE)%-15s$(NC) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(GREEN)Usage examples:$(NC)"
	@echo "  make bootstrap          # Initial setup"
	@echo "  make lab MODULE=sdks    # Run labs for a specific module"
	@echo "  make fix MODULE=mcp     # Auto-correct with gabarito"
	@echo "  make test               # Run all tests"
	@echo "  make deploy             # Deploy applications"

bootstrap: ## Initial setup - install dependencies and configure environment
	@echo "$(BLUE)🚀 Bootstrapping Agents Course...$(NC)"
	@if [ ! -f .env ]; then \
		echo "$(YELLOW)⚠️  Creating .env from template...$(NC)"; \
		cp .env.example .env; \
		echo "$(GREEN)✓ Please configure your API keys in .env$(NC)"; \
	fi
	@echo "$(BLUE)📦 Installing Python dependencies...$(NC)"
	@pip install --upgrade pip
	@pip install -r requirements.txt
	@if [ -f requirements-dev.txt ]; then \
		pip install -r requirements-dev.txt; \
	fi
	@echo "$(BLUE)📦 Installing Node dependencies...$(NC)"
	@if [ -f package.json ]; then \
		npm install; \
	fi
	@echo "$(BLUE)🔧 Setting up pre-commit hooks...$(NC)"
	@if command -v pre-commit >/dev/null 2>&1; then \
		pre-commit install; \
	fi
	@echo "$(GREEN)✅ Bootstrap complete!$(NC)"

check-env: ## Check if environment is properly configured
	@echo "$(BLUE)🔍 Checking environment configuration...$(NC)"
	@if [ ! -f .env ]; then \
		echo "$(RED)❌ .env file not found. Run 'make bootstrap' first.$(NC)"; \
		exit 1; \
	fi
	@python shared/check_env.py
	@echo "$(GREEN)✅ Environment check passed!$(NC)"

install: bootstrap ## Alias for bootstrap

lab: check-env ## Run labs for a specific module (MODULE=sdks|mcp|agents|agentkit)
	@if [ -z "$(MODULE)" ]; then \
		echo "$(RED)❌ Please specify MODULE (e.g., make lab MODULE=sdks)$(NC)"; \
		exit 1; \
	fi
	@echo "$(BLUE)🔬 Running $(MODULE) labs...$(NC)"
	@python -m pytest $(MODULE)/labs/ -v --color=yes
	@echo "$(GREEN)✅ Labs complete!$(NC)"

fix: check-env ## Auto-correct with gabarito (answer key) for a module
	@if [ -z "$(MODULE)" ]; then \
		echo "$(RED)❌ Please specify MODULE (e.g., make fix MODULE=sdks)$(NC)"; \
		exit 1; \
	fi
	@echo "$(BLUE)🔧 Running auto-correction for $(MODULE)...$(NC)"
	@python shared/gabarito.py $(MODULE)
	@echo "$(GREEN)✅ Auto-correction complete!$(NC)"

evals: check-env ## Run evaluations to assess progress
	@echo "$(BLUE)📊 Running evaluations...$(NC)"
	@python shared/evaluator.py
	@echo "$(GREEN)✅ Evaluations complete!$(NC)"

test: ## Run all tests
	@echo "$(BLUE)🧪 Running all tests...$(NC)"
	@python -m pytest tests/ -v --color=yes --cov=. --cov-report=term-missing
	@echo "$(GREEN)✅ All tests passed!$(NC)"

test-module: ## Run tests for a specific module (MODULE=sdks|mcp|agents|agentkit)
	@if [ -z "$(MODULE)" ]; then \
		echo "$(RED)❌ Please specify MODULE (e.g., make test-module MODULE=sdks)$(NC)"; \
		exit 1; \
	fi
	@echo "$(BLUE)🧪 Running tests for $(MODULE)...$(NC)"
	@python -m pytest $(MODULE)/tests/ -v --color=yes
	@echo "$(GREEN)✅ Tests complete!$(NC)"

lint: ## Run linters on all code
	@echo "$(BLUE)🔍 Running linters...$(NC)"
	@ruff check .
	@black --check .
	@echo "$(GREEN)✅ Linting complete!$(NC)"

format: ## Format all code
	@echo "$(BLUE)✨ Formatting code...$(NC)"
	@black .
	@ruff check --fix .
	@echo "$(GREEN)✅ Formatting complete!$(NC)"

deploy: check-env ## Deploy applications
	@echo "$(BLUE)🚀 Deploying applications...$(NC)"
	@if [ -n "$(TARGET)" ]; then \
		python shared/deploy.py $(TARGET); \
	else \
		python shared/deploy.py; \
	fi
	@echo "$(GREEN)✅ Deployment complete!$(NC)"

capstone-medical: check-env ## Run Medical PDF Reader capstone
	@echo "$(BLUE)🏥 Running Medical PDF Reader capstone...$(NC)"
	@cd capstones/medical_pdf_reader && python main.py
	@echo "$(GREEN)✅ Capstone complete!$(NC)"

capstone-b2c: check-env ## Run B2C Customer Service capstone
	@echo "$(BLUE)💬 Running B2C Customer Service capstone...$(NC)"
	@cd capstones/b2c_service && python main.py
	@echo "$(GREEN)✅ Capstone complete!$(NC)"

passport: ## Check progress passport
	@echo "$(BLUE)🎫 Checking your progress passport...$(NC)"
	@python shared/passport.py
	@echo "$(GREEN)✅ Passport checked!$(NC)"

clean: ## Clean build artifacts and cache files
	@echo "$(BLUE)🧹 Cleaning up...$(NC)"
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@rm -rf .coverage htmlcov/ 2>/dev/null || true
	@rm -rf dist/ build/ 2>/dev/null || true
	@echo "$(GREEN)✅ Cleanup complete!$(NC)"

ci: lint test ## Run CI checks (lint + test)
	@echo "$(GREEN)✅ All CI checks passed!$(NC)"

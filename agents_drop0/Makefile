SHELL := /bin/bash

.PHONY: bootstrap docs status

bootstrap:
	@echo '[bootstrap] preparando ambiente mínimo'
	@mkdir -p env labs/.templates .passports
	@if [ ! -f env/.env.example ]; then cp env/.env.example env/.env.example; fi
	@echo 'OK.'

docs:
	@echo 'docs/agents/00_conceitos_iniciais.md'

status:
	@echo 'Passports:'
	@ls -1 .passports 2>/dev/null || echo '(vazio)'

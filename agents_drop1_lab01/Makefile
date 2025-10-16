SHELL := /bin/bash

.PHONY: bootstrap docs status lab fix

bootstrap:
	@echo '[bootstrap] instalando deps mínimas (stub)'
	@mkdir -p env labs/.templates .passports
	@cp -n env/.env.example env/.env.local 2>/dev/null || true
	@echo 'OK.'

docs:
	@echo 'docs/agents/00_conceitos_iniciais.md'

status:
	@echo 'Passports:'
	@ls -1 .passports 2>/dev/null || echo '(vazio)'

lab:
	@LAB=${LAB}; if [ -z "$$LAB" ]; then echo 'Use: make lab LAB=01_sdk_boot'; exit 1; fi
	@bash labs/$$LAB/run.sh

fix:
	@LAB=${LAB}; if [ -z "$$LAB" ]; then echo 'Use: make fix LAB=01_sdk_boot'; exit 1; fi
	@bash labs/$$LAB/fix.sh

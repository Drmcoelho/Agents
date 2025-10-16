SHELL := /bin/bash

.PHONY: bootstrap lab fix

bootstrap:
	@echo '[bootstrap] preparando Drop 2 (sem deps externas)'
	@mkdir -p env .passports

lab:
	@LAB=${LAB}; if [ -z "$$LAB" ]; then echo 'Use: make lab LAB=02_mcp'; exit 1; fi
	@bash labs/$$LAB/run.sh

fix:
	@LAB=${LAB}; if [ -z "$$LAB" ]; then echo 'Use: make fix LAB=02_mcp'; exit 1; fi
	@bash labs/$$LAB/fix.sh

.PHONY: help setup build serve test

help:
	@echo 'Makefile for pyconuk.org'
	@echo ''
	@echo 'Usage:'
	@echo '   make setup    create virtualenv and install requirements'
	@echo '   make build    build the site into the output directory'
	@echo '   make serve    build the site and serve on port 8000, watching for changes'
	@echo '   make test     test that site builds, has no broken links, and spells the conference name correctly'
	@echo ''

setup:
	virtualenv .venv; . .venv/bin/activate; pip install -r requirements.txt

build:
	. .venv/bin/activate; wok

serve:
	. .venv/bin/activate; wok --serve

test:
	. .venv/bin/activate; python test_ssl_import.py

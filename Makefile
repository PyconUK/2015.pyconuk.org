.PHONY: help build serve test

help:
	@echo 'Makefile for pyconuk.org'
	@echo ''
	@echo 'Usage:'
	@echo '   make build    build the site into the output directory'
	@echo '   make serve    build the site and serve on port 8000, watching for changes'
	@echo '   make test     test that site builds, has no broken links, and spells the conference name correctly'
	@echo ''

build:
	wok

serve:
	wok --serve

test:
	./pre-flight-checks.sh

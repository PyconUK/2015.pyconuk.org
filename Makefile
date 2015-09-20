.PHONY: help build serve test deploy

help:
	@echo 'Makefile for pyconuk.org'
	@echo ''
	@echo 'Usage:'
	@echo '   make build    build the site into the output directory'
	@echo '   make serve    build the site and serve on port 8000, watching for changes'
	@echo '   make test     test that site builds, has no broken links, and spells the conference name correctly'
	@echo '   make deploy   deploy site'
	@echo ''

build:
	python hooks/flat_schedule.py
	python hooks/guidebook.py
	python hooks/schedule_summary.py
	wok

serve:
	python hooks/flat_schedule.py
	python hooks/guidebook.py
	python hooks/schedule_summary.py
	wok --serve

test:
	./pre-flight-checks.sh

deploy:
	./deploy.sh

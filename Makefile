.PHONY: help build serve

help:
	@echo 'Makefile for pyconuk.org'
	@echo ''
	@echo 'Usage:'
	@echo '   make build                       build the site into the output directory'
	@echo '   make serve                       build the site and serve on port 8000, watching for changes'
	@echo ''

build:
	virtualenv venv
	( \
	. venv/bin/activate; \
	pip install -r requirements.txt; \
	wok; \
	echo ''; \
	echo 'Build complete. Now run "make serve" to view the website'; \
	echo 'You can remove the venv/ directory when you are finished.'; \
	)

serve:
	( \
	. venv/bin/activate; \
	wok --serve; \
	)


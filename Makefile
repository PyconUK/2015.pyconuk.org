help:
	@echo 'Makefile for pyconuk.org'
	@echo ''
	@echo 'Usage:'
	@echo '   make build                       build the site into the output directory
	@echo '   make serve                       build the site and serve on port 8000, watching for changes
	@echo ''

build:
	wok

serve:
	wok --serve


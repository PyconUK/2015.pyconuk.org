help:
	@echo 'Makefile for pyconuk.org'
	@echo ''
	@echo 'Usage:'
	@echo '   make build                       build the docker container'
	@echo '   make run                         run the docker container'
	@echo ''

build:
	docker build -t pyconuk.org .

run:
	docker run -p 80:4000 -v $(pwd):/opt/pyconuk/site:rw -ti pyconuk.org

export COMPOSE_FILE=./Docker/dev/docker-compose-dev.yml
export COMPOSE_PROJECT_NAME=comeo

include ./tools/Makefile-base

test: stop
	cd ./Docker/test && make test

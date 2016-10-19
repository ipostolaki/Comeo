# This Makefile is used for the development environment

export COMPOSE_FILE=./Docker/dev/docker-compose-dev.yml
export COMPOSE_PROJECT_NAME=comeo_dev

include ./tools/Makefile-base

test: stop
	cd ./Docker/test && make test

flake:
	flake8 --config=.flake8 .
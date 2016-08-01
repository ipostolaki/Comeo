# TODO: makefiles inheritance

export COMPOSE_FILE=./docker-compose-test.yml
export COMPOSE_PROJECT_NAME=comeo_test

.PHONY: logs

default: build

test: stop
    # docker-compose will run tests after db containers readiness; db containers will be stopped after tests
	-docker rm comeotest_neo_1  # remove neo4j container and related data volume before tests run
	-docker volume rm comeotest_neo_data
	docker-compose up --abort-on-container-exit --no-recreate

build:
	docker-compose build

stop:
	docker-compose stop
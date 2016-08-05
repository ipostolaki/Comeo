export COMPOSE_FILE=./docker-compose-test.yml
export COMPOSE_PROJECT_NAME=comeo_test

default: build

test: stop
	# remove neo4j container and related data volume before tests run
	-docker rm comeotest_neo_1
	-docker volume rm comeotest_neo_data
    # docker-compose will run tests after db containers readiness; db containers will be stopped after tests
	docker-compose up --abort-on-container-exit --no-recreate

build:
	docker-compose build

stop:
	docker-compose stop
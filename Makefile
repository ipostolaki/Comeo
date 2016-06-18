export COMPOSE_FILE=./Docker/dev/docker-compose-dev.yml
export COMPOSE_PROJECT_NAME=comeo

default: build

build:
	docker-compose build
run:
	docker-compose up
stop:
	docker-compose stop
migrate:
	docker-compose exec django ./manage.py migrate
migrations:
	docker-compose exec django ./manage.py makemigrations
django_bash:
	docker-compose exec django bash
django_shell:
	docker-compose exec django ./manage.py shell_plus
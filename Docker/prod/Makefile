default: build

build:
	docker-compose build
run:
	docker-compose up
migrate:
	docker-compose exec django ./manage.py migrate
migrations:
	docker-compose exec django ./manage.py makemigrations
django_bash:
	docker-compose exec django bash
django_shell:
	docker-compose exec django ./manage.py shell_plus
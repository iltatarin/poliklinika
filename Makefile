all:
	@echo "Commands:"
	@echo " run-postgres:   start Docker-container with PostgreSQL"
	@echo " remove-postgres:   remove Docker-container with PostgreSQL"
	@echo " run-server:     start django server listening 8040 port"
	@echo " test:           run pytest for django app"
	@echo ""
	@echo "Service commands:"
	@echo " collectstatic"
	@echo " createsuperuser"
	@echo " makemigrations"
	@echo " migrate"

run-postgres:
	docker run -d --rm --name poliklinika -e POSTGRES_PASSWORD=123456 -p 35432:5432 -v $(shell pwd)/docker/postgres_data:/var/lib/postgresql/data postgres:11

remove-postgres:
	docker rm -f poliklinika

run-server: migrate
	python3 poliklinika/manage.py runserver 0.0.0.0:8060

test:
	pytest poliklinikar

collectstatic:
	python3 poliklinika/manage.py collectstatic

makemigrations:
	python3 poliklinika/manage.py makemigrations

migrate:
	python3 poliklinika/manage.py migrate

createsuperuser:
	python3 poliklinika/manage.py createsuperuser

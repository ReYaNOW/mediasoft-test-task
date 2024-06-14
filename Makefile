PORT ?= 8080


install:
	poetry install --no-root
	make migrate
	poetry run python manage.py createsuperuser --noinput --username admin --email admin@mail.com || true

start:
	poetry run python manage.py runserver 0.0.0.0:$(PORT)

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

start-db:
	docker compose up -d

enter-db:
	docker compose exec -it db psql -U pguser -d pgdb psql

stop-db:
	docker compose stop || true

lint:
	flake8 shop_locator --exclude=settings.py,*/migrations/*


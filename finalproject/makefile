start:	
	docker compose run --rm web poetry run python manage.py runserver

migrate:
	docker compose run --rm web poetry run python manage.py migrate

migrations:
	docker compose run --rm web poetry run python manage.py makemigrations


createsuperuser:
	docker compose run --rm web poetry run python manage.py createsuperuser

new-app:
	poetry run python manage.py startapp $(app)
	@# to execute run 'make new-app app=cenas'

tests:
	poetry run pytest -vvv


compose.start:
	docker compose up --build --force-recreate

compose.migrate:
	docker compose run --rm web poetry run python manage.py migrate
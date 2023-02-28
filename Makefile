runserver:
	python manage.py runserver

makemig:
	python manage.py makemigrations

test:
	python manage.py test

test-cov:
	coverage run --source='.' manage.py test

xml:
	coverage xml

lint:
	poetry run flake8 task_manager --exclude migrations

install:
	poetry install

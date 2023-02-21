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

# build:
# 	poetry build

# package-install:
# 	python3 -m pip install --user dist/*.whl

# package-reinstall:
# 	python3 -m pip install --user --force-reinstall dist/*.whl

# tests:
# 	poetry run pytest

# test-cov:
# 	poetry run pytest --cov=page_loader --cov-report xml
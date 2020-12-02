#!/bin/sh

# wait for postgres container to start
while ! nc -z dd-postgres-dev 5432; do
    echo "postgres is unavailable. waiting ..." && sleep 20
done
echo "postgres is up" && sleep 10

# install dependencies
cd /code
pipenv install --dev

# change to application root
cd /code/application


# run migrations
pipenv run python manage.py migrate

## run to feed the data once
# pipenv run python manage.py loaddata application/fixtures/data/*

# coverage implementation
pipenv run coverage run -m pytest
pipenv run coverage html
# start dev server
pipenv run python manage.py runserver 0.0.0.0:8000
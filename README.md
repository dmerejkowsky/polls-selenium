# Django poll example app

## First run

Install Python >= 3.7

Install Poetry

Run `poetry install`

Run the migrations

```
$ poetry run python manage.py migrate
```

## Starting new

Delete *all* the data from the database

```
$ poetry run python manage.py flush
```

Load the test admin user

```
$ poetry run python manage.py loaddata tests/auth.json
```

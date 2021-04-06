# Django poll example app



## Setup

Install Google Chrome

Install Python >= 3.7

Install [Poetry](https://python-poetry.org/)


Run `poetry install`

Run the migrations

```
$ poetry run python manage.py migrate
```

Create a super user

```
$ poetry run python manage.py createsuperuser
```

## Running the server


```
$ poetry run python manage.py runserver
```

## Checking the server works

Visit `http://127.0.0.1:8000/admin`, login with the credentails
of the super user.

Create a question "Are you sure?" with two answers "Yes", and "No"

Visit `http://127.0.0.1:8000/polls`. You should be able to vote.

## Running selenium tests with Chrome

Visit:

https://sites.google.com/a/chromium.org/chromedriver/home
and download the latest stable release

Extract the archive

Create `C:\chromedriver`

Put `chromedriver.exe` inside `c:\chromedriver\chromedriver.exe`

Add `C:\chromedriver` to the PATH environment variable for your account.

Keep the server running, and type the following commands in a new window:

```
set PYTHONBREAKPOIRT=ipdb.set_trace
poetry run pytest -vs
```

You should get:

* A Chrome instance controlled by Python
* And an interactive Python shell where you can type code that Chrome executes.


## Resetting the database

Visit the `polls/reset` URL

## Instructions

Try and write a test that
* resets the DB
* creates a poll
* votes one on answer

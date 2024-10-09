# Initial Set Up


# The first step is to create a dedicated directory for our code

```
cd onedrive\desktop\
mkdir Django
cd Django
```

# Next, activate a new virtual environment called .venv.

```
python -m venv .venv
.venv\Scripts\Activate.ps1
 python -m pip install django~=5.0
 ```

# Then install Django, create a new Django project, and run migrate to initialize the new database, and execute runserver to start up the local web server provided by Django.
```
django-admin startproject django_project .
python manage.py migrate
 python manage.py runserver
 ```

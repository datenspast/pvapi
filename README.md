# PV API Tutorial

Requirements: Python and pipenv installed

## Prepare environment

```
mkdir pvapi
cd pvapi
pipenv install
pipenv shell
pipenv install django djangorestframework gunicorn whitenoise install django-heroku
```

## Prepare Django App and make it ready for Heroku deploy
Create Django Project:

`django-admin startproject pvapi`

Move the pipfile and pipfile.loc to the root directory (same as manage.py)
Add a Procfile to the root directory (same as pipfile)

`web: gunicorn myproject.wsgi`

Add the following import statement to the top of settings.py:

`import django_heroku`

Then add the following to the bottom of settings.py:
```
# Activate Django-Heroku.
django_heroku.settings(locals())
```
Make sure the app is running: 

```
cd pvapi
python manage.py runserver 8001
```

Visit http://127.0.0.1:8001/. You should see the default Django Start page.



## Deploy to heroku via git
Initialize a git repository in the project root and commit changes.
```
git init
git commit
```




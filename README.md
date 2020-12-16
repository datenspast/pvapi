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

`web: gunicorn pvapi.wsgi`

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
Add a `.gitignore` file to the project root direcotry.
```
*.pyc
*.db
*~
.*

/site/
/htmlcov/
/coverage/
/build/
/dist/
/*.egg-info/
/env/
MANIFEST
coverage.*

!.gitignore
!.travis.yml
!.isort.cfg

```
Initialize a new git repository in the project root and commit changes.
```
git init
git commit .
```

Add a new Repository to github and push the changes.
```
git remote add origin https://github.com/YOURGITHUBNAME/pvapi.git
git branch -M master
git push -u origin master
```

Create a new heroku app and select GitHub as deployment method.
Connect to the repository and hit "manual deploy".
View the app. You should see the Django start page.

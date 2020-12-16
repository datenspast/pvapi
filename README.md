# PV API Tutorial

Requirements: Python and pipenv installed

## Prepare environment

```
mkdir pvapi
cd pvapi
pipenv install
pipenv shell
pipenv install django djangorestframework gunicorn whitenoise django-heroku django-url-filter
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

Juhu!

## Prepare the REST API

Create a new django app: `python manage.py startapp api`.
Add following to the `INSTALLED_APPS` Array in `pvapi/settings.py`:

```
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'api',
]
```

Modify the newly created `models.py` in the folder `api`.
```
from django.db import models

class YieldPerKwp(models.Model):
    state = models.CharField("State", max_length=50)
    yield_kWp = models.IntegerField("Yield in kWh/kWp/a")

    def __str__(self):
        return self.state + ": " + str(self.yield_kWp)
```
Migrate the changes:
```
python manage.py makemigrations
python manage.py migrate
```

Add a new file `serializers.py` into the `/api` folder:
```
from rest_framework import serializers
from .models import YieldPerKwp


class YieldPerKwpSerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldPerKwp
        fields = ('yield_kWp', 'state')
```

Write a view in `api/views.py`.

```
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import YieldPerKwpSerializer
from .models import YieldPerKwp

class YieldPerKwpViewSet(viewsets.ModelViewSet):
    queryset = YieldPerKwp.objects.all()
    serializer_class = YieldPerKwpSerializer

```

Add a new file `api/urls.py`:

```
from rest_framework.routers import DefaultRouter
import views

router = DefaultRouter()
router.register(r'pv_yield', views.YieldPerKwpViewSet, basename='pv_yield')
urlpatterns = router.urls
```

To register the urls in the `pv_api/urls.py` file, make following changes:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

Check if it works and visit: http://127.0.0.1:8001/api/ -> You should see the Django Rest View of the request.

## Add Date via the Django Admin interface

First, register the model in the `api/admin.py`:

```
from django.contrib import admin
from .models import YieldPerKwp

class YieldPerKwpAdmin(admin.ModelAdmin):
    pass

admin.site.register(YieldPerKwp, YieldPerKwpAdmin)
```
Create a Admin-Superuser: `python manage.py createsuperuser`
Visit http://127.0.0.1:8001/admin/, log in and add some data.
Visit http://127.0.0.1:8001/api/pv_yield/ and see the data as served by the API.

## Filtering
Add the following to the `pvapi/settings.py`:
```
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'url_filter.integrations.drf.DjangoFilterBackend',
    ],
}
```
Add modify the `api/views.py`:

```
class YieldPerKwpViewSet(viewsets.ModelViewSet):
    # ...
    filter_fields = ['state']
```

You can now use url filters for "state": http://127.0.0.1:8001/api/pv_yield/?state=by

Commit the changes, push them to GitHub and deploy the app.
In order to use the admin interface on heroku, you have to create a Superuser there as well.
One option is in the web interface.
```
python manage.py migrate
python manage.py createsuperuser
```
Add some data and try the API.




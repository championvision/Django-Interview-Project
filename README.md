# Django-Interview-Project
Variable based template display.\
Regarding the aggregations: sum is implement one in Python code and average as database query, using Django's database API over raw SQL.\
Bootstrap as front-end framework\
Keeped the URL logic according to <http://applicationtask.herokuapp.com>

# Requirements
(virtualenv)project/directory$:pip freeze:

Django==2.0\
pytz==2017.3

# Django Install
Python Version: 3.5.2

Install through pip in a Virtualenv for the version 3 of Python <https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-16-04#install-through-pip-in-a-virtualenv>

# Run Django Server
(virtualenv)project/directory$: python manager.py runserver

# Application Start
If you want to have an application in your project, you will need to start an application.\
(virtualenv)project/directory$: python manage.py startapp <application name that you want>

# Database
To set your models into db:\
(virtualenv)project/directory$: python manage.py makemigrations <application name in your project>\
  
For migration:\
(virtualenv)project/directory$: python manage.py migrate <application name in your project>

# Unit Test

You may find the unit test in sites/tests.py file.

# Note
Under sites/views.py, you may see a E128(E128 continuation line under-indented for visual indent) PEP8 problem; nevertheless, the conflict comes from the style of Django.

# Django-Interview-Project
Implemented the project according to the requirements below: 

Regarding the aggregations: sum is implement one in Python code and average as database query, using Django's database API over raw SQL.

Bootstrap as front-end framework

Keeped the URL logic according to <http://applicationtask.herokuapp.com>

# Prerequisities
(virtualenv)project/directory$:pip freeze:


Django==2.0\
flake8==3.5.0\
mccabe==0.6.1\
pycodestyle==2.3.1\
pyflakes==1.6.0\
pytz==2017.3

# Installing && Running
Clone project, git clone https://github.com/iskenderunlu/Django-Interview-Project.git \
Create a python3.5.2 virtual environment \
Inside environment, run pip install -r requirements.txt, to install depencencies. \
At the root of the project, start Django runserver, python manage.py runserver

# Django Install
Python Version: 3.5.2

Install through pip in a Virtualenv for the version 3 of Python <https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-16-04#install-through-pip-in-a-virtualenv>

# Run Django Server
(virtualenv)project/directory$: python manager.py runserver

# Application Start
If you want to have an application in your project, you will need to start an application.\
(virtualenv)project/directory$: python manage.py startapp 'application name that you want'

# Database

To create models for database: \
(virtualenv)project/directory$: python manage.py makemigrations 'application name in your project'
  
To apply models into database:\
(virtualenv)project/directory$: python manage.py migrate 'application name in your project'
  
# Unit Test

You may find the unit test in sites/tests.py file.

To run the unit tests:\
(virtualenv)project/directory$: python manager.py test sites.tests

# Note
Under sites/views.py, you may see a E128(E128 continuation line under-indented for visual indent) PEP8 problem; nevertheless, the conflict comes from the style of Django.

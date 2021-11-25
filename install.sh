#!/bin/sh
python manage.py migrate
python3 manage.py runserver 0:8080

export DJANGO_SUPERUSER_PASSWORD=cloud
export DJANGO_SUPERUSER_USERNAME=cloud
export DJANGO_SUPERUSER_EMAIL=cloud@a.com
python manage.py createsuperuser  --noinput
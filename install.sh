#!/bin/sh
python3 manage.py migrate

export DJANGO_SUPERUSER_PASSWORD=cloud
export DJANGO_SUPERUSER_USERNAME=cloud
export DJANGO_SUPERUSER_EMAIL=cloud@a.com
python3 manage.py createsuperuser  --noinput

python3 manage.py runserver 0:8080
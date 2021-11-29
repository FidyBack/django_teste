#!/bin/sh
sudo apt install python3-dev libpq-dev python3-pip -y
python3 -m pip install -r /home/ubuntu/django_teste/requirements.txt
python3 /home/ubuntu/django_teste/manage.py migrate

echo '@reboot python3 /home/ubuntu/django_teste/manage.py runserver 0:8080' | crontab

export DJANGO_SUPERUSER_PASSWORD=cloudx
export DJANGO_SUPERUSER_USERNAME=cloud
export DJANGO_SUPERUSER_EMAIL=cloud@a.com
python3 /home/ubuntu/django_teste/manage.py createsuperuser --noinput

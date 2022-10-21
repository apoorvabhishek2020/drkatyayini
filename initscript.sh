#!/bin/bash
python manage.py makemigrations --noinput
python manage.py migrate
python manage.py initadmin
gunicorn -w 3 --bind 0.0.0.0:8000 dr_katyayini.wsgi 
# python manage.py runserver 0.0.0.0:8000
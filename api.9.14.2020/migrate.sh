#!/bin/bash
rm db.sqlite3
rm api/migrations/0*
python manage.py makemigrations
python manage.py migrate

#!/bin/bash
python manage.py createsuperuser
python manage.py changepassword admin@example.com

#!/bin/bash

# Start Gunicorn processes
source venv/bin/activate
pip3 install -r requirements.txt
source variables.env
python3 Entry_Management_App/manage.py runserver

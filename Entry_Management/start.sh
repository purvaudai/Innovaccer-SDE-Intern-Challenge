#!/bin/bash

# Start Gunicorn processes
source venv/bin/activate
pip install -r requirements.txt
source variables.env
python Entry_Management_App/manage.py runserver

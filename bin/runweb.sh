#!/bin/sh

exec gunicorn demo.app:app --bind 0.0.0.0:8000 --workers 2 --threads 2 --access-logfile -

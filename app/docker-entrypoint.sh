#!/bin/sh
set -e
# create tables
flask init-db
# seed
flask seed
flask run --host=0.0.0.0# gunicorn --bind 0.0.0.0:5000 wsgi:app
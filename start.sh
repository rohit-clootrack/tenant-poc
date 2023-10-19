#!/bin/sh
set -o errexit
set -o nounset

python /app/manage.py collectstatic
python /app/manage.py migrate
/usr/local/bin/gunicorn tenant_management.wsgi --bind 0.0.0.0:8000 --chdir=/app

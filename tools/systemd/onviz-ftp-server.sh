#!/bin/bash

APP_DIR=/opt/onviz-server
cd ${APP_DIR}

if [ -d .env ]; then
    source .env/bin/activate
fi
if [ -d .venv ]; then
    source .venv/bin/activate
fi

python manage.py run_ftp_server

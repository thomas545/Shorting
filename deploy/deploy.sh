#!/bin/bash

cd Shorting
source ~/.virtualenvs/shorting/bin/activate
git pull origin master
python manage.py migrate
pip install -r requirements.txt

deactivate

sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
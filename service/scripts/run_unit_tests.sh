#!/usr/bin/env bash

cd src
python manage.py test --settings=lumicore.settings
pytest --ds=lumicore.settings --durations=0 -p no:warnings
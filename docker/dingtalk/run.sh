#!/bin/bash
sed -i s/accessToken/"$accessToken"/ alert.py

gunicorn -w 4 -b 0.0.0.0:9166 alert:app
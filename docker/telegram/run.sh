#!/bin/bash

sed -i s/botToken/"$botToken"/ alert.py
sed -i s/chatID/"$chatID"/ alert.py

gunicorn -w 4 -b 0.0.0.0:9165 alert:app
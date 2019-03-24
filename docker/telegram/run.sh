#!/bin/bash

sed -i s/botToken/"$botToken"/ telegram_alert.py
sed -i s/chatID/"$chatID"/ telegram_alert.py

gunicorn -w 4 -b 0.0.0.0:9165 telegram_alert:app
#!/bin/bash
sed -i s/accessToken/"$accessToken"/ dingtalk_alert.py

gunicorn -w 4 -b 0.0.0.0:9166 dingtalk_alert:app
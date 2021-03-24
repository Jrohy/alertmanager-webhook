#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import hmac
import hashlib
import base64
import urllib.parse
import logging
import requests
from flask import Flask, request

# Enable logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

access_token=os.getenv("access_token")
secret=os.getenv("secret")

dingtalk_url=f"https://oapi.dingtalk.com/robot/send?access_token={access_token}"

# Initial Flask app
app = Flask(__name__)

def generate_url():
    global dingtalk_url
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    dingtalk_url=f"{dingtalk_url}&timestamp={timestamp}&sign={sign}"

@app.route('/alert', methods=['POST'])
def alert():
    content = request.get_json()
    logger.info(f"alertmanager json == > {content}")
    generate_url()
    try:
        from msg import alert_msg_handler
        for alert_json in content['alerts']:
            title, parse_msg = alert_msg_handler(alert_json)
            post_data = {"msgtype": "markdown","markdown": {"title":title,"text":parse_msg}}
            logger.info(f"post json == > {post_data}\n")
            requests.post(dingtalk_url, json=post_data)
    except Exception as e:
        logger.error(e)
    return 'ok'

if __name__ == "__main__":
    # Running server
    from waitress import serve
    serve(app, host='0.0.0.0', port=9166)
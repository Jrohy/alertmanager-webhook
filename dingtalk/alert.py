#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import requests
from flask import Flask, request

# Enable logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

access_token="accessToken"
dingtalk_url=f"https://oapi.dingtalk.com/robot/send?access_token={access_token}"

# Initial Flask app
app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    content = request.get_json()
    logger.info(f"alertmanager json == > {content}")
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
    app.run(host='0.0.0.0', port=9166)
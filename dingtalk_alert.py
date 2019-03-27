#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import requests
from flask import Flask, request

# Enable logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

dingtalk_url="https://oapi.dingtalk.com/robot/send?access_token={}"

# Initial Flask app
app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def tg_handler():
    content = request.get_json()
    try:
        access_token="accessToken"
        from msg_handler import alert_msg_handler
        for alert_json in content['alerts']:
            transform_msg = alert_msg_handler(alert_json)
            post_data = {"msgtype": "markdown","markdown": {"title":"test","text":transform_msg}}
            logger.info("post json == > {}".format(post_data))
            requests.post(dingtalk_url.format(access_token), json=post_data)
    except Exception as e:
        logger.error(e)
    return 'ok'

if __name__ == "__main__":
    # Running server
    app.run(host='0.0.0.0', port=9166)
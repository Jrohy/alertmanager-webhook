#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import requests
from flask import Flask, request

# Enable logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

dingtalk_url="https://oapi.dingtalk.com/robot/send?access_token={}"

data_template="""
{
    "msgtype": "markdown",
    "markdown": {
        "title":"{0}",
        "text":"{1}"
     }
}
"""

# Initial Flask app
app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def tg_handler():
    content = request.get_json()
    try:
        logger.info("post json == > {}".format(content))
        access_token="accessToken"
        from msg_handler import alert_msg_handler
        for alert_json in content['alerts']:
            transform_msg = alert_msg_handler(alert_json)
            post_data = data_template.format("test", transform_msg)
            requests.post(dingtalk_url.format(access_token), data=post_data)
    except:
        logger.error("parse error ==> {}".format(content))
    return 'ok'

if __name__ == "__main__":
    # Running server
    app.run(host='0.0.0.0', port=9166)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from flask import Flask, request

# Enable logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Initial Flask app
app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    content = request.get_json()
    logger.info(f"alertmanager json == > {content}")
    try:
        import telegram
        # Initial bot by Telegram access token
        bot = telegram.Bot(token="botToken")
        chat_id = "-chatID"
        from msg import alert_msg_handler
        for alert_json in content['alerts']:
            parse_msg = alert_msg_handler(alert_json)
            logger.info(f"post json == > {parse_msg}")
            bot.sendMessage(chat_id=chat_id, text=parse_msg, parse_mode="Markdown")
    except:
        logger.error(f"parse error ==> {content}")
    return 'ok'

if __name__ == "__main__":
    # Running server
    app.run(host='0.0.0.0', port=9165)
FROM python:3-slim

LABEL maintainer "Jrohy <euvkzx@gmail.com>"

WORKDIR /alertmanager-telegram

COPY alert.py msg.py run.sh /alertmanager-telegram/

RUN pip install flask python-telegram-bot gunicorn && \
    chmod +x /alertmanager-telegram/run.sh && \
    rm -rf /root/.cache

ENTRYPOINT ["./run.sh"]
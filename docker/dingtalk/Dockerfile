FROM alpine:latest

LABEL maintainer "Jrohy <euvkzx@gmail.com>"

WORKDIR /alertmanager-dingtalk

COPY dingtalk_alert.py msg_handler.py run.sh /alertmanager-dingtalk/

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    pip install flask gunicorn && \
    chmod +x /alertmanager-dingtalk/run.sh && \
    rm -r /root/.cache

ENTRYPOINT ["./run.sh"]
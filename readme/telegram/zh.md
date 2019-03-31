## alertmanager-telegram
![Docker Pulls](https://img.shields.io/docker/pulls/jrohy/alertmanager-telegram.svg)
[![](https://images.microbadger.com/badges/image/jrohy/alertmanager-telegram.svg)](https://microbadger.com/images/jrohy/alertmanager-telegram "Get your own image badge on microbadger.com")
1. 利用[BotFather](https://telegram.me/BotFather)生成机器人, 获取botToken  

2. 将机器人拉到一个群组, 打开web版telegram获取到该群组的chatID  
    ![chatId](../../images/chatID.png)

3. 运行docker run启动容器, 其中**botToken**和**chatID**替换为实际的对应值  
    ```
    docker run -d --name alertmanager-telegram --restart always -e botToken="telegramBotToken" -e chatID="telegramChatID" -p 9165:9165 jrohy/alertmanager-telegram
    ```

4. 配置alertmanager webhook规则:  
    ```
    receivers:
    - name: 'alert-webhook'
    webhook_configs:
        - url: http://xx.xx.xx.xx:9165/alert
          send_resolved: true
    ```
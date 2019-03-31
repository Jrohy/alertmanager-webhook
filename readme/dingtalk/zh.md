## alertmanager-dingtalk
![Docker Pulls](https://img.shields.io/docker/pulls/jrohy/alertmanager-dingtalk.svg)
[![](https://images.microbadger.com/badges/image/jrohy/alertmanager-dingtalk.svg)](https://microbadger.com/images/jrohy/alertmanager-dingtalk "Get your own image badge on microbadger.com")
1. 在一个钉钉群组里添加群机器人  
    ![addBot](../../images/addBot.png)

2. 获取群机器人accessToken  
    ![accessToken](../../images/accessToken.png)

3. 运行docker run启动容器, 其中**accessToken**替换为实际的对应值  
    ```
    docker run -d --name alertmanager-dingtalk --restart always -e accessToken="accessToken" -p 9166:9166 jrohy/alertmanager-dingtalk
    ```

4. 配置alertmanager webhook规则:  
    ```
    receivers:
    - name: 'alert-webhook'
      webhook_configs:
      - url: http://xx.xx.xx.xx:9166/alert
        send_resolved: true
    ```
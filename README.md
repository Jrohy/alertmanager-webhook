# alertmanager-webhook
prometheus alertmanager webhook容器, 支持telegram和dingtalk
### alertmanager-telegram
`
docker run -d --name alertmanager-telegram --restart always -e botToken="telegramBotToken" -e chatID="telegramChatID" -p 9165:9165 jrohy/alertmanager-telegram
`

### alertmanager-dingtalk
`
docker run -d --name alertmanager-dingtalk --restart always -e accessToken="accessToken" -p 9166:9166 jrohy/alertmanager-dingtalk
`
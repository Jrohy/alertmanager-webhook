# alertmanager-webhook
### alertmanager-telegram
`
docker run -d --name alertmanager-telegram -e botToken="telegramBotToken" -e chatID="telegramChatID" -p 9165:9165 jrohy/alertmanager-telegram
`
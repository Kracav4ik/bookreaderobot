# encoding: utf-8

from telegram import TelegramAPI

tele = TelegramAPI()

while True:
    a = tele.poll(3)
    if a["ok"]:
        for msg in a['result']:
            text = msg['message'].get('text')
            if text is None:
                continue
            tele.send(msg['message']['chat']['id'], "HELLO " + text)

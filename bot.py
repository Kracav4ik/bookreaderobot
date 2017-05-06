# encoding: utf-8

from telegram import TelegramAPI

tele = TelegramAPI()

with open("test.txt", encoding='utf8') as f:
    botText = f.read().split('\n\n')
botText.append('again?(Y/N)')
idx = 0
button1Name = 'next'
curText = botText[0]
while True:
    a = tele.poll(3)
    if a["ok"]:
        for msg in a['result']:
            text = msg['message'].get('text')
            if text is None:
                continue
            if text == 'Y' and botText[idx - 1] == 'again?(Y/N)':
                idx = 0

            if text == 'N' and botText[idx - 1] == 'again?(Y/N)':
                idx -= 1
            if text == button1Name:
                if idx > len(botText) - 1:
                    idx -= 1
                curText = botText[idx]
                idx += 1
            else:
                curText = 'click on a button'
            tele.send_button(msg['message']['chat']['id'], curText,
                             '{"keyboard": [ [ {"text": "%s"} ] ] }' % button1Name)

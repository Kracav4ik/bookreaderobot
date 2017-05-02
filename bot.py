# encoding: utf-8

import requests
import time


def get_url(method):
    from secret import TOKEN
    return 'https://api.telegram.org/%s/%s' % (TOKEN, method)


def get_max_offset(answer):
    """
    :rtype: int
    """
    return max((msg['update_id'] for msg in answer['result']), default=0)


updates = get_url('getUpdates')
lastText = ''
r = requests.get(updates)
a = r.json()
offset = get_max_offset(a) + 1
mm = {'timeout': 10, "offset": offset}

while True:
    start = time.time()
    print('send...')
    r = requests.get(updates, data=mm)
    print('  received in %.2f sec' % (time.time() - start))
    a = r.json()

    if a["ok"]:
        if not a['result']:
            continue
        mm['offset'] = get_max_offset(a) + 1
        for msg in a['result']:
            m = {'chat_id': msg['message']['chat']['id'], 'text': "HELLO " + msg['message']['text']}
            requests.get(get_url('sendMessage'), data=m)

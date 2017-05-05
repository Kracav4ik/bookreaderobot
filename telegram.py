# encoding: utf-8

import requests
import time


class TelegramAPI:
    @staticmethod
    def __get_url(method):
        from secret import TOKEN
        return 'https://api.telegram.org/%s/%s' % (TOKEN, method)

    def __init__(self):
        self.__offset = 0

    def __update_offset(self, answer):
        if answer.get('result'):
            # noinspection PyTypeChecker
            self.__offset = max(m['update_id'] for m in answer['result']) + 1

    def poll(self, timeout=0):
        start = time.time()
        print('poll for %d seconds...' % timeout)
        result = requests.get(self.__get_url('getUpdates'), data={
            'timeout': timeout,
            'offset': self.__offset,
        })
        print('  received in %.2f sec' % (time.time() - start))

        answer = result.json()
        self.__update_offset(answer)

        return answer

    def send(self, chat_id, text):
        requests.get(self.__get_url('sendMessage'), data={
            'chat_id': chat_id,
            'text': text
        })

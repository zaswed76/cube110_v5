#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
key = 'trnsl.1.1.20160118T034046Z.e27999dc29670d9f.efb20585c9571f33a2ae818e936e415a8f5ff6e6'
text = 'увеличить счётчик'
lang = 'ru-en'
r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
# Выводим результат
print(json.loads(r.text)["text"])



def translate(text, from_on):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20160118T034046Z.e27999dc29670d9f.efb20585c9571f33a2ae818e936e415a8f5ff6e6'
    r = requests.post(url, data={'key': key, 'text': text, 'lang': from_on})
    return json.loads(r.text)["text"][0]
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weibo import Client
import webbrowser, json
import demjson

APP_KEY = '415390189'
APP_SECRET = '958ea2c93dcad4ab45a99098b44b016a'
REDIRECT_URI = 'https://api.weibo.com/oauth2/authorize'
client = Client(APP_KEY, APP_SECRET, REDIRECT_URI)
url = client.authorize_url
'https://api.weibo.com/oauth2/authorize?client_id=415390189&response_type=code&redirect_uri=958ea2c93dcad4ab45a99098b44b016a'
print (url)
webbrowser.open_new(url)
print ('输入url中code后面的内容后按回车键：')
code = raw_input()
client.set_code(code)
token = client.token
uuid = client.uid
d = json.dumps(client.get('statuses/user_timeline', uid=uuid, separators=(',', ':')))
print (d)
s = json.loads(d)
length = len(s['statuses'])
print (length)
for i in range(0,length):
    print (s['statuses'][i]['text'])

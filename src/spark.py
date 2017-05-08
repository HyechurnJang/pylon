# -*- coding: utf-8 -*-
'''
Created on 2017. 4. 21.
@author: HyechurnJang
'''

import json
import requests

BOT_KEY = 'Bearer ZmY2MjViMjUtNmY1ZC00MjRkLWI5Y2QtNzAwZGZkMDllN2U1NTY1YWQ0MWQtZmUx'
ROOM_ID = 'Y2lzY29zcGFyazovL3VzL1JPT00vZjljYjJmNzAtMjY2My0xMWU3LTliNDYtZDM0NzBhNDQ1Mzkx'

def sendTo(who, text):
    print('Spark Send To : %s' % who)
    if isinstance(text, dict): text = json.dumps(text, indent=2)
    elif isinstance(text, list): text = json.dumps(text, indent=2)
    resp = requests.post('https://api.ciscospark.com/v1/messages',
                         headers={'Content-Type' : 'application/json; charset=utf-8',
                                  'Authorization' : BOT_KEY},
                         json={'toPersonEmail' : who, 'text' : text})
    if resp.status_code == 200: print('Spark Send Msg : Success\n')
    else:
        try:
            print('Spark Send To : Failed with %d\n%s\n' % (resp.status_code, resp.json()['message']))
        except:
            print('Spark Send To : Failed with %d\n%s\n' % (resp.status_code, json.dumps(resp.json(), indent=2)))

def sendRoom(who, text):
    print('Spark Send Room : SuperCat Space')
    if isinstance(text, dict): text = json.dumps(text, indent=2)
    elif isinstance(text, list): text = json.dumps(text, indent=2)
    text = 'From : %s\n%s' % (who, text)
    resp = requests.post('https://api.ciscospark.com/v1/messages',
                         headers={'Content-Type' : 'application/json; charset=utf-8',
                                  'Authorization' : BOT_KEY},
                         json={'roomId' : ROOM_ID, 'text' : text})
    if resp.status_code == 200: print('Spark Send Msg : Success\n')
    else:
        try:
            print('Spark Send Room : Failed with %d\n%s\n' % (resp.status_code, resp.json()['message']))
        except:
            print('Spark Send Room : Failed with %d\n%s\n' % (resp.status_code, json.dumps(resp.json(), indent=2)))
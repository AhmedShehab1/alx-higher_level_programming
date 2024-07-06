#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        payload = r.read()
    print('Body response:')
    print(f'\ttype: {type(payload)}')
    print(f'\tcontent: {payload}')
    print(f'\tutf8 content: {payload.decode("utf-8")}')

#!/usr/bin/python3
'''
Script that takes a URL and an email
sends a POST request with the payload
to the URL and displays the response's body (utf-8 decoded)
'''
import sys
import urllib.request
if __name__ == '__main__':
    payload = sys.argv[2].encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data=payload) as r:
        print(r.read().decode('utf-8'))

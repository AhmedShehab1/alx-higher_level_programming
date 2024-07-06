#!/usr/bin/python3
'''
Script sends a pOST request to a given URL and shows the response's body
'''
import requests
import sys
if __name__ == '__main__':
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)

#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
'''
import requests
import sys
if __name__ == '__main__':
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
    except Exception:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

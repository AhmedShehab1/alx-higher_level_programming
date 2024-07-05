#!/usr/bin/python3
'''
Script that takes your github credentials
and uses GITHUB API to retreive the id
'''
import requests
import sys
if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    response = response.json()
    print(response.get("id"))

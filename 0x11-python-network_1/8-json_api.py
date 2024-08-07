#!/usr/bin/python3
'''
Script That takes a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
import sys

if __name__ == '__main__':
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""

    response = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": letter})
    try:
        response = response.json()
    except Exception:
        print("Not a valid JSON")
    else:
        if not response:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"),
                                   response.get("name")))

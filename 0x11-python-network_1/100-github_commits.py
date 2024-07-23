#!/usr/bin/python3
"""
Script to list 10 most recent commits given owner
name and repo as CL arg
"""
import sys
import requests


if __name__ == "__main__":
    headers = {"Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"

    response = requests.get(url, headers=headers)

    if response:
        response = response.json()
        for i, result in enumerate(response):
            print(f"{result.get('sha')}: {result['commit']['author']['name']}")
            if (i == 9):
                break
    else:
        raise Exception(f"error: {response.status_code}")

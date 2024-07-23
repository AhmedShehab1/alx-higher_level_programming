#!/usr/bin/python3
"""
Script to list 10 most recent commits given owner
name and repo as CL arg
"""
import sys
import requests


if __name__ == "__main__":
    headers = {"Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    response = requests.get(url, headers=headers)

    if response:
        response = response.json()
        for result in response[:10]:
            print(f"{result.get('sha')}: {result['commit']['author']['name']}")
    else:
        raise Exception(f"error: {response.status_code}")

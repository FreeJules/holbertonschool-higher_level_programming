#!/usr/bin/python3
"""
6-post_email.py
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, {'email': email})
    print(r.text)

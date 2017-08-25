#!/usr/bin/python3
"""
8-json_api.py
"""
import requests
import sys

if __name__ == "__main__":
    q = None
    if len(sys.argv) > 1:
        q = sys.argv[1]
    value = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', value)
    json_check = r.headers.get('content-type')
    if json_check == 'application/json':
        json = r.json()
        if not json:
            print("No result")
        else:
            print("[{}] {}".format(json.get("id"), json.get("name")))
    else:
        print("Not a valid JSON")

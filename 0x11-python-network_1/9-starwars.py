#!/usr/bin/python3
"""
9-starwars.py
"""
import requests
import sys
url = 'https://swapi.co/api/people/'

if __name__ == "__main__":
    value = {'search': sys.argv[1]}
    r = requests.get(url, params=value)
    json = r.json()
    print('Number of result: {}'.format(json.get("count")))
    for i in json.get("results"):
        print (i.get("name"))

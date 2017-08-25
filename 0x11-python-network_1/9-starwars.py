#!/usr/bin/python3
"""
9-starwars.py
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/'
    value = {'search': sys.argv[1]}
    r = requests.get(url, params=value)
    json = r.json()
    print('Number of results: {}'.format(json.get("count")))
    for i in json.get("results"):
        print(i.get("name"))

#!/usr/bin/python3
"""
requests URL and displays the value of the variable X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])

#!/usr/bin/python3
"""
manages urllib.error.HTTPError exceptions
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print (html.decode('utf8'))
    except urllib.error.HTTPError as e:
        print ('Error code: {}'.format(e.code))

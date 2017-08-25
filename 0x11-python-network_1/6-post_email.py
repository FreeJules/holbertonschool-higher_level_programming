#!/usr/bin/python3
# takes in a URL and an email address, sends a POST request
import requests
import sys

r = requests.post(sys.argv[1], {'email': sys.argv[2]})
print (r.text)

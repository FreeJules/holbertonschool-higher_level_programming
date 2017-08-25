#!/usr/bin/python3
# takes in a URL and an email, sends a POST request
import urllib.request
import sys

url = sys.argv[1]
email = {'email': sys.argv[2]}

data = urllib.parse.urlencode(email)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
print (the_page.decode('utf8'))

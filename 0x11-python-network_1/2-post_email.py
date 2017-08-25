#!/usr/bin/python3
"""
2-post_email.py
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email_arg = sys.argv[2]
    email = {'email': email_arg}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(the_page.decode('utf8'))

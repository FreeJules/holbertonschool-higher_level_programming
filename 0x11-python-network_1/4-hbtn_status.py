#!/usr/bin/python3
# fetches https://intranet.hbtn.io/status using requests
import requests

r = requests.get('https://intranet.hbtn.io/status')
print ('Body response:')
print ('    - type: {}'.format(type(r.text)))
print ('    - type: {}'.format(r.text))

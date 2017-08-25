#!/usr/bin/python3
"""
4-hbtn_status.py
"""
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- type: {}'.format(r.text))

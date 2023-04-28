#!/usr/bin/python3
"""
Python script that fetches an URL with requests
"""
import requests


if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    text = req.text
    print('Body response:\n\t- type: {}'.format(type(text)))
    print('\t- content: {}'.format(text))

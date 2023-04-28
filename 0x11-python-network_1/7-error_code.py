#!/usr/bin/python3
""""Python script send a request to a url and display the value of X_Request-Id
Handle errors
"""
import requests
import sys


if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print('Error code: {}'.format(req.status_code))
    else:
        print(req.text)

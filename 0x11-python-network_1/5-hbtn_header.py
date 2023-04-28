#!/usr/bin/python3
"""
Python script that fetches an URL with requests
and displays the value of X-Request-Id
"""
import requests
import sys


if __name__ == '__main__':
    try:
        req = requests.get(sys.argv[1])
        print(req.headers['X-Request-Id'])

#!/usr/bin/python3
""""Python script to fetch X-Request-Id of a url"""
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as res:
        html = res.info()
        print(html.get('X-Request-Id'))

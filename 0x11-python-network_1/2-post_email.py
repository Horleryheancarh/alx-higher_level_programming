#!/usr/bin/python3
""""Python script send a post request to a url"""
from urllib import request, parse
import sys


if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))

#!/usr/bin/python3
""""Python script that sends a post request to a url"""
import requests
import sys


if __name__ == '__main__':
    data = {'q': ''}

    try:
        data['q'] = sys.argv[1]
    except:
        pass

    req = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        obj = req.json()
        if not obj:
            print('No result')
        else:
            print('[{}] {}'.format(obj.get('id'), obj.get('name')))
    except:
        print('Not a valid JSON')

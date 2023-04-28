#!/usr/bin/python3
"""
Show last 10 commits of a repo in github
"""
from requests import get
import sys


if __name__ == '__main__':
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        res = get(url)
        obj = res.json()
        for i in range(10):
            sha = obj[i].get('sha')
            name = obj[i].get('commit').get('author').get('name')
            print('{}: {}'.format(sha, name))
    except:
        pass

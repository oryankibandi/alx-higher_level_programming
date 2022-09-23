#!/usr/bin/python3
"""
Gets a github id from hithub user API
"""


if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))

    if r.status_code != 200:
        print('status code: {}'.format(r.status_code))
        print("None")
    else:
        print(r.json()['id'])

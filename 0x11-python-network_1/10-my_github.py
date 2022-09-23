#!/usr/bin/python3
"""
Gets a github id from hithub user API
"""


if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]

    authorization = "Bearer {}".format(password)

    headers = {
               "Authorization": authorization,
               "Accept": "application/vnd.github+json"}

    r = requests.get('https://api.github.com/user', headers=headers)

    if r.status_code != 200:
        print('status code: {}'.format(r.status_code))
        print("None")
    else:
        print(r.json()['id'])

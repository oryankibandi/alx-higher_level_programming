#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status with urllib"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.
    urlopen('https://alx-intranet.hbtn.io/status') as response:
        resp = response.read()
        print('Body response:$')
        print('\t- type: {}$'.format(type(resp)))
        print('\t- content: {}$'.format(resp))
        print('\t- utf8 content: {}$'.format(resp.decode('UTF-8')))

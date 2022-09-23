#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.response
    import sys

    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read()
            print(body.decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))

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

    with urllib.request.urlopen(req) as resp:
        header = resp.getheader('X-Request-Id')
        print(header)

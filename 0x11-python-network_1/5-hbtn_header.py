#!/usr/bin/python3
"""
fetches from a URL with requests package and displays a header
"""


if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])

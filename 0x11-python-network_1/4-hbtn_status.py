#!/usr/bin/python3
"""
fetches from a URL with requests package
"""


if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:$")
    print("\t- type: {}$".format(type(r.text)))
    print("\t- content: {}$".format(r.content.decode('UTF-8')))

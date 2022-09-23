#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""


if __name__ == '__main__':
    import sys
    import requests

    q = sys.argv[1] if sys.argv[1] is not None else ""
    payload = {"q": q}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        body = r.json()
        if len(body) <= 0:
            print("No result")
        else:
            print("[{}] {}".format(body['id'], body['name']))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")

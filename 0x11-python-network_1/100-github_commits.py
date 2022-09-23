#!/usr/bin/python3
"""
gets commits to a repository
"""


if __name__ == '__main__':
    import sys
    import requests

    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]
    url = 'https://api.github.com/repos/'
    params = '{}/{}/commits?per_page=10'.format(repo_owner, repo_name)
    url_string = url + params
    headers = {"Accept": "application/vnd.github+json"}

    r = requests.get(url_string, headers=headers)
    try:
        commits = r.json()
        for commit in commits:
            print("{}: {}"
                  .format(commit['sha'], commit['commit']['author']['name']))
    except requests.exceptions.JSONDecodeError:
        pass

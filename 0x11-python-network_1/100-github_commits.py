#!/usr/bin/python3
"""
script shows lalst 10 commits of a user
"""

import sys
import requests


if __name__ == "__main__":
    my_url = "https://api.github.com/repos/{}/{}/commits".format(
               sys.argv[2], sys.argv[1])

    res = requests.get(my_url)
    commits = res.json()
    try:
        for me in range(10):
            print("{}: {}".format(
                commits[me].get("sha"),
                commits[me].get("commit").get("author").get("name")))
    except IndexError:
        pass

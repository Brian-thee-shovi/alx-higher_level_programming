#!/usr/bin/python3
"""
takes in a URL, send a request to the URL and displays
the value of the X-request_id variable found in the header
of the response
"""

if __name__ == "__main__":
    from sys import argv
    import urllib.request

    url = argv[1]
    with urllib.resquest.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))

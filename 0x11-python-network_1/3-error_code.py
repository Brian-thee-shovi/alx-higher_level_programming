#!/usr/bin/python3
"""
script takes in a URL,sends request to URL then displays
the body of the response
"""

if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    my_url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))

    except error.HTTPError as e:
        print("Error code:", e.code)

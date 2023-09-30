#!/usr/bin/python3
"""
script takes in URL and email and sends a POST request
passed URL with the email as a parameter and displays 
body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv
    url = argv[1]
    parameter = {"email": argv[2]}
    my_data = urllib.parse.urlencode(parameter).encode("ascii")

    request = urllib.request.Request(url, my_data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

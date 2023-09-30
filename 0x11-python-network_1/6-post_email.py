#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends
POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    my_url = argv[1]
    value = {"email": argv[2]}
    my_re = requests.post(my_url, data=value)
    print(my_r.text)

#!/usr/bin/python3
"""
fetches URLL content
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    p = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(p.text)))
    print("\t- content: {}".format(p.text))

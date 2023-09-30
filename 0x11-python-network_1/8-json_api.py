#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a
parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    m = "" if len(argv) == 1 else argv[1]
    my_value = {"q": m}

    r = requests.post("http://0.0.0.0:5000/search_user", data=my_value)
    try:
        r_json = r.json()
        if r_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get("id"), r_json.get("name")))
    except ValueError:
        print("Not a valid JSON")

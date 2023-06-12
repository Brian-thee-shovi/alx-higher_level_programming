#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return 0, None  # length 0 and none as first character

    k = len(sentence)
    character = sentence[0]

    return k, character

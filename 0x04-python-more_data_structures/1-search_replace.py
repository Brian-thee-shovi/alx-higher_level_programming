#!/usr/bin/python3

def search_replace(my_list, search, replace):
    answer = list(my_list)
    for f in range(len(answer)):
        if answer[f] == search:
            answer[f] = replace
    return answer

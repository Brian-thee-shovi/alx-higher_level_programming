#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:  # checks empty list
        return 0
    me_score = 0
    me_weight = 0
    for score, weight in my_list:
        me_score = me_score + (score * weight)
        me_weight = me_weight + weight
    if me_weight == 0:
        return 0
    average = me_score / me-weight
    return average

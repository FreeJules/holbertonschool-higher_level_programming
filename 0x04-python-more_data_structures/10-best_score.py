#!/usr/bin/python3
def best_score(my_dict):
    score = 0
    key = ''
    if my_dict is None:
        return None
    else:
        for k, v in my_dict.items():
            if v > score:
                score = v
                key = k
    if score == 0:
        return None
    return key

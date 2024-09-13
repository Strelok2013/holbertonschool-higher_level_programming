#!/usr/bin/python3

def best_score(a_dictionary):
    score_comp = 0
    best_score = ""
    if a_dictionary == None:
        return None
    for item in a_dictionary:
        if a_dictionary[item] > score_comp:
            score_comp = a_dictionary[item]
            best_score = item
    return best_score

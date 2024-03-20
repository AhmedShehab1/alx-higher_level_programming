#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return "None"
    Values = list(a_dictionary.values())
    Max = Values[0]
    for i in range(1, len(Values)):
        if Values[i] > Max:
            Max = Values[i]
    for key, value in a_dictionary.items():
        if value == Max:
            return key

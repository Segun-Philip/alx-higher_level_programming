#!/usr/bin/python3
def multiple_returns(sentence):
    multi_tuple = ()
    if len(sentence) == 0:
        multi_tuple = 0, "None"
    else:
        multi_tuple = len(sentence), sentence[0]
    return multi_tuple


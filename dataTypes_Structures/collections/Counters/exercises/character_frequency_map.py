# give a string, return a dictionary where
# keys are characters
# values are how many times they appear

from collections import Counter


def ch_frequency(sentence: str) -> dict:
    return Counter(sentence)


print(ch_frequency(sentence="la mama de la mama"))

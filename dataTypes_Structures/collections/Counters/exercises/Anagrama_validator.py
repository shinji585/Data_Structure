# given two strings
#
# write a function that returns True if:
# both strings contains the same characters
# with the same frequencies
# ignoring order
#
# otherwise, return False

from collections import Counter


def anagrama_validator(sentences1: str, sentences2: str) -> bool:
    if Counter(sentences1) == Counter(sentences2):
        return True
    return False


print(anagrama_validator(sentences1="hello", sentences2="bello"))

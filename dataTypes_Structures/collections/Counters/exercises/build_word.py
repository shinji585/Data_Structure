# given:
# a string letters
# a string target
#
# return true if you can build target using characters from letters

from collections import Counter


def build_word(letters: str, target: str) -> bool:
    c = Counter(letters)

    value_str = ""
    for x in set(c.keys()):
        value_str += x

    if sorted(value_str) == sorted(target):
        return True

    return False


print(build_word(letters="aabbcc", target="abc"))

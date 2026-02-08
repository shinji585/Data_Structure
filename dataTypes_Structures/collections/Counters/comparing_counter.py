# we could compare counter we the manual counting
from collections import Counter


def coun[T](data: list[T]) -> dict:
    return {x: sum(1 for y in data if y == x) for x in set(data)}


# and with counter we make this quickly
def coun2[T](data: list[T]) -> dict:
    return Counter(data)


c = coun(data=[1, 1, 1, 1, 2, 3, 4, 5, 6])

print(c.setdefault("acercg"))

# given a list of numbers, returns the element that appears the most times

from collections import Counter


def common[T](arr: list[T]) -> int:
    return Counter(arr).most_common(1)[0][1]


print(common(arr=["apple", "banana", "apple", "orange", "banana", "apple"]))

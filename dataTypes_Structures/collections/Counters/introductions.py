# A counter is a dictionary subclass that counts how many times each element appears
#
# Counter == dict[element -> frequency]
#
from collections import Counter


data = ["a", "b", "a", "c", "b", "a"]

c = Counter(data)
print(c)

# the ouput is Counter({"a": 3,"b":2, "c":1})
#
# counter behaves like a dict
# c["a"] 3
# c["z"] 0 <- important: missing keys return 0

# we can create counters from list/iterable
print(Counter([1, 2, 1, 2, 3, 3, 45, 6]))
print(Counter(((1, 2), (12, 33), (1, 1), (1, 2))))

# from a string
print(Counter("banana"))

# from a dict
print(Counter({"a": 2, "b": 5}))


# we have some methods
# the first is most_common(n) it returns us the most common values
print(c.most_common(2))  # it will return us the two most common values

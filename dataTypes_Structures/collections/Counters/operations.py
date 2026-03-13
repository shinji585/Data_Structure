from collections import Counter

# with Counter we have arithmetic operation between them
c1 = Counter("abbc")
c2 = Counter("bccd")

# adds counts
print(c1 + c2)

# substract counts
print(c1 - c2)


# intersection and union
print(c1 & c2)  # min counts
print(c1 | c2)  # max counts

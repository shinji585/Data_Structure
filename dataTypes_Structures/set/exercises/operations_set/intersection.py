# find users who completed both A and B


a: list[str] = ["samuel", "katrina", "santiago", "sebastian", "paola"]
b: list[str] = ["samuel", "santiago", "sebastian"]


def intersection_union[T](a: list[T], b: list[T]) -> set[T]:
    return set(a).intersection(b)


print(intersection_union(a=a, b=b))

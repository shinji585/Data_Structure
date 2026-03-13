# you process a list of values one by one
# for each value:
# determinate wheter it has been seen before
# update your tracking structure


def seen_before[T](values: list[T]) -> set[T]:
    seen_values: set[T] = set()
    for x in values:
        if x not in seen_values:
            seen_values.add(x)

    return seen_values

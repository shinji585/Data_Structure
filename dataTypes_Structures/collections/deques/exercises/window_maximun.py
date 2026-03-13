from collections import deque
from typing import Union


def window_maximun_value[T](values: list[T], k: int) -> list[T]:
    q = deque()
    l = r = 0
    output: list = []

    while r < len(values):
        while q and values[q[-1]] < values[r]:
            q.pop()
        q.append(r)
        # remove left val from window
        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(values[q[0]])
            l += 1
        r += 1
    return output


print(window_maximun_value(values=[1, 2, 3, 4], k=2))
print(
    # take the maximun values from the str list
    window_maximun_value(
        values=["users", "counts", "people", "business", "employee"], k=3
    )
)

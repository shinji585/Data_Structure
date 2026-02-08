from collections import deque
from typing import Union


def window_maximun_value(numbers: list[Union[int, float]], k: int) -> list[int]:
    q = deque()
    l = r = 0
    output: list = []

    while r < len(numbers):
        while q and numbers[q[-1]] < numbers[r]:
            q.pop()
        q.append(r)
        # remove left val from window
        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(numbers[q[0]])
            l += 1
        r += 1
    return output


print(window_maximun_value(numbers=[1, 2, 3, 4], k=2))

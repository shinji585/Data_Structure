from collections import deque
from typing import Union
# given:
#
# a list of integers
# a window size k
#
#
# return a list with the maxmum value of each sliding window


def window(arr: list, k: int) -> Union[deque, list]:
    if k == 1:
        return arr

    arr_deque = deque(maxlen=len(arr) - k + 1)

    for i in arr:
        arr_deque.append(arr[i])
        if arr[i] > arr_deque[i]:
            arr_deque.append(arr[i])


print(window(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

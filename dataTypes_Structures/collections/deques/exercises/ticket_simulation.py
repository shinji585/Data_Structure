from collections import deque
from typing import Optional


def services(person: Optional[str], people: deque) -> Optional[deque]:
    if person is not None:
        people.append(person)

    return people.popleft()


print(
    services(
        person=None, people=deque(iterable=["samuel", "ana", "martha", "santiago"])
    )
)

# in this section I'm going to study what is a singly linked lists and how it function connected to nodes
from typing import Any, TypeVar, Generic, Optional, cast, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Optional[Node] = None


# definimos la clase syngly linked list
# pero primero y mas importante antes de escribir codigo
# tenemos que entender que es una syngli linked list
# A linkedd list is a class that store nodes to it and this create a list of them where
# each node is relate with the other but here we introduce a concept that is new
# the head and this concept we are going to understand in the future


class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.tail: Optional[Node[T]] = None

    # first append
    def append(self, data: T) -> None:
        node = Node(data=data)

        if self.tail is None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node

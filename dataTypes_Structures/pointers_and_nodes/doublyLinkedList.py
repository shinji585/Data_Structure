# en esta seccion se va a estudiar
# lo que viene siendo una lista doble enlazada y como se conforma esta
from __future__ import annotations
from typing import Optional, TypeVar, Generic


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T = None) -> None:
        self.data = data
        self.prev: Optional[Node[T]] = None
        self.next: Optional[Node[T]] = None


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.count = 0

    # implementamos el metodo append
    def append(self, data: T) -> None:
        new_node = Node(data=data)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

            self.count += 1

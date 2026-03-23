# in this file I'm going to create the singly linked list by myself
# and I'm going to try to understand this concepts in another way different from book
from __future__ import annotations
from typing import Any, Optional, TypeVar, Generic, Generator


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.__data = data
        self.__next: Optional[Node[T]] = None

    @property
    def data(self) -> T:
        return self.__data

    @data.setter
    def data(self, data: T) -> None:
        self.__data = data

    @property
    def next(self) -> Optional[Node[T]]:
        return self.__next

    @next.setter
    def next(self, value: Any) -> None:  # type: ignore
        if value is not None and not isinstance(value, Node):  # type: ignore [reportUnreachableCode]
            raise TypeError(f"Expected Node or None, but got {type(value).__name__}")
        self.__next = value


class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.__head: Optional[Node[T]] = None
        self.__size = 0

    def prepend(self, data: T) -> None:
        new_node = Node(data=data)
        self.__size += 1

        # movemos el puntero del new node de None hacia head
        new_node.next = self.__head

        # convertimos el nuevo nodo en la cabeza
        self.__head = new_node

    def append(self, data: T) -> None:
        new_node = Node(data=data)
        self.__size += 1

        if self.__head is None:
            self.__head = new_node
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = new_node

    # implementamos las operaciones de recorrido y mostramos los valores dentro de esta

    def __iter__(self) -> Generator[T]:
        current = self.__head
        while current:
            yield current.data
            current = current.next

    def traversal(self):
        for data in self.__iter__():
            print(data)

    def __str__(self) -> str:
        return f"Elements -> {[x for x in self.__iter__()]},Size -> {self.__size}"


if __name__ == "__main__":
    # test prepend
    test: SinglyLinkedList[int] = SinglyLinkedList()

    test.prepend(data=1)
    print(f"Test 1: \n{test}")
    test.prepend(data=2)
    print(test)
    test.prepend(data=10)
    print(test)
    test.prepend(data=100)
    print(test)

    #   test append
    test2: SinglyLinkedList[int] = SinglyLinkedList()
    test2.append(data=1)
    print(f"Test 2: \n{test2}")
    test2.append(data=2)
    print(test2)
    test2.append(data=3)
    print(test2)
    test2.append(data=10)
    print(test2)

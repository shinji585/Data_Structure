# in this section I'm going to study what is a singly linked lists and how it function connected to nodes
from typing import Any, Iterator, TypeVar, Generic, Optional, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Optional[Node[T]] = None


# definimos la clase syngly linked list
# pero primero y mas importante antes de escribir codigo
# tenemos que entender que es una syngli linked list
# A linkedd list is a class that store nodes to it and this create a list of them where
# each node is relate with the other but here we introduce a concept that is new
# the head and this concept we are going to understand in the future


class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.size: int = 0

    # first append
    def append(self, data: T) -> None:
        node = Node(data=data)
        self.size += 1

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def __size__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current:
            yield current.data
            current = current.next

    # para eliminar algun valor de un nodo tenemos diferentes aspectos a tener en cuenta que se deben seguir
    # uno de estos aspectos es el siguiente en donde eliminamos un valor mediante un dato que se nos pasa
    # en esta forma utilizamos dos punteros uno que nos ayuda a recorrer y el otro que nos ayuda a mover la referencia
    # si el valor que se quiere eliminar esta en el medio de dos datos
    def delete(self, data: T) -> None:
        current = self.head
        prev: Optional[Node[T]] = None

        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next  # asignamos el valor siguiente a head eliminando el valor que este tenia
                else:
                    if prev is not None:
                        prev.next = current.next  # en caso contrario el valor que viene despues del previo toma el siguiente a el
                    self.size -= 1
                    return
            prev = current
            current = current.next

    # buscar elemenetos, al principio definimos iter por lo que habra algo que deberemos colocar antencion
    # no es un nodo lo que estamos comparando si datos
    def search(self, data: T) -> bool:
        for node in self.__iter__():
            if data == node:
                return True
        return False

    # clear method
    def clear(self) -> None:
        """clear the entire list"""
        self.head = None
        self.size = 0

    def __str__(self):
        return f"Elementos: {[x for x in self.__iter__()]}, size: {self.size}"


# prueba de la singlyLinkedList
if __name__ == "__main__":
    singlyLinkedList: Any = SinglyLinkedList()

    # agregamos elementos
    cantidad = int(input("Ingrese la cantidad de elementos: "))
    i = 0
    while i < cantidad:
        elemento = input("Ingrese el elemento: ")
        singlyLinkedList.append(elemento)
        i += 1

    # despues de agregar elemenetos eliminamos elementos
    print(singlyLinkedList)
    cantidad = int(input("Ingrese la cantidad de elementos a eliminar: "))
    i = 0
    while i < cantidad:
        elemento = input("Ingrese el elemento a eliminar: ")
        singlyLinkedList.delete(elemento)
        i += 1

    print(singlyLinkedList)

    # buscamos un elemento
    elemento = input("Ingrese el elemento a buscar: ")
    print(f"El elemento a buscar fue encontrado?: {singlyLinkedList.search(elemento)}")

    # limpiamos la lista
    singlyLinkedList.clear()
    print(f"LinkedList limpiada: {singlyLinkedList}")

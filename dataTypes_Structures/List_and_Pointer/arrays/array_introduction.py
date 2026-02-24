from typing import Any, TypeVar, Generic
from dataclasses import dataclass

T = TypeVar("T")


@dataclass(init=False)
class Array(Generic[T]):
    # declaramos 3 variables
    __a: list[Any]
    __capacity: int
    __size: int

    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.__size = 0
        self.__a = [None] * self.__capacity

    # implementamos el metodo de inserccion
    def insertar_inicio(self, valor_insertar: int) -> None:
        if self.__size == self.__capacity:
            raise Exception("Posible desbordamiento de memoria - vector lleno")

        for k in range(self.__size, 0, -1):
            self.__a[k] = self.__a[k - 1]

        self.__a[0] = valor_insertar
        self.__size += 1

    def insertar_final(self, value: T) -> None:
        if self.__size == self.__capacity:
            raise Exception("The Array is full.")

        self.__a[self.__size] = value
        self.__size += 1

    def insertar_referencia(self, referencia: int, value: T) -> None:
        if self.__size == self.__capacity:
            raise Exception("The array is full")

        # si la referencia es mayor a la cantidad de elementos actuales este no permite agregar
        if referencia > self.__size:
            raise Exception("No se puede insertar mas alla del tamaño")

        for k in range(self.__size, referencia, -1):
            self.__a[k] = self.__a[k - 1]

        self.__a[referencia] = value
        self.__size += 1

    def eliminar_posicion(self, posicion: int) -> None:
        if 0 < posicion < self.__size:
            raise Exception("La posicion es menor o mayor a size")

        for k in range(posicion, self.__size - 1):
            self.__a[k] = self.__a[k + 1]

        self.__size -= 1
        self.__a[self.__size] = None

    def eliminar_inicion(self) -> None:
        if self.__size == 0:
            raise Exception("Posible subdesbordamiento de memoria - vector vacio")
        else:
            if self.__size > 0:
                # eliminamos por inicio
                for k in range(self.__size, 0, -1):
                    self.__a[k] = self.__a[k + 1]
            self.__size -= 1
            self.__a[self.__size] = None

    def eliminar_dato(self, dato: T) -> None:
        p = 0
        if self.__size == 0:
            raise Exception("Posible subdesbordamiento de memoria - vector vacio")
        else:
            p -= self.busqueda_lineal(dato)
            if p == -1:
                raise Exception("Dato no existe")
            else:
                self.eliminar_posicion(p)

    def busqueda_lineal(self, value: T) -> int:
        pos: int = -1
        if self.__size == 0:
            raise Exception("vector vacio")

        for k in range(self.__size):
            if self.__a[k] == value:
                pos = k
                break
        return pos

    def recorrer(self) -> None:
        if self.__size == 0:
            raise Exception("Vector vacio")
        else:
            for k in range(0, self.__size):
                print(f"[{self.__a[k]}]", end="\n")


if __name__ == "__main__":
    array: Array = Array(capacity=10)

    # insertamos elementos
    array.insertar_inicio(valor_insertar=1)
    array.insertar_inicio(valor_insertar=2)
    array.insertar_inicio(valor_insertar=10)

    # mostramos el array 1
    print("Array 1")
    array.recorrer()

    array2: Array = Array(capacity=2)

    array2.insertar_inicio(10)
    print("\nArray 2")
    array2.recorrer()

    array.insertar_inicio(20)
    print("\nArray 2 con nuevo valor y nuevo desplazamiento")
    array2.recorrer()

    # insertar por referencia
    array.insertar_referencia(referencia=1, value=30)
    print(f"\nArray despues de insercion por referencia: {array}")

    print(array.busqueda_lineal(-1))

    # eliminamos el valor 10
    array.eliminar_dato(dato=20)
    print(array)

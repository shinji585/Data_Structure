# en esta seccion se estudiara que son los arrays dinamicos y como implementar estos
# dichos arrays dinamicos parten de saber y entender el modelamiento y funcionamiento de los arrays estaticos

# para entender lo que es un array dinamico tenemos que enteder primero un array estatico lo cual ya se hizo y como bien se sabe
# los arrays estaticos tienen una capacidad maxima de elementos los cuales pueden almacenar y tienen lo que viene siendo un size
# que son la cantidad de elementos actuales que tiene el array, los arrays dinamicos son lo mismo la diferencia transcribe en el hecho de que
# cada vez que capacity == size entonces ellos se reasignan en memoria y crecen de nuevo duplicando su tamaño para poder almacenar mas elementos
# y es esta accion la que los hace dinamicos


# dicho concepto es conocido como list en python, ArrayList en lenguaje como java y vector en lenguajes como c++

# el proceso aqui en el array dinamico es el siguiente cada vez que la capacity == size entonces duplicamos el tamaño eso esta claro pero lo hacemos en el add
# y entonces esto tiene que tener un proceso en donde el size crece en tamaño
from typing import TypeVar, Generic, Iterable, Any
from dataclasses import dataclass

T = TypeVar("T")


# array dinamico pero basado en un arraylist (el array dinamico de java se conocera despues en otro tipo de array)


@dataclass(init=False)
class Dynamic_Array(Generic[T]):
    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.__size = 0
        self.__items: list[Any] = capacity * [None]

    # el metodo add tiene que tener la funcion de reasinar elementos to a new array if it is full
    def _resize(self, new_capacity) -> None:
        B = new_capacity * [None]

        for i in range(self.__size):
            B[i] = self.__items[i]

        # reasginamos
        self.__items = B
        self.__capacity = new_capacity

    # ahora creamos el metodo add
    def add(self, value: T) -> None:
        if self.__capacity == self.__size:
            # reasignamos la matrix
            self._resize(2 * self.__capacity)

        self.__items[self.__size] = value
        self.__size += 1

    def len(self) -> int:
        return self.__size

    def iter_sequence(self) -> Iterable[T]:
        if not self.__size == 0:
            raise Exception("Matrix is empty.")

        # utilizamos un generador para poder acceder a elemento por elemento
        for x in range(self.__size):
            yield self.__items[x]

    # creamos los famosos getters y setter del Static_Array pero la diferencia es que tenemos que validar primero que el indiex exista para el get
    def get_at(self, i: int) -> T:
        if not (0 <= i < self.__size):
            raise Exception("Index out of bounds.")

        # en caso contrario retornamos el elemento
        return self.__items[i]

    def set_at(self, i: int, value: T) -> None:
        if not (0 <= i < self.__size):
            raise Exception("Index out of bounds.")

        self.__items[i] = value

    def __repr__(self) -> str:
        return f"Dynamic_Array(Items: {self.__items},Capacity: {self.__capacity},Size: {self.__size})"


if __name__ == "__main__":
    array_dinamico: Dynamic_Array[int] = Dynamic_Array(capacity=3)

    array_dinamico.add(value=1)
    array_dinamico.add(value=2)
    array_dinamico.add(value=10)

    print(array_dinamico)

    # si yo vengo y agrego otro elemento
    array_dinamico.add(value=5)
    print(f"Array dinamico con memoria duplicada: {array_dinamico}")

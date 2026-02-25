# en esta clase se implementara los metodos de la clase array estudiado en clases y utilizando mi logica a lo pytonic
from typing import TypeVar, Generic

T = TypeVar(name="T")


class FixedArrayList(Generic[T]):
    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.__size = 0
        self.__A: list = self.__capacity * [
            None
        ]  # [None] significa que la matrix esta vacia

    # los primeros metodos a generar son los metodos de insertar que siguen la misma regla logica
    # primero verifican que el size y la capacity no sean la misma luego reorganizan los elementos si es posible (esto no aplica para insertar a el final)
    # luego increamentan
    def add_start(self, value: T) -> None:
        if self.__size == self.__capacity:
            raise RuntimeError(
                f"Elements must remain in positions 0 to {self.__size - 1} with not gaps"
            )

        # en caso contrario que esto no se cumpla
        if self.__size >= 0:
            for k in range(self.__size, 0, -1):
                self.__A[k + 1] = self.__A[k]

            # agregamos el elemento al inicio y aumentamos la cantidad de elementos que esta contiene
            self.__A[0] = value
            self.__size += 1

    def add_end(self, value: T) -> None:
        if self.__size == self.__capacity:
            raise RuntimeError(
                f"Elements must remain in positions 0 to {self.__size - 1} with not gaps"
            )

        if self.__size >= 0:
            self.__A[self.__size] = value
            self.__size += 1

    def insertAt(self, value: T, i: int) -> None:
        if self.__size == self.__capacity:
            raise RuntimeError(
                f"Elements must remain in positions 0 to {self.__size - 1} with not gaps"
            )

        # ahora validamos que el index no este por fuera del
        if 0 <= i <= self.__size:
            raise IndexError(
                f"Index {i} out bounds for insert: valid range 0 to {self.__size - 1}"
            )

        # en caso de que dicha exception no se cumplan entonces movemos los ementos a la derecha y agregamos el elemento en la posicion que queremos
        # tenemos que tener en cuenta un concepto importante y es que el for each va desde size hasta el index
        for k in range(self.__size, i, -1):
            self.__A[k] = self.__A[
                k - 1
            ]  # we move the value on the positions 0 to size into the next right positions until k stay on the positions that i says

        # luego de mover los elementos agregamos el valor en dicha posicion y lo agregamos
        self.__A[i] = value
        self.__size += 1

    # implementamos los metodos antes y despues
    def insert_after(self, value: T) -> None:
        if self.__size == self.__capacity:
            raise RuntimeError(
                f"Elements must remain in positions 0 to {self.__size - 1} with not gaps"
            )

        # si no se lanza la exception entonces agregamos el valor en la posicion siguiente del size y aumentamos este
        self.__A[self.__size + 1] = value
        self.__size += 1

    def insert_before(self, value: T) -> None:
        if self.__size == self.__capacity:
            raise RuntimeError(
                f"Elements must remain in positions 0 to {self.__size - 1} with not gaps"
            )

        for k in range(self.__size, self.__size - 1, -1):
            self.__A[k] = self.__A[k - 1]

        # agregamos el valor en la posicion anterior a size
        self.__A[self.__size - 1] = value
        self.__size += 1

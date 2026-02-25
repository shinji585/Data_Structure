# en esta clase se implementara los metodos de la clase array estudiado en clases y utilizando mi logica a lo pytonic
from typing import Sized, TypeVar, Generic

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
                self.__A[k] = self.__A[k - 1]

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

        # ahora validamos que el index no este por fuera del size
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
    def insert_after(self, value: T, value_reference: T) -> None:
        pos = -1
        if self.__size == self.__capacity:
            raise RuntimeError(
                f"Elements must remain in positions 0 to {self.__size - 1} with not gaps"
            )

        for k in range(0, self.__size):
            if self.__A[k] == value_reference:
                pos = k

        # despues de buscar la posicion como referencia verificamos que esta no sea menor que cero o mayor o igual al size por que nos estariamos saliendo de los rangos a los que podriamos
        # agrupar valores
        if pos < 0 or pos >= self.__size:
            raise Exception("Reference not found")

        # luego de tener la posicion de referencia movemos los elementos a la derecha
        for k in range(self.__size, pos, -1):
            self.__A[k] = self.__A[k - 1]

        # agregamos el elemento
        self.__A[pos + 1] = value
        self.__size += 1

    # ya teniendo esa logica de posicionamiento
    def insert_before(self, value: T, value_reference: T) -> None:
        pos = -1
        if self.__size == self.__capacity:
            raise RuntimeError(
                f"Elements must remain in positions 0 to {self.__size - 1} with not gaps"
            )

        # obtenemos el pos
        for k in range(0, self.__size):
            if self.__A[k] == value_reference:
                pos = k

        # validamos que pos no sea menor a cero o mayor o igual al size
        if pos < 0 or pos >= self.__size:
            raise Exception("Reference not found")

        # en el caso en que tenga que ingresar un elemento en un array de la forma [1,2,3,4,5] tenemos que los indixes son 0,1,2,3,4
        # por lo que si pos es igual a 1 entonces tendria que mover desde el size hasta el pos hacia la derecha y cuando se haga eso la posicion estara libre
        # y podre en teoria agregar el elemento
        for k in range(self.__size, pos, -1):
            self.__A[k] = self.__A[k - 1]

        # agregamos el elemento
        self.__A[pos] = value
        self.__size += 1

    # los siguientes metodos elimina valores dentro del array utilizando estrategias diferentes cada uno
    # con el primer metodo que se comenzara sera eliminar al inicio
    def remove_start(self) -> None:
        if self.__size == self.__capacity:
            raise RuntimeError(
                f"Elements must remain in pos 0 to {self.__size - 1} with not gaps"
            )

        # si no tenemos una exception entonces eliminamos el elemento en la posicion 0 y le restamos 1 a size
        for k in range(0, self.__size - 1):
            self.__A[k] = self.__A[k - 1]
        self.__size -= 1

    def remove_end(self) -> None:
        if self.__size == self.__capacity:
            raise RuntimeError(
                f"Elements must remain in pos 0 to {self.__size - 1} with not gaps"
            )

        self.__size -= 1

    def remove_at(self, i: int) -> None:
        if self.__size == self.__capacity:
            raise RuntimeError(
                f"Elements must remain in pos 0 to {self.__size - 1} with not gaps"
            )

        if 0 <= i <= self.__size:
            raise IndexError(
                f"Index {i} out bounds for insert: valid range 0 to {self.__size - 1}"
            )

        for k in range(i, self.__size - 1):
            self.__A[k] = self.__A[k - 1]

        self.__size -= 1

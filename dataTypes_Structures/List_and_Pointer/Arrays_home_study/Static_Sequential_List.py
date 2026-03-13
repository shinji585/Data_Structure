# en esta clase se implementara los metodos de la clase array estudiado en clases y utilizando mi logica a lo pytonic
from typing import TypeVar, Generic

T = TypeVar(name="T")


class FixedArrayList(Generic[T]):
    def __init__(self, capacity: int) -> None:
        # verificamos que capacity no sea igual a cero o menor a esta
        if capacity <= 0:
            raise Exception("The capacity can't be equal or lower than zero")

        self.__capacity = capacity
        self.__size = 0
        self.__A: list = self.__capacity * [
            None
        ]  # [None] significa que la matrix esta vacia

    # creamos una funcion llamada compare que realizara la comparacion entre el size y la capacity para ahorra codigo repetitivo
    def __compare__(self) -> bool:
        return self.__size == self.__capacity

    # implementamos el metodo len
    def __len__(self) -> int:
        return self.__size

    # implementamos el metodo valid_range el cual valida que i no sea menor o igual que cero o que i no sea mayor que el size
    def __valid_range__(self, i: int) -> bool:
        return not (0 <= i < self.__size)

    # los primeros metodos a generar son los metodos de insertar que siguen la misma regla logica
    # primero verifican que el size y la capacity no sean la misma luego reorganizan los elementos si es posible (esto no aplica para insertar a el final)
    # luego increamentan
    def add_start(self, value: T) -> None:
        if self.__compare__():
            raise RuntimeError(
                f"Elements must remain in positions 0 to {self.__size - 1} with not gaps"
            )

        # en caso contrario que esto no se cumpla
        if self.__size >= 0:
            for k in range(self.__size, 0):
                self.__A[k] = self.__A[k - 1]

            # agregamos el elemento al inicio y aumentamos la cantidad de elementos que esta contiene
            self.__A[0] = value
            self.__size += 1

    def add_end(self, value: T) -> None:
        if self.__compare__():
            raise RuntimeError(
                f"Elements must remain in positions 0 to {self.__size - 1} with not gaps"
            )

        if self.__size >= 0:
            self.__A[self.__size] = value
            self.__size += 1

    def insertAt(self, value: T, i: int) -> None:
        if self.__compare__():
            raise RuntimeError(
                f"Elements must remain in positions 0 to {self.__size - 1} with not gaps"
            )

        # ahora validamos que el index no este por fuera del size
        if self.__valid_range__(i):
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
        if self.__compare__():
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
        if self.__compare__():
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
        # si no tenemos una exception entonces eliminamos el elemento en la posicion 0 y le restamos 1 a size
        for k in range(0, self.__size - 1):
            self.__A[k] = self.__A[k - 1]
        self.__size -= 1

    def remove_end(self) -> None:
        self.__size -= 1

    def remove_at(self, i: int) -> None:
        if self.__valid_range__(i):
            raise IndexError(
                f"Index {i} out bounds for insert: valid range 0 to {self.__size - 1}"
            )

        for k in range(i, self.__size - 1):
            self.__A[k] = self.__A[k - 1]

        self.__size -= 1

    def remove_value(self, value: T) -> None:
        pos = -1

        for k in range(0, self.__size):
            if self.__A[k] == value:
                pos = k

        if 0 < pos or pos >= self.__size:
            raise Exception("Reference not found")

        # si encontramos la posicion de la referencia entonces movemos los elementos a la izquierda desde el indice de la referencia hasta el size
        for k in range(pos, self.__size - 1):
            self.__A[k] = self.__A[k - 1]

        self.__size -= 1

    # impementamos los metodos de busqueda
    # el primer metodo a implementar es el sequencial que se le pasa un valor y devuelve -1 si no esta o la posicion de este
    def search_sequential(self, value: T) -> int:
        pos = -1

        # buscamos los valores y comparamos
        for k in range(0, self.__size):
            if self.__A[k] == value:
                pos = k

        # retornamos el valor
        return pos

    # implementamos un metodo para verificar si el array esta ordenado
    def __is_sorted(self) -> bool:
        for k in range(0, self.__size - 1):
            if self.__A[k] > self.__A[k + 1]:
                return False
        return True

    # implementamos el algoritmo de ordenamiento que nos permite ordenar nuestro array
    def __insertion__sort(self) -> None:
        for k in range(1, self.__size):
            key = self.__A[k]
            j = k - 1

            while j >= 0 and key < self.__A[j]:
                self.__A[j + 1] = self.__A[j]
                j -= 1

            self.__A[j + 1] = key

    def __selection_sort(self) -> None:
        for k in range(0, self.__size - 1):
            menor = self.__A[k]
            pos = -1
            for j in range(1 + k, self.__size):
                if self.__A[j] < menor:
                    menor = self.__A[j]
                    pos = j

            self.__A = menor
            self.__A[k], self.__A[pos] = menor, self.__A[k]

    def __burble_sort(self) -> None:
        swapped = False
        for k in range(0, self.__size):
            for j in range(0, self.__size - k - 1):
                if self.__A[j] > self.__A[j + 1]:
                    self.__A[j], self.__A[j + 1] = self.__A[j + 1], self.__A[j]
                    swapped = True
            if not swapped:
                break

    def partition(self, low: int, high: int) -> int:
        pivot = self.__A[high]
        i = low - 1

        for j in range(low, high):
            if self.__A[j] < pivot:
                i += 1
                self.__A[i], self.__A[j] = self.__A[j], self.__A[i]

        self.__A[i + 1], self.__A[high] = (
            self.__A[high],
            self.__A[i + 1],
        )
        return i + 1

    def quicksort(self, low, hight) -> None:
        if low < hight:
            pi = self.partition(low, hight)

            self.quicksort(low, pi - 1)
            self.quicksort(pi + 1, hight)

    def sort(self) -> None:
        self.quicksort(0, self.__size - 1)

    # impementamos la busqueda sequencial
    def binary_search(self, value: T) -> int:
        start = 0
        end = self.__size - 1

        if not self.__is_sorted():
            raise ValueError("Binary search requires sorted Array.")

        while start <= end:
            middle = (start + end) // 2

            if self.__A[middle] == value:
                return middle
            elif self.__A[middle] < value:
                start = middle + 1

            else:
                end = middle - 1

        return -1


# esta es la mejor implementacion que he hecho entendi por primera vez una estructura de datos y no me importa como haya quedado
# nota: nada de este codigo se cambiara una mejor version de este sin los comentarios y la suciedad del codigo sera implementado por ahora se
# deja este aqui como muestra de todo el proceso mental para poder llegar a una solucion

from typing import Optional, TypeVar, Generic, Iterator, cast, Protocol, Any
from exception.FixedArrayListException import (
    CapacityError,
    FullArrayError,
    EmptyArrayError,
    IndexOutOfBoundsError,
    ValueNotFoundError,
    UnsortedArrayError,
)


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


class FixedArrayList(Generic[T]):
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise CapacityError(
                "Invalid capacity: {capacity}. Capacity must be greater than zero."
            )

        self.__capacity__ = capacity
        self.__size__ = 0
        self.__A__: list[Optional[T]] = [None] * self.__capacity__

    # implementamos los metodos privados que nos serviran para verificar los estados del array
    def __is__full(self) -> bool:
        return self.__size__ == self.__capacity__

    def __is__empty(self) -> bool:
        return self.__size__ == 0

    def __validate_access__index(self, index: int) -> None:
        if not (0 <= index < self.__size__):
            raise IndexOutOfBoundsError(
                f"Index {index} is out of bounds. Valid range is 0 to {self.__size__ - 1}."
            )

    def __validate_insert_index(self, index: int) -> None:
        if not (0 <= index <= self.__size__):
            raise IndexOutOfBoundsError(
                f"Index {index} is out of bounds. Valid range is 0 to {self.__size__ - 1}."
            )

    def __shift__right(self, index: int) -> None:
        for k in range(self.__size__, index, -1):
            self.__A__[k] = self.__A__[k - 1]

    def __shift_left(self, index: int) -> None:
        for k in range(index, self.__size__ - 1):
            self.__A__[k] = self.__A__[k + 1]

    def __index_of(self, value: T) -> int:
        for k in range(0, self.__size__):
            if self.__A__[k] == value:
                return k
        raise ValueNotFoundError(f"Value {value} was not found in the array.")

    def __partition(self, arr: list, low: int, high: int) -> int:
        pivot = arr[high]

        i = low - 1

        for j in range(low, high):
            if arr[j] is not None and cast(T, arr[j]) < cast(T, pivot):
                i += 1
                self.__swap(arr, i, j)

        self.__swap(arr, i + 1, high)

        return i + 1

    def __swap(self, arr: list, i: int, j: int) -> None:
        arr[i], arr[j] = arr[j], arr[i]

    def __quick_sort_recursive(self, arr: list, low: int, high: int) -> None:
        if low < high:
            # pi es el indice de particion, arr[pi] ya esta en el lugar correcto
            pi = self.__partition(arr, low, high)

            # ordenamos los elementos antes y despues de la particion
            self.__quick_sort_recursive(arr, low, pi - 1)
            self.__quick_sort_recursive(arr, pi + 1, high)

    # implemtamos los dunder methods que nos permitiran accer operaciones basicas de un array

    def __len__(self) -> int:
        return self.__size__

    def __setitem__(self, index: int, value: T) -> None:
        self.__validate_access__index(index=index)
        self.__A__[index] = value

    def __getitem__(self, index: int) -> T:
        self.__validate_access__index(index=index)
        return cast(T, self.__A__[index])

    def __iter__(self) -> Iterator[T]:
        for i in range(self.__size__):
            yield cast(T, self.__A__[i])

    def __repr__(self):
        elements = [self.__A__[i] for i in range(self.__size__)]
        return f"FixedArrayList({elements}, size={self.__size__}, capacity={self.__capacity__}"

    # implemtamos los metodos de insertar
    def append(self, value: T) -> None:
        if self.__is__full():
            raise FullArrayError(
                f"Cannot insert element: array capacity of {self.__capacity__} has been reached."
            )

        self.__A__[self.__size__] = value
        self.__size__ += 1

    def insert(self, index: int, value: T) -> None:
        if self.__is__full():
            raise FullArrayError(
                f"Cannot insert element: array capacity of {self.__capacity__} has been reached."
            )

        self.__validate_insert_index(index=index)

        # movemos a la derecha
        self.__shift__right(index)

        # agregaos el valor
        self.__A__[index] = value
        self.__size__ += 1

    def insert_at_start(self, value: T) -> None:
        self.insert(0, value)

    def insert_after(self, value: T, reference: T) -> None:
        pos = self.__index_of(reference)
        self.insert(pos + 1, value)

    def insert_before(self, value: T, reference: T) -> None:
        pos = self.__index_of(reference)
        self.insert(pos, value)

    # implementamos los metodos de eliminar posiciones
    def remove_at_start(self) -> T:
        if self.__is__empty():
            raise EmptyArrayError("Cannot perform operation: the array is empty.")

        value = self.__getitem__(0)
        self.__shift_left(0)
        self.__size__ -= 1
        return value

    def remove_at_end(self) -> T:
        if self.__is__empty():
            raise EmptyArrayError("Cannot perform operation: the array is empty.")

        value = self.__A__[self.__size__ - 1]
        self.__size__ -= 1
        self.__A__[self.__size__] = None
        return cast(T, value)

    def pop(self, index: Optional[int] = None) -> T:
        if index is None:
            return self.remove_at_end()
        self.__validate_access__index(index=index)
        value = self.__A__[index]
        self.__shift_left(index)
        self.__size__ -= 1
        self.__A__[self.__size__] = None
        return cast(T, value)

    def remove_value(self, value: T) -> None:
        pos = self.__index_of(value)
        self.__shift_left(pos)
        self.__size__ -= 1
        self.__A__[self.__size__] = None

    # implementamos para obtener un elemento del array y verificar si un elemento esta contenido dentro del array
    def get(self, index: int) -> Optional[T]:
        self.__validate_access__index(index=index)
        return self.__A__[index]

    def contains(self, value: T) -> bool:
        for k in range(0, self.__size__):
            if self.__A__[k] == value:
                return True
        return False

    # creamos los metodos de busqueda binaria y sequencial para obtener los elementos
    def index_of(self, value: T) -> int:
        return self.__index_of(value)

    def is_sorted(self) -> bool:
        for k in range(0, self.__size__ - 1):
            if cast(T, self.__A__[k]) > self.__A__[k + 1]:
                return False
        return True

    def sort(self) -> None:
        for k in range(1, self.__size__):
            key = cast(T, self.__A__[k])
            j = k - 1

            while j >= 0 and key < cast(T, self.__A__[j]):
                self.__A__[j + 1] = self.__A__[j]
                j -= 1

            self.__A__[j + 1] = key

    def selection_sort(self) -> None:
        for k in range(self.__size__):
            min_idx = k
            for j in range(1 + k, self.__size__):
                if cast(T, self.__A__[j]) < cast(T, self.__A__[min_idx]):
                    min_idx = j
            self.__A__[k], self.__A__[min_idx] = self.__A__[min_idx], self.__A__[k]

    def bubble_sort(self) -> None:
        for k in range(0, self.__size__):
            swappe = False
            for j in range(0, self.__size__ - k - 1):
                if cast(T, self.__A__[j]) > cast(T, self.__A__[j + 1]):
                    self.__A__[j], self.__A__[j + 1] = self.__A__[j + 1], self.__A__[j]
                    swappe = True

            if not swappe:
                break

    # implementamos el metodo de busqueda mas complejo de entender para mi hasta el momento
    def quick_sort(self) -> None:
        if self.__size__ > 1:
            self.__quick_sort_recursive(self.__A__, 0, self.__size__ - 1)

    def binary_search(self, value: T) -> int:
        if not self.is_sorted():
            raise UnsortedArrayError(
                "Binary search cannot be performed: the list is not sorted."
            )

        left = 0
        right = self.__size__ - 1

        while left <= right:
            mid = (left + right) // 2

            if self.__A__[mid] == value:
                return mid
            elif self.__A__[mid] < value:
                left = mid + 1
            else:
                right = mid - 1

        raise ValueNotFoundError(f"Value {value} was not found in the array.")


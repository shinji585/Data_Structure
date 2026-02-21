# en la notacion big O encontramos que cada linea de codigo representa O(1) lo cual es constante
# pero cada representacion por ejemplo for, bucles while dicha condicion cambia ya que aqui podemos encontrar O(n) or O(n^2)
# pero cuando encontramos multiplicaciones dentro de un ciclo for o un while la cosa cambia ya que dicha multiplicacion o division hace
# que el ciclo tenga una complejidad de tipo O(log n)
from typing import TypeVar, Protocol, Self, Any


# definimos un comparable para poder firmar un contracto y que se pueda comparar los tipos genericos
class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


# ejemplos
def multiply(n: int) -> int:  # O(1)
    return n * 2  # O(1)


def division(n: int) -> float:  # O(1)
    counter = 0  # O(1)
    while n > 1:  # O(log n)
        n = n // 2  # O(1)
        counter += n  # O(1)
    return counter  # por que lo que el algoritmo termina siendo de tipo O(log n)


# otro ejemplo mas complejo puede ser una busqueda binaria en la cual el algoritmo termina siendo O(log n)
def binary_search[T: Comparable](arr: list[T], target: T) -> bool:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


# y esto es big O en pocas palabras

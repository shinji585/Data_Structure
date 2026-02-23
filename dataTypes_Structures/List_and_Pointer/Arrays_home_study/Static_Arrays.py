# en este documento se implementara y se creara lo que viene siendo la clase array como una ayuda para entender el funcionamiento, comportamiento y diseño de esta
# dicha clase sera una implementacion sin tener que utilizar librerias que tengan que ver alguna relacion con lo que viene siendo los arrays y su construccion natural
from typing import TypeVar, Generic, Iterable

T = TypeVar("T")
# Los arrays son tipos de datos que se pueden clasificar en dos estructuras
# los arrays estaticos o los arrays dinamicos, en el estudio que tendremos
# me enfocare en los arrays estaticos ya que estos son la base para poder enter los dinamicos
# y mas adelante entender las listas, listas enlazadas y como crearlas al tener la base que las conforma


# comencemos entonces a lo que vinimos entender como estan logicamente dados este tipo de arrays
# primero tenemos que entender que son sequencias estaticas con las cuales estamos trabajando y que estas significan que
# mantenemos: x0,x1,....,xn-1
# esto implica que:
# los elementos esten ordenados
# cada elemento tiene un index en la memoria
# la mamemoria es contiguo
# size n <=capacity
# la capacidad esta fijada al momento de crear el array por lo que no podemos cambiarlo


# tambien hay dos imporantes variables dentro del array que sin ellas no podriamos manejar el array como tal
# n -> numero de elementos guardados
# capacity -> maximos elementos permitidos


# tenemos operaciones basicas despues de esto que se implementan dentro de lo que viene siendo el array
# la cual son build, len,iter_sequence,get_at(i),set_at(i) las cuales implementaremos


# implementacion de un array estatico


class Static_Array(Generic[T]):
    # sabemos que un array tiene items, sizes, capacity
    __items: list
    __capacity: int  # es la cantidad de elementos que el array puede contener
    __size: int  # representa la cantidad de elementos actuales que tenemos en el array

    # inicializamos los valores este seria nuestro build
    def __init__(self, capacity: int) -> None:
        self.__items = capacity * [None]
        self.__capacity = capacity
        self.__size = 0

    # definimos nuestro metodo set_at el cual almacena los elementos
    def add(self, value: T) -> None:
        if self.__capacity == self.__size:
            raise Exception("The Array is full.")

        # si el array no esta full entonces agregamos el elemento y nos movemos una posicion en el size
        self.__items[self.__size] = value
        self.__size += 1

    def insertar_final(self, value: T) -> None:
        if self.__size == self.__capacity:
            raise Exception("The Array is full.")

        self.__items[self.__size] = value
        self.__size += 1

    # para obtener el size
    def len(self) -> int:
        return self.__size

    def iter_sequence(self) -> Iterable[T]:
        if not self.__items:
            raise Exception("Matrix is empty.")

        # utilizamos un generador para poder acceder a elemento por elemento
        for x in range(self.__size):
            yield self.__items[x]

    # creamos los famosos getters y setter del Static_Array pero la diferencia es que tenemos que validar primero que el indiex exista para el get
    def get_at(self, i: int) -> T:
        if 0 <= i < self.__capacity:
            raise Exception("Index out of bounds.")

        # en caso contrario retornamos el elemento
        return self.__items[i]

    def set_at(self, i: int, value: T) -> None:
        if not (0 <= i < self.__capacity):
            raise Exception("Index out of bounds.")

        self.__items[i] = value
        self.__size += 1

    def __repr__(self) -> str:
        return f"Static_Array(Items: {self.__items},Capacity: {self.__capacity},Size: {self.__size})"


if __name__ == "__main__":
    array: Static_Array = Static_Array(capacity=9)

    array.add(value=1)
    array.add(value=2)
    array.add(value=3)
    array.add(value=4)
    array.add(value=5)

    # mostramos los valores
    for x in array.iter_sequence():
        print(f"Array {x} - valor = {x}")

    # agregamos un elemento en una posicion especifica
    array.set_at(i=8, value=20)

    print(array)

    # and this an static array and how implement it
    #
    #

    # aplicamos el metodo de insertar_final
    array.insertar_final(value=97)
    array.insertar_final(value=18)
    array.insertar_final(value=77)

    # mostramos el array con los cambios
    print(f"\nArray con las inserciones al final: {array}")

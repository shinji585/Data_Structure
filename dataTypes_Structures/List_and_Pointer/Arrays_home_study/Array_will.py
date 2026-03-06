from typing import TypeVar, Generic, Protocol, cast


class Comparable(Protocol):
    def __lt__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...


T = TypeVar("T", bound=Comparable)


class Array(Generic[T]):
    def __init__(self, tam: int) -> None:
        if tam <= 0:
            raise ValueError("La capacidad debe ser mayor que cero")

        self.__a = cast(list[T], [None] * tam)
        self.__tam = tam
        self.__cant = 0

    def __compare__(self) -> bool:
        return self.__cant == self.__tam

    def __valid_range__(self, i: int) -> bool:
        return 0 <= i < self.__cant

    def __len__(self) -> int:
        return self.__cant
    
    def __valid_insert_position__(self, pos: int) -> bool:
        return 0 <= pos <= self.__cant    

    def insertar_inicio(self, valor: T) -> bool:
        if self.__compare__():
            return False

        for i in range(self.__cant, 0, -1):
            self.__a[i] = self.__a[i - 1]

        self.__a[0] = valor
        self.__cant += 1
        return True

    def insertar_final(self, valor: T) -> bool:
        if self.__compare__():
            return False

        self.__a[self.__cant] = valor
        self.__cant += 1
        return True

    def insertar_en_posicion(self, pos: int, valor: T) -> bool:
        if self.__compare__() or not self.__valid_insert_position__(pos):
            return False

        for i in range(self.__cant, pos, -1):
            self.__a[i] = self.__a[i - 1]

        self.__a[pos] = valor
        self.__cant += 1
        return True

    def insertar_antes_de(self, pos: int, valor: T) -> bool:
        return self.insertar_en_posicion(pos, valor)

    def insertar_despues_de(self, pos: int, valor: T) -> bool:
        return self.insertar_en_posicion(pos + 1, valor)

    def eliminar_inicio(self) -> bool:
        if self.__cant == 0:
            return False

        for i in range(self.__cant - 1):
            self.__a[i] = self.__a[i + 1]

        self.__cant -= 1
        return True

    def eliminar_final(self) -> bool:
        if self.__cant == 0:
            return False

        self.__cant -= 1
        return True

    def eliminar_por_posicion(self, pos: int) -> bool:
        if not self.__valid_range__(pos):
            return False

        for i in range(pos, self.__cant - 1):
            self.__a[i] = self.__a[i + 1]

        self.__cant -= 1
        return True

    def eliminar_por_dato(self, valor: T) -> bool:
        pos = self.busqueda_secuencial(valor)
        return self.eliminar_por_posicion(pos) if pos != -1 else False

    def busqueda_secuencial(self, valor: T) -> int:
        for i in range(self.__cant):
            if self.__a[i] == valor:
                return i
        return -1

    def busqueda_binaria(self, valor: T) -> int:
        if not self.esta_ordenado():
            raise ValueError("El arreglo no está ordenado")

        izquierda = 0
        derecha = self.__cant - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            actual = self.__a[medio]

            if actual == valor:
                return medio
            elif actual < valor:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        return -1

    def obtener_elementos(self) -> list[T]:
        return self.__a[:self.__cant]

    def esta_ordenado(self) -> bool:
        for i in range(self.__cant - 1):
            if self.__a[i] > self.__a[i + 1]:
                return False
        return True

    def __str__(self) -> str:
        return str(self.obtener_elementos())
    
    def mostrar(self) -> None:
        print(self.obtener_elementos())


        
if __name__ == "__main__":
    arr = Array(10)  # Crear un arreglo con capacidad de 10 elementos

    print("Insertando elementos...")
    arr.insertar_final(10)
    arr.insertar_final(20)
    arr.insertar_final(30)
    arr.insertar_inicio(5)
    arr.insertar_en_posicion(2, 15)

    arr.mostrar()  # [5, 10, 15, 20, 30]

    print("Búsqueda secuencial de 15:", arr.busqueda_secuencial(15))
    print("Búsqueda binaria de 10:", arr.busqueda_binaria(10))

    print("Eliminando inicio...")
    arr.eliminar_inicio()
    arr.mostrar()

    print("Eliminando final...")
    arr.eliminar_final()
    arr.mostrar()

    print("Eliminando por dato (15)...")
    arr.eliminar_por_dato(15)
    arr.mostrar()
    
    print("Eliminando por posición (0)...")
    arr.eliminar_por_posicion(0)
    arr.mostrar()
    
    arr2 = Array(10)  # Crear un arreglo con capacidad de 10 elementos
    arr2.insertar_final(10)
    arr2.insertar_final(20)
    arr2.insertar_inicio(5)
    arr2.insertar_en_posicion(2, 15)
    arr2.insertar_final(30)

    arr2.mostrar()

    print("Búsqueda binaria de 20:", arr2.busqueda_binaria(20))
    
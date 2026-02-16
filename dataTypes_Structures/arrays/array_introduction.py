class Array:
    # declaramos 3 variables
    __a: list[int]
    __tam: int
    __cant: int

    def __init__(self, n: int) -> None:
        self.__a = []
        self.__tam = n
        self.__cant = 0

    # implementamos el metodo de inserccion
    def insertar_inicio(self, valor_insertar: int) -> None:
        if self.__tam == self.__cant:
            raise Exception("Posible desbordamiento de memoria - vector lleno")
        else:
            if self.__cant > 0:
                for k in range(self.__cant - 1, 0):
                    self.__a[k + 1] = self.__a[k]

            self.__a.insert(0, valor_insertar)
            self.__cant += 1

    def recorrer(self) -> None:
        if self.__cant == 0:
            raise Exception("Vector vacio")
        else:
            for k in range(0, self.__cant):
                print(f"[{self.__a[k]}]", end="\n")


if __name__ == "__main__":
    array = Array(n=10)

    # insertamos elementos
    array.insertar_inicio(valor_insertar=1)
    array.insertar_inicio(valor_insertar=2)
    array.insertar_inicio(valor_insertar=10)

    # mostramos el array 1
    print("Array 1")
    array.recorrer()

    array2 = Array(n=2)

    array2.insertar_inicio(10)
    print("\nArray 2")
    array2.recorrer()

    array2.insertar_inicio(20)
    print("\nArray 2 con nuevo valor y nuevo desplazamiento")
    array2.recorrer()

    array2.insertar_inicio(valor_insertar=30)
    array2.recorrer()

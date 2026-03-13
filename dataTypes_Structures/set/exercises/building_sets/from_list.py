# te estan dado una lita de enteros la cual puede contener duplicados
# tu tarea es:
# construir un contenedor que solamente tenga numeros positivos
# ignora los zeros y negativos


numers: list[int] = [0, -1, -2, -3, -5, 1, 2, 3, 4, 5]


def from_list(n: list[int]) -> set:
    return {x for x in n if x >= 1}


print(from_list(n=numers))

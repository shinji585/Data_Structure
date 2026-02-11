from collections import defaultdict


# en este ejemplo imaginemos que nos pasan una lista con valores en forma de tuplas en donde estan relacionados
# dia -> materia y queremos organizarlos de acuerdo a que cada dia contenga sus materias correspondientes

materias_por_dia = defaultdict(list)

horario: list[tuple] = [
    ("Lunes", "Matematicas"),
    ("Martes", "Fisica"),
    ("Lunes", "Programacion"),
]


for dia, materia in horario:
    materias_por_dia[dia].append(
        materia
    )  # esto nos permite realizar ya que cada key tiene una factory de list y la cual utiliza como su propio almacenador individual de elementos


print(dict(materias_por_dia))

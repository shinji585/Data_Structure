# tienes un diccionario de el color favorito de la gente
# necesitas crear un nuevo diccionario cuando el color es la key y el valor es una lista de nombres


favorites: dict = {"Alice": "Blue", "Bob": "Red", "Charlie": "Blue", "David": "Green"}


def f(x: dict) -> dict:
    inverted: dict[str, list] = {}
    for k, v in x.items():
        if v not in inverted:
            inverted[v] = []
        inverted[v].append(k)

    return inverted


print(f(x=favorites))

# como puedo pasar esto a dict comprehension?
#
#
# la solucion esta limitada no podemos crear una lista vacia y luego ir agregando valores a esta
# utilizando dict comprehension (esto tal vez sea erroneo y no le encuentre solucion a esto en el momento)

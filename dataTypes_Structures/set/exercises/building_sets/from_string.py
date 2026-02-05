# te estan dando un string el cual contiene letras, numeros y simbolos
# tu tarea es:
# construir un set de todos los distintos caracteres del alfabeto
# casos como "A" y "a" cuenta como el mismo

endpoint: str = "https://api.github.com/users/{shinji585}"


def set_endpoint(endpoint: str) -> set:
    return {ord(x) for x in endpoint if ord(x) >= 32 and ord(x) <= 126}


print(set_endpoint(endpoint=endpoint))

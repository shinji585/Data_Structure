# tienes una lista de los id de los usuarios que tienen acceso a el servidor
# algunos usuarios loggeados in multiples 19:05:58
# tu meta es crear un dict el cual tiene una key que es el user id and the v is a bool


logs: list = [102, 305, 102, 400, 305, 102]


def f(x: list) -> dict:
    filter: dict = {}
    for _ in x:
        if _ not in filter:
            filter[_] = False
        else:
            filter[_] = True
    return filter


print(f(x=logs))

# ahora la idea es llevar esa funcion a dict comprehension?

filter: dict = {key: (True if logs.count(key) > 1 else False) for key in logs}
print(f"Utilizando dict comprehension: {filter}")

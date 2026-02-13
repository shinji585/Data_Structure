# utilizamos UserDict, UserList and UserString cuando queremos o necesitamos que una clase actue
# almenos identicamente que a la clase que se se le esta haciendo un wrapped
# ya sea por que queremos que los elementos de dicha clase tengan un comportamiento
# o por que queremos que los elementos de dicha clase se comporte de la forma que queramos

# esto los encontramos en el paquete collections

# el siguiente ejemplo tiene que ver con que cada vez que pasamos una key esta debe ser minuscula y str
# y esto lo logramos de dos formas o creando una clase configurada para ello o haciendo validaciones
# lo cual no siempre es lo mejor

from collections import UserDict


class LowerDict(UserDict):
    def __setitem__(self, key, item) -> None:
        key = key.lower()
        return super().__setitem__(key, item)


ordinals = LowerDict({"FIRST": 1, "SECOND": 2})
ordinals["THIRD"] = 3

ordinals.update({"FOURTH": 4})

print(ordinals)

# en esta seccion veremos las operacciones que se pueden realizar con deques
from collections import deque

# podemos utilizar iterables para crear deques
iterable1 = deque((x for x in range(5)))

iterable2 = deque([x for x in range(5) if x % 2 == 0])


iterable3 = deque(
    "abcd"
)  # toma cada caracter y lo agrega en una posicion del deque (caracter individual)

print(f"Iterable 1: {iterable1}\nIterable 2: {iterable2}\nIterable 3: {iterable3}")

# pop en deques no es igual al que tenemos en las listas ya que estos no soportan un .pop arbirtrariamente por que romperia esa doble lista enlazada que tienen
# deque("abcd").pop(2) no seria permitido


# algo que tenemos son metodos que nos permite extender los deques con nuevos elementos sin tener que eliminar elementos antiguos o realizando funciones o estructuras para ello


# extend extiende un deque existente
iterable2.extend([x for x in range(10)])

# mientras que si queremos extender por izquierda lo hacemos utilizando el metodo
# extendleft()
iterable1.extendleft([x for x in range(2)])

print(f"Iterable 1: {iterable1}\nIterable 2: {iterable2}")


# podemos insertar elementos utilizando la funcion insert dando le la posicion en la cual lo queremos insertar
iterable1.insert(0, 100)  # primero pasamos la posicion y luego el elemento
print(iterable1)

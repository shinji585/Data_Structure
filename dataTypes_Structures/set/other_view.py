# los set puede ser creados de dos formas una de ellas ya la visualizamos
# para crear set utilizado otra forma podemos utilizar el objecto inmutable frozenset
# el cual le pasamos una lista o un rango y este nos genera el numero que nosotros queramos

a: frozenset = frozenset([1, 2, 3, 4, 5, 6])
b: frozenset = frozenset([1, 2, 3, 4, 10, 22, 33, 55])
c: set = set(x for x in range(10))
# en esta seccion estaremos visualizando los metodos que podemos encontrar y utilizar en los sets

# 1. len() nos devuelve el numero de elementos en el
print(len(a))

# 2. copy() nos devuelve una sombra o copia del objecto
print(a.copy())

# 3. difference(value) returns a set of all items in s but not in t (los valores que estan en s pero no en t)
print(a.difference(b))

# 4. intersection(t) returns a set of all items in both t and s
print(a.intersection(b))

# 5. isdisjoint(t) returns true if s and t have no items in common
print(
    a.isdisjoint(b)
)  # esto verifica la disjuntion que contienen en este caso dos sets y es verdadero si ambos no tienen elementos en comun del contrario es falso


# 6. issubset(t) returns true si todos los elementos en s estan tambien t por lo que es s subconjunto de t
print(a.issubset(b))

# 7. issuperset() retorna true si todos los elementos en t estan tambien en s
print(b.issuperset(a))

# 8. symmetric_difference(t) retorna un set of all items that are in s or t, but not both
print(a.symmetric_difference(b))

# 9. union() returns a set of all items in s or t
print(a.union(b))  # crea un nuevo set y nos retorna ese set

# metodos mas importantes

# 1. add() agrega elementos hacia s. no tiene efecto si el item ya esta presente
c.add(25)
print(c)

# 2. clear() remove todos los items de s
c.clear()
print(c)

# 3. pop() es un metodo importante remueve y devuelve el elemento eliminado arbirtrariamente
c = {x for x in range(20)}

print(c.pop())
print(c)

# 4. remove(item) elimina el item de s
c.remove(19)  # no retorna nada
print(c)

# 5. update(t) agrega todos los elementos en un objecto iterable de t hacia s
c.update(b)
print(c)

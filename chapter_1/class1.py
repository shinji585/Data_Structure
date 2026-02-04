# las funciones que toman otras funciones como argumentos son llamadas funciones de alto orden
# estas funciones pueden ser (map,filter) que son funciones que nos devuelven un iterable
#
#
# ejemplo tenemos la siguiente lista
lst: list[int] = [1, 2, 3, 4]

# y queremos que elevar al cubo dicha lista
lst = [x**3 for x in lst]  # esta es una forma
print(lst)

# pero la forma clasica y que requiere un poco mas de codigo es
lst = list(map(lambda x: x**3, lst))
print(lst)

# la otra funcion filter nos permite filtar items en una lista
lst = list(filter((lambda x: x % 2 == 0), lst))
print(lst)

# como podemos apreciar la funcion map permite cambiar o transformar cada item dentro de la sequence
# esta aplicando una funcion mientras que la funcion filter permite tambien lo mismo pero de una forma pequeña mente distinta

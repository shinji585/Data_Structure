# con los deques podemos realizar operaciones avanzadas que en las listas son faciles pero por la complejidad de los deques
# o su estructura nos toca ingeniarnolas y utilizar otros metodos o modulos para ello y una de esas funcionalidades es el
# slicing que en los deques no es permitido ya que nos lanza typeError directamente
# entonces nuestra solucion es sencilla utilizar itertools.islice para logar hacer esto

from collections import deque
from itertools import islice

# la funcion islice cumple la misma funcion que tienen las listas con el slicing
# pero hay una diferencia crucial en este comportamiento ya que islice es aplicado para iteradores
# los cuales no pueden aplicarse les slicing
# islice es un generador con un comportamiento el cual no extrae los datos de inmediato. si no que crea un "puntero" que sabe cuantos elementos saltar y donde denternse
# y obviamente esto tiene beneficios en la memoria ya que si tenemos archivos de 10GB (los cuales pueden ser tomados y serializados como deques) y queremos tomar solo las
# 10 primeras lineas entonces, islice "camina" por los 10 primeros elemetos y se detiene. Su consumo de memopria es constante: O(1)

# la sintaxis es la siguiente: islice(iterable,start,stop,step)
# donde:
# iterable: la fuente de datos
# start: donde empezar (opcional, por defecto es 0)
# stop: donde terminar (obligatorio si no hay start)
# step: de cuanto en cuanto saltar (opcional)

numeros_infinitos = deque(iterable=[x for x in range(1000000)])

# queremos del elemento 10 al 20, de 2 en 2
ventana = islice(numeros_infinitos, 10, 20, 2)

print(list(ventana))

# un ejemplo de esto puede ser


# imaginar teneer un flujo infinito de datos (streaming)
# y queremos acceder o rebanar el flujo infinito sin colapasar el sistema para obtener los 10 primeros datos
def data_streaming():
    n = 0
    while True:
        yield f"Dato_{n}"
        n += 1


# islice permite obtener los 10 primeros elementos
first_ten = islice(data_streaming(), 10)

for dato in first_ten:
    print(dato)

# la primera estructura diseñada en collections fue deque
# esta diseñado principalmente para generealizar estructuras como stacks y queues
# con una memoria mas eficiente no creando espacios adicionales como si lo realizaria
# las list
# dicha eficiencia permite agregar y remover elementos utilizando las funciones
# append and pop
#
# deque es mas eficiente que las listas ya que no cuenta con el mismo tiempo de complejidad computacional
# esto por que python en las listas tienen que mover todos los elementos a la derecha para poder insertar un nuevo item a el comienzo

# encontramos dos operaciones principales que se dan de acuerdo a su naturalidad
# la primera se da cuando agregamos un item a el final de una queue y esto es conocido como enqueue operation
# mientras que eliminar un item del comienzo de una queue es llamado dequeue

from collections import deque

# creamos los tiques
tickets_queue = deque()

# agregamos personas a esta lista de espera
tickets_queue.append("Jane")
tickets_queue.append("Samuel")
tickets_queue.append("John")


# mostramos el queue
print(tickets_queue)


# eliminamos los usuarios dependiendo de cada ticket que va teniendo cada uno
tickets_queue.popleft()

print(tickets_queue)

# los metodos append nos permite agregar elementos desde la parte derecha hasta el final de una deque
# para eliminar los elementos a la izquierda y aplicar los conceptos de dequeue utilizamos el metodo .popleft()
# el cual elimina y nos devuelve el elemento eliminado


# deque puedes ser inicializados tomando argumentos optionales
# el primero de ellos es iterable el cual esconde un iterable que sirve comoun inicializador
# maxlen escode un integer number that specifies el maximo de argumentos que puede tomar el deque
# este ultimo tiene una funcionalidad nativa que se vera de acuerdo a el uso

recent_files = deque(iterable=["core.py", "README.md", "__init__.py"], maxlen=3)

# agregamos un elemento por la izquierda
recent_files.appendleft("database.py")

# y mostremos el resultado
print(recent_files)

# cuando visualizamos lo que contiene la variable recent_files nos damos cuenta que el deque
# core.py fue eliminado o removido y esto es porque cuando fijamos el maximo de elementos que puede contener el deque
# este automaticamente no permite que se sobrepase y cada vez que agregamos un elemento nuevo que sobrepase el limite elimina el elemento en el lado opuesto al final
# si no se especifica maxlen este le permite al deque crecer de forma arbirtraria

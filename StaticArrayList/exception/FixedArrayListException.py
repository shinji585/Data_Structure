class FixedArrayListException(Exception):
    """clase base para errores que este relacionado con el array"""

    pass


class CapacityError(FixedArrayListException):
    """Se lanza cuando hay un error con respecto a la capacidad"""

    pass


class FullArrayError(FixedArrayListException):
    """Se lanza cuando el array esta lleno"""


class EmptyArrayError(FixedArrayListException):
    """Se lanza cuando el array esta vacio"""

    pass


class IndexOutOfBoundsError(FixedArrayListException):
    """Se lanza cuando el index pasado esta por fuera del array"""

    pass


class ValueNotFoundError(FixedArrayListException):
    """Se lanza cuando un valor no esta dentro del array"""
    
    pass

class UnsortedArrayError(FixedArrayListException):
    """Se lanza cuando una operación requiere que la lista esté ordenada pero no lo está."""
    
    pass

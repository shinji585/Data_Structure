# se solucionara el problema de factorial de un numero calculado utilizando recursividad que en el fondo es divide and conquer


def factorial(n: int) -> int:
    if n == 0:
        return 1
    f = n * factorial(n - 1)
    return f


print(factorial(n=30))

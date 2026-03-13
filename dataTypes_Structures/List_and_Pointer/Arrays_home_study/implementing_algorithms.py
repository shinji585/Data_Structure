# en esta seccion voy a implementar los algoritmos explicados la clase pasada por mi propia cuenta para definir que los entiendo
def selection_sort(arr: list) -> list:
    size = len(arr)
    for k in range(size):
        min_idx = k
        for j in range(1 + k, size):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[k], arr[min_idx] = arr[min_idx], arr[k]

    return arr


# implementado bubble sort algorithm
def bubble_sort(arr: list) -> list:
    for k in range(0, len(arr)):
        swappe = False
        for j in range(0, len(arr) - k - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swappe = True
        if not swappe:
            break

    return arr


# quick sort implementation
#
#
# para este algoritmo tenemos que tener primero una particion que viene siendo
# tomamos un pivote que es nuestro valor de referencia de ordenamiento
# y partimos el array a la izquierda los valores menores a este pivote y a la derecha los mayores de este
# cabe decir que despues de esto cada valor a la izquierda y derecha puede ser un posible pivote dependiendo que tan grande sea con respecto a los otros
# este proceso se repite hasta que se halla ordenrado el array por completo
# utilizamos una funcion recursiva para ello


# particion


def partition(arr, low, hight) -> int:
    pivot = arr[hight]

    i = low - 1

    for j in range(low, hight):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, hight)

    return i + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# implementamos el quick sort
def quicksort(arr, low, hight) -> list:
    if low < hight:
        pi = partition(arr, low, hight)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, hight)

    return arr


if __name__ == "__main__":
    print(
        f"Array de entrada: [12,1,3,12,2,24,18,26,5] -> array de salidad: {quicksort([12, 1, 3, 12, 2, 24, 18, 26, 5], 0, len([12, 1, 3, 12, 2, 24, 18, 26, 5]) - 1)}"
    )

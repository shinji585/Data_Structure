# en esta seccion voy a implementar los algoritmos explicados la clase pasada por mi propia cuenta para definir que los entiendo
def selection_sort(arr: list) -> list:
    size = len(arr)
    for k in range(size - 1):
        min_idx = k
        for j in range(1 + k, size):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[k], arr[min_idx] = arr[min_idx], arr[k]

    return arr


if __name__ == "__main__":
    print(
        f"Array de entrada: [12,1,3] -> array de salidad: {selection_sort([12, 1, 3])}"
    )

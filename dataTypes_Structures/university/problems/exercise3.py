def nota(codes: list[int], p1: list[float], p2: list[float]) -> None:
    # verificamos si las longitudes son la misma si no lanzamos un error
    if len({len(codes), len(p1), len(p2)}) != 1:
        raise ValueError("The len of the sequences are different")

    # si las longitudes son las mismas obtenemos la longitud o cantidad de veces que iteraremos
    n = len(codes)

    final_grades: list[float] = []

    total_final = 0.0
    max_improvement = p2[0] - p1[0]
    student_max_improvement = codes[0]

    passed: list[int] = []
    failed: list[int] = []

    for i in range(n):
        if p2[i] > p1[i]:
            final = (p1[i] + p2[i]) / 2
        else:
            final = (p2[i] * 0.6) + (p1[i] * 0.4)

        final_grades.append(final)
        total_final += final

        # improvement student
        improvement = p2[i] - p1[i]
        if improvement > max_improvement:
            max_improvement = improvement
            student_max_improvement = codes[i]

        # pass and fails validation
        if final >= 70:
            passed.append(codes[i])
        else:
            failed.append(codes[i])

    # calculamos el promedio del curso
    average = total_final / n

    # mostramos los estudiantes que aprueba y desaprueban
    below_average_and_failed: list[int] = []
    equal_to_average = False

    for i in range(n):
        if final_grades[i] < average and final_grades[i] < 70:
            below_average_and_failed.append(codes[i])

        if final_grades[i] == average:
            equal_to_average = True

    # mostramos los resultados
    print(f"Course average: {average:.2f}")
    print(f"Student with max improvement: {student_max_improvement}")
    print(f"Passed students: {passed}")
    print(f"Failed and below average: {below_average_and_failed}")

    if equal_to_average:
        print("There is at least one students with final grade equal to the average")
    else:
        print("No student has a final grade equal to the average")


if __name__ == "__main__":
    nota(
        codes=[101, 102, 103, 104, 105],
        p1=[101, 102, 103, 104, 105],
        p2=[65.0, 70.0, 55.0, 80.0, 90.0],
    )

# el usuario ingresa el codigo de maquina, la cantidad producidad, y la candidad defectuosa
#
# la cantidad defectuosa la calculamos total = (total defectuosas / total producidas) x 100
#
# el ingreso termina cuando el codigo de maquina es 0  lo que nos dice que el usuario puede ingresar cualquier codigo de maquina

# la siguiente solucion solo toma en cuenta los codigos 1,2 o 3 ya que codigos superiores a esto no estan especificados en el problema


def produccion_total() -> None:
    # global variables
    total_produce_m1 = total_produce_m2 = total_produce_m3 = 0
    total_defected_m1 = total_defected_m2 = total_defected_m3 = 0

    days_over_500 = between = less = 0
    total_produced = 0
    total_defected = 0

    defective_percent = machine_max_production = machine_max_defects = 0
    while True:
        codigo_maquina = int(input("Enter the machine code (1-3, 0 to stop): "))

        if codigo_maquina == 0:
            break

        if codigo_maquina < 1 or codigo_maquina > 3:
            print("Invalid machine code")
            continue

        produced = int(input("Porduced: "))
        defective = int(input("Defective: "))

        if codigo_maquina == 1:
            total_produce_m1 += produced
            total_defected_m1 += defective
        elif codigo_maquina == 2:
            total_produce_m2 += produced
            total_defected_m2 += defective
        else:
            total_produce_m3 += produced
            total_defected_m3 += defective

        total_produced += produced
        total_defected += defective

        # calculamos el defecto global
        if total_produced > 0:
            defective_percent = (total_defected / total_produced) * 100
        else:
            defective_percent = 0

        # determinamos la produccion maxima
        max_production = total_produce_m1
        machine_max_production = 1

        if total_produce_m2 > max_production:
            max_production = total_produce_m2
            machine_max_production = 2

        if total_produce_m3 > max_production:
            max_production = total_produce_m3
            machine_max_production = 3

        # determinamos los defectos maximso que se tienen
        max_defects = total_defected_m1
        machine_max_defects = 1

        if total_defected_m2 > max_defects:
            max_defects = total_defected_m2
            machine_max_defects = 2

        if total_defected_m3 > max_defects:
            max_defects = total_defected_m3
            machine_max_defects = 3

        if produced > 500:
            days_over_500 += 1
        elif produced >= 200 and produced <= 500:
            between += 1
        else:
            less += 1

    # mostramos los resultados
    print(f"Global defect percentage: {defective_percent:.2f}%")
    print(f"Machine with max production: {machine_max_production}")
    print(f"Machine with max defects: {machine_max_defects}")
    print(f"The number of days in which production was over 500: {days_over_500}")
    print(f"The number of days in which production was between 200 and 500: {between}")
    print(f"The number of days in which production was less to 200: {less}")


if __name__ == "__main__":
    produccion_total()

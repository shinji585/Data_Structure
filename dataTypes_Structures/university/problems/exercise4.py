def sistema_control_claves():
    n = int(input("Enter the number of keys (N): "))
    claves = []

    for i in range(n):
        while True:
            clave = int(input(f"Enter key {i + 1} (1000-9999): "))
            if 1000 <= clave <= 9999:
                claves.append(clave)
                break
            print("Error: The key must have exactly 4 digits.")

    estados = []
    validas_lista = []
    total_invalidas = 0
    existe_especial = False

    # esta parte fue hecha con IA :/
    for i in range(n):
        num = claves[i]

        d1 = num // 1000
        d2 = (num // 100) % 10
        d3 = (num // 10) % 10
        d4 = num % 10

        es_valida = True

        if d1 % 2 != 0:
            es_valida = False
        elif d4 % 2 == 0:
            es_valida = False
        elif (d1 + d2 + d3 + d4) <= 20:
            es_valida = False
        elif d1 == d2 or d2 == d3 or d3 == d4:
            es_valida = False
        elif d2 <= d3:
            es_valida = False

        if es_valida:
            estados.append("Valid")
            validas_lista.append(num)

            suma = d1 + d2 + d3 + d4
            if d4 == 7 and suma % 5 == 0:
                existe_especial = True
        else:
            estados.append("Invalid")
            total_invalidas += 1

    porcentaje_invalidas = (total_invalidas / n) * 100

    print(f"\nValid Keys: {validas_lista}")
    print(f"Total Valid: {len(validas_lista)}")
    print(f"Total Invalid: {total_invalidas}")
    print(f"Percentage of Invalid Keys: {porcentaje_invalidas:.2f}%")

    if existe_especial:
        print("There is a valid key ending in 7 with a sum multiple of 5.")
    else:
        print(
            "No valid key matches the special condition (ending in 7 and sum multiple of 5)."
        )


if __name__ == "__main__":
    sistema_control_claves()

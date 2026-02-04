# dict comprehension es la misma sintaxis utilizanda para las list comprehension y las genrexps pero con diferencias claves
# las cuales key: va primero mientras que segundo colovamos el valor
# tercero recorremos nuestra lista de tuplas o el elemento que queramos configurar utilizando dict comprehension
# luevo veremos como utilizar esta estructura de dato de forma mas compleja
dial_codes: list[tuple] = [
    (800, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
    (62, "Indonesia"),
    (81, "Japan"),
    (234, "Nigeria"),
    (92, "Pakistan"),
    (7, "Russia"),
    (1, "United states"),
    (57, "Colombia"),
]

# ahora que tenemos nuestra lista de tuplas configuradas supongamos el siguiente caso
# entra el jefe y dice que dicha estructura esta mal ya que tendria que estar los nombres primero
# y los codigos segundos y nos da solo 1 minuto para resolverlo
# tenemos dos formas o reconfigurar la funcion que teniamos o exportar esto de una forma diferente utilizando dict comprehension
dial_codes_dict: dict = {code: key for key, code in dial_codes}
print(dial_codes_dict, "\n")

# Una forma de complejizar nuestro dict comprehensiones aplicando condicionales
# estos son aplicados a el final de la dict comprehension o se provocan al principio
# si los datos que vamos a meter deben estar primero
print(
    {
        code: country.upper()
        for country, code in sorted(dial_codes_dict.items())
        if code < 70
    }
)

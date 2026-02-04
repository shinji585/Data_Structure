# los diccionarios tambien puede ser usados para analizar el texto este analisis puede consistir en contar la longitud de cada palabra o almacenar dichas
# palabras en un formato de k,v donde la k es igual a la palabra y el v termina siendo una matrix que representa la cadena
def wordcount(fname: str) -> dict:
    try:
        fhand = open(fname)
    except Exception:
        print("File canot be opened")
        exit()

    count: dict = {}
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return count


# el codigo anterior cuanta la cantidad de veces que una palabra sale en un archivo
print(wordcount(fname="example.txt"))


# podemos ahora filtrar dichos archivos, sentences o lo que queramos utilizando dict comprehension
count = wordcount(fname="example.txt")
filtered: dict = {key: value for key, value in count.items() if value < 5 and value > 3}
print(f"Valores filtrados: \n{filtered}")

# estas analizando un codigo secreto
# tu meta es tomar un string y crear un diccionario que cuente unicamente las vocales.
# si un caracter is a consonant or a space, your "walk" should ignore it and move to the next step
from typing import Optional

message = "hello data structures"


def f(x: str) -> Optional[dict]:
    # eliminamos los espacios
    x = x.strip()

    mapping: dict = {}
    for vowel in x:
        if vowel in "aeiou":
            if vowel not in mapping:
                mapping[vowel] = 1
            else:
                mapping[vowel] += 1
        else:
            continue
    return mapping


print(f(x=message))

# como transformo esto a dict comprehension

mapping: dict = {vowel: message.count(vowel) for vowel in message if vowel in "aeiou"}
print(f"\nUtilizando dict comprehension: {mapping}")

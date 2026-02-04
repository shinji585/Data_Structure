# en esta seccion se vera lo que es el set comprehension and how to start use it


from unicodedata import name

# name function from unicodedata to obtain character names

print({chr(i) for i in range(32, 256) if "SIGN" in name(chr(i), "")})

# build set of characters with codes from 32 to 255 that have the word "SIGN" in their names
#
# set comprehension is directly inspired by set-builder notation in mathematics:
# { x ∈ s | condition(x)}

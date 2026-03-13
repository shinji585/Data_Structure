from collections import defaultdict

# the defaultdict takes a function object as its first argument. when you access a key that doesn't exits, defaultdict automatically calls that function without arguments to create a suittable
# default value for the key at hand


# defaultdict make this for each value in something if that value doesn't exits then create the key and add the default object (if init 1, if a list create a list each simulitud) something

# examples 1.
#
# here we create a count of letter where if a letter doens't exits on the dictionary
# it create the key and then add the value that we pass it could be whatever but follow the logic you need add the supposed value


contador = defaultdict(int)

text = "banana"

for letter in text:
    contador[letter] += 1


print(dict(contador))

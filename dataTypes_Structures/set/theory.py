# en esta seccion se estara viendo la parte teorica de lo que son los set
#
#
# the books says this: A set is a collections of unique objects.
# were the duplication is removing

list_strings: list = ["spam", "spam", "eggs", "spam", "bacon", "eggs"]

# and if we apply this
print(set(list_strings))

# no puedes cambiar los tipos si utilizas la funcion set

# if you want to remove duplicates but also preserve the order of the first ocurrence of each item


# Set Literals

# the set literals notation looks exactly like the math notation
# {1}, {1,2}, etc
# one important exception: there's no literal notation for the empty set, so must remember to wirte set()
# because if you wirte {} you are creating an empty dict - this hasn't changed in python 3

s: set = {1}
print(type(s))

# with set pop we get the element
print(s.pop())

# and for create an empty set
empty: set = set()
print(f"Set vacio: {empty}")

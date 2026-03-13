# In this section, I'm going to study what is defaultdict inside the collections class and how use it


# defaultdict was created to improve a problem when we have or working with dictionaries
# in those dictionaries you have missing keys and those missing keys 'cause this error: KeyError


# example
favorites = {"pet": "dog", "color": "blue", "language": "python"}

try:
    print(favorites["fruit"])
except Exception:
    pass  # the error is missing because, I add pass, with this key word, I say the program to ignore the error


# for fix this we could get two approach
#
# the first approach is to use setdefault that take the key and if doesn'f found the key then returns a default value


print(favorites.setdefault("fruit", "apple"))


# the second approach is to use get that do the same of setdefault


print(favorites.get("fruit", "apple"))

# the main different here is with setdefault the unknow key is create or added to the dict
# and for get no change


print(favorites)

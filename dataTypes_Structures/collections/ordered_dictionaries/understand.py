# order dict is created for a those special case when you want the order of the entry in dict are the same
# this class follow the same structure that dict but the different is this:
#
# 1. when you compare two objects that are dict and you want to know if they have the same items
# you only put in and that's it but if you don't only want to compare you want to know how they are organized
# here odered dict is a well option


# importating OrderedDict
from collections import OrderedDict

life_stages = OrderedDict()


life_stages["childhood"] = "0-9"
life_stages["adolescence"] = "9-18"
life_stages["adulthood"] = "18-65"
life_stages["old"] = "+65"


# the create a key-value taking the index as the key and value as a content

print(life_stages)

# if you want to show the information as a dict-str or json use the method dict
# print(dict(life_stages))


# we could use the same methods that we have on dict the only different are two methods


# 1. move_to_end(), which is a method that a llows you to manipulate the order of item and put it at the end of the sequence

# 2. popitem() allow us to remove items from ither end of the underlying dictionary


# example
letters = OrderedDict(b=2, d=4, a=1, c=3)

print(letters)


letters.move_to_end("b")
print(letters)

# we can desactive with an atribute that is a bool the last value
letters.move_to_end("b", last=False)
print(letters)

# and we could sorted this element follow the order that how they appear
for key in sorted(letters):
    letters.move_to_end(key=key)

print(letters)

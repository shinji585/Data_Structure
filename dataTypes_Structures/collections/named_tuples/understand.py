# namedtuple are use for solve the problem that each value on the tuple represent whaever
# because it's an empty value and with namedtuple we could add names for find and take the value quickly

from collections import namedtuple

# ejemplo sin namedtuple
point = (
    10,
    20,
)  # we have this and we don't know what this mean really os a point, is some numbers, is the gb that a bytes has, is a sum or multiplication

# and the values don't have names that represent their actions


# bun using nametuple solve this problem

point2 = namedtuple("Point", ["x", "y"])

# and here python know that point2 is a class and it's name is Point and the value (axis) that it has are x and y

use = point2(10, 20)
print(use)


# internally python make this
class Point(tuple):
    __slots__ = ()

    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))

    x = property(lambda self: self[0])
    y = property(lambda self: self[1])


p = Point(10, 20)
print(p.y)

# another form to use this factory is follow the next example
Person = namedtuple("Person", "name job", defaults=["Backend developer"])

# then when we create a instance of this namedtuple it will have the next form:
# Person(name: str,job: Backend developer)
#
# defaults add the default values to the rightmost fields
person = Person(name="samuel", job="Quantitative developer")
person_2 = Person(name="Ana")

print(person)
print(person_2)


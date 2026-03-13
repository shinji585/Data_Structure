# create a set of squares include only numbers divisible by 3

print({x**2 for x in range(10) if x % 3 == 0})

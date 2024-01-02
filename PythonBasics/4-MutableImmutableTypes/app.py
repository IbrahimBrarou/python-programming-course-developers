# integers, bytes, frozen set, tuples, strings, booleans and floating-point numbers are immutable
# x = 1 and x = x+1 will have different locations
x = 1
print(id(x))

x = x+1
print(id(x))

# lists, sets, dictionary, bytearray and array are mutable
# y = [1, 2, 3] and y.append(4) will have the the same location add
y = [1, 2, 3]
print(id(y))

y.append(4)
print(id(y))

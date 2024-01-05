x = 10
y = 11

temp = x
x = y
y = temp
print(x, y)


x, y = y, x  # better in python x, y = (11, 10) it is a tuple unpacking

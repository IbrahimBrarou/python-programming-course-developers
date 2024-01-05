# tuples = read only list : canot modify, add new object, or modifying existing one
point = 1, 2  # or (1, 2) if it is only one number then it needs comma 1,
print(type(point))


point1 = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)
point2 = tuple([1, 2])  # change iterable to tuple
print(point2[0])


x, y = point
if 10 in point:
    print("exist")


point[0] = 1  # is not possible because type is read only

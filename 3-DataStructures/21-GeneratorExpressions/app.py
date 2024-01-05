from sys import getsizeof

values = (x*2 for x in range(10000))
print(getsizeof(values))
# generetor for big amount of data, as theye generate items and not storing them

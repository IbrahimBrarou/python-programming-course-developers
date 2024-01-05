from collections import namedtuple
# When dealing with classes that have no behavior, and just have data, whe can use namedtuple instead.
# Importing form the "collection" module the "namedtuple()" function

Point_t = namedtuple("Point", ['x', "y", "z"])
p4 = Point_t(x=1, y=2, z=3)
p5 = Point_t(x=1, y=2, z=3)
print(p4 == p5)
print(p4)
print(p4.x)

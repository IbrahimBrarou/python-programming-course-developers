class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.z = 10  # objs in python are dynamic similar to js, attributes can be added after creation
point.draw()
print(point.default_color)
print(Point.default_color)


# x, y are called instance attribute they are diff from an obj to another
# default_color is class attribute, it is shared between all objects and it is the same, can be accessed through the class and instances

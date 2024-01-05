# When we call point = Point(1,2), a place in memory is created for point obj and self points to it (the current obj)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
point.draw()

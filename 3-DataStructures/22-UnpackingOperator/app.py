numbers = [1, 2, 3]
print(*numbers)

# * is the same as ... in js

values = list(range(5))
print(*values)  # or values = [*range(5)]


first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 5}  # {"x": 10, "y": 2, "z": 1}

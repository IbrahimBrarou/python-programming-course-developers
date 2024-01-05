# dictions are js objscts


point = {"x": 1, "y": 2}
point2 = dict(x=1, y=2)
print(point["x"])
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
point.get("a", 0)  # if a is not found, return 0
del point["x"]

for key in point:
    print(key, point[key])


for key, value in point.items():
    print(key, value)
point.clear()

# Else Block will execute if the for loop finishes all iterations without calling the break

names = ["aJhon", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")

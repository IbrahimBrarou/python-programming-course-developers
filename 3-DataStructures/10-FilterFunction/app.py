items = [("Product2", 10), ("Product1", 8), ("Product3", 9)]

x = list(filter(lambda item: item[1] >= 10, items))

print(x)

items = [("Product2", 10), ("Product1", 8), ("Product3", 9)]


prices = list(map(lambda item: item[1], items))
prices1 = [item[1] for item in items]  # this is better than map

filtered = list(filter(lambda item: item[1] >= 10, items))
# this is better than filter
filtered1 = [item for item in items if item[1] >= 10]

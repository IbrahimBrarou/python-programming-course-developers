numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)


numbers.sort(reverse=True)
print(numbers)

sorted_numbers = sorted(numbers)
sorted_numbers_reverse = sorted(numbers, reverse=True)


def sort_item(item):
    return item[1]


items = [("Product2", 10), ("Product1", 8), ("Product3", 9)]
items.sort(key=sort_item)
print(items)

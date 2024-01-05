# sets are collections with no duplactes
numbers = [1, 1, 2, 3, 4]
firsts = set(numbers)
second = {1, 4}
second.add(5)
second.remove(5)
len(second)
print(firsts)

print(firsts | second)  # union {1,2,3,4,5}
firsts & second  # intersection {1}
firsts - second  # difference {2,3,4}
firsts ^ second  # symmetric diff {2, 3, 4, 5}
firsts[0]  # not possible to access item at index 0 because sets are unordered: unaccessuible by index

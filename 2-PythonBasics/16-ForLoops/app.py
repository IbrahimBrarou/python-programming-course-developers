for x in "Python":
    print(x)


for x in ['a', 'b', 'c']:
    print(x)

# prints 0, 1, 2, 3, 4
for x in range(5):
    print(x)

# prints 2, 3, 4
for x in range(2, 5):
    print(x)

# will print 0, 2, 4, 6, 8; 2 is the step
for x in range(0, 10, 2):
    print(x)

# range is a range object type and not a list
# range is used because it takes less memory using a counter, better than to have a list of 5 billion items for example

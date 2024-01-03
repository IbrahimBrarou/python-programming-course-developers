# by=1 is default value for by
def increment(number: int, by: int = 1) -> tuple:
    # this is a tuple of the origial number and the modified one
    return (number, number + by)


print(increment(number=2, by=3))
print(increment(number=2))

# This is number=2 a keyword argument, to specify which arg is which

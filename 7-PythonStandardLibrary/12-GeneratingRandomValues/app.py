import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
# returns 2 random values in a list [4, 1]
print(random.choices([1, 2, 3, 4], k=2))
print(random.choices("abcdefh", k=4))  # ['c', 'e', 'h', 'e']

# creates a random password
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)

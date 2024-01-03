name = "Ibrahim"

if not name.strip():
    print("Name is empty")


age = 22
if age >= 18 and age < 65:
    print("Eligible")


# we can also use chanining comparison operators the same as in math.
if 18 <= age < 65:
    print("Eligible")

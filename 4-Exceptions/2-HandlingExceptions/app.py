try:
    age = int(input("Age: "))
except ValueError as ex:
    print("you did not enter a valid age")
    print(ex)
else:
    print("no exceptions were thrown")

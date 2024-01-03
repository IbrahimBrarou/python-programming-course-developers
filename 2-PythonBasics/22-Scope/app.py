def greet():
    if True:
        message = "a"
    print(message)


greet()


message1 = "a"


def greet1():
    global message  # without this line the function will create a new variable called message1
    message1 = "b"


greet1()
print(message1)

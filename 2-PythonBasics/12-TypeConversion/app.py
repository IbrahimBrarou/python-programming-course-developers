# Python is a strongly typed language which means it doesnt do any implicit type conversion on your half

x = input("x: ")
y = x + 1  # will give error
# "1" + "1" > "11" or 1 + 1 > 2

# TO solve the problem we need to cast input
int(x)
float(x)
bool(x)
str(x)

# bool(x) will return false in case of x being false, "", 0, [] or None(null)

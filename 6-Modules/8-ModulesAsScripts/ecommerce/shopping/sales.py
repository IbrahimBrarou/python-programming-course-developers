print("sales initialised")


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":
    print("sales initialised")
    calc_tax()
# In this example if we add the magic method "__name__" to the "print("Sales initialized", __name__)"
# Here we will see the name of the module, but if we run the file in "esales.py" we will get "Sales initialized __main__"
# The name of the module that starts our program is always "__main__"

from abc import ABC, abstractmethod


# Here we are defining an abstract class with an abstract method.
class UIControl(ABC):
    @abstractmethod
    # This abstract method with the decorater "@abstractmethod" difines the common feature or method that must be implemented in the the class that derive from  "UIControl()".
    def draw(self):
        pass


# Here we define a class deriving from "UIControl()".
class TextBox(UIControl):
    def draw(self):
        print("TextBox")


# Here we define another class derivign from "UIContorl()".
class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# def draw(control): # Here we also have a funtion called draw, tjat takes a controle object and call the draw method in that object.
#     control.draw()

# here we create a DropDownList object by istanciate the "DropDownList()" in the variable "ddl".
ddl = DropDownList()
# Because the "DropDownList()" class derives from the class "UIControl()" the "ddl" object is an istance of the "UIControl()" class.
print(isinstance(ddl, UIControl))

tb = TextBox()
print(isinstance(tb, UIControl))

# draw(ddl) # Here we apply the function draw in the variable "ddl" that will call the drw mehtod from the "dropDownList()" class.
# draw(tb)


# Here we would implment a function that takes an iteable like a list or a tuple and iterates over it with a for loop.
def draw(controls):
    for control in controls:  # In each iterations it will call the "draw()" method from "DropDownList()" or "TextBox()", depending on each obect it iterates.
        control.draw()


draw([ddl, tb])  # Passing the list to the function "draw()",

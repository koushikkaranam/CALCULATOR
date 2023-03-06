from tkinter import *
import operations
import math

root = Tk()
root.title("CALCULATOR")


# Create Widgets

inputField = Entry(root, width=35, borderwidth=3)



def button_click(number):
    current = inputField.get()
    inputField.delete(0, END)
    return inputField.insert(0, str(current) + str(number))
def button_clear():
    inputField.delete(0, END)
def add():
    first_number = inputField.get()
    global f_num
    global ops
    ops = "add"
    f_num = float(first_number)
    inputField.delete(0,END)
def subtract():
    first_number = inputField.get()
    global f_num
    global ops
    ops = "subtract"
    f_num = float(first_number)
    inputField.delete(0,END)
def multiply():
    first_number = inputField.get()
    global f_num
    global ops
    ops = "multiply"
    f_num = float(first_number)
    inputField.delete(0,END)
def divide():
    first_number = inputField.get()
    global f_num
    global ops
    ops = "divide"
    f_num = float(first_number)
    inputField.delete(0,END)
def squareRoot():
    first_number = inputField.get()
    inputField.delete(0,END)
    inputField.insert(0, math.sqrt(float(first_number)))
def backSpace():
    first_number = inputField.get()
    inputField.delete(0,END)
    inputField.insert(0, first_number[:-1])
def percent():
    first_number = float(inputField.get())
    inputField.delete(0,END)
    inputField.insert(0, first_number/100)
def equals():
    second_number = inputField.get()
    inputField.delete(0,END)
    if ops == "add":
        inputField.insert(0, f_num + float(second_number))
    if ops == "subtract":
        inputField.insert(0, f_num - float(second_number))
    if ops == "multiply":
        inputField.insert(0, f_num * float(second_number))
    if ops == "divide":
        inputField.insert(0, f_num / float(second_number))
num0 = Button(root, text=" 0 ", padx=40, pady=20, command=lambda: button_click(0))
num1 = Button(root, text=" 1 ", padx=40, pady=20, command=lambda: button_click(1))
num2 = Button(root, text=" 2 ", padx=40, pady=20, command=lambda: button_click(2))
num3 = Button(root, text=" 3 ", padx=40, pady=20, command=lambda: button_click(3))
num4 = Button(root, text=" 4 ", padx=40, pady=20, command=lambda: button_click(4))
num5 = Button(root, text=" 5 ", padx=40, pady=20, command=lambda: button_click(5))
num6 = Button(root, text=" 6 ", padx=40, pady=20, command=lambda: button_click(6))
num7 = Button(root, text=" 7 ", padx=40, pady=20, command=lambda: button_click(7))
num8 = Button(root, text=" 8 ", padx=40, pady=20, command=lambda: button_click(8))
num9 = Button(root, text=" 9 ", padx=40, pady=20, command=lambda: button_click(9))
add = Button(root, text=" + ", padx=40, pady=20, command= add)
subtract = Button(root, text=" - ", padx=40, pady=20, command= subtract)
multiply = Button(root, text=" * ", padx=40, pady=20, command= multiply)
divide = Button(root, text=" / ", padx=40, pady=20, command= divide)
clear = Button(root, text="AC", padx=40, pady=20, command=button_clear)
squareRoot = Button(root, text=" V- ", padx=40, pady=20, command= squareRoot)
percent = Button(root, text=" % ", padx=40, pady=20, command= percent)
equals = Button(root, text=" = ", padx=40, pady=20, command= equals)
backSpace = Button(root, text=" < ", padx=40, pady=20, command= backSpace)
decimalPoint = Button(root, text=" . ", padx=40, pady=20, command=lambda: button_click("."))
# Display on screen
inputField.grid(row=0, column=0, columnspan=4, padx=10)
clear.grid(row=1, column=0)
squareRoot.grid(row=1, column=1)
percent.grid(row=1, column=2)
divide.grid(row=1, column=3)
num7.grid(row=2, column=0)
num8.grid(row=2, column=1)
num9.grid(row=2, column=2)
multiply.grid(row=2, column=3)
num4.grid(row=3, column=0)
num5.grid(row=3, column=1)
num6.grid(row=3, column=2)
subtract.grid(row=3, column=3)
num1.grid(row=4, column=0)
num2.grid(row=4, column=1)
num3.grid(row=4, column=2)
add.grid(row=4, column=3)
num0.grid(row=5,column=0)
decimalPoint.grid(row=5,column=1)
backSpace.grid(row=5,column=2)
equals.grid(row=5,column=3)


root.mainloop()

from tkinter import *

root = Tk()
root.title("SHIT")

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# e.insert(0, "Enter a Value you Shit!")


def value(number):
    # e.delete(0, END)
    temp = e.get()
    e.delete(0, END)
    e.insert(0, str(temp) + str(number))


def clr():
    e.delete(0, END)


def add():
    first_value = e.get()
    global f_num
    f_num = int(first_value)
    e.delete(0, END)


def equal():
    second_value = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_value))


# Define btn

b_1 = Button(root, text="1", padx=25, pady=10, command=lambda: value(1))
b_2 = Button(root, text="2", padx=25, pady=10, command=lambda: value(2))
b_3 = Button(root, text="3", padx=25, pady=10, command=lambda: value(3))
b_4 = Button(root, text="4", padx=25, pady=10, command=lambda: value(4))
b_5 = Button(root, text="5", padx=25, pady=10, command=lambda: value(5))
b_6 = Button(root, text="6", padx=25, pady=10, command=lambda: value(6))
b_7 = Button(root, text="7", padx=25, pady=10, command=lambda: value(7))
b_8 = Button(root, text="8", padx=25, pady=10, command=lambda: value(8))
b_9 = Button(root, text="9", padx=25, pady=10, command=lambda: value(9))
b_0 = Button(root, text="0", padx=25, pady=10, command=lambda: value(0))

b_add = Button(root, text="+", padx="24", pady=10, command=lambda: add())
b_equal = Button(root, text="=", padx="48", pady=10, command=lambda: equal())
b_clear = Button(root, text="C", padx="48", pady=10, command=clr)

# Organizing btn on screen


b_1.grid(row=3, column=0)
b_2.grid(row=3, column=1)
b_3.grid(row=3, column=2)

b_4.grid(row=2, column=0)
b_5.grid(row=2, column=1)
b_6.grid(row=2, column=2)

b_7.grid(row=1, column=0)
b_8.grid(row=1, column=1)
b_9.grid(row=1, column=2)

b_0.grid(row=4, column=0)
b_add.grid(row=5, column=0)
b_equal.grid(row=5, column=1, columnspan=2)
b_clear.grid(row=4, column=1, columnspan=2)

# m1 = Button(root, text="Click Here", command=Add, bg="purple")

root.mainloop()

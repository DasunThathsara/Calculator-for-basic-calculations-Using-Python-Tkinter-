from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=10)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# ------------------------------ Numbers Click ------------------------------
def button_click(number):
    global n
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
# --------------------------------- Clear -----------------------------------
def button_clear():
    e.delete(0, END)
# ---------------------------------- ADD ------------------------------------
def button_add():
    global TOO
    TOO = "add"
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
# ---------------------------------- DIF ------------------------------------
def button_dif():
    global TOO
    TOO = "dif"
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
# ---------------------------------- MUL ------------------------------------
def button_mul():
    global TOO
    TOO = "mul"
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
# ---------------------------------- DIV ------------------------------------
def button_div():
    global TOO
    TOO = "div"
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
# ---------------------------------- PM -------------------------------------
def button_PM():
    number = e.get()
    e.delete(0, END)
    global f_num
    if float(number)<0:
        f_num = float(number[1:])
    else:
        f_num = -abs(float(number))
    e.insert(0, f_num)
# ---------------------------------- Equal -----------------------------------
def button_equal():
    try:
        secound_number = e.get()
        e.delete(0, END)
        if TOO=="add":
            e.insert(0, f_num + float(secound_number))
        elif TOO=="dif":
            e.insert(0, f_num - float(secound_number))
        elif TOO=="mul":
            e.insert(0, f_num * float(secound_number))
        elif TOO=="div":
            e.insert(0, f_num / float(secound_number))
    except ZeroDivisionError:
        e.insert(0, "Error : Zero Division Error")
    except NameError:
        e.insert(0, "0")
    except ValueError:
        e.insert(0, "Error : Please Enter Valid Numbers")
# ------------------------------ Define Button ------------------------------

button_add = Button(root, text="+", padx=20, pady=10, comman=button_add, borderwidth=5)
button_dif = Button(root, text="-", padx=20, pady=10, comman=button_dif, borderwidth=5)
button_mul = Button(root, text="x", padx=20, pady=10, comman=button_mul, borderwidth=5)
button_div = Button(root, text="/", padx=20, pady=10, comman=button_div, borderwidth=5)
button_equal = Button(root, text="=", padx=60, pady=10, comman=button_equal, borderwidth=5)
button_clear = Button(root, text="Clear", padx=60, pady=10, comman=button_clear, borderwidth=5)
button_PM = Button(root, text="+/-", padx=24, pady=10, comman=button_PM, borderwidth=5)

button_1 = Button(root, text="1", padx=30, pady=10, comman=lambda: button_click(1), borderwidth=5)
button_2 = Button(root, text="2", padx=30, pady=10, comman=lambda: button_click(2), borderwidth=5)
button_3 = Button(root, text="3", padx=30, pady=10, comman=lambda: button_click(3), borderwidth=5)
button_4 = Button(root, text="4", padx=30, pady=10, comman=lambda: button_click(4), borderwidth=5)
button_5 = Button(root, text="5", padx=30, pady=10, comman=lambda: button_click(5), borderwidth=5)
button_6 = Button(root, text="6", padx=30, pady=10, comman=lambda: button_click(6), borderwidth=5)
button_7 = Button(root, text="7", padx=30, pady=10, comman=lambda: button_click(7), borderwidth=5)
button_8 = Button(root, text="8", padx=30, pady=10, comman=lambda: button_click(8), borderwidth=5)
button_9 = Button(root, text="9", padx=30, pady=10, comman=lambda: button_click(9), borderwidth=5)
button_0 = Button(root, text="0", padx=30, pady=10, comman=lambda: button_click(0), borderwidth=5)
button_dot = Button(root, text=".", padx=30, pady=10, comman=lambda: button_click("."), borderwidth=5)

# ------------------------ Put the button on the screen -----------------------

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_mul.grid(row=2, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_dif.grid(row=3, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_0.grid(row=4, column=1)
button_dot.grid(row=4, column=0)
button_PM.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_clear.grid(row=5, column=0, columnspan=2)
button_equal.grid(row=5, column=2, columnspan=2)



root.mainloop()

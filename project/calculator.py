from tkinter import *

calculation = ""


def add_to_calculations(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculations():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = Tk()
root.geometry("420x390")           # Size of total box
root.title("Simple Calculator")    # Tittle of the calculator

text_result = Text(root, height=2, width=24, font=("Arial", 24))
text_result.grid(columnspan=5)
b1 = Button(root, text="1", command=lambda: add_to_calculations(1), width=5, font=("Arial", 24))
b1.grid(row=2, column=1)

b2 = Button(root, text="2", command=lambda: add_to_calculations(2), width=5, font=("Arial", 24))
b2.grid(row=2, column=2)

b3 = Button(root, text="3", command=lambda: add_to_calculations(3), width=5, font=("Arial", 24))
b3.grid(row=2, column=3)

b_plus = Button(root, text="+", command=lambda: add_to_calculations("+"), width=5, font=("Arial", 24))
b_plus.grid(row=2, column=4)

b4 = Button(root, text="4", command=lambda: add_to_calculations(4), width=5, font=("Arial", 24))
b4.grid(row=3, column=1)

b5 = Button(root, text="5", command=lambda: add_to_calculations(5), width=5, font=("Arial", 24))
b5.grid(row=3, column=2)

b6 = Button(root, text="6", command=lambda: add_to_calculations(6), width=5, font=("Arial", 24))
b6.grid(row=3, column=3)

b_minus = Button(root, text="-", command=lambda: add_to_calculations("-"), width=5, font=("Arial", 24))
b_minus.grid(row=3, column=4)

b7 = Button(root, text="7", command=lambda: add_to_calculations(7), width=5, font=("Arial", 24))
b7.grid(row=4, column=1)

b8 = Button(root, text="8", command=lambda: add_to_calculations(8), width=5, font=("Arial", 24))
b8.grid(row=4, column=2)

b9 = Button(root, text="9", command=lambda: add_to_calculations(9), width=5, font=("Arial", 24))
b9.grid(row=4, column=3)

b_mul = Button(root, text="*", command=lambda: add_to_calculations("*"), width=5, font=("Arial", 24))
b_mul.grid(row=4, column=4)

b_open = Button(root, text="(", command=lambda: add_to_calculations("("), width=5, font=("Arial", 24))
b_open.grid(row=5, column=1)

b0 = Button(root, text="0", command=lambda: add_to_calculations(0), width=5, font=("Arial", 24))
b0.grid(row=5, column=2)

b_close = Button(root, text=")", command=lambda: add_to_calculations(")"), width=5, font=("Arial", 24))
b_close.grid(row=5, column=3)

b_div = Button(root, text="/", command=lambda: add_to_calculations("/"), width=5, font=("Arial", 24))
b_div.grid(row=5, column=4)

b_equals = Button(root, text="=", command=lambda: evaluate_calculations(), width=11, font=("Arial", 24))
b_equals.grid(row=6, column=3, columnspan=2)

b_clear = Button(root, text="C", command=lambda: clear_field(), width=11, font=("Arial", 24))
b_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
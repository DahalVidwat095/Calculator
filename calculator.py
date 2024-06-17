from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap('calculator.ico')  

e = Entry(root, width=24, borderwidth=14, font=("Verdana", 18), bg="white", justify=RIGHT)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(END, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_total():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons
row_val = 1
col_val = 0
for button_val in buttons:
    button = Button(root, text=button_val, padx=20, pady=20, bd=5, font=("Verdana", 16), command=lambda x=button_val: button_click(x))
    if button_val == '=':
        button.config(bg='red', fg='white')
        button['command'] = button_total
    elif button_val == 'C':
        button.config(bg='slate gray2', fg='white')
        button['command'] = button_clear
    elif button_val in ['+', '-', '*', '/']:
        button.config(bg='green')
        if button_val == '+':
            button['command'] = button_add
        elif button_val == '-':
            button['command'] = button_subtract
        elif button_val == '*':
            button['command'] = button_multiply
        else:
            button['command'] = button_divide
    button.grid(row=row_val, column=col_val, sticky=NSEW)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()

from tkinter import *

def click(event):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + event.widget["text"])

def clear():
    entry.delete(0, END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Window setup
root = Tk()
root.title("Simple Calculator")

# Entry field
entry = Entry(root, font=("Arial", 18), bd=5, relief=SUNKEN, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Place buttons
row_val = 1
col_val = 0

for btn_text in buttons:
    btn = Button(root, text=btn_text, font=("Arial", 18), width=4, height=2)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    if btn_text == "=":
        btn.config(command=evaluate)
    elif btn_text == "C":
        btn.config(command=clear)
    else:
        btn.bind("<Button-1>", click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()

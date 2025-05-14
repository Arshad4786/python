from tkinter import *

root = Tk()
root.title("Greeting")

root.minsize(777,444)

def greet():
    name = entry.get()
    if name:
        label1.config(text=f"Hello, {name}!")
    else:
        label1.config(text="Please Enter your name")

label = Label(root,text="Please Enter you Name")
label.pack()

entry = Entry(root,borderwidth=6,bg='white')
entry.pack(pady=15)

submit = Button(root,text="Submit",command=greet)
submit.pack()

label1 = Label(root,text=" ")
label1.pack()

root.mainloop()

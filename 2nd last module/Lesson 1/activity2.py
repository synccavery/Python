from tkinter import *
from datetime import date
window = Tk()
window.title('Getting started with Widgets')
window.geometry('400x300')
lbl = Label(window, text="Hey There!", fg="white", bg ="#C19A6B", height = 1, width = 300)
lbl.pack()
name_lbl = Label(window, text="Full Name", fg="white", bg ="#C2B19D")
name_lbl.pack()
name_entry = Entry(window, width=20)
name_entry.pack()

def display():
    name = name_entry.get()
    global message
    message = f"Hello {name}. \nWelcome to the world of Python Tkinter!\nToday's date id {date.today()}."
    text_box.insert(END, message)
text_box = Text(height = 3)
text_box.pack()
btn = Button(window, text="Click me!", command=display)
btn.pack()
window.mainloop()
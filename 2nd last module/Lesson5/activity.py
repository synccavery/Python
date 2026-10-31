from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Denomination Counter")
window.configure(bg="lightblue")
window.geometry("650x400")

label1 = Label(window, text="Hey, user! Welcome to Denomination Counter Application", bg="lightblue")
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.askokcancel("Alert", "Do you want to calculate the denomination count?")
    if MsgBox:  # True if user clicks OK
        topwin()

button1 = Button(window, text="Let's Get started!", command=msg, bg="brown", fg="white")
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Counter")
    top.configure(bg="lightblue")
    top.geometry("650x400")

    label = Label(top, text="Enter your amount", bg="lightgrey")
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg="lightgrey")
    l1 = Label(top, text="1000", bg="lightgrey")
    l2 = Label(top, text="500", bg="lightgrey")
    l3 = Label(top, text="100", bg="lightgrey")
    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)

    def calculate():
        try:
            amount = int(entry.get())
            note1000 = amount // 1000
            amount = amount % 1000
            note500 = amount // 500
            amount = amount % 500
            note100 = amount // 100
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e1.insert(END, str(note1000))
            e2.insert(END, str(note500))
            e3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    btn = Button(top, text="Calculate", command=calculate, bg="brown", fg="white")
    
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)  # Fixed from 1200 to 120
    lbl.place(x=140, y=170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    e1.place(x=270, y=200)
    e2.place(x=270, y=230)
    e3.place(x=270, y=260)

window.mainloop()

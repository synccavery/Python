from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("300x300")
# Event handler for a keypress from the keyboard
def handle_keypress(event):
    print("key pressed:", event.char)
window.bind("<Key>", handle_keypress)
# Event handler for a mouse click
def handle_mouse_click(event):
    print("The mouse is clicked")
button = Button(window, text="Click Me!")
button.pack()
button.bind("<Button-1>", handle_mouse_click)

window.mainloop()

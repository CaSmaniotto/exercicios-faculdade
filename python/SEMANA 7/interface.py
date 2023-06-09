from tkinter import Tk, Label, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
    showinfo(message=time)

window = Tk()
button = Button(window, text='Clique!', command=clicked)
button.pack()
window.minsize(100, 100)
window.mainloop()

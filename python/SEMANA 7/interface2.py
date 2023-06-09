from tkinter import Tk, Label, Button, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime

def clicked():
    global entry
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%b %d %Y'))
    showinfo(message=f'{date} foi um(a) {weekday}')

window = Tk()
label = Label(window, text='Digite a data: ')
label.grid(row=0, column=0)
entry = Entry(window)
entry.grid(row=0, column=1)

button = Button(window, text='Clique!', command=clicked)
button.grid(row=1, column=0, columnspan=2)
window.minsize(height=200, width=250)
window.mainloop()

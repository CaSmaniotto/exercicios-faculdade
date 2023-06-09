import calendar
from tkinter import *
from calendar import monthrange

def cal(x, y):

    window = Tk()
    window.title('Calendário')

    dia, n_dias = monthrange(x, y)
    d_semana = ['Mon', 'Tue', 'Wed', 'Thu', 'Fry', 'Sat', 'Sun']


    sem = 1
    for i in range(7):
        label = Label(window, text=d_semana[i])
        label.grid(row=0, column=i)

    for i in range(1, n_dias+1):
        label_dias = Label(window, text= i)
        label_dias.grid(row=sem, column=dia)

        dia += 1
        if dia > 6:
            dia = 0
            sem += 1

    window.mainloop()

cal(2022, 10)

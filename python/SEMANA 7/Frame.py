from tkinter import Tk, Canvas, Frame,Button, SUNKEN, LEFT, RIGHT

window = Tk()

def up():
    global y, canvas
    canvas.create_line(x, y, x, y-10)
    y -= 10

def left():
    global y, canvas, x
    canvas.create_line(x, y, x-10, y)
    x -= 10

def right():
    global y, canvas, x
    canvas.create_line(x, y, x+10, y)
    x += 10

def down():
    global y, canvas
    canvas.create_line(x, y, x, y+10)
    y += 10

canvas = Canvas(window, height=100, width=150, relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)
box = Frame(window)
box.pack(side=RIGHT)

button = Button(box, text='up',command=up)
button.grid(row=0, column=0,columnspan=2)
button = Button(box, text='left',command=left)
button.grid(row=1, column=0)
button = Button(box, text='right',command=right)
button.grid(row=1, column=1)
button = Button(box, text='down',command=down)
button.grid(row=2, column=0,columnspan=2)

x,y = 50, 75 # posição da caneta, inicialmente no meio

window.mainloop()
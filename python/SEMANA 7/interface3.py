from tkinter import Tk, Text, BOTH

def key_pressed(event):
    print('char: {}'.format(event.keysym))

def mouse_clicked_left(event):
    print('mouse left clicked')

def mouse_clicked_right(event):
    print('mouse right clicked')

window = Tk()
text = Text(window, width=20, height='5')
text.bind('<KeyPress>', key_pressed)
text.bind('<Button-1>', mouse_clicked_left)
text.bind('<Button-3>', mouse_clicked_right)
text.pack(expand=True, fill=BOTH)
window.mainloop()

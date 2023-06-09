from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM, SUNKEN


root = Tk()
labels = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]

root.title('Calculadora')
# não é uma calculadora

for r in range(4):
    for c in range(3):
        label = Label(root, relief=SUNKEN, bg='Red', padx=10, text=labels[r][c], width=5, height=5)
        label.grid(row=r, column=c)
root.mainloop()
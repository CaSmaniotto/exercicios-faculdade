from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='coin.gif').subsample(2)
image = Label(master=root, image=photo) #width=300, height=300 para alterar a resolucao da janela
image.pack(side=TOP)
hello = Label(master=root, font=("Arial", 18),  text='Olá!')
hello.pack(side=BOTTOM)
root.mainloop()


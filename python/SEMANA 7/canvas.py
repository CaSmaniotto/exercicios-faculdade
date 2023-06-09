from tkinter import Tk, Canvas

window = Tk()

def begin(event):
    'inicializa o início da curva com a posição do mouse '
    global oldx, oldy
    oldx, oldy = event.x, event.y

def draw(event):
    'desenha um segmento de linha da posição antiga do mouse à nova'
    global oldx, oldy, canvas # x e y serão mudados

    newx, newy = event.x, event.y # nova posição do mouse

    # conecta posição anterior do mouse à atual
    canvas.create_line(oldx, oldy, newx, newy)

    oldx, oldy = newx, newy # nova posição torna-se a anterior

oldx, oldy = 0, 0 # coordenadas do mouse (variáveis globais)

canvas = Canvas(window, height=400, width=400)

canvas.bind("<Button-1>", begin)
canvas.bind("<Button1-Motion>", draw)

canvas.pack()
window.mainloop()

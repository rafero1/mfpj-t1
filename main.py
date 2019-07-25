from tkinter import Tk, Canvas, BOTH, LAST
from random import shuffle
from vector import Vector2D
from functools import partial
from copy import deepcopy

root = Tk()
root.geometry("600x600")
root.title("Editor de Vetores")

click_flag = False
x, y = 0, 0
vecs = []


def draw_textbox(vec):
    """Desenha uma label para o vetor"""
    center_x = (vec.x1 + vec.x2)/2
    center_y = (vec.y1 + vec.y2)/2
    t = canvas.create_text(center_x, center_y, anchor="center", text=vec.name, tag=vec.name)
    r = canvas.create_rectangle(canvas.bbox(t), fill="white", outline="white", tag=vec.name)
    canvas.tag_lower(r, t)


def draw_vec(vec, label=True):
    """Desenha o vetor no canvas"""
    canvas.create_line(vec.getPos(), width=2, fill=vec.color, tag=vec.name, arrow=LAST)
    if label is True:
        draw_textbox(vec)


def remove_vec(vec):
    """Remove o vetor do canvas"""
    canvas.delete(vec.name)


def click(event):
    global x, y, click_flag, vecs
    if click_flag:
        # Criar o vetor
        vec = Vector2D(x, y, event.x, event.y)
        vec.name = "v" + str(len(vecs)+1)
        vec.color = "black"
        vecs.append(vec)

        # Desenhar o vetor na tela
        draw_vec(vec)

        # Desenha o vetor soma
        if (len(vecs) > 1):
            sum_vec = Vector2D(vecs[0].x1, vecs[0].y1, 0, 0)
            for vect in vecs:
                sum_vec += vect
            sum_vec.name = "vR"
            sum_vec.color = "#c314ce"
            remove_vec(sum_vec) # Se achar um vetor já desenhado com essa tag, deleta ele
            draw_vec(sum_vec, False)

        # Setar ponto de origem para o próximo vetor
        x, y = event.x, event.y
    else:
        # Setar a origem
        x, y = event.x, event.y
        click_flag = True

def rearrange(event):
    global vecs
    # Remove os vetores desenhados
    for vec in vecs:
        remove_vec(vec)
    # Cria nova lista randomizada
    vecs2 = deepcopy(vecs)
    shuffle(vecs2)
    # Desenha os vetores randomizados
    n = 0
    for vec in vecs2:
        if (n == 0):
            # Se for o primeiro vetor da lista
            vec.x1 = vecs[n].x1
            vec.y1 = vecs[n].y1
            vec.x2 = vecs[n].x1 + vec.x
            vec.y2 = vecs[n].y1 + vec.y
        else :
            vec.x1 = vecs2[n-1].x2
            vec.y1 = vecs2[n-1].y2
            vec.x2 = vec.x1 + vec.x
            vec.y2 = vec.y1 + vec.y
        draw_vec(vec)
        n += 1

canvas = Canvas(root)
canvas.bind("<Button-1>", click) # Botão esquerdo do mouse
canvas.bind("<Button-3>", rearrange) # Botão direito do mouse
canvas.pack(fill=BOTH, expand=1)
root.mainloop()
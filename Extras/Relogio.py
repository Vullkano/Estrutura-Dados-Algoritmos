import datetime
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class Clock:
    def __init__(self, master):
        self.nossaTela = master
        self.lblRelogio = tk.Label(
            self.nossaTela, font=('Times New Roman', 80), fg='Black', background='pink')
        self.lblRelogio.pack(pady=30, padx=30)
        self.alteracao()

    def alteracao(self):
        now = datetime.datetime.now()

        self.lblRelogio['text'] = now.strftime('%H:%M:%S - %d/%m/%Y')

        self.nossaTela.after(100, self.alteracao)


janelaRaiz = tk.Tk()

janelaRaiz.title('Clock')

image = Image.open('juan.jpg')
tk_image = ImageTk.PhotoImage(image)
canvas = Canvas(janelaRaiz, width=300, height=700)
canvas.pack(fill="both", expand=True, side='bottom')

# Display image
canvas.create_image(0, 0, image=tk_image, anchor="nw")

janelaRaiz.geometry('1050x1100')

# janelaRaiz.config(background='C:/Users/diogo/OneDrive/Ambiente de Trabalho/Concurso/Juan.jpg')
Clock(janelaRaiz)

janelaRaiz.mainloop()

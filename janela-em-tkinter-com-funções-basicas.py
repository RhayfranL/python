#coding: utf-8
from tkinter import *
root = Tk()
a = 1
def seguir():
     #Mensagem que aparece no terminal ao clicar o botão
     print("Clicado")
     #Muda o valor "text" da label para Clicado
     lbl['text'] = "Clicado"


#Botão
bt1 = Button(root, width=20, text="Seguir", command=seguir)
#Posição do botão
bt1.place(x=0, y=1)
#Label
lbl = Label(root, width=20, text="1")
#Posição da Label
lbl.place(x=0, y=30)


root.geometry("400x400")
root.mainloop()

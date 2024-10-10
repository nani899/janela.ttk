from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox

def conf():
    tk.Message('Are You Sure?')

def verificar():
    nomr = nom.get()
    senhr = sen.get()
    if nomr == "vai bolsonaro" and senhr == "vai 17 vai 17":
        messagebox.showinfo("Title", 'Senha certa meu querido')
    else:
        messagebox.showerror("Tittle", 'saporra ta errada seu merda do cacete')

janela_ = tk.Tk()
janela_.title("Login Para Cadastro")
janela_.geometry("400x400")
janela_.config(background='black')


bt = tk.Button(janela_,text='fecha', command= janela_.destroy)
bt.config(background='green')
bt.place(y=0, x=130, width= 130, height= 40)

nome = tk.Label(janela_,text='Insira Aqui Embaixo Seu Nome')
nome.place(y=50, x=70, width= 250, height= 40)
nome.config(font=20, background='pink')

nom = tk.Entry(janela_)
nom.place(y=100, x=99, width= 190, height= 40)
nom.config(font=20, background='pink')

#---------------------------------------------------------------------------------------------|
#nome acima e senha abaixo  🐈🐈🐈🐈🐈🐈🐈🐈🐈🐈🐈🐈                                    |
#---------------------------------------------------------------------------------------------|

senh = tk.Label(janela_,text='Insira Aqui Embaixo Seu Nome')
senh.place(y=150, x=70, width= 250, height= 40)
senh.config(font=20, background='pink')

sen = tk.Entry(janela_)
sen.place(y=200, x=99, width= 190, height= 40)
sen.config(font=50, background='pink')

bt = tk.Button(janela_,text='Confirmar', command= verificar)
bt.config(background='green')
bt.place(y=300, x=80, width= 230, height= 40)

janela_.mainloop()
import sys
import tkinter
from tkinter import ttk

def funcion():
    print('clicado')
def saludar(event):
    print('click')
def salir(event):
    print('adios')
    window.quit()


window = tkinter.Tk()

#window.columnconfigure(0, weight = 1)
#window.columnconfigure(1, weight = 3)

frame = ttk.Frame(window)
frame['relief']='sunken'

lista =['Windows','Mac OS','MS DOS','Linux','AmigaOS','BeOS','OS/2']
lista_items = tkinter.StringVar(value=lista)

listbox=tkinter.Listbox(window, height=100, listvariable=lista_items)
#listbox.grid(column=0,row=0,sticky=tkinter.W)

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Si', value='1', variable=selected)
#r1.grid(column=3,row=1, padx=5,pady=5)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected)
#r2.grid(column=3,row=2, padx=5,pady=5)
r3 = ttk.Radiobutton(window, text='Quizá', value='3', variable=selected)
#r3.grid(column=3,row=3, padx=5,pady=5)
label=ttk.Label(frame, text='hola')
#label.grid(column=0,row=0,sticky=tkinter.W, padx=50, pady=50)
#frame.grid(column=0,row=0,sticky=tkinter.W, padx=50, pady=50)

boton = tkinter.Button(window, text='Haz click')
boton.pack()
boton.bind('<Button-1>', saludar)

boton = tkinter.Button(window, text='Salir')
boton.pack()
boton.bind('<Button-1>', salir)

seleccion = tkinter.StringVar()
#checkbox = ttk.Checkbutton(
#    window, text='acepto las condiciones', variable= seleccion, command =funcion)
#checkbox.grid(row = 0, column=3)
window.mainloop()
sys.exit()

window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 3)

username_label = ttk.Label(window, text = 'Username:')
username_label.grid(column=0,row = 0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5,pady=5)

password_label = ttk.Label(window, text='Password:')
password_label.grid(column=0, row=1, sticky=tkinter.E, padx=5, pady=5)

password_entry = ttk.Entry(window, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

login_button = ttk.Button(window, text = 'enviar')
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5,pady=5)


from tkinter import *

window = Tk()
opcion = StringVar()
opcion.set(None)

lista =['Windows','Mac OS','MS DOS','Linux','AmigaOS','BeOS','OS/2']
lista_items = StringVar(value=lista)

listbox= Listbox(window, height=10, listvariable=lista_items)
listbox.grid(column=0,row=0,sticky= W)

password_label = Label(window, text='Selección:')
password_label.grid(column=2, row=0, sticky=E, padx=5, pady=5)

monitor = Label(window)
monitor.grid(column=3, row = 0, sticky=E, padx=5, pady=5)

def seleccion(event):
    opcion.set(listbox.get(listbox.curselection()))
    monitor.config(text="{}".format(opcion.get()))


listbox.bind('<<ListboxSelect>>', seleccion)


window.mainloop()

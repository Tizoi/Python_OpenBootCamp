import tkinter
import pprint
import time

window = tkinter.Tk()
label_saludo = tkinter.Label(window, text = '¡Hola!', bg='yellow', fg='blue')
label_saludo.pack(ipadx=50,ipady=50, expand = True)

label_adios = tkinter.Label(window, text = 'Adios :(', bg = 'red', fg = 'white')
label_adios.pack(ipadx=50, ipady=100, fill = 'both', expand = True)

label_opcion = tkinter.Label(window, text = 'opción', bg = 'blue', fg = 'green')
label_opcion.pack(ipadx=30, ipady=30, side = 'left')

window.mainloop()


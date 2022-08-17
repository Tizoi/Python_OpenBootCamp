import sys
import tkinter
from tkinter import ttk



window = tkinter.Tk()

def reiniciar(event):
    global selected
    del selected

selected = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text='Si', value='1', variable=selected)
r1.grid(column=0,row=1, padx=5,pady=5)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected)
r2.grid(column=0,row=2, padx=5,pady=5)
r3 = ttk.Radiobutton(window, text='Quizá', value='3', variable=selected)
r3.grid(column=0,row=3, padx=5,pady=5)

boton = tkinter.Button(window, text='Reiniciar')
boton.grid(column=0,row=4, padx=5,pady=5)
boton.bind('<Button-1>', reiniciar)


window.mainloop()
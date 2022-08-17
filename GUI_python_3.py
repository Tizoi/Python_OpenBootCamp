import tkinter
from tkinter import ttk

window = tkinter.Tk()

label1 = tkinter.Label(window, text='Posicimiento absoluto', bg='blue', fg='white')
label1.place(x=10, y=50)

label1 = tkinter.Label(window, text='otro más ñ', bg='red', fg='white')
label1.place(x=150, y=200, anchor='sw')


window.mainloop()
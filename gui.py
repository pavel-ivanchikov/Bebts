from ProcessesManager import ProcessesManager
from tkinter import *
import os

def change():
    if button['text'] == 'Putin':
        button['text'] = 'Hyilo'
    else:
        button['text'] = 'Putin'


def new_button():
    button3.pack()


def new_button_act():
    button.destroy()


path = r"C:/DebtCounter/first/"
pm = ProcessesManager(path)

root = Tk()
a = Label(root, text="Debt Counter")

buttons = {}
for name in pm.main_dict.keys():
    buttons[name] = Button(root, text=name, command=new_button)

button = Button(root, text='Hi', command=change)
button2 = Button(root, text='Close', command=quit)

button3 = Button(root, text='Hi', command=new_button_act)

a.pack()
button.pack()
for i in buttons.values():
    i.pack()
button2.pack()

root.mainloop()



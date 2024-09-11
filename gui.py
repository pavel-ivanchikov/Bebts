from ProcessesManager import ProcessesManager
from tkinter import *


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
first_process_name = '1726038875105655'

pm = ProcessesManager(path, first_process_name)

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



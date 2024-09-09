from ProcessesManager import ProcessesManager
from tkinter import *
root = Tk()
a = Label(root, text="Debt Counter")

path = r"C:/DebtCounter/first/"
first_process_name = '1725860502812180'

pm = ProcessesManager(path, first_process_name)


def change():
    if button['text'] == 'Putin':
        button['text'] = 'Hyilo'
    else:
        button['text'] = 'Putin'


buttons = {}
for name in pm.main_dict.keys():
    buttons[name] = Button(root, text=name, command=quit)


button = Button(root, text='Hi', command=change)
button2 = Button(root, text='Close', command=quit)

a.pack()
button.pack()
for i in buttons.values():
    i.pack()
button2.pack()
root.mainloop()



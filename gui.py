# Python tkinter hello world program
from tkinter import *
root = Tk()
a = Label(root, text="Hello World")


def change():
    if button['text'] == 'Putin':
        button['text'] = 'Hyilo'
    else:
        button['text'] = 'Putin'


button = Button(root, text='Hi', command=change)

a.pack()
button.pack()
root.mainloop()



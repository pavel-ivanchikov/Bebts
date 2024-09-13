from ProcessesManager import ProcessesManager
from tkinter import *


def new_screen(name):
    def fun():
        if main_list:
            for w in main_list:
                w.destroy()
            main_list.clear()
        main_list.append(Button(root, text=name))
        for process in pm.main_dict[name].related_processes:
            main_list.append(Button(root, text=process.get_name(), command=new_screen(process.get_name())))
        main_list.append(Label(root, text=pm.main_dict[name]))
        main_list.append(Button(root, text='Close', command=quit))
        for w in main_list:
            w.pack()
    return fun


path = r"C:/DebtCounter/first/"
first_process_name = '1726038875105655'
pm = ProcessesManager(path, first_process_name)

root = Tk()
main_list = []
new_screen(first_process_name)()
root.mainloop()

from ProcessesManager import ProcessesManager
from tkinter import *


def new_screen(name):
    def fun():
        for i in main_list:
            i.destroy()
        main_list.clear()
        main_list.append(Button(root, text=name))
        for process in pm.main_dict[name].related_processes:
            main_list.append(Button(root, text=process.get_name(), command=new_screen(process.get_name())))
        main_list.append(Label(root, text=pm.main_dict[name]))
        main_list.append(Button(root, text='Close', command=quit))
        for i in main_list:
            i.pack()
    return fun


path = r"C:/DebtCounter/first/"
first_process_name = '1726038875105655'

pm = ProcessesManager(path, first_process_name)

root = Tk()
main_list = []
main_list.append(Button(root, text=first_process_name))
for process in pm.main_dict[first_process_name].related_processes:
    name = process.get_name()
    main_list.append(Button(root, text=name, command=new_screen(name)))
main_list.append(Label(root, text=pm.main_dict[first_process_name]))
main_list.append(Button(root, text='Close', command=quit))
for i in main_list:
    i.pack()

root.mainloop()



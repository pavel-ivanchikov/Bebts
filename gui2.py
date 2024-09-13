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
        main_list.append(Text(root, height=5))
        main_list.append(Button(root, text='Add Message', command=transact(name, False)))
        main_list.append(Button(root, text='Split', command=transact(name, True)))
        main_list.append(Button(root, text='Cross', command=transact(name, True)))
        main_list.append(Label(root, text=pm.main_dict[name]))
        main_list.append(Button(root, text='Close', command=quit))
        for w in main_list:
            w.pack()
    return fun


def transact(name, official):
    def fun():
        input_text = main_list[-6].get(1.0, "end-1c")
        if input_text:
            rez = pm.main_dict[name].act(input_text, official=official)
            if rez:
                pm.add_new_process(rez)
            new_screen(name)()
    return fun


path = r"C:/DebtCounter/first/"
first_process_name = '1726239543341073'
pm = ProcessesManager(path, first_process_name)

root = Tk()
main_list = []
new_screen(first_process_name)()
root.mainloop()

from ProcessesManagerDC import ProcessesManagerDC
from MyLife import MyLife
from tkinter import *
import os


def row(name, main_start, main_finish):
    n = 50
    ans = ['-' for _ in range(n + 2)]
    one = (main_finish - main_start) / n
    start = pm.main_dict[name].get_identifier()[0]
    if start > main_start:
        for i in range(round((start - main_start) / one)):
            ans[i] = '_'
    for transaction in pm.main_dict[name].get_data():
        if transaction.official:
            time_crossing = transaction.date
            position = round((time_crossing - main_start) / one)
            ans[position] = 'x'
    return ''.join(ans) + '>'


def new_screen(name):
    def fun():
        if main_list:
            for w in main_list:
                w.destroy()
            main_list.clear()
        main_start = min(pm.main_dict[name].get_first_date(),
                         min(pm.main_dict[name].related_processes,
                             key=lambda x: x.get_first_date()).get_first_date())
        main_finish = max(pm.main_dict[name].get_last_date(),
                          max(pm.main_dict[name].related_processes,
                              key=lambda x: x.get_last_date()).get_last_date())
        rows = []
        main_list.append(Button(root, text='Close', command=quit))
        main_list.append(Button(root, text=pm.main_dict[name].get_button_name()))
        rows.append(row(name, main_start, main_finish))
        for process in pm.main_dict[name].related_processes:
            main_list.append(Button(root, text=process.get_button_name(), command=new_screen(process.get_process_name())))
            rows.append(row(process.get_process_name(), main_start, main_finish))
        main_list.append(Label(root, text='\n'.join(rows), justify=LEFT))
        main_list.append(Text(root, height=2))
        main_list.append(Button(root, text='Add Message', command=transact(name, False)))
        main_list.append(Button(root, text='Split', command=transact(name, True)))
        main_list.append(Button(root, text='Cross', command=transact(name, True)))
        main_list.append(Label(root, text=pm.main_dict[name].get_not_official_transaction(), justify=LEFT))
        for w in main_list:
            w.pack()
    return fun


def transact(name, official):
    def fun():
        input_text = main_list[-5].get(1.0, "end-1c")
        if input_text:
            rez = pm.main_dict[name].act(input_text, official=official)
            if rez:
                pm.add_new_process(rez)
            new_screen(name)()
    return fun


path = r"C:/DebtCounter/second/"
pm = ProcessesManagerDC(path)
first_process_name = min(os.listdir(path)).split('.')[0]

root = Tk()
root.title("Debt Counter")
root.geometry('420x600')
root.resizable(False, False)
main_list = []
new_screen(first_process_name)()
root.mainloop()

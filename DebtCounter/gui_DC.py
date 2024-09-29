from ProcessesManagerDC import ProcessesManagerDC
from tkinter import Tk, Button, Label, Text, LEFT


def row(name, main_start, main_finish, text):
    n = 70
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
    return text + '\n' + ''.join(ans) + '>'


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
        rows = [row(name, main_start, main_finish, pm.info_dict[name][2])]
        for process in pm.main_dict[name].related_processes:
            text1 = pm.info_dict[process.get_process_name()][1]
            text2 = pm.info_dict[process.get_process_name()][2]
            main_list.append(Button(root, text=text1, command=new_screen(process.get_process_name())))
            rows.append(row(process.get_process_name(), main_start, main_finish, text2))
        main_list.insert(0, Label(root, text='\n'.join(rows), justify=LEFT))
        main_list.append(Label(root, text=pm.previous_action_result))
        main_list.append(Text(root, height=2, width=42))
        main_list.append(Button(root, text='Add Message', command=transact(name, False)))
        main_list.append(Label(root, text=pm.info_dict[name][0]))
        main_list.append(Button(root, text='Official', command=transact(name, True)))
        main_list.append(Label(root, text=pm.main_dict[name].get_all_transaction(), justify=LEFT))

        for w in main_list:
            w.pack()
    return fun


def transact(name, official):
    def fun():
        input_text = main_list[-5].get(1.0, "end-1c")
        if input_text:
            try:
                rez = pm.main_dict[name].act(input_text, official=official)
                if rez:
                    pm.add_new_process(rez)
                pm.controller()
                pm.previous_action_result = 'Success!'
                new_screen(name)()
            except Exception as e:
                pm.previous_action_result = str(e)
                new_screen(name)()
    return fun


path = r"C:/DebtCounter/second/"
pm = ProcessesManagerDC(path)
pm.deserialization()
first_process_name = pm.first_process_name

root = Tk()
root.title("Debt Counter")
root.geometry('420x620')
root.resizable(False, True)
main_list = []
new_screen(first_process_name)()
root.mainloop()

from ProcessesManager import ProcessesManager

path = r"C:/DebtCounter/first/"
first_process_name = '1726230292029195'

pm = ProcessesManager(path, first_process_name)

pm.main_dict['1726230292029195'].act('Ещё одно сообщение в первом процессе')

print(*pm.main_dict.keys())
print(pm.main_dict['1726230292029195'])


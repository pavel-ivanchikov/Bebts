from ProcessesManager import ProcessesManager

path = r"C:/DebtCounter/first/"
first_process_name = '1725850934387396'

pm = ProcessesManager(path, first_process_name)

pm.main_dict['1725850934387396'].act('Ещё одно сообщение в первом процессе')

print(*pm.main_dict)

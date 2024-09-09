from ProcessesManager import ProcessesManager

path = r"C:/DebtCounter/first/"
first_process_name = '1725860502812180'

pm = ProcessesManager(path, first_process_name)

pm.main_dict['1725860502812180'].act('Ещё одно сообщение в первом процессе')

print(*pm.main_dict.keys())
print(pm.main_dict['1725860502812180'])


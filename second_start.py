from ProcessesManager import ProcessesManager

path = r"C:/DebtCounter/first/"
first_process_name = '1726038875105655'

pm = ProcessesManager(path, first_process_name)

pm.main_dict['1726038875105655'].act('Ещё одно сообщение в первом процессе')

print(*pm.main_dict.keys())
print(pm.main_dict['1726038875105655'])


from ProcessesManager import ProcessesManager

path = r"C:/DebtCounter/first/"
first_process_name = '1725768496791185'

pm = ProcessesManager(path, first_process_name)

pm.main_dict['1725768496791185'].act('Четвёртое сообщение в первом процессе')

print(pm.main_dict['1725768496791185'])

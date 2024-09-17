from ProcessesManager import ProcessesManager
import os

path = r"C:/DebtCounter/first/"
pm = ProcessesManager(path)

print(*pm.main_dict.keys())
print(pm.main_dict['1726230292029195'])


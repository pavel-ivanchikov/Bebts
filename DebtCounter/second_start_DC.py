from ProcessesManagerDC import ProcessesManagerDC

path = r"C:/DebtCounter/second/"
pm = ProcessesManagerDC(path)

print(*pm.main_dict.keys())
keys = sorted(pm.main_dict.keys())
print(pm.main_dict[keys[0]])
print(pm.main_dict[keys[1]])
print(pm.main_dict[keys[2]])

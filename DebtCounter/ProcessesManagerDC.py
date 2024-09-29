from ProcessesManager import ProcessesManager
from MyLife import MyLife
from Person import Person
from Debt import Debt


class ProcessesManagerDC(ProcessesManager):
    def __init__(self, path: str):
        super().__init__(path)
        self.new_process_tags = ('SPLIT', 'NEW_PERSON', 'NEW_DEBT')
        self.info_dict = {}
        self.previous_action_result = 'Wellcome!'

    def controller(self):
        total_amount = 0
        for process in self.main_dict.values():
            if isinstance(process, MyLife):
                self.info_dict[process.get_process_name()] = ['CROSS, ' + ', '.join(process.additional_ables.keys())]
                self.info_dict[process.get_process_name()].append(process.name)
            elif isinstance(process, Person):
                self.info_dict[process.get_process_name()] = ['CROSS, ' + ', '.join(process.additional_ables.keys())]
                self.info_dict[process.get_process_name()].append(process.name)
                amount = sum(map(lambda x: x.debt_amount, process.debts))
                total_amount += amount
                self.info_dict[process.get_process_name()].append(process.name + ' Total balance: ' + str(amount))
            elif isinstance(process, Debt):
                self.info_dict[process.get_process_name()] = ['CROSS, ' + ', '.join(process.additional_ables.keys())]
                self.info_dict[process.get_process_name()].append('Debt of ' + process.related_processes[0].name)
                self.info_dict[process.get_process_name()].append(process.related_processes[0].name + "'s debt: " + str(process.debt_amount) + ' ' + str(process.debt_currency))
            else:
                self.info_dict[process.get_process_name()] = ['CROSS, SPLIT']
                self.info_dict[process.get_process_name()].append(process.get_process_name())
                self.info_dict[process.get_process_name()].append(process.get_process_name() + " from " + process.related_processes[0].name)
        self.info_dict[self.first_process_name].append(self.first_process.name + ' Total balance: ' + str(total_amount))

    def get_main_process(self):
        return MyLife.create_first_process(int(self.first_process_name) / 10 ** 6)

    def deserialization(self):
        super().deserialization()
        self.controller()

    def add_new_process(self, process):
        super().add_new_process(process)
        self.controller()
